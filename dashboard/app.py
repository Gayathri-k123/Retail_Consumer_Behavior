import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Page Config
st.set_page_config(page_title="Retail Dashboard", layout="wide")

# Load Data
df = pd.read_csv('../data/cleaned_customer_shopping_behavior.csv')

# Title
st.title("🛍️ Retail Consumer Behavior Dashboard")
st.markdown("Analyze shopping trends and customer behavior")

# Sidebar Filters
st.sidebar.header("Filters")
season = st.sidebar.multiselect("Select Season", 
         options=df['Season'].unique(), 
         default=df['Season'].unique())

category = st.sidebar.multiselect("Select Category", 
           options=df['Category'].unique(), 
           default=df['Category'].unique())

gender = st.sidebar.multiselect("Select Gender", 
         options=df['Gender'].unique(), 
         default=df['Gender'].unique())

# Filter Data
filtered_df = df[
    (df['Season'].isin(season)) & 
    (df['Category'].isin(category)) & 
    (df['Gender'].isin(gender))
]

# KPI Cards
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Customers", len(filtered_df))
col2.metric("Avg Purchase ($)", round(filtered_df['Purchase Amount (USD)'].mean(), 2))
col3.metric("Avg Rating", round(filtered_df['Review Rating'].mean(), 2))
col4.metric("Total Revenue ($)", round(filtered_df['Purchase Amount (USD)'].sum(), 2))

st.markdown("---")

# Row 1 - Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("Gender Distribution")
    fig1 = px.pie(filtered_df, names='Gender', 
                  color_discrete_sequence=['skyblue','pink'])
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("Category Distribution")
    fig2 = px.bar(filtered_df['Category'].value_counts().reset_index(), 
                  x='Category', y='count')
    st.plotly_chart(fig2, use_container_width=True)

# Row 2 - Charts
col3, col4 = st.columns(2)

with col3:
    st.subheader("Age Distribution")
    fig3 = px.histogram(filtered_df, x='Age', nbins=20, 
                        color_discrete_sequence=['orange'])
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    st.subheader("Season Distribution")
    fig4 = px.bar(filtered_df['Season'].value_counts().reset_index(), 
                  x='Season', y='count', 
                  color_discrete_sequence=['green'])
    st.plotly_chart(fig4, use_container_width=True)

# Row 3 - Charts
col5, col6 = st.columns(2)

with col5:
    st.subheader("Payment Method")
    fig5 = px.bar(filtered_df['Payment Method'].value_counts().reset_index(), 
                  x='Payment Method', y='count')
    st.plotly_chart(fig5, use_container_width=True)

with col6:
    st.subheader("Discount Impact on Purchase Amount")
    fig6 = px.box(filtered_df, x='Discount Applied', y='Purchase Amount (USD)')
    st.plotly_chart(fig6, use_container_width=True)
# Machine Learning Section
st.markdown("---")
st.header("🤖 Machine Learning Insights")

import joblib
from sklearn.preprocessing import LabelEncoder

# Load the saved model
model = joblib.load('../data/loyalty_model.pkl')

# Recreate Loyal_Customer column for full df
median_purchases = df['Previous Purchases'].median()
df['Loyal_Customer'] = (df['Previous Purchases'] > median_purchases).astype(int)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Loyal vs Regular Customers")
    loyal_counts = df['Loyal_Customer'].value_counts()
    fig7 = px.pie(values=loyal_counts.values, 
                  names=['Regular','Loyal'],
                  color_discrete_sequence=['lightcoral','lightgreen'])
    st.plotly_chart(fig7, use_container_width=True)

with col2:
    st.subheader("Feature Importance")
    
    le = LabelEncoder()
    df['Gender_enc'] = le.fit_transform(df['Gender'])
    df['Category_enc'] = le.fit_transform(df['Category'])
    df['Season_enc'] = le.fit_transform(df['Season'])
    df['Discount_enc'] = le.fit_transform(df['Discount Applied'])
    df['Promo_enc'] = le.fit_transform(df['Promo Code Used'])
    df['Payment_enc'] = le.fit_transform(df['Payment Method'])
    df['Subscription_enc'] = le.fit_transform(df['Subscription Status'])

    feature_cols = ['Age', 'Gender_enc', 'Purchase Amount (USD)', 
                     'Category_enc', 'Season_enc', 'Discount_enc', 
                     'Promo_enc', 'Payment_enc', 'Subscription_enc',
                     'Review Rating']
    
    importance = pd.Series(model.feature_importances_, index=feature_cols)
    importance = importance.sort_values(ascending=False)
    
    fig8 = px.bar(x=importance.values, y=importance.index, orientation='h',
                  labels={'x':'Importance','y':'Feature'})
    st.plotly_chart(fig8, use_container_width=True)

st.info("💡 **Business Insight:** The features above show what factors most influence customer loyalty. Focus marketing efforts on these top factors!")

# Footer
st.markdown("---")
st.markdown("Dashboard created using Streamlit | Retail Consumer Behavior Project")