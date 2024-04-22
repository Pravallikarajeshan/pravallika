import streamlit as st
from PIL import Image

# Define colors
primary_color = "#1E90FF"  # Dodger Blue
secondary_color = "#FF6347"  # Tomato

# Custom function to display section headers with custom styling
def styled_header(text):
    st.markdown(
        f'<h2 style="color:{primary_color};">{text}</h2>',
        unsafe_allow_html=True
    )

# Custom function to display section subheaders with custom styling
def styled_subheader(text):
    st.markdown(
        f'<h3 style="color:{secondary_color};">{text}</h3>',
        unsafe_allow_html=True
    )

def main():
    st.title("🚀 Pravallika K.R - Resume 🚀")
    st.markdown("---")

    # About me section with stylized heading
    styled_header("👩‍💻 About Me")
    st.markdown("Hello! I'm Pravallika K.R, a dedicated professional eager to explore new opportunities in the field of AI engineering. With a fervent passion for innovation and problem-solving, I am driven by the prospect of contributing to cutting-edge projects that push the boundaries of technology. I thrive in collaborative environments, where my strong work ethic and commitment to excellence align seamlessly with team goals. Beyond my academic and professional pursuits, I find fulfillment in the melodic intricacies of Carnatic singing, a cherished hobby that adds depth and balance to my life. As I embark on this journey, I am excited to leverage my skills and expertise to make meaningful contributions in the dynamic landscape of artificial intelligence.")
    st.markdown("---")

    # Education section with stylized heading
    styled_header("📚 Education")
    styled_subheader("BTech in Artificial Intelligence and Data Science")
    st.write("Reva University (Graduation Year: 2025)")
    st.write("- Currently pursuing my 6th semester")
    st.write("- Average CGPA of all 5 semesters: 8.980")
    
    styled_subheader("12th - State Board")
    st.write("Poorna Prajna College (Passed out year: 2021)")
    st.write("Percentage: 93.33")

    styled_subheader("10th - CBSE Board")
    st.write("Narayana School (Passed out year: 2019)")
    st.write("Percentage: 79.90")
    st.markdown("---")

    # Skills section with stylized heading
    styled_header("💡 Skills")
    styled_subheader("Programming Languages")
    st.write("Advanced Python, Data Structures and Algorithms (DSA) in C and Python, SQL (Structured Query Language)")
    
    styled_subheader("Frameworks/Libraries")
    st.write("Numpy, Pandas, Data Visualization (PowerBI), Math and Statistics for AI, EDA (Exploratory Data Analysis), Machine Learning (ML), Natural Language Processing (NLP), ML Ops (Machine Learning Operations), NNDL (Neural Networks and Deep Learning), Streamlit, Computer Vision, General Artificial Intelligence (Gen AI)")
    
    styled_subheader("Version Control")
    st.write("GitHub, Git")
    
    styled_subheader("Database Management Systems (DBMS)")
    st.write("SQL, NoSQL (MongoDB)")
    
    styled_subheader("Miscellaneous")
    st.write("LLN (Language Learning Networks), LangChain (Language Chains)")
    st.markdown("---")

    # Projects section with stylized heading
    styled_header("🛠️ Projects")
    styled_subheader("NLPantry - Recipe Generator Application")
    st.write("Currently developing a web application using Streamlit and Gemini Pro API to create an intuitive recipe generator. Implementing advanced image processing and NLP techniques to enhance functionality and accuracy.")
    
    styled_subheader("LangChain News Research Tool: Building an End-to-End LLM Project")
    st.write("Developed an end-to-end LLM project utilizing LangChain, OpenAI API, and Streamlit, creating a sophisticated news research tool for equity research analysts. Enhanced skills in NLP, API integration, and industry-focused project development, adding substantial value to the data science and NLP engineering portfolio.")
    
    styled_subheader("Empowering Early Disease Assessment with Deep Learning in Retinopathy Detection")
    st.write("Led a team of four in developing an innovative deep learning solution for early disease assessment in retinopathy detection. Collaborated closely with a guide to implement cutting-edge techniques, leveraging deep learning algorithms to improve diagnostic accuracy and facilitate timely intervention.")
  

    # Publication section with stylized heading
    styled_header("📝 Publication")
    st.write("Paper Title: Retina Vigil: Deep Learning-Enabled Retinopathy Detection for Early Disease Assessment")
    st.write("Spearheaded a team of four members under guidance to publish the paper titled 'Retina Vigil: Deep Learning-Enabled Retinopathy Detection for Early Disease Assessment' at IEEE MysuruCon-2023, the esteemed 3rd Edition of Mysore Subsection Flagship International Conference. Contributed to groundbreaking research in leveraging deep learning for early disease assessment in retinopathy detection, showcasing expertise in collaborative research and academic publication.")
    st.write("link here , you can view our paper:(https://ieeexplore.ieee.org/document/10396854/authors)")

    # Contact section with stylized heading
    styled_header("📞 Contact")
    st.write("- Email: pravallikarajesh773@example.com")
    st.write("- Phone: 9513896465")
    st.write("- LinkedIn: [Pravallika Rajesh](www.linkedin.com/in/pravallika-rajesh-a02a5628a)")
    st.markdown("---")

if __name__ == "__main__":
    main()


  
