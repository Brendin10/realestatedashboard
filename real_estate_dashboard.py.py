import streamlit as st
import pandas as pd
import plotly.express as px

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
    '1 Year': [12.4, 8.7, 15.2, 11.8, 13.9, 14.1, 9.8, 10.5, 7.2, 8.9, 11.3, 6.8, 7.9, 5.4, 6.1],
    '3 Year': [48.2, 52.7, 68.4, 45.9, 55.1, 49.8, 41.3, 44.6, 38.9, 42.7, 39.4, 35.2, 33.8, 31.5, 34.1],
    '5 Year': [89.5, 81.2, 94.7, 71.3, 78.6, 76.4, 67.8, 69.2, 58.9, 65.4, 59.7, 54.3, 51.8, 48.9, 53.2]
}

df = pd.DataFrame(data)

# ====================== SIDEBAR & FILTER ======================
st.sidebar.header("Filters")
period = st.sidebar.selectbox(
    "Select Appreciation Period",
    options=["1 Year", "3 Year", "5 Year"],
    index=2  # Default to 5 Year
)

# ====================== PROCESS DATA ======================
# Get top 10 and sort ascending for the horizontal bar chart
top_10 = df.nlargest(10, period).sort_values(period, ascending=True)

# ====================== MAIN CHART ======================
fig = px.bar(
    top_10,
    x=period,
    y='City',
    orientation='h',
    title=f"Top 10 Cities by {period} Real Estate Appreciation",
    labels={period: f'{period} Appreciation (%)', 'City': ''},
    text=period,
    color=period,
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
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    margin=dict(l=20, r=20, t=60, b=20)
)

st.plotly_chart(fig, use_container_width=True)

# ====================== INSIGHTS ======================
st.subheader("📌 Key Insights")
col1, col2, col3 = st.columns(3)

top_city_name = top_10.iloc[-1]['City']
top_city_val = top_10.iloc[-1][period]

with col1:
    st.metric(label="Top City", value=top_city_name, delta=f"{top_city_val:.1f}%")

with col2:
    st.metric(label="Average Appreciation", value=f"{top_10[period].mean():.1f}%")

with col3:
    # Changed to show max value cleanly as a main metric
    st.metric(label="Highest Growth", value=f"{top_city_val:.1f}%", delta=top_city_name)

# Footer
st.caption("Note: This dashboard uses sample market data based on current real estate analytics platforms.")

# ====================== HOW TO RUN ======================
if st.checkbox("Show installation instructions"):
    st.code("""
    pip install streamlit pandas plotly
    
    # Run the dashboard:
    streamlit run real_estate_dashboard.py
    """, language="bash")
