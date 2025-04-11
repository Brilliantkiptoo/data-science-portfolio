import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(page_title="Brilliant | Data Scientist", page_icon="📊", layout="centered")

# Sidebar
st.sidebar.title("Connect with Me")
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/brilliant-kiptoo)")
st.sidebar.markdown("[GitHub](https://github.com/Brilliantkiptoo)")

# Home
st.title("👋 Hi, I'm Brilliant")
st.subheader("Data Scientist / Data Analyst")
st.markdown("""
Welcome to my personal portfolio site built with Streamlit.  
I'm passionate about turning data into actionable insights and building smart solutions.  
Explore my work below!
""")

# About
st.header("🧠 About Me")
st.write("""
I'm a data scientist/data analyst with a strong interest in statistical modeling, machine learning, and data storytelling.  
I thrive on transforming raw data into valuable insights and intuitive visualizations.
""")

# Projects
st.header("📁 Projects")

project_data = [
    {
        "title": "📊 Financial Sentiment Analysis Web App",
        "desc": "A Streamlit app that analyzes financial news sentiment using BERT and NLP techniques.",
        "link": "https://github.com/Brilliantkiptoo/NLP-Group10"
    },
    {
        "title": "💱 Currency Converter App",
        "desc": "Python-based web app that converts currencies using the Frankfurter API and Streamlit.",
        "link": "https://github.com/Brilliantkiptoo/currency-converter"
    },
    {
        "title": "🎬 IMDB Movie Reviews Classifier",
        "desc": "Sentiment analysis classifier trained on IMDB reviews using traditional ML techniques.",
        "link": "https://github.com/Brilliantkiptoo/IMDB-sentiment-analysis"
    },
    {
        "title": "🎙️ Radio Talkshow Transcript Analyzer",
        "desc": "NLP project analyzing Australian radio transcripts for key themes, sentiment, and entities.",
        "link": "https://github.com/Brilliantkiptoo/radio-talkshow-analyzer"
    }
]

for title, details in project_data.items():
    st.markdown(f"### [{title}]({details['link']})")
    st.write(details['desc'])

# Contact
st.header("📬 Contact")
st.markdown("Email: brilliantkip@gmail.com") 

