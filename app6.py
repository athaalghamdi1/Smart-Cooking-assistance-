import streamlit as st
import cv2
import numpy as np 
from roboflow import Roboflow
import google.generativeai as genai
from huggingface_hub import InferenceClient



if "page" not in st.session_state:
    st.session_state.page="Home"

def v(pagename):
    st.session_state.page= pagename


if st.session_state.page == "Home":

    @st.dialog("Sign up")
    def Signup():
        if "Username" not in st.session_state:
            st.session_state.Username= ""

        Username = st.text_input("Username", st.session_state["Username"])
        if st.button("Submit"):
            v("Cooking")
            st.session_state["Username"] = Username
            st.rerun()
            
        
            


    if Signup not in st.session_state:
        st.markdown(

            "<h1 style='text-align: center;'>Smart Cooking Assistant</h1>",
            unsafe_allow_html=True
        )
        st.write("\n")
        if st.button("**Start**", type="primary", use_container_width=True):
            Signup()



if st.session_state.page == "Cooking":
    
    with st.sidebar:
        
        st.write(":blue[***Welcom!***]" + "\t" + f":blue[***{st.session_state["Username"]}***]")
        st.write("\n")
        if st.button("Logout", type="primary"):
            st.session_state.page= "Home"
    st.markdown(

        "<h1 style='text-align: center;'>Start with upload an image</h1>",
        unsafe_allow_html=True
    )

    upload = st.file_uploader(" ", accept_multiple_files=False)
    if upload:
       st.image(upload)
    if upload is not None:
        bytes_data = upload.read()
        image= np.asarray(bytearray(bytes_data)) 
        image = cv2.imdecode(image, 0) 
        cv2.imshow("output", image) 
        with st.spinner("Please wait..."):
            rf = Roboflow(api_key="I6nmZqWCWSwrNT08Yzkn")
            project = rf.workspace().project("recipe-ingredients-cn-bpkvk-es8pm-xgfdf-26wc9")
            model = project.version(3).model

        result = model.predict(image, confidence=40, overlap=30).json()
        labels = [item["class"] for item in result["predictions"]]
        with st.container(border=10):
            compent= st.multiselect(":blue[***Select Component***]", labels, default=None, key=None, help=None, on_change=None, args=None, kwargs=None, max_selections=None, placeholder="Choose an option", disabled=False, label_visibility="visible")
            button= st.button("***make recipes***", type="primary", use_container_width=True)
            if button:
                genai.configure(api_key="AIzaSyAGqVi4J1zxCKJJ9FBDnKw1sLMS1ywurkE")
                model = genai.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content(f"create cooking recipes as options of food ingredients, I have:{compent}")
                try:

                    with st.container(border=10):
                        if response:
                            with st.spinner("Please wait..."):
                                st.write(response.text)
                                client = InferenceClient("black-forest-labs/FLUX.1-dev", token=open("key.txt").read())
                                Image = client.text_to_image(f"make a plate of dishes based on,{response.text}")
                                st.image(Image, output_format="PNG")
                except Exception:
                    st.warning("Try agin")