import streamlit as st
    # Define background images for each section
   
def main():
    
    st.title("Resume-Professional Passport")
    st.sidebar.title("Navigation Panel")
    page = st.sidebar.radio("Go to", ["About me",  "Education", "Skills","Projects","Publishment", "Contact"])

    if page == "About me":
        st.header("About me")
        st.write("Hello! I'm Pravallika K.R, a dedicated professional eager to explore new opportunities in the field of AI engineering. With a fervent passion for innovation and problem-solving, I am driven by the prospect of contributing to cutting-edge projects that push the boundaries of technology. I thrive in collaborative environments, where my strong work ethic and commitment to excellence align seamlessly with team goals. Beyond my academic and professional pursuits, I find fulfillment in the melodic intricacies of Carnatic singing, a cherished hobby that adds depth and balance to my life. As I embark on this journey, I am excited to leverage my skills and expertise to make meaningful contributions in the dynamic landscape of artificial intelligence.")

    elif page == "Experience":
        st.header("Experience")
        st.subheader("Company A")
        st.write("- Position: Software Engineer")
        st.write("- Duration: Jan 2020 - Present")
        st.write("- Responsibilities: Developed and maintained web applications using Python and Django.")

        st.subheader("Company B")
        st.write("- Position: Data Analyst")
        st.write("- Duration: May 2018 - Dec 2019")
        st.write("- Responsibilities: Analyzed large datasets to extract insights and make data-driven decisions.")

    elif page == "Education":
        st.header("BTech in Artificial Intelligence and Data Science")
        st.subheader("Reva University")
        st.write("-Currently persuing my 6th sem")
        st.write("- Graduation Year: 2025")
        st.write("- Average CGPA of all 5sems-8.980")
        st.header("12th STATE board")
        st.subheader("Poorna Prajna College")
        st.write("Passed out year-2021")
        st.write("Percentage-93.33")
        st.header("10th CBSE board ")
        st.subheader("Narayana School")
        st.write("Passed out year-2019")
        st.write("Percentage-79.90")


    elif page == "Skills":
        st.header("Capabilities")
        st.subheader("Programming Languages:")
        st.write("Advanced Python ,Data Structures and Algorithms (DSA) in C and python ,SQL (Structured Query Language)")
        st.subheader("Frameworks/Libraries:")
        st.write("Numpy,Pandas ,Data Visualization (PowerBI),Math and Statistics for AI,EDA (Exploratory Data Analysis),Machine Learning (ML),Natural Language Processing (NLP),ML Ops (Machine Learning Operations),NNDL (Neural Networks and Deep Learning),Streamlit,Computer Vision,General Artificial Intelligence (Gen AI)")
        st.subheader("Version Control:")
        st.write("GitHub,Git")
        st.subheader("Database Management Systems (DBMS):")
        st.write("SQL,NoSQL (MongoDB)")
        st.subheader("Miscellaneous:")
        st.write("LLN (Language Learning Networks),LangChain (Language Chains)")

    elif page == "Projects":
        st.header("NLPantry - Recipe Generator Application")
        st.write("Developed a web application using Streamlit and Gemini Pro API to generate recipes based on user input. Implemented image processing and NLP techniques to enhance functionality and accuracy.")
        st.header("Title: LangChain News Research Tool: Building an End-to-End LLM Project")
        st.write("Developed an end-to-end LLM project utilizing LangChain, OpenAI API, and Streamlit, creating a sophisticated news research tool for equity research analysts. Enhanced skills in NLP, API integration, and industry-focused project development, adding substantial value to the data science and NLP engineering portfolio.")
        st.header("Empowering Early Disease Assessment with Deep Learning in Retinopathy Detection")
        st.write("Led a team of four in developing an innovative deep learning solution for early disease assessment in retinopathy detection. Collaborated closely with a guide to implement cutting-edge techniques, leveraging deep learning algorithms to improve diagnostic accuracy and facilitate timely intervention.")
    elif page =="Publishment":
        st.header("Paper Title:Retina Vigil: Deep Learning-Enabled Retinopathy Detection for Early Disease Assessment") 
        st.write("Spearheaded a team of four members under guidance to publish the paper titled :Retina Vigil: Deep Learning-Enabled Retinopathy Detection for Early Disease Assessment at IEEE MysuruCon-2023, the esteemed 3rd Edition of Mysore Subsection Flagship International Conference. Contributed to groundbreaking research in leveraging deep learning for early disease assessment in retinopathy detection, showcasing expertise in collaborative research and academic publication.")   
    elif page == "Contact":
        st.header("Contact")
        st.write("- Email: pravallikarajesh773@example.com")
        st.write("- Phone: 9513896465")
        st.write("- LinkedIn: (www.linkedin.com/in/pravallika-rajesh-a02a5628a)")

if __name__ == "__main__":
    main()

  
