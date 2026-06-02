#!/usr/bin/env python
# coding: utf-8

# In[5]:

# ====================== PAGE CONFIG ======================
st.set_page_config(
    page_title="Real Estate Appreciation Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("🏠 Top 10 U.S. Cities by Real Estate Appreciation")
st.markdown("### Select a time period to see the current market leaders")

# ====================== SAMPLE DATA ======================
data = {
    'City': [
        'Miami, FL', 'Austin, TX', 'Boise, ID', 'Raleigh, NC', 'Tampa, FL',
        'Orlando, FL', 'Phoenix, AZ', 'Nashville, TN', 'Las Vegas, NV',
        'Charlotte, NC', 'Jacksonville, FL', 'Denver, CO', 'Atlanta, GA',
        'Dallas, TX', 'Salt Lake City, UT'
    ],
    '1_Year': [12.4, 8.7, 15.2, 11.8, 13.9, 14.1, 9.8, 10.5, 7.2, 8.9, 11.3, 6.8, 7.9, 5.4, 6.1],
    '3_Year': [48.2, 52.7, 68.4, 45.9, 55.1, 49.8, 41.3, 44.6, 38.9, 42.7, 39.4, 35.2, 33.8, 31.5, 34.1],
    '5_Year': [89.5, 81.2, 94.7, 71.3, 78.6, 76.4, 67.8, 69.2, 58.9, 65.4, 59.7, 54.3, 51.8, 48.9, 53.2]
}

df = pd.DataFrame(data)

# ====================== SIDEBAR ======================
st.sidebar.header("Filters")
period = st.sidebar.selectbox(
    "Select Appreciation Period",
    options=["1 Year", "3 Year", "5 Year"],
    index=2  # Default to 5 Year
)

# Map selection to column name
period_map = {
    "1 Year": "1_Year",
    "3 Year": "3_Year",
    "5 Year": "5_Year"
}

selected_column = period_map[period]

# ====================== PROCESS DATA ======================
top_10 = df.nlargest(10, selected_column).copy()
top_10 = top_10.sort_values(selected_column, ascending=True)  # For better bar chart display

# ====================== MAIN CHART ======================
fig = px.bar(
    top_10,
    x=selected_column,
    y='City',
    orientation='h',
    title=f"Top 10 Cities by {period} Real Estate Appreciation (2025)",
    labels={selected_column: f'{period} Appreciation (%)', 'City': ''},
    text=selected_column,
    color=selected_column,
    color_continuous_scale='Viridis'
)

fig.update_traces(
    texttemplate='%{text:.1f}%',
    textposition='outside',
    marker_line_color='rgb(8,48,107)',
    marker_line_width=1.5
)

fig.update_layout(
    height=600,
    title_font_size=22,
    xaxis_title_font_size=14,
    yaxis_title_font_size=14,
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    margin=dict(l=20, r=20, t=60, b=20)
)

st.plotly_chart(fig, use_container_width=True)

# ====================== INSIGHTS ======================
st.subheader("📌 Key Insights")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Top City", top_10.iloc[-1]['City'], 
              f"{top_10.iloc[-1][selected_column]:.1f}%")

with col2:
    st.metric("Average Appreciation", 
              f"{top_10[selected_column].mean():.1f}%")

with col3:
    st.metric("Highest Growth", 
              f"{top_10[selected_column].max():.1f}%", 
              f"{top_10.iloc[-1]['City']}")

# Footer
st.caption("Note: This dashboard uses sample market data based on 2024–2025 trends from major real estate analytics platforms.")

# ====================== HOW TO RUN ======================
if st.checkbox("Show installation instructions"):
    st.code("""
    pip install streamlit pandas plotly
    
    # Run the dashboard:
    streamlit run real_estate_dashboard.py
    """, language="bash")


# In[1]:


get_ipython().system('pip install streamlit pandas plotly')


# In[7]:


get_ipython().system('streamlit run real_estate_dashboard.py')


# In[ ]:




