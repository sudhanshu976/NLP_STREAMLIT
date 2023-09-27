from pathlib import Path

import streamlit as st
from PIL import Image
st.set_page_config(
    page_title="NLP WEB APP"
)


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "my_resume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | John Doe"
PAGE_ICON = ":wave:"
NAME = "SUDHANSHU"
DESCRIPTION = """
Aspiring Data Scientist | 18-Year-Old Data Enthusiast | 1 Year of Hands-On Experience | Passionate about Solving Real-World Problems"
"""
EMAIL = "gusainsudhanshu43@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com/",
    "LinkedIn": "https://www.linkedin.com/in/sudhanshu-gusain-34271028a/",
    "GitHub": "https://github.com/sudhanshu976",
    "Website": "https://huggingface.co/spaces/Sudhanshu976/NLP_FULL_APP",
}
PROJECTS = {
    "🏆 POWER-BI Dashboards - Making interactive and dynamic dashboards": "https://github.com/sudhanshu976/POWER-BI-PROJECTS",
    "🏆 Potato Disease Classifier using CNN - Checks whether a given potato leaf is healthy , early-blight or late-blight": "https://github.com/sudhanshu976/POTATO-DISEASE-CLASSIFIER-WITH-DEPLOYMENT",
    "🏆 Combined NLP WEB APP - This web app contains all NLP Projects I have made till date ": "https://github.com/sudhanshu976/NLP_FULL",
}




# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 1 Year expereince of performing various Data Science and NLP tasks
- ✔️ Strong hands on experience and knowledge in Python , ML , DL and NLP
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas , Numpy , Pytorch , Tensorflow)
- 📊 Data Visulization: PowerBi, Matplotlib , Seaborn
- 📚 Modeling: Supervised and Unsupervised ML algorithms , ANN , RNN , CNN
- 🗄️ Databases: MySQL
- 🗄️ WEB DEPLOYMENT: FLASK , Streamlit , Heroku
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Freelancer Data Scientist and NLP Engineer**")
st.write("05/2023 - Present")
st.write(
    """
- ► Used PowerBI for creating interactive dashboards 
- ► Solved many ML , DL and NLP problems in various fields like medical , agriculture , etc
- ► Well versed in solving real life problems especially using NLP
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")