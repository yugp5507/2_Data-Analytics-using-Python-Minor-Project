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
- [Student Result & Performance Predictor](#-student-result--performance-predictor-predictpy)
- [Installation & Running predict.py](#-installation--running-predictpy-detailed-guide)
- [Maintenance Guide](#-maintenance-guide)
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


---

## �️ Installation & Running predict.py (Detailed Guide)

### Step 1: Install Streamlit

Open your terminal and install Streamlit:

```bash
pip install streamlit
```

**Verify Installation:**
```bash
streamlit --version
```

### Step 2: Install Additional Dependencies

Ensure all required libraries are installed:

```bash
pip install pandas joblib reportlab scikit-learn
```

Or install from requirements.txt:

```bash
pip install -r requirements.txt
```

### Step 3: Verify Model Files Exist

Before running the app, check that model files exist in the `models/` directory:

```bash
# Windows
dir models\

# Mac/Linux
ls models/
```

**Required files:**
- `kmeans_model.pkl` – K-means clustering model
- `scaler.pkl` – StandardScaler for feature normalization

✅ If both files exist, you're ready to run!

### Step 4: Run the Streamlit Application

Navigate to the project directory and run:

```bash
# Option 1: Run directly from src folder
cd src
streamlit run predict.py

# Option 2: Run from project root
streamlit run src/predict.py
```

### Step 5: Access the Application

The application will automatically open in your browser at:

```
http://localhost:8501
```

**If it doesn't open automatically:**
- Open your browser
- Paste: `http://localhost:8501`

---

### 🎯 Quick Start Commands

**Single command to run everything:**

```bash
# Windows
cd src && streamlit run predict.py

# Mac/Linux
cd src && streamlit run predict.py
```

**Stop the application:**
- Press `Ctrl + C` in the terminal

---

## 🔧 Maintenance Guide

### Regular Maintenance Tasks

#### 1. **Update Dependencies**

Check for package updates:

```bash
pip list --outdated
```

Update specific packages:

```bash
pip install --upgrade streamlit pandas scikit-learn
```

Update all packages:

```bash
pip install --upgrade -r requirements.txt
```

#### 2. **Clear Streamlit Cache**

If models are loading incorrectly, clear the cache:

```bash
# Windows
rmdir /s %APPDATA%\streamlit\*.

# Mac/Linux
rm -rf ~/.streamlit/
```

#### 3. **Verify Model Integrity**

Check if model files are corrupted:

```python
import joblib

try:
    kmeans = joblib.load("models/kmeans_model.pkl")
    scaler = joblib.load("models/scaler.pkl")
    print("✅ Models loaded successfully")
except Exception as e:
    print(f"❌ Error loading models: {e}")
```

#### 4. **Monitor Application Performance**

Enable debug mode for troubleshooting:

```bash
streamlit run predict.py --logger.level=debug
```

---

### Common Maintenance Issues & Solutions

#### Issue 1: "ModuleNotFoundError: No module named 'streamlit'"

**Solution:**
```bash
pip install streamlit
```

#### Issue 2: "FileNotFoundError: models/kmeans_model.pkl"

**Solution:**
- Verify models folder exists in the project root
- Check file paths in predict.py (line 18-19)
- Ensure you're running from the correct directory

#### Issue 3: "Port 8501 already in use"

**Solution - Use a different port:**
```bash
streamlit run predict.py --server.port 8502
```

#### Issue 4: Slow Application Loading

**Solution - Increase cache settings:**

Edit predict.py and modify:
```python
@st.cache_resource
def load_models():  # Models cache across sessions
```

#### Issue 5: PDF Generation Issues

**Solution - Install ReportLab properly:**
```bash
pip install --upgrade reportlab
```

---

### 📋 Monthly Maintenance Checklist

- [ ] Update all packages: `pip install --upgrade -r requirements.txt`
- [ ] Test model predictions with sample data
- [ ] Verify PDF generation works correctly
- [ ] Check for any error messages in terminal
- [ ] Review code for deprecated functions
- [ ] Backup current models in a separate folder
- [ ] Test on different Python versions if possible

---

### 🔐 Backup & Recovery

**Create a backup of models:**

```bash
# Create backup folder
mkdir models_backup

# Copy models
copy models\*.pkl models_backup\  (Windows)
cp models/*.pkl models_backup/    (Mac/Linux)
```

**Restore from backup:**

```bash
# Copy back
copy models_backup\*.pkl models\  (Windows)
cp models_backup/*.pkl models/    (Mac/Linux)
```

---

### 📊 Performance Optimization

#### 1. **Reduce CSS Styling Size**

Minimize HTML in predict.py for faster rendering

#### 2. **Cache Model Loading**

The `@st.cache_resource` decorator already optimizes this

#### 3. **Optimize DataFrame Operations**

Use vectorized operations instead of loops

#### 4. **Monitor Memory Usage**

```bash
streamlit run predict.py --client.maxMessageSize=50
```

---

### 🐛 Debugging Tips

**Enable verbose logging:**
```bash
streamlit run predict.py --logger.level=debug
```

**Check Python version:**
```bash
python --version
```

**Verify all imports work:**
```bash
python -c "import streamlit; import pandas; import joblib; import reportlab; print('✅ All imports working')"
```

**Test the app locally:**
```bash
streamlit run predict.py --client.showErrorDetails=true
```

---

### 🚀 Deployment Considerations

Before deploying to production:

1. **Test with different datasets** – Verify model accuracy
2. **Check file permissions** – Ensure read/write access for PDF generation
3. **Monitor resource usage** – Check CPU and memory usage
4. **Update Streamlit configuration** – Set production settings:

```bash
# Increase client timeout
streamlit run predict.py --client.toolbarMode=minimal
```

5. **Secure sensitive data** – Don't expose model internals
6. **Version control models** – Keep track of model versions

---

```

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
