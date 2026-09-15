"""
Video Games Sales Dashboard
A comprehensive Streamlit dashboard for video game sales analysis
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Video Games Sales Dashboard",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
        .metric-card {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0;
        }
        .header-title {
            color: #1f77d2;
            font-size: 2.5em;
            font-weight: bold;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load and process the video games sales data"""
    df = pd.read_csv('video games sales.csv')
    
    # Data cleaning
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
    df = df.dropna(subset=['Year'])
    df['Year'] = df['Year'].astype(int)
    
    # Add calculated columns based on your Power BI model
    df = add_calculated_columns(df)
    
    return df

def add_calculated_columns(df):
    """Add calculated columns from the semantic model"""
    
    # Decade Released
    def get_decade(year):
        if pd.isna(year):
            return "Unknown"
        elif year < 1980:
            return "Pre-80s"
        elif 1980 <= year < 1990:
            return "80s"
        elif 1990 <= year < 2000:
            return "90s"
        elif 2000 <= year < 2010:
            return "2000s"
        elif 2010 <= year < 2020:
            return "2010s"
        else:
            return "2020s"
    
    df['Decade Released'] = df['Year'].apply(get_decade)
    
    # Game Age (relative to 2017)
    def get_game_age(year):
        if pd.isna(year):
            return "Unknown"
        game_age = 2017 - year
        if game_age <= 2:
            return "New Release (0-2 years)"
        elif game_age <= 5:
            return "Recent (3-5 years)"
        elif game_age <= 10:
            return "Modern (6-10 years)"
        elif game_age <= 20:
            return "Established (11-20 years)"
        elif game_age <= 30:
            return "Classic (21-30 years)"
        else:
            return "Vintage (30+ years)"
    
    df['Game Age'] = df['Year'].apply(get_game_age)
    
    # Sales Category
    def get_sales_category(global_sales):
        if global_sales >= 20:
            return "Blockbuster (20M+)"
        elif global_sales >= 10:
            return "Major Hit (10-20M)"
        elif global_sales >= 5:
            return "Hit (5-10M)"
        elif global_sales >= 1:
            return "Successful (1-5M)"
        elif global_sales >= 0.5:
            return "Moderate (0.5-1M)"
        elif global_sales >= 0.1:
            return "Niche (0.1-0.5M)"
        else:
            return "Low Seller (<0.1M)"
    
    df['Sales Category'] = df['Global_Sales'].apply(get_sales_category)
    
    # Franchise mapping
    franchise_mapping = {
        'FIFA': ['FIFA'],
        'Madden NFL': ['Madden'],
        'NBA': ['NBA'],
        'NHL': ['NHL'],
        'Pro Evolution Soccer': ['Pro Evolution Soccer', 'PES'],
        'Call of Duty': ['Call of Duty'],
        'Mario': ['Mario'],
        'Pokemon': ['Pokemon', 'Pokémon'],
        'Grand Theft Auto': ['Grand Theft Auto', 'GTA'],
        "Assassin's Creed": ["Assassin's Creed"],
        'Final Fantasy': ['Final Fantasy'],
        'The Sims': ['The Sims'],
        'Need for Speed': ['Need for Speed'],
        'Battlefield': ['Battlefield'],
        'Halo': ['Halo'],
        'The Legend of Zelda': ['Zelda'],
        'Resident Evil': ['Resident Evil'],
        'Metal Gear': ['Metal Gear'],
        'Tomb Raider': ['Tomb Raider'],
        'Uncharted': ['Uncharted'],
        'Music/Rhythm Games': ['Guitar Hero', 'Rock Band'],
        'Just Dance': ['Just Dance'],
        'LEGO Games': ['LEGO'],
        'Minecraft': ['Minecraft'],
        'Star Wars': ['Star Wars'],
        'Borderlands': ['Borderlands'],
        'Far Cry': ['Far Cry'],
        'Deus Ex': ['Deus Ex'],
        'HomeFront': ['HomeFront'],
    }
    
    def get_franchise(name):
        if pd.isna(name):
            return "Other"
        name_lower = str(name).lower()
        for franchise, keywords in franchise_mapping.items():
            for keyword in keywords:
                if keyword.lower() in name_lower:
                    return franchise
        return "Other"
    
    df['Franchise'] = df['Name'].apply(get_franchise)
    
    # Favorite flag
    favorite_games = ['Borderlands', 'Far Cry', 'Deus Ex', 'HomeFront']
    df['Favorite'] = df['Name'].apply(
        lambda x: 1 if any(game.lower() in str(x).lower() for game in favorite_games) else 0
    )
    
    return df

