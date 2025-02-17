import google.generativeai as genai
from textblob import TextBlob
from dotenv import load_dotenv
import os
# Initialize Gemini Client (Replace with your actual API key)
genai.configure(api_key=os.getenv("API_KEY"))
class DebateAI:
    def __init__(self, topic):
        self.topic = topic
        self.context = []  # Stores the conversation history
        self.user_stances = []  # Tracks the user's stance over time
        self.stance = "neutral"
        self.contradiction_flag = False  # Flag for contradiction detection
        self.responses=[]
        self.prompts=[]
    def analyze_sentiment(self, text):
        """Improved stance detection with neutral handling."""
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity
        if polarity > 0.1:
            return "for"
        elif polarity < -0.1:
            return "against"
        else:
            return "neutral"

    def check_contradiction(self, current_stance):
        """Check if the user contradicts their previous stance."""
        if len(self.user_stances) < 2:  # Need at least 2 stances to compare
            return False
        
        # Check if the current stance contradicts any previous stance
        for past_stance in self.user_stances[:-1]:  # Exclude the last stance (current one)
            if past_stance != "neutral" and past_stance != current_stance:
                return True  # Contradiction detected
        return False

    def generate_argument(self, stance,user_input):
        """Generate an argument using Gemini Flash."""
        
        prompt = f"Provide 1 argument {stance} {self.topic} given that users argument is: {user_input} and the argument history is {self.prompts} and your response history is {self.responses} and give flag if contradiction is detected"
        self.prompts.append(prompt)
        # Call Gemini API
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction="You are a logical and persuasive debate assistant. Start your answer with a counter to the user's statement. Provide structured, well-reasoned arguments while respecting opposing views.",
            generation_config={
                "temperature": 0.7,  # Controls creativity
                "top_p": 0.9,        # Sampling strategy
                "max_output_tokens": 100,  # Increase token limit for better responses
            }
        )
        response = model.generate_content(prompt)
        
        self.responses.append(response.text.strip())
        # Extract response safely
        argument = response.text.strip() if response.text else "I couldn't generate an argument."
        return argument

    def respond(self, user_input):
        """Improved stance switching logic with contradiction detection."""
        # Analyze the user's stance
        user_stance = self.analyze_sentiment(user_input)
        self.user_stances.append(user_stance)  # Track the user's stance

        # Check for contradiction
        self.contradiction_flag = self.check_contradiction(user_stance)

        # Determine AI's stance
        if user_stance == "for":
            self.stance = "against"
        elif user_stance == "against":
            self.stance = "for"
        else:
            self.stance = "against" if self.stance == "for" else "for"

        # Generate argument
        argument = self.generate_argument(self.stance,user_input)
        self.context.append((user_input, argument))  # Update conversation history

        return argument

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Debate AI")
    parser.add_argument("--topic", type=str, default="climate change", help="Debate topic")
    args = parser.parse_args()
    ai = DebateAI(args.topic)
    print(f"AI: Let's debate {args.topic}. You go first. (Type 'quit' to exit)")
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ["quit", "exit"]:
                print("AI: Thanks for the debate!")
                break
            response = ai.respond(user_input)
            print(f"AI: {response}")
            print()
            if ai.contradiction_flag:
                print("[System Notice] Contradiction detected in your stance!")
            print()
        except KeyboardInterrupt:
            print("\nAI: Debate ended abruptly.")
            break