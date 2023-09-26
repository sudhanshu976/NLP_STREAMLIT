import streamlit as st
import requests
from PIL import Image
from streamlit_lottie import st_lottie


st.set_page_config(
    page_title="NLP WEB APP"
)

#---------------------LOTTIE  ANIMATION ------------------------
def load_lottie(url):
    r = requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

lottie_coding = load_lottie("https://lottie.host/e0a6d7e0-6b3d-428f-addc-aa44a746d653/MImt8ecbMs.json")


st.sidebar.success("Select a page above")



# -------------- HEADER ----------------------------
with st.container():
    st.subheader("Hi , I am Sudhanshu :wave:")
    st.title("A Data Scientist and NLP Engineer from INDIA")
    st.write("I am passionate about finding ways to solve real life problems through my skills of ML , DL and NLP")
    st.write("[Know more about me  >> ](https://www.linkedin.com/in/sudhanshu-gusain-34271028a/)")

# --------------------WHAT I DO --------------------------
with st.container():
    st.write("-----")
    left_column ,center, right_column = st.columns(3)
    with left_column:
        st.header("MY SKILLS")
        st.write("##")
        st.write("""  
                📊 **Data Science Explorer**: Over the past year, I've dedicated myself to understanding and harnessing the power of data. I've translated my knowledge into tangible projects, gaining expertise in a wide range of skills, including:

- **Power BI**
- **Machine Learning**
- **Deep Learning**
- **NLP (Natural Language Processing)**
- **Flask**
- **SQL and Python**
- **Web Services**

                    """)
        
        with center:
            st.write("")
        with right_column:
            st.header("MY PROJECTS")
            st.write("##")
            st.write("""
                    ##### 1. SMS-SPAM-CLASSIFIER USING ML 
                    ##### 2. LANGUAGE-DETECTOR USING ML
                    ##### 3. SENTIMENT-ANALYZER USING BERT 
                    ##### 4. NEXT-WORD-PREDICTOR USING LSTM """)

with st.container():
    st.write("--------------------------------------------------------------------------------------------------")           
with st.container():
    st_lottie(lottie_coding)          
            

        


        

