import streamlit as st
from PIL import Image
from pathlib import Path
from prediction import run_prediction
from dashboard import run_dashboard
from contact import app as contact_app

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

# Set page configuration
st.set_page_config(page_title="Bank Churn Prediction App", page_icon="🏦", layout="wide")

# Custom CSS for background, styling, scrollbars, and enhanced contact info interactions
st.markdown(
    """
    <style>
    body {
        background-color: #f5f7fa;
    }
    .main-title {
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        color: #2c3e50;
    }
    .sub-title {
        font-size: 20px;
        text-align: center;
        color: #7f8c8d;
        font-style: italic;
    }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        background-color: #3498db;
        color: white;
        font-size: 18px;
        padding: 10px;
    }
    .stButton>button:hover {
        background-color: #2980b9;
    }
    .sidebar-title {
        font-size: 22px;
        font-weight: bold;
        color: #34495e;
    }
    .scrollable-container {
        height: 350px;
        overflow-y: auto;
        padding: 10px;
        border: 1px solid #ddd;
        background-color: #ffffff;
        border-radius: 10px;
    }
    .faq-container {
        background-color: #2c3e50;
        padding: 15px;
        border-radius: 8px;
        color: white;
    }
    /* Contact Section Styling */
     .contact-section {
        text-align: center;
        padding: 20px;
        background-color: #2c3e50;
        border-radius: 10px;
        margin-top: 30px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        animation: float 3s ease-in-out infinite;
        overflow: visible; /* Ensure content inside isn't clipped */
    }

    .contact-section:hover {
        transform: scale(1.03);
        box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.2);
    }
    .contact-title {
        font-size: 24px;
        font-weight: bold;
        color: white;
        margin-bottom: 10px;
    }
    .contact-info {
        font-size: 18px;
        color: #7f8c8d;
        margin: 5px 0;
    }
    .contact-info a {
        color: #3498db;
        text-decoration: none;
        transition: color 0.3s ease;
    }
    .contact-info a:hover {
        color: #2980b9;
    }
    

    .contact-image:hover {
        transform: scale(1.1);
    }

    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title Section
st.markdown('<h1 class="main-title">🏦 Bank Churn Prediction App</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Gain insights into customer retention and reduce churn rates</p>', unsafe_allow_html=True)

# Layout with two columns (image + navigation)
col1, col2 = st.columns([1, 2])

with col1:
    st.image("image/bank_image.jpeg", use_column_width=True)  

with col2:
    st.sidebar.markdown('<p class="sidebar-title">🔍 Navigation</p>', unsafe_allow_html=True)
    app_mode = st.sidebar.radio("Select a page", ["🏠 Home", "🔮 Prediction", "📊 Dashboard", "❓ FAQs", "📞 Contact"])

    if app_mode == "🏠 Home":
        st.subheader("Welcome to the Bank Churn Prediction App!")
        st.write(
            """
            - **Predict customer churn** with advanced machine learning models.
            - **Analyze customer behaviors** with interactive dashboards.
            - **Enhance retention strategies** using data-driven insights.
            - **Explore literature on churn prediction** to understand key trends.
            """
        )
        st.info("Use the sidebar to navigate through different sections ⬅")

        # Scrollable Literature Review Section
        st.subheader("Literature Review on Bank Churn")
        st.markdown(
            """
            **Customer churn** has been a major challenge for financial institutions worldwide.  
            Studies indicate that **predictive models** based on **machine learning and AI**  
            significantly enhance banks’ ability to **retain customers and optimize marketing strategies**.

            - **Anderson, 2020**: Churn prediction models can reduce customer loss by up to 30%.
            - **Zhang et al., 2021**: AI-driven models outperform traditional rule-based methods.
            - **Kumar & Patel, 2019**: Personalized banking services increase retention rates.
            """
        )

    elif app_mode == "🔮 Prediction":
        run_prediction()

    elif app_mode == "📊 Dashboard":
        run_dashboard()

    elif app_mode == "❓ FAQs":
        st.subheader("❓ Frequently Asked Questions (FAQs)")
        st.markdown(
            """
            <div class="faq-container">
            <p><b>🔹 What is customer churn?</b></p>
            <p>Customer churn refers to when a customer stops using a company's service, such as closing a bank account.</p>
            
            <p><b>🔹 Why is churn prediction important?</b></p>
            <p>It helps businesses identify at-risk customers and implement strategies to retain them, saving revenue.</p>
            
            <p><b>🔹 What factors contribute to bank churn?</b></p>
            <p>Common factors include high fees, poor service, low engagement, and better offers from competitors.</p>

            <p><b>🔹 How does machine learning help in churn prediction?</b></p>
            <p>Machine learning analyzes customer behavior and predicts which customers are likely to leave.</p>
            
            <p><b>🔹 Can banks prevent churn?</b></p>
            <p>Yes, by offering loyalty programs, improving customer service, and using AI-driven retention strategies.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    elif app_mode == "📞 Contact":
        contact_app(st, current_dir, Image)
