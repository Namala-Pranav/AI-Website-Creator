# AI-Website-Creator
Website AI Generator is a Streamlit app powered by Google Gemini that creates complete frontend websites (HTML, CSS, JS) from text prompts. Users describe an idea, generate clean responsive code, and download ready-to-use website files as a ZIP.

# 🌐 Website AI Generator

Website AI Generator is a Streamlit-based web application powered by **Google Gemini** that generates complete frontend websites (HTML, CSS, and JavaScript) from simple text descriptions. Users can describe their website idea and instantly download ready-to-use website files as a ZIP.

---

## 🚀 Features
- Generate full frontend websites using AI
- Clean separation of HTML, CSS, and JavaScript
- Responsive and modern code structure
- Download generated website as a ZIP file
- Simple, beginner-friendly UI

---

## 🛠 Tech Stack
- Python
- Streamlit
- LangChain
- Google Gemini API

---

## 📁 Project Structure
```

website-ai-generator/
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md

````

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
https://github.com/VigneshKalla/AI-Website-Creator/tree/main
```

### 2️⃣ (Optional) Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add API Key

Create a `.env` file using `.env.example`:

```env
GEMINI=your_google_gemini_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📦 Output

The app generates and downloads:

* `index.html`
* `style.css`
* `script.js`
* `website.zip`

---

## 🧠 How It Works

1. User enters a website idea.
2. Gemini generates HTML, CSS, and JS code.
3. The app extracts and saves the files.
4. Files are zipped and provided for download.

