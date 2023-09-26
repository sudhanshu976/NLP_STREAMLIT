import streamlit as st
st.set_page_config(
    page_title="NLP WEB APP"
)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")


st.title("CONTACT US")
st.sidebar.success("Select a page above")

with st.container():
    st.write("-----")
    st.header("Get in Touch with Me !")
    st.write("##")

    contact_form="""

     <form action="https://formsubmit.co/cus146126@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here ... " required></textarea>

     <button type="submit">Send</button>
     </form>

 """

left_col , right_col = st.columns(2)
with left_col:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_col:
    st.empty()