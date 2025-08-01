#importing libraries
import os
import streamlit as st
import PyPDF2 as pdf
import google.generativeai as genai
from dotenv import load_dotenv

#loading env variables

load_dotenv() 

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#function for Response

def gemini_resp(inp):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(inp)
    return response.text

#function to convert pdf to text

def pdf_to_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += str(page.extract_text())


#prompt (update as required)

input_prompt="""You are a very skilled and experiences ATS (Application Tracking System)
with deep understanding of technological field, data science, AI, ML
Web development, Finance, Business, HR. Your task is to evaluate the resume based on the 
given job description. Considering job markey is highly competitive
and you should provide best assistance for improving the resumes.
Assign the percentage matching based on Jd (job description) and the messing keywords with high accuracy
resume:{text}
description:{jd}

The response should be in single string having the structure where you first provide 
Job Description Match:% 
followed by the MissingKeywords in a list followed by the resume summary and HR profile summary if the person is fit or not
"""

#streamlit app

st.title("AI ATS")
st.text("Improve your ATS")
jd=st.text_area("Enter Your Description")
file=st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the pdf")

submit=st.button("Submit")

if submit:
    if file is not None:
        text=pdf_to_text(file)
        response=gemini_resp(input_prompt)
        st.subheader(response)


