import streamlit as st

# Page config
st.set_page_config(page_title="Brilliant's Portfolio", page_icon="📊", layout="wide")

# Sidebar with contact info
st.sidebar.title("📌 Connect with Me")
st.sidebar.markdown("[💼 LinkedIn](https://www.linkedin.com/in/brilliant-kiptoo)")
st.sidebar.markdown("[💻 GitHub](https://github.com/Brilliantkiptoo)")

# Main content
st.title("👋 Hi, I'm Brilliant Kiptoo")
st.subheader("Data Scientist / Data Analyst")

# About section
st.header("💬 About Me")
st.write("""
I'm a data scientist and data analyst with a strong interest in statistical modeling, machine learning, and data storytelling.  
I thrive on transforming raw data into valuable insights and intuitive visualizations.
""")

# Projects section
st.header("📁 Project Reports")
st.write("Explore categorized reports in various domains of data science:")

# ETL & Pipelines
st.subheader("🔄 ETL & Data Pipelines")
st.markdown("- [Advanced ELT Pipeline Construction with Airflow](https://github.com/Brilliantkiptoo/project-Reports/blob/main/Advanced%20ELT%20Pipeline%20Construction%20with%20Airflow%20-%20Copy.pdf)")
st.markdown("- [Data Lakehouse with Snowflake](https://github.com/Brilliantkiptoo/project-Reports/blob/main/Data%20Lakehouse%20with%20Snowflake.pdf)")

# Predictive Modeling
st.subheader("📈 Predictive Modeling")
st.markdown("- [Predictive Model to Forecast College Players' Selection](https://github.com/Brilliantkiptoo/project-Reports/blob/main/PREDICTIVE%20MODEL%20TO%20FORECAST%20COLLEGE%20PLAYERS'%20SELECTION%20.pdf)")
st.markdown("- [Predicting Diabetes Risk Factors from Dietary Intake](https://github.com/Brilliantkiptoo/project-Reports/blob/main/predicting%20the%20risk%20factors%20of%20diabetes%20based%20on%20the%20user's%20dietary%20intake-Group%20project.pdf)")

# Data Mining
st.subheader("🧠 Data Mining & Classification")
st.markdown("- [Data Mining Problem](https://github.com/Brilliantkiptoo/project-Reports/blob/main/Data%20Mining%20Problem.pdf)")
st.markdown("- [Fraud Detection Using Data Mining Techniques](https://github.com/Brilliantkiptoo/project-Reports/blob/main/fraud%20Detection%20by%20applying%20data%20mining%20techniques%20and%20classification%20analysis.pdf)")

# Healthcare Analytics
st.subheader("🏥 Healthcare Analytics")
st.markdown("- [Predicting Hospital Readmissions Using Machine Learning](https://github.com/Brilliantkiptoo/project-Reports/blob/main/Predicting%20Hospital%20Readmissions%20Using%20Machine%20Learning.pdf)")

# General repo link
st.markdown("📂 [View All Reports in Repository](https://github.com/Brilliantkiptoo/project-Reports)")

# Contact
st.header("📬 Contact")
st.markdown("📧 Email: [brilliantkip@gmail.com](mailto:brilliantkip@gmail.com)")

