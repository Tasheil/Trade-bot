# NOTE: This script requires Streamlit. If you are running in a sandbox or limited environment,
# this code will not work without access to install external packages (like streamlit and openai).

try:
    import streamlit as st
    from PIL import Image
    import openai
    import base64
except ModuleNotFoundError as e:
    print("Error: Required package not found. Please make sure 'streamlit', 'openai', and 'Pillow' are installed.")
    print("You can install them using: pip install streamlit openai pillow")
    raise e

# Title and instructions
st.set_page_config(page_title="Forex Trade Assistant", page_icon="📈")
st.title("📈 Forex Trade Assistant Bot")
st.markdown("""
Upload a **forex chart screenshot** and enter a **news headline or market comment**.
The bot will analyze both and provide a **trade suggestion**.
""")

# API key (use secrets if deployed)
openai.api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else "your-openai-api-key"

# Upload chart image
uploaded_image = st.file_uploader("Upload Chart Image", type=["png", "jpg", "jpeg"])

# Input news or notes
user_news = st.text_area("News Headline or Notes", placeholder="Example: EUR/USD rebounds after dovish FOMC statement")

# Button to trigger analysis
if st.button("Analyze Trade Setup"):
    if not uploaded_image or not user_news:
        st.warning("Please upload a chart image and enter some news or market notes.")
    else:
        with st.spinner("Analyzing chart and market news..."):
            # Convert image to base64
            img_bytes = uploaded_image.read()
            img_base64 = base64.b64encode(img_bytes).decode()

            # Build GPT-4 Vision API request
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4-vision-preview",
                    messages=[
                        {"role": "system", "content": "You are a forex trading analyst. Provide clear and concise trade suggestions based on chart and news."},
                        {"role": "user", "content": [
                            {"type": "text", "text": f"Here is a forex chart and some related news: {user_news}"},
                            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img_base64}", "detail": "high"}}
                        ]}
                    ],
                    max_tokens=800
                )

                trade_idea = response.choices[0].message.content
                st.success("📊 Trade Analysis Result")
                st.markdown(trade_idea)

            except Exception as e:
                st.error(f"Error: {e}")