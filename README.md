# Forex Trade Assistant Bot

This is a Streamlit web app that helps analyze forex charts and related news headlines using OpenAI's GPT-4 Vision API to provide trade suggestions.

## Setup

1. Clone this repo or download the files.

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your OpenAI API key in `.streamlit/secrets.toml`:
   ```
   OPENAI_API_KEY = "your-openai-api-key"
   ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```

## Deployment on Streamlit Cloud

1. Push the repo to GitHub under your account.

2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and create a new app linking this repo.

3. Set your OpenAI API key as a secret in Streamlit Cloud.

4. Deploy and share your app!