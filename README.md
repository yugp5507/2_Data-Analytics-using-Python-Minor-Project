# 📊 Data Analytics using Python – Minor Project

This project focuses on **Exploratory Data Analysis (EDA)** using Python to analyze restaurant data and understand customer preferences and trends.

---

## 📌 Project Objective

The main goal of this project is to:

- ✅ Identify popular restaurant categories
- ✅ Analyze customer ratings and votes
- ✅ Compare online vs offline ordering trends
- ✅ Understand cost preferences for dining
- ✅ Perform univariate, bivariate, and multivariate analysis
- ✅ Generate actionable insights through data visualization

---

## 📋 Table of Contents

- [Project Objective](#-project-objective)
- [Project Setup Guide](#-project-setup-guide-step-by-step)
- [Project Structure](#-project-structure)
- [Project Features](#-project-features)
- [Key Insights](#-key-insights)
- [Common Issues & Fixes](#-common-issues--fixes)
- [Tech Stack](#-tech-stack)
- [Analysis Workflow](#-analysis-workflow)
- [Author](#-author)
- [Support](#-support)

---

## 🚀 Project Setup Guide (Step-by-Step)

### 📁 Step 1: Clone Repository

```bash
git clone https://github.com/yugp5507/Data-Analytics-using-Python-Minor-Project.git
cd Data-Analytics-using-Python-Minor-Project
```

### 🐍 Step 2: Install Python

- **Download Python:** https://www.python.org/downloads/
- **Recommended Version:** Python 3.10 or 3.11
- ⚠️ Make sure to check **"Add Python to PATH"**

**Check version:**
```bash
python --version
```

### 🧪 Step 3: Create Virtual Environment

```bash
python -m venv venv
```

### ⚡ Step 4: Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### ⬆️ Step 5: Upgrade pip

```bash
pip install --upgrade pip
```

### 📦 Step 6: Install Required Libraries (Compatible Versions)

```bash
pip install seaborn==0.12.2 matplotlib==3.7.2 pandas==1.5.3 numpy==1.23.5 scikit-learn==1.3.0
```

### 📄 Step 7: (Optional) Create requirements.txt

Generate requirements file:
```bash
pip freeze > requirements.txt
```

Install later using:
```bash
pip install -r requirements.txt
```

### ▶️ Step 8: Run Project

**Run Python file:**
```bash
python main.py
```

**Run Jupyter Notebook:**
```bash
pip install notebook
jupyter notebook
```

### 🧠 Step 9: Check Kernel in VS Code

**Method 1:**
- Open `.ipynb` file
- Check top-right corner
- Example: `Python 3.10 (venv)`

**Method 2:**
- Press `Ctrl + Shift + P`
- Search: `Python: Select Interpreter`

**Method 3 (Code Check):**
```python
import sys
print(sys.executable)
```

### ✅ Step 10: Verify Installation

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

print("All libraries working ✅")
```

---

## 📂 Project Structure

```
Data-Analytics-using-Python-Minor-Project/
├── main.ipynb                                  # Main analysis notebook
├── requirements.txt                            # Project dependencies
├── README.md                                   # Project documentation
├── Charts/                                     # Generated visualizations
├── Data/
│   ├── raw/
│   │   └── VNSGU_SEM4_All_Student_Results.csv # Raw dataset
│   └── processed/
│       └── VNSGU_SEM4_All_Student_Results_Cleaned.csv # Cleaned dataset
├── Documentation/                              # Project documentation
├── Notebooks/
│   ├── 01_data_loading.ipynb                  # Data loading & exploration
│   ├── 02_preprocessing.ipynb                 # Data cleaning & preprocessing
│   ├── 03_graphs.ipynb                        # Data visualization
│   ├── 04_kmeans_clustering.ipynb             # Clustering analysis
│   └── SWEETVIZ_REPORT.html                   # Automated EDA report
├── outputs/
│   └── cluster_summary.csv                    # Clustering results
├── models/                                     # Trained models
└── src/
    └── predict.py                             # Prediction script
```

---

## 📊 Project Features

- 🔍 **Data Cleaning** – Handling missing values, formatting, and data validation
- 📈 **Univariate Analysis** – Countplot, histogram, distribution analysis
- 🔗 **Bivariate Analysis** – Groupby operations, scatter plots, line plots
- 🌐 **Multivariate Analysis** – Heatmap, correlation analysis
- 🎨 **Data Visualization** – Seaborn & Matplotlib for insightful graphics
- 🤖 **Clustering Analysis** – K-means clustering for customer segmentation
- 📊 **Automated EDA Report** – Sweetviz report generation

---

## 📈 Key Insights

- 🍽️ **Majority of restaurants** fall into the Dining category
- ⭐ **Dining restaurants** receive the highest votes
- 📱 **Most restaurants** do not accept online orders
- 🌟 **Ratings** mostly range between 3.5 to 4.0
- 💰 **Couples** prefer dining cost around ₹300
- 📊 **Online orders** receive better ratings than offline orders

---

## ⚠️ Common Issues & Fixes

### ModuleNotFoundError
**Cause:** Wrong kernel selected  
**Fix:** Select correct venv kernel using `Python: Select Interpreter`

### Graph Not Showing
**Solution:** Use `plt.show()` in your code

### Version Conflict
**Fix:**
```bash
pip install --upgrade seaborn matplotlib pandas numpy
```

### Kernel Not Found
**Solution:**
```bash
python -m ipykernel install --user --name venv --display-name "Python (venv)"
```

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **Data Processing:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn
- **Notebook:** Jupyter Notebook
- **EDA Automation:** Sweetviz

---

## 📊 Analysis Workflow

1. **Data Loading & Exploration** – Load raw data and understand structure
2. **Data Preprocessing** – Clean data, handle missing values, feature engineering
3. **Univariate Analysis** – Individual variable distributions
4. **Bivariate Analysis** – Relationships between two variables
5. **Multivariate Analysis** – Relationships among multiple variables
6. **Clustering** – Customer segmentation using K-means
7. **Insights & Recommendations** – Generate actionable business insights

---

## 🎓 Student Result & Performance Predictor (predict.py)

### Overview

The `predict.py` script is a **Streamlit-based web application** that allows students to enter their exam marks across multiple subjects and get:
- ✅ Detailed result marksheet (HTML & PDF format)
- ✅ SGPA calculation
- ✅ Pass/Fail status determination
- ✅ Performance prediction using K-means clustering (High Performer/Average/Needs Improvement)
- ✅ Downloadable PDF result report

### Features

- **Student Information Input** – Enter seat number, name, and college
- **Subject Marks Entry** – Input external theory, external practical, internal theory, and internal practical marks
- **Automatic Calculations** – Total marks, SGPA, and result status
- **ML-based Performance Prediction** – Uses trained K-means model to classify performance levels
- **PDF Report Generation** – Export marksheet as PDF for records
- **Responsive UI** – Clean, user-friendly Streamlit interface

### Supported Subjects

1. JAVA PROGRAMMING LANGUAGE (Practical)
2. .NET PROGRAMMING (Practical)
3. MOBILE APPLICATION DEVELOPMENT - II (Practical)
4. INTERNET OF THINGS (IOT) (Theory only)
5. ORGANIZATIONAL SOFT-SKILLS IN SOFTWARE INDUSTRY (Theory only)
6. CERTIFICATE COURSE IN WEB DESIGNING (Theory only)
7. BHARATIYA MULYA PARAMPARA - II (Theory only)

### How to Start

#### Prerequisites

Make sure Streamlit is installed:
```bash
pip install streamlit
```

#### Run the Application

```bash
# Navigate to the src directory
cd src

# Run Streamlit app
streamlit run predict.py
```

The application will open in your default browser at `http://localhost:8501`

### How to Use

1. **Enter Student Information:**
   - Seat Number
   - Student Name
   - College Name

2. **Enter Marks for Each Subject:**
   - For practical subjects (JAVA, .NET, MAD-II): Enter External Theory, External Practical, Internal Theory, Internal Practical
   - For theory-only subjects: Enter External Theory and Internal Theory

3. **Click "Generate Result & Predict"**
   - View the marksheet with all calculations
   - See your SGPA and performance prediction
   - Download PDF report

### Output Example

```
Seat Number: 12345
Name: John Doe
College: VNSGU

Total Marks: 520 / 700
SGPA: 7.43
Result: PASS
Performance: 🌟 High Performer
```

### Code Structure

```python
# Key Components:
- Page Configuration (Streamlit setup)
- Model Loading (K-means & Scaler)
- PDF Generation Function
- Student Information Input
- Subject Marks Input Functions
- Result Calculation & Prediction
- HTML Marksheet Display
- PDF Export Functionality
```

### Model Details

- **K-means Clustering Model:** Predicts performance levels (High/Average/Needs Improvement)
- **Scaler:** StandardScaler for feature normalization
- **Models Location:** `models/kmeans_model.pkl` and `models/scaler.pkl`

### Dependencies

```
streamlit
pandas
joblib
reportlab
scikit-learn
```

Install all dependencies:
```bash
pip install -r requirements.txt
```

---

### predict.py - Complete Code

```python
import streamlit as st
import pandas as pd
import joblib

# PDF libraries
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Student Result System", layout="centered")

st.title("🎓 Student Result & Performance Predictor")

# ---------------- LOAD MODELS ----------------
@st.cache_resource
def load_models():
    kmeans = joblib.load("../models/kmeans_model.pkl")
    scaler = joblib.load("../models/scaler.pkl")
    return kmeans, scaler

kmeans, scaler = load_models()

# ---------------- PDF FUNCTION ----------------
def generate_pdf(data, filename="result.pdf"):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("COLLEGE RESULT MARKSHEET", styles['Title']))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph(f"Seat Number: {data['seat']}", styles['Normal']))
    elements.append(Paragraph(f"Name: {data['name']}", styles['Normal']))
    elements.append(Paragraph(f"College: {data['college']}", styles['Normal']))
    elements.append(Spacer(1, 10))

    table_data = [["Subject", "External Theory", "External Practical", "Internal Theory", "Internal Practical", "Total Marks"]] + data["marks"]

    table = Table(table_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('GRID', (0,0), (-1,-1), 1, colors.black)
    ]))

    elements.append(table)
    elements.append(Spacer(1, 10))

    elements.append(Paragraph(f"Total Marks: {data['total']} / 700", styles['Normal']))
    elements.append(Paragraph(f"SGPA: {data['sgpa']}", styles['Normal']))
    elements.append(Paragraph(f"Result: {data['result']}", styles['Normal']))
    elements.append(Paragraph(f"Performance: {data['performance']}", styles['Normal']))

    doc.build(elements)

# ---------------- STUDENT INFO ----------------
st.subheader("👤 Student Information")

seat = st.text_input("Seat Number")
name = st.text_input("Student Name")
college = st.text_input("College Name")

# ---------------- SUBJECT INPUT ----------------
st.subheader("📊 Enter Marks")

def subject_full(subject):
    st.markdown(f"### {subject}")
    col1, col2 = st.columns(2)

    with col1:
        ext_th = st.number_input(f"{subject} External Theory", 0, key=subject+"1")
        ext_pr = st.number_input(f"{subject} External Practical", 0, key=subject+"2")

    with col2:
        int_th = st.number_input(f"{subject} Internal Theory", 0, key=subject+"3")
        int_pr = st.number_input(f"{subject} Internal Practical", 0, key=subject+"4")

    total = ext_th + ext_pr + int_th + int_pr
    return ext_th, ext_pr, int_th, int_pr, total


def subject_theory_only(subject):
    st.markdown(f"### {subject}")
    col1, col2 = st.columns(2)

    with col1:
        ext_th = st.number_input(f"{subject} External Theory", 0, key=subject+"5")

    with col2:
        int_th = st.number_input(f"{subject} Internal Theory", 0, key=subject+"6")

    total = ext_th + int_th
    return ext_th, int_th, total

# ---------------- INPUT SUBJECTS ----------------

java_ext_th, java_ext_pr, java_int_th, java_int_pr, java_total = subject_full("JAVA PROGRAMMING LANGUAGE")

net_ext_th, net_ext_pr, net_int_th, net_int_pr, net_total = subject_full(".NET PROGRAMMING")

mad_ext_th, mad_ext_pr, mad_int_th, mad_int_pr, mad_total = subject_full("MOBILE APPLICATION DEVELOPMENT - II")

iot_ext_th, iot_int_th, iot_total = subject_theory_only("INTERNET OF THINGS (IOT)")

oss_ext_th, oss_int_th, oss_total = subject_theory_only("ORGANIZATIONAL SOFT-SKILLS IN SOFTWARE INDUSTRY")

cc_ext_th, cc_int_th, cc_total = subject_theory_only("CERTIFICATE COURSE IN WEB DESIGNING")

bmp_ext_th, bmp_int_th, bmp_total = subject_theory_only("BHARATIYA MULYA PARAMPARA - II")

# ---------------- BUTTON ----------------
if st.button("🚀 Generate Result & Predict", use_container_width=True):

    # TOTAL CALCULATION
    total_marks = (
        java_total + net_total + mad_total +
        iot_total + oss_total + cc_total + bmp_total
    )

    sgpa = round((total_marks / 700) * 10, 2)
    result_status = "PASS" if total_marks >= 280 else "FAIL"

    # ---------------- ML INPUT (FIXED) ----------------
    input_data = pd.DataFrame([{
        "JAVA_Total": java_total,
        "NET_Total": net_total,
        "MAD_Total": mad_total,
        "IOT_Total": iot_total,
        "OSS_Total": oss_total,
        "CC_Total": cc_total,
        "BMP_Total": bmp_total
    }])

    scaled = scaler.transform(input_data)
    cluster = kmeans.predict(scaled)[0]

    performance_map = {
        1: "🌟 High Performer",
        0: "👍 Average Performer",
        2: "⚠️ Needs Improvement"
    }

    performance = performance_map.get(cluster, "Unknown")

    # ---------------- HTML MARKSHEET ----------------
    st.markdown("---")

    html = f"""
    <div style="border:2px solid black; padding:20px; border-radius:10px">
    <h2 style="text-align:center;">COLLEGE RESULT MARKSHEET</h2>

    <p><b>Seat Number:</b> {seat}</p>
    <p><b>Name:</b> {name}</p>
    <p><b>College:</b> {college}</p>

    <table border="1" style="width:100%; text-align:center; border-collapse: collapse;">

    <tr>
    <th>Subject</th>
    <th>External Theory</th>
    <th>External Practical</th>
    <th>Internal Theory</th>
    <th>Internal Practical</th>
    <th>Total Marks</th>
    </tr>

    <tr><td>JAVA</td><td>{java_ext_th}</td><td>{java_ext_pr}</td><td>{java_int_th}</td><td>{java_int_pr}</td><td>{java_total}</td></tr>
    <tr><td>.NET</td><td>{net_ext_th}</td><td>{net_ext_pr}</td><td>{net_int_th}</td><td>{net_int_pr}</td><td>{net_total}</td></tr>
    <tr><td>MAD-II</td><td>{mad_ext_th}</td><td>{mad_ext_pr}</td><td>{mad_int_th}</td><td>{mad_int_pr}</td><td>{mad_total}</td></tr>
    <tr><td>IOT</td><td>{iot_ext_th}</td><td>-</td><td>{iot_int_th}</td><td>-</td><td>{iot_total}</td></tr>
    <tr><td>OSS</td><td>{oss_ext_th}</td><td>-</td><td>{oss_int_th}</td><td>-</td><td>{oss_total}</td></tr>
    <tr><td>WEB DESIGNING</td><td>{cc_ext_th}</td><td>-</td><td>{cc_int_th}</td><td>-</td><td>{cc_total}</td></tr>
    <tr><td>BMP-II</td><td>{bmp_ext_th}</td><td>-</td><td>{bmp_int_th}</td><td>-</td><td>{bmp_total}</td></tr>

    </table>

    <h3>Total Marks: {total_marks} / 700</h3>
    <h3>SGPA: {sgpa}</h3>
    <h3>Result: {result_status}</h3>
    <h3>Performance: {performance}</h3>
    </div>
    <br></br>
    """

    st.markdown(html, unsafe_allow_html=True)

    # ---------------- PDF ----------------
    pdf_data = {
        "seat": seat,
        "name": name,
        "college": college,
        "marks": [
            ["JAVA", java_ext_th, java_ext_pr, java_int_th, java_int_pr, java_total],
            [".NET", net_ext_th, net_ext_pr, net_int_th, net_int_pr, net_total],
            ["MAD-II", mad_ext_th, mad_ext_pr, mad_int_th, mad_int_pr, mad_total],
            ["IOT", iot_ext_th, "-", iot_int_th, "-", iot_total],
            ["OSS", oss_ext_th, "-", oss_int_th, "-", oss_total],
            ["WEB DESIGNING", cc_ext_th, "-", cc_int_th, "-", cc_total],
            ["BMP-II", bmp_ext_th, "-", bmp_int_th, "-", bmp_total]
        ],
        "total": total_marks,
        "sgpa": sgpa,
        "result": result_status,
        "performance": performance
    }

    generate_pdf(pdf_data)

    with open("result.pdf", "rb") as f:
        st.download_button("📥 Download Result PDF", f, file_name="SEM4_Result.pdf")
```

---

## 👨‍💻 Author

**Yug Patel**  
GitHub: https://github.com/yugp5507

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests with improvements.

---

## 📝 License

This project is open source and available under the MIT License.

---

## ⭐ Support

If you found this project useful, please **star the repository** ⭐

**Want a portfolio-level upgrade?** 🔥 I can add:
- 🖼️ **Screenshots section** with key visualizations
- 🏷️ **Badges** (Python version, license, status)
- 🎬 **Live demo style README**
- 📄 **Resume description**
- 📊 **Results and findings section**

Just let me know!

---

**Last Updated:** March 2026  
**Status:** Active & Maintained ✅  
**Python Version:** 3.10+
