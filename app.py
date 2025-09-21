import streamlit as st
from few_shot import FewShotsPost
from post_generator import generate_post

length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

def main():
    st.title("LinkedIn Post Generator")
    col1, col2, col3, col4 = st.columns(4)
    fs = FewShotsPost()
    with col1:
        selectedTag = st.selectbox("Title", options=fs.get_tags())
    with col2:
        selectedLength = st.selectbox("Length", options=length_options)
    with col3:
        selectedLanguage = st.selectbox("Language", options=language_options)
    with col4:
        selectedCreator = st.selectbox("Creator", options=fs.get_unique_creators())
    
    if st.button("Generate"):
        post = generate_post(tag=selectedTag, language=selectedLanguage, length=selectedLength, creator=selectedCreator)
        st.write(post)
        

if __name__ == "__main__":
    main()