import os
from PIL import Image
import streamlit as st

def app(st, current_dir, Image):
    # _______________________ directory of needed files __________
    resume_file = current_dir / "Resume" / "MyResume.pdf"
    profile_pic_path = current_dir / "Photos" / "profile_pic.jpg"
    linkedin_pic_path = current_dir / "Photos" / "linkedin.png"
    github_pic_path = current_dir / "Photos" / "github.png"
    gmail_pic_path = current_dir / "Photos" / "gmail.png"

    # ___________________________ Picture and About Me __________________
    c1, c2 = st.columns([1, 2])
    profile_pic = Image.open(profile_pic_path)  # Open image
    c1.image(profile_pic, caption="OGBEIFUN PRECIOUS OMIJIE", width=150)
    
    with c2:
        st.header('About Me')
        st.markdown(
            "My name is **OGBEIFUN PRECIOUS OMIJIE**. I am a Master's student at Teesside University Middlesbrough, UK, studying Financial Technology with Advanced Practice. With over three years of experience in data analysis, I specialize in transforming complex datasets into actionable insights that drive informed decision-making. My expertise includes statistical analysis, data mining, predictive modeling, and data visualization using tools like E-Views, Excel, SQL, and Power BI. I have a strong problem-solving ability, keen attention to detail, and excellent presentation skills. Passionate about leveraging data for business strategy and innovation, I am eager to apply my knowledge to real-world challenges in financial technology and beyond.")
        st.caption('May 2025')

        # # Resume download
        # with open(resume_file, "rb") as pdf_file:
        #     PDFbyte = pdf_file.read()

        # st.download_button(
        #     label=" 📄 Download Resume",
        #     data=PDFbyte,
        #     file_name='OGBEIFUN OMIJIE_Resume.pdf',
        #     mime="application/pdf",
        # )
            
    st.write('#')

    # ___________________________ Social Links __________________
    st.write("### Connect with me:")

    # Open images correctly
    linkedin_pic = Image.open(linkedin_pic_path)
    github_pic = Image.open(github_pic_path)
    gmail_pic = Image.open(gmail_pic_path)

    # Display social media icons and links
    sub = st.columns(3)

    # LinkedIn
    sub[0].image(linkedin_pic, width=50)
    sub[0].markdown('[LinkedIn](https://www.linkedin.com/in/precious-ogbeifun-omijie-1b0293294/)')

    # GitHub
    sub[1].image(github_pic, width=50)
    sub[1].markdown('[GitHub](https://github.com/omijieprecious)')

    # Gmail
    sub[2].image(gmail_pic, width=50)
    sub[2].markdown('[Gmail](mailto:omijieprecious09@gmail.com)')
