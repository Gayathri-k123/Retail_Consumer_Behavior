# 🛍️ Retail Consumer Behavior Analysis
### Data Analytics & Machine Learning Project

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python) ![Pandas](https://img.shields.io/badge/Pandas-2.0-darkblue?style=for-the-badge&logo=pandas) ![ScikitLearn](https://img.shields.io/badge/ScikitLearn-1.3-orange?style=for-the-badge&logo=scikit-learn) ![Streamlit](https://img.shields.io/badge/Streamlit-1.28-red?style=for-the-badge&logo=streamlit) ![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?style=for-the-badge&logo=jupyter)

---

## 🎯 Business Problem
> **"How can a retail company leverage consumer shopping data to identify trends, improve customer engagement, and optimize marketing and product strategies?"**

A leading retail company noticed changes in purchasing patterns across demographics, product categories, and sales channels. They needed data-driven insights to improve sales, customer satisfaction, and long-term loyalty.

---

## 👩‍💻 My Role & Responsibilities
As a **Data Analyst** on this project, I was responsible for:
- ✅ Cleaning and preparing raw customer data
- ✅ Performing exploratory data analysis with 10 charts
- ✅ Building machine learning model to predict customer loyalty
- ✅ Creating interactive business dashboard
- ✅ Delivering 6 actionable business recommendations

---

## 📊 Dataset Overview
| Detail | Info |
|---|---|
| **Source** | Kaggle - Consumer Behavior Dataset |
| **Total Customers** | 3,900 |
| **Total Features** | 18 |
| **Missing Values Found** | 37 |
| **Missing Values Fixed** | ✅ Mean Imputation |
| **Duplicate Records** | 0 |

---

## 🛠️ Tech Stack
| Category | Technology |
|---|---|
| **Language** | Python 3.11 |
| **Data Analysis** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn, Plotly |
| **Machine Learning** | Scikit-learn |
| **Dashboard** | Streamlit |
| **Environment** | Virtual Environment (venv) |
| **IDE** | VS Code + Jupyter Notebook |
| **Version Control** | Git & GitHub |

---

## 📁 Project Structure
retail_project/

│

├── 📁 data/

│   ├── customer_shopping_behavior.csv

│   ├── cleaned_data.csv

│   └── loyalty_model.pkl

│

├── 📁 notebooks/

│   ├── 01_cleaning.ipynb

│   ├── 02_eda.ipynb

│   └── 03_ml_model.ipynb

│

├── 📁 dashboard/

│   └── app.py

│

├── .gitignore

└── README.md

---

## 🔄 Project Workflow
Raw Data (3,900 customers)

↓

Phase 1: Data Cleaning

↓

Phase 2: Exploratory Data Analysis

↓

Phase 3: Machine Learning Model

↓

Phase 4: Interactive Dashboard

↓

6 Business Recommendations ✅

---

## ✅ Phase 1 — Data Cleaning
**File:** `notebooks/01_cleaning.ipynb`
- Loaded raw dataset with 3,900 rows and 18 columns
- Identified **37 missing values** in Review Rating column
- Fixed missing values using **mean imputation** technique
- Verified **zero duplicate** records across entire dataset
- Saved final cleaned dataset for further analysis

`Pandas` `NumPy` `Data Quality` `Missing Value Treatment`

---

## ✅ Phase 2 — Exploratory Data Analysis
**File:** `notebooks/02_eda.ipynb`

| # | Chart | Business Question |
|---|---|---|
| 1 | Gender Distribution | Who are our customers? |
| 2 | Age Distribution | What age group shops most? |
| 3 | Product Categories | What products sell most? |
| 4 | Sales by Season | When do customers buy? |
| 5 | Payment Methods | How do customers pay? |
| 6 | Discount Impact | Do discounts increase spending? |
| 7 | Review Ratings | How satisfied are customers? |
| 8 | Purchase Amount | How much do they spend? |
| 9 | Subscription Status | How many are subscribers? |
| 10 | Purchase Frequency | How often do they shop? |

`Matplotlib` `Seaborn` `Plotly` `Data Visualization` `Statistical Analysis`

---

## ✅ Phase 3 — Machine Learning Model
**File:** `notebooks/03_ml_model.ipynb`
- Created target variable **Loyal Customer** based on Previous Purchases median
- Applied **Label Encoding** on 7 categorical variables
- Selected **10 most relevant features** for prediction
- Split data into **80% training / 20% testing**
- Trained **Random Forest Classifier** with 100 decision trees
- Evaluated model with accuracy score, classification report, confusion matrix
- Visualized **Feature Importance** to identify loyalty drivers
- Saved trained model as **loyalty_model.pkl**

`Scikit-learn` `Random Forest` `Feature Engineering` `Model Evaluation`

---

## ✅ Phase 4 — Interactive Dashboard
**File:** `dashboard/app.py`
- **4 KPI Cards:** Total Customers, Average Purchase, Average Rating, Total Revenue
- **Sidebar Filters:** Season, Category, Gender with real-time updates
- **6 Interactive Charts** with zoom and hover features
- **ML Insights Section:** Loyal vs Regular customers and Feature importance

`Streamlit` `Plotly` `Dashboard Design` `Business Reporting`

---

## 📈 Key Findings

### 👥 Customer Demographics
- **68% Male customers** — Female segment is untapped opportunity
- **Peak age group: 25-45 years** — Working professionals dominate
- Customers spread across **50 different locations**

### 🛒 Shopping Behavior
- **Clothing** is the number 1 most purchased category
- Sales **consistent across all 4 seasons**
- **Credit Card** is most preferred payment method
- Discounts show **higher purchase amounts**

### ⭐ Customer Satisfaction
- Average review rating: **3.75 out of 5**
- Only **27% customers** have active subscriptions
- **Monthly buyers** are most frequent segment

### 🤖 ML Model Insights
Top 4 factors driving customer loyalty:
1. 💰 Purchase Amount — High spenders are more loyal
2. 👤 Age — Certain age groups show higher loyalty
3. ⭐ Review Rating — Satisfied customers stay longer
4. 🏷️ Discount Applied — Discounts build repeat behavior

---

## 💡 Business Recommendations

| # | Recommendation | Expected Impact |
|---|---|---|
| 1 | Launch Female targeted campaigns | Grow female segment to 45% |
| 2 | Create Premium Loyalty Program | Increase retention by 20% |
| 3 | Improve product quality | Push ratings above 4.5 stars |
| 4 | Convert shoppers to subscribers | Increase subscriptions to 40% |
| 5 | Focus on 25-45 age group marketing | Maximize marketing ROI |
| 6 | Introduce seasonal promotions | Boost year-round revenue |

---

## 🚀 How to Run

``bash
# Clone repository
git clone https://github.com/yourusername/retail_project.git
cd retail_project

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install libraries
pip install pandas numpy matplotlib seaborn plotly scikit-learn streamlit jupyter ipykernel

# Run dashboard
cd dashboard
streamlit run app.py
```

---

## 📂 Skills Demonstrated
Technical Skills:          Analytical Skills:

✅ Python                  ✅ Data Storytelling

✅ Data Cleaning           ✅ Business Problem Solving

✅ Data Visualization      ✅ Translating Data to Insights

✅ Machine Learning        ✅ Actionable Recommendations

✅ Streamlit Dashboard     ✅ End-to-End Project Management

✅ Git & GitHub

---

## 🎯 Project Outcome
- ✅ Identified key customer segments and demographics
- ✅ Discovered factors that drive purchasing decisions
- ✅ Built predictive ML model for customer loyalty
- ✅ Created interactive real-time business dashboard
- ✅ Provided 6 data-driven actionable recommendations
- ✅ Delivered complete end-to-end data analytics solution


> ⭐ **If you found this project useful, please give it a star!** ⭐
> 💼 **Actively looking for Data Analyst opportunities!**

