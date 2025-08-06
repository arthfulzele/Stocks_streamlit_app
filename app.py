import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set Streamlit page config
st.set_page_config(page_title="Nifty Stocks Dashboard", layout="wide")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("Nifty_Stocks.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data()

# Title
st.title("📈 Nifty Stocks Interactive Dashboard")

# Sidebar filters
st.sidebar.header("Filter Options")

# Unique Categories
categories = df['Category'].dropna().unique()
selected_category = st.sidebar.selectbox("Select a Category", sorted(categories))

# Filter symbols based on selected category
filtered_df = df[df['Category'] == selected_category]
symbols = filtered_df['Symbol'].dropna().unique()
selected_symbol = st.sidebar.selectbox("Select a Symbol", sorted(symbols))

# Filter final data
final_df = filtered_df[filtered_df['Symbol'] == selected_symbol]

# Show basic info
st.subheader(f"Showing Data for: {selected_symbol} ({selected_category})")
st.dataframe(final_df.sort_values('Date', ascending=False).head(10), use_container_width=True)

# Plot
st.subheader("📊 Stock Price Over Time")

fig, ax = plt.subplots(figsize=(14, 6))
sns.lineplot(data=final_df, x='Date', y='Close', ax=ax)
ax.set_title(f"{selected_symbol} Closing Price Over Time", fontsize=16)
ax.set_xlabel("Date")
ax.set_ylabel("Close Price")
st.pyplot(fig)

# Optional: Show entire dataset toggle
with st.expander("🔍 View Full Dataset"):
    st.dataframe(final_df, use_container_width=True)
