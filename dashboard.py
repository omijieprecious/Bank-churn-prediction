import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

# Load the dataset
@st.cache_data
def load_data():
    return pd.read_csv('Bank Customer Churn Prediction.csv')

def run_dashboard():
    st.title("Customer Churn Dashboard")
    data = load_data()

    # Show dataset
    if st.checkbox("Show Raw Data"):
        st.write(data.head())

    # Summary Statistics
    st.subheader(" Dataset Summary")
    st.write(data.describe())


    # Churn Distribution (Pie Chart)
    st.subheader("Churn Distribution")
    churn_counts = data['churn'].value_counts()

    # Mapping churn values to labels
    churn_labels = {0: "Stayed (Not Churned)", 1: "Exited (Churned)"}

    fig_pie = px.pie(values=churn_counts, 
                    names=[churn_labels[idx] for idx in churn_counts.index],  # Replacing 0 & 1 with labels
                    color=churn_counts.index, 
                    color_discrete_map={0: 'green', 1: 'red'},
                    title="Percentage of Customers Who Churned vs. Stayed")


    st.plotly_chart(fig_pie)



    # Churn Distribution (Bar Chart)
    st.subheader("📊 Churn Count Plot")
    churn_counts = data['churn'].value_counts()

    fig_bar = px.bar(
        x=['Stayed (Not Churned)', 'Exited (Churned)'],
        y=churn_counts.values,
        text=churn_counts.values,
        labels={'x': 'Churn Status', 'y': 'Count'},
        color=['Stayed (Not Churned)', 'Exited (Churned)'],
        color_discrete_map={'Stayed (Not Churned)': 'green', 'Exited (Churned)': 'red'},
        title="Churn Count Distribution"
    )
    st.plotly_chart(fig_bar)

    # Age Distribution (Histogram)
    st.subheader("📊 Age Distribution")
    fig_age = px.histogram(
        data, x='age', nbins=30, color_discrete_sequence=['blue'],
        title="Age Distribution of Customers",
        marginal="box"  # Adds a small box plot for additional insights
    )
    st.plotly_chart(fig_age)


    # Interactive Scatter Plot: Balance vs. Estimated Salary
    st.subheader("Balance vs Estimated Salary")
    fig_scatter = px.scatter(data, x="balance", y="estimated_salary", color="churn",
                             title="Balance vs Estimated Salary (Colored by Churn)")
    st.plotly_chart(fig_scatter)

    # Balance vs. Churn (Box Plot)
    st.subheader("Balance Distribution by Churn")
    fig_box = px.box(data, x="churn", y="balance", color="churn",
                     labels={"churn": "Churn (0 = No, 1 = Yes)", "balance": "Balance Amount"})
    st.plotly_chart(fig_box)

    # Churn by Gender
    st.subheader("Churn by Gender")
    fig_gender = px.histogram(data, x="gender", color="churn", barmode="group", text_auto=True)
    st.plotly_chart(fig_gender)

    # Churn by Country
    st.subheader("Churn by Country")
    country_counts = data.groupby(['country', 'churn']).size().reset_index(name="Count")
    fig_country = px.bar(country_counts, x="country", y="Count", color="churn",
                         labels={"churn": "Churn Status", "country": "Country"},
                         title="Churn Distribution by Country")
    st.plotly_chart(fig_country)
