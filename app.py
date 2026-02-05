## app.py
import os , zipfile, streamlit as st
import langchain
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

## Load .env (API Key)
load_dotenv() 
os.environ["GOOGLE_API_KEY"] = os.getenv("Gemini")

# ---------------- User Interface ----------------
st.set_page_config(page_title="AI Website Creator", page_icon="🤖✨", layout="centered")
## Title 
st.markdown(
    '<h1 style="text-align:center;color:#34A853;font-family:Urbanist,sans-serif;font-size:42px;font-weight:700;">Website AI Generator</h1>',
    unsafe_allow_html=True,)
## Space
st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
## Sub-title
st.markdown(
    '<p style="text-align:center;font-family:Poppins,sans-serif;font-size:18px;color:#90EE90;margin-top:-10px;">'
    'Describe your website idea — layout, sections, theme, colors, and features.'
    '</p>',
    unsafe_allow_html=True
)
## Space
st.markdown("<div style='height:50px'></div>", unsafe_allow_html=True)
## Text Area
prompt= st.text_area("💡 Describe your website idea here...", height=100)
## ---------------- System Prompt ----------------
system_prompt = """
You are an expert frontend developer with deep knowledge of modern web design principles,
including responsive layouts, clean UI structure, accessibility, and best practices in HTML, 
CSS, and JavaScript.
Your task is to generate a complete, well-structured frontend website based on the user's description.

Follow these rules:
1. The output must include **HTML, CSS, and JavaScript** as separate blocks.
2. The website should be responsive, clean, and easy to understand.
3. Use modern standards (semantic HTML5, organized CSS, minimal JS).
4. Do NOT explain the code. Only output the code blocks.

Return the result in the EXACT format below using these delimiters:

--html--
[Full and complete HTML document here]
--html--

--css--
[All required CSS code here]
--css--

--js--
[All JavaScript code here]
--js--
"""
## ---------------- Button: Generate Website ----------------
if st.button("Generate Website"):
    model= ChatGoogleGenerativeAI(model="gemini-2.5-flash") # Initialize Model
    message= [("system", system_prompt), ("user", prompt)]  # Structure the prompt for the model

    response = model.invoke(message) # Get response
    content = response.content  # model output text
    
    ## 1.Extract blocks safely
    html = content.split("--html--")[1].split("--html--")[0].strip()
    css  = content.split("--css--")[1].split("--css--")[0].strip()
    js   = content.split("--js--")[1].split("--js--")[0].strip()
    ## 2. Save Files
    files = {
        "index.html": html,
        "style.css": css,
        "script.js": js
    }
    for name, data in files.items():
        with open(name, "w", encoding="utf-8") as f:
            f.write(data)
    ## 3.Create ZIP file
    with zipfile.ZipFile("website.zip", "w") as zipf:
        for file in files: 
            zipf.write(file)
    ## Space
    st.markdown("<div style='height:25px'></div>", unsafe_allow_html=True)
    ## Download Button
    with open("website.zip", "rb") as f:
        st.download_button("⇩ Click to Download Website Files", f.read(), "website.zip")
        
    st.success("Website files generated successfully!")
## Footer   
st.markdown("<p style='text-align:center;font-family:Poppins,sans-serif;font-size:14px;color:#666;margin-top:40px;'>© 2025 Website AI Generator — Built with 🌟 using Streamlit & Gemini</p>", unsafe_allow_html=True)

