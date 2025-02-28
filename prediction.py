import streamlit as st
import joblib
import plotly.express as px

def run_prediction():
    # Load the model
    try:
        model = joblib.load('catboost_best_model.pkl')
    except FileNotFoundError:
        st.error("❌ Model file not found. Please ensure the model file exists.")
        return
    except Exception as e:
        st.error(f"⚠️ Error loading the model: {e}")
        return
    
    #  Set up the UI
    st.title("💳 Bank Customer Churn Prediction")
    st.markdown(
        """
        🔍 **Find out whether a customer is likely to stay or leave!**  
        Get actionable insights to **retain valuable customers** and boost engagement.  
        """
    )

    # 🔹 Sidebar for user inputs
    st.sidebar.header("📋 Enter Customer Details")
    
    # Input fields
    credit_score = st.sidebar.number_input("📊 Credit Score", min_value=0)
    age = st.sidebar.number_input("🎂 Age", min_value=0)
    tenure = st.sidebar.number_input("📅 Tenure (in years)", min_value=0)
    balance = st.sidebar.number_input("💰 Account Balance", min_value=0.0)
    num_of_products = st.sidebar.number_input("📦 Number of Products", min_value=0)
    has_credit_card = st.sidebar.selectbox("💳 Has Credit Card?", ["Yes", "No"])
    is_active_member = st.sidebar.selectbox("📈 Is Active Member?", ["Yes", "No"])
    estimated_salary = st.sidebar.number_input("💵 Estimated Salary", min_value=0.0)
    country = st.sidebar.selectbox("🌍 Country", ["Germany", "Spain", "France"])
    gender = st.sidebar.selectbox("👤 Gender", ["Male", "Female"])

    # Mapping categorical variables
    geography_germany = 1 if country == "Germany" else 0
    country_spain = 1 if country == "Spain" else 0
    country_france = 1 if country == "France" else 0
    gender = 1 if gender == "Male" else 0
    has_credit_card = 1 if has_credit_card == "Yes" else 0
    is_active_member = 1 if is_active_member == "Yes" else 0
    
    #  Prediction Button
    if st.sidebar.button("🔍 Predict Churn"):
        try:
            # Perform prediction
            prediction = model.predict([[credit_score, age, tenure, balance, 
                                         num_of_products, has_credit_card, is_active_member, 
                                         estimated_salary, geography_germany, 
                                         country_spain, gender]])
            
            probability = model.predict_proba([[credit_score, age, tenure, balance, 
                                                num_of_products, has_credit_card, is_active_member, 
                                                estimated_salary, geography_germany, 
                                                country_spain, gender]])[0][1]
            
            #  Display prediction results
            st.subheader("📊 Prediction Results")
            if prediction == 0:
                st.success(f"✅ The customer is **likely to stay**! (Exit Probability: {probability:.2%})")
                
                # Probability bar
                fig = px.bar(
                    x=["Stay", "Exit"], 
                    y=[1 - probability, probability],
                    color=["Stay", "Exit"], 
                    color_discrete_map={"Stay": "green", "Exit": "red"},
                    text=[f"{(1 - probability) * 100:.1f}%", f"{probability * 100:.1f}%"],
                    title="Churn Probability Breakdown"
                )
                st.plotly_chart(fig)
                
                #  Recommendations for Retention
                st.subheader(" Retention Strategies for Loyal Customers")
                st.markdown("""
                -  **Reward Loyalty**: Offer perks like cashback, bonuses, or VIP access.  
                -  **Enhance Communication**: Personalized emails, financial guidance, or tips.  
                -  **Increase Engagement**: Offer savings programs, investments, or special discounts.  
                -  **Expand Product Offerings**: Suggest credit cards, loans, or investment plans.  
                """)

            else:
                st.warning(f"⚠️ The customer is **likely to exit**! (Exit Probability: {probability:.2%})")

                # Probability bar
                fig = px.bar(
                    x=["Stay", "Exit"], 
                    y=[1 - probability, probability],
                    color=["Stay", "Exit"], 
                    color_discrete_map={"Stay": "green", "Exit": "red"},
                    text=[f"{(1 - probability) * 100:.1f}%", f"{probability * 100:.1f}%"],
                    title="Churn Probability Breakdown"
                )
                st.plotly_chart(fig)

                #  Recommendations to Reduce Churn
                st.subheader(" Urgent Actions to Prevent Customer Loss")
                st.markdown("""
                -  **Personalized Offers**: Discounted loan rates, waived fees, or exclusive benefits.  
                -  **Strengthen Customer Support**: Improve response times and issue resolution.  
                -  **Monitor Engagement**: Proactively check customer activity & offer assistance.  
                -  **Exclusive Retention Programs**: Provide tailored promotions for high-risk customers.  
                """)

        except Exception as e:
            st.error(f"⚠️ An error occurred during prediction: {e}")
