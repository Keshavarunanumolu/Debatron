# DebateAI: AI-Powered Command Line Debate Assistant

A dynamic debate assistant leveraging Google's Gemini AI for real-time argument generation, stance detection, and contradiction analysis.

## Features

- 🗣️ **Real-Time Debate**: Engage in structured debates on any topic
- 📊 **Sentiment Analysis**: Automatic detection of user's stance (for/against/neutral)
- ⚠️ **Contradiction Detection**: Flags inconsistent positions during debate
- 🤖 **Context-Aware Responses**: Maintains conversation history for coherent arguments
- 🚀 **Gemini AI Integration**: Uses state-of-the-art language model for response generation

## Installation

1. **Requirements**:
   - Python 3.8+
   - Google Gemini API key

2. **Install dependencies**:
   ```bash
   pip install google-generativeai textblob argparse python-dotenv
3. **API key**:
   Add your Gemini GenAI API key (Create Google API key at Google AI Studio) in the .env_sample file, and rename the file to .env.

## Key Components

### **DebateAI Class**
- **Sentiment analysis with TextBlob**: Detects user stance (for/against/neutral) using sentiment analysis.
- **Contradiction detection system**: Flags inconsistencies in the user's stance during the debate.
- **Context-aware prompt engineering**: Maintains conversation history for coherent and relevant responses.
- **Gemini API integration for argument generation**: Leverages Google's Gemini AI for generating logical and persuasive arguments.

---

## Features

- **Automatic stance switching (pro/con)**: Automatically takes the opposite stance of the user (or a neutral stance if needed).
- **Conversation history tracking**: Keeps track of the debate context for better response generation.
- **Response length control (100 tokens)**: Ensures concise and focused arguments.
- **Temperature-controlled creativity**: Balances creativity and logical reasoning in responses.

---

## Dependencies

- **`google-generativeai`**: Integration with Google's Gemini AI for argument generation.
- **`textblob`**: Sentiment analysis to determine the user's stance.
- **`argparse`**: Command-line interface for running the debate assistant.

---

## Limitations

- **Requires Gemini API access**: Dependent on Google's Gemini API for functionality.
- **Basic sentiment analysis (TextBlob-based)**: Limited to English and basic sentiment detection.
- **English language only**: Currently supports only English debates.
- **Command-line interface only**: No graphical user interface (GUI) available.

---

## Future Improvements

- **Add GUI interface**: Develop a user-friendly graphical interface for easier interaction.
- **Support multiple languages**: Expand language support for non-English debates.
- **Implement advanced contradiction detection**: Enhance contradiction detection with more sophisticated logic.
- **Add debate scoring system**: Introduce a scoring mechanism to evaluate debate performance.
- **Include fact-checking capabilities**: Integrate fact-checking to verify claims during debates.
   
