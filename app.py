# 🎯 Streamlit App for Salary Prediction
import streamlit as st
import joblib
import numpy as np

# 🖼️ Banner Image
st.image("assets/banner.png", use_container_width=True)

# 🎨 Custom CSS Styling
st.markdown("""
    <style>
    /* 🔷 App background */
    div[data-testid="stAppViewContainer"] {
        background: #f4f6f8;
        padding: 10px;
    }

    /* 🔶 Main content block */
    div[data-testid="stVerticalBlock"] {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        color: #2c3e50;
        box-shadow: 0px 5px 12px rgba(0, 0, 0, 0.05);
    }

    /* 🟦 Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #2c3e50;
        padding: 20px;
        border-radius: 10px;
        color: #ecf0f1;
    }

    /* 🔹 Title and Headings */
    h1, h2, h3 {
        color: #2c3e50 !important;
    }

    /* 🧮 Inputs */
    .stTextInput, .stSelectbox, .stNumberInput, .stSlider {
        background-color: #ecf0f1;
        border-radius: 10px;
        color: #2c3e50;
    }

    /* 💚 Buttons */
    div[data-testid="stButton"] > button {
        background-color: #34495e;
        color: #ecf0f1;
        border-radius: 8px;
        font-size: 16px;
    }

    div[data-testid="stButton"] > button:hover {
        background-color: #1abc9c;
        color: white;
    }

    /* ✒️ Markdown Text */
    .markdown-text-container {
        color: #2c3e50;
    }

    /* ⚙️ Fix faded labels above inputs */
    label, .stSelectbox label, .stSlider label, .stNumberInput label {
        color: #2c3e50 !important;
        font-weight: 600;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# 🧠 App Title
st.title("Employee Salary Predictor")

# 📊 Sidebar with Project Info
st.sidebar.title("📝 Project Info")
st.sidebar.markdown("Built by **M.Furqan Alam**")
st.sidebar.markdown("📦 Model Used: Random Forest")
st.sidebar.markdown("📍 Deployment: Streamlit App")
st.sidebar.markdown("🔗 Tools: Python, Joblib, NumPy")
st.sidebar.markdown("---")
st.sidebar.markdown("📧 Contact: furqanalam622@gmail.com")

# 📁 Load ML Model
model = joblib.load('salary_predictor.pkl')

# 🧩 Inputs from user
st.markdown("### 💼 Select Job Title")
job_title = st.selectbox("Select Job Title", ['Analyst', 'Manager', 'Developer', 'Consultant', 'Sales'])

st.markdown("### 📊 Select Department")
department = st.selectbox("Select Department", ['HR', 'Finance', 'IT', 'Marketing', 'Sales', 'Operations'])

st.markdown("### 🌍 Select Country")
country = st.selectbox("Select Country", ['Pakistan', 'USA', 'India', 'Germany', 'UK'])

st.markdown("### ⏳ Tenure (Years)")
tenure = st.slider("Tenure (Years)", 0, 40, 5)

st.markdown("### 🏢 Department Size")
department_size = st.slider("Department Size", 1, 500, 50)

st.markdown("### 🧮 Country Average Salary")
country_avg_salary = st.number_input("Country Average Salary", min_value=10000, max_value=300000, value=80000)

# 🔢 Manual Encoding
job_map = {'Analyst': 0, 'Manager': 1, 'Developer': 2, 'Consultant': 3, 'Sales': 4}
dept_map = {'HR': 0, 'Finance': 1, 'IT': 2, 'Marketing': 3, 'Sales': 4, 'Operations': 5}
country_map = {'Pakistan': 0, 'USA': 1, 'India': 2, 'Germany': 3, 'UK': 4}

# 🧮 Create Input Array
input_data = np.array([[tenure, department_size, country_avg_salary,
                        job_map[job_title], dept_map[department], country_map[country]]])

# 📈 Predict Salary
st.markdown("### 💰 Predicted Salary Output")
if st.button("📈 Predict Salary"):
    predicted_salary = model.predict(input_data)[0]
    st.success(f"💸 Predicted Salary: PKR {predicted_salary:,.0f}")

# 📄 Footer
st.markdown("""
    <hr style="margin-top: 40px; margin-bottom: 10px;">
    <div style='text-align: center; font-size: 14px; color: #7f8c8d;'>
        © 2025 M. Furqan Alam • Salary Predictor using Random Forest<br>
        Powered by Python, NumPy, Joblib & Streamlit
    </div>
""", unsafe_allow_html=True)