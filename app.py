import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Page config
st.set_page_config(page_title="Netflix Content Analysis", layout="wide")

# Title
st.title("Netflix Content Analysis Dashboard")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("netflix_cleaned_data.csv")
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")

content_type = st.sidebar.multiselect(
    "Select Content Type",
    options=df["type"].unique(),
    default=df["type"].unique()
)

df = df[df["type"].isin(content_type)]

# =============================
# 1. Movies vs TV Shows
# =============================
st.subheader("📊 Movies vs TV Shows")

type_count = df["type"].value_counts()

fig1, ax1 = plt.subplots()
type_count.plot(kind="bar", ax=ax1)
ax1.set_xlabel("Type")
ax1.set_ylabel("Count")
ax1.set_title("Movies vs TV Shows")

st.pyplot(fig1)

# =============================
# 2. Top 10 Countries
# =============================
st.subheader("🌍 Top 10 Countries by Content")

top_countries = df["country"].value_counts().head(10)

fig2, ax2 = plt.subplots()
top_countries.plot(kind="barh", ax=ax2)
ax2.set_xlabel("Count")
ax2.set_ylabel("Country")
ax2.set_title("Top 10 Countries")

st.pyplot(fig2)

# =============================
# 3. Content Added by Year
# =============================
st.subheader("📅 Content Added by Year")

year_count = df["year_added"].value_counts().sort_index()

fig3, ax3 = plt.subplots()
year_count.plot(kind="line", marker="o", ax=ax3)
ax3.set_xlabel("Year")
ax3.set_ylabel("Count")
ax3.set_title("Content Added Over the Years")

st.pyplot(fig3)

# Footer
st.markdown("---")
st.markdown("👩‍💻 **Developed by Anitha** | Netflix Data Analysis Project")