def main():
    # Header
    st.markdown("<h1 class='header-title'>🎮 Video Games Sales Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("*Comprehensive analysis of video game sales data across regions and platforms*")
    st.divider()
    
    # Load data
    try:
        df = load_data()
    except FileNotFoundError:
        st.error("❌ Could not find 'video games sales.csv'. Please ensure the CSV file is in the same directory as this script.")
        return
    
    # Sidebar filters
    with st.sidebar:
        st.header("🔍 Filters")
        
        # Year range slider
        year_range = st.slider(
            "Year Range",
            int(df['Year'].min()),
            int(df['Year'].max()),
            (int(df['Year'].min()), int(df['Year'].max()))
        )
        
        # Genre filter
        genres = st.multiselect(
            "Genre",
            sorted(df['Genre'].unique()),
            default=sorted(df['Genre'].unique())
        )
        
        # Platform filter
        platforms = st.multiselect(
            "Platform",
            sorted(df['Platform'].unique()),
            default=sorted(df['Platform'].unique())[:5]
        )
        
        # Publisher filter (top 20)
        top_publishers = df.groupby('Publisher')['Global_Sales'].sum().nlargest(20).index.tolist()
        publishers = st.multiselect(
            "Publisher (Top 20)",
            top_publishers,
            default=top_publishers[:5]
        )
    
    # Apply filters
    filtered_df = df[
        (df['Year'].between(year_range[0], year_range[1])) &
        (df['Genre'].isin(genres)) &
        (df['Platform'].isin(platforms)) &
        (df['Publisher'].isin(publishers))
    ]
    
    # Key Metrics Row
    st.subheader("📊 Key Metrics")
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("Total Games", f"{filtered_df['Name'].nunique():,}")
    
    with col2:
        global_sales = filtered_df['Global_Sales'].sum()
        st.metric("Global Sales", f"${global_sales:,.1f}M")
    
    with col3:
        na_sales = filtered_df['NA_Sales'].sum()
        st.metric("NA Sales", f"${na_sales:,.1f}M")
    
    with col4:
        eu_sales = filtered_df['EU_Sales'].sum()
        st.metric("EU Sales", f"${eu_sales:,.1f}M")
    
    with col5:
        jp_sales = filtered_df['JP_Sales'].sum()
        st.metric("JP Sales", f"${jp_sales:,.1f}M")
    
    st.divider()
    
    # Charts Row 1
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Sales by Region")
        regional_sales = pd.DataFrame({
            'Region': ['North America', 'Europe', 'Japan', 'Other'],
            'Sales': [
                filtered_df['NA_Sales'].sum(),
                filtered_df['EU_Sales'].sum(),
                filtered_df['JP_Sales'].sum(),
                filtered_df['Other_Sales'].sum()
            ]
        })
        
        fig_pie = px.pie(
            regional_sales,
            values='Sales',
            names='Region',
            color_discrete_sequence=px.colors.qualitative.Set3,
            hole=0.4
        )
        fig_pie.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig_pie, width='stretch')
    
    with col2:
        st.subheader("Top 10 Games by Global Sales")
        top_games = filtered_df.nlargest(10, 'Global_Sales')[['Name', 'Platform', 'Global_Sales']].copy()
        
        fig_bar = px.bar(
            top_games,
            x='Global_Sales',
            y='Name',
            orientation='h',
            color='Global_Sales',
            color_continuous_scale='Viridis',
            labels={'Global_Sales': 'Sales (Millions)', 'Name': 'Game'}
        )
        fig_bar.update_layout(height=500, showlegend=False)
        st.plotly_chart(fig_bar, width='stretch')
    
    st.divider()
    
    # Charts Row 2
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Global Sales by Year")
        yearly_sales = filtered_df.groupby('Year')['Global_Sales'].sum().reset_index()
        
        fig_line = px.line(
            yearly_sales,
            x='Year',
            y='Global_Sales',
            markers=True,
            title='',
            labels={'Global_Sales': 'Sales (Millions)', 'Year': 'Year'}
        )
        fig_line.update_traces(line=dict(color='#1f77d2', width=3), marker=dict(size=8))
        st.plotly_chart(fig_line, width='stretch')
    
    with col2:
        st.subheader("Global Sales by Genre")
        genre_sales = filtered_df.groupby('Genre')['Global_Sales'].sum().nlargest(10).reset_index()
        genre_sales = genre_sales.sort_values('Global_Sales')
        
        fig_genre = px.bar(
            genre_sales,
            x='Global_Sales',
            y='Genre',
            orientation='h',
            color='Global_Sales',
            color_continuous_scale='Plasma',
            labels={'Global_Sales': 'Sales (Millions)', 'Genre': 'Genre'}
        )
        fig_genre.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig_genre, width='stretch')
    
    st.divider()
    
    # Charts Row 3
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Top 10 Publishers by Sales")
        pub_sales = filtered_df.groupby('Publisher')['Global_Sales'].sum().nlargest(10).reset_index()
        pub_sales = pub_sales.sort_values('Global_Sales')
        
        fig_pub = px.bar(
            pub_sales,
            x='Global_Sales',
            y='Publisher',
            orientation='h',
            color='Global_Sales',
            color_continuous_scale='Teal',
            labels={'Global_Sales': 'Sales (Millions)', 'Publisher': 'Publisher'}
        )
        fig_pub.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig_pub, width='stretch')
    
    with col2:
        st.subheader("Sales by Category")
        category_order = [
            'Blockbuster (20M+)', 'Major Hit (10-20M)', 'Hit (5-10M)',
            'Successful (1-5M)', 'Moderate (0.5-1M)', 'Niche (0.1-0.5M)', 'Low Seller (<0.1M)'
        ]
        category_sales = filtered_df.groupby('Sales Category').size().reindex(
            [cat for cat in category_order if cat in filtered_df['Sales Category'].unique()],
            fill_value=0
        ).reset_index()
        category_sales.columns = ['Category', 'Count']
        
        fig_category = px.bar(
            category_sales,
            x='Category',
            y='Count',
            color='Count',
            color_continuous_scale='Blues',
            labels={'Count': 'Number of Games', 'Category': 'Sales Category'}
        )
        fig_category.update_layout(height=400, showlegend=False, xaxis_tickangle=-45)
        st.plotly_chart(fig_category, width='stretch')
    
    st.divider()
    
    # Charts Row 4
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Sales by Platform")
        platform_sales = filtered_df.groupby('Platform')['Global_Sales'].sum().nlargest(15).reset_index()
        platform_sales = platform_sales.sort_values('Global_Sales')
        
        fig_plat = px.bar(
            platform_sales,
            x='Global_Sales',
            y='Platform',
            orientation='h',
            color='Global_Sales',
            color_continuous_scale='Oranges',
            labels={'Global_Sales': 'Sales (Millions)', 'Platform': 'Platform'}
        )
        fig_plat.update_layout(height=450, showlegend=False)
        st.plotly_chart(fig_plat, width='stretch')
    
    with col2:
        st.subheader("Franchise Performance")
        franchise_sales = filtered_df[filtered_df['Franchise'] != 'Other'].groupby('Franchise')['Global_Sales'].sum().nlargest(10).reset_index()
        franchise_sales = franchise_sales.sort_values('Global_Sales')
        
        fig_fran = px.bar(
            franchise_sales,
            x='Global_Sales',
            y='Franchise',
            orientation='h',
            color='Global_Sales',
            color_continuous_scale='Reds',
            labels={'Global_Sales': 'Sales (Millions)', 'Franchise': 'Franchise'}
        )
        fig_fran.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig_fran, width='stretch')
    
    st.divider()
    
    # Data Table
    st.subheader("📋 Detailed Game Data")
    
    display_df = filtered_df[[
        'Name', 'Platform', 'Year', 'Genre', 'Publisher',
        'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales'
    ]].copy()
    
    display_df = display_df.sort_values('Global_Sales', ascending=False)
    
    # Formatters
    display_df['NA_Sales'] = display_df['NA_Sales'].round(2)
    display_df['EU_Sales'] = display_df['EU_Sales'].round(2)
    display_df['JP_Sales'] = display_df['JP_Sales'].round(2)
    display_df['Other_Sales'] = display_df['Other_Sales'].round(2)
    display_df['Global_Sales'] = display_df['Global_Sales'].round(2)
    
    st.dataframe(
        display_df,
        width='stretch',
        height=400
    )
    
    # Download button
    csv = display_df.to_csv(index=False)
    st.download_button(
        label="📥 Download filtered data as CSV",
        data=csv,
        file_name=f"video_games_sales_{datetime.now().strftime('%Y%m%d')}.csv",
        mime="text/csv"
    )
    
    st.divider()
    st.caption("Dashboard created with Streamlit | Data sourced from video_games_sales.csv")

if __name__ == "__main__":
    main()
