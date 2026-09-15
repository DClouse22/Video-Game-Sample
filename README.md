# 🎮 Video Games Sales Dashboard

A comprehensive interactive dashboard for analyzing video game sales data across multiple regions, platforms, and genres. Built with Streamlit and Plotly for fast, interactive visualizations.

## Features

✨ **Interactive Filters**
- Filter by year range, genre, platform, and publisher
- Real-time data updates as you adjust filters

📊 **Key Metrics**
- Total games count
- Global sales by region (NA, EU, JP, Other)
- Regional breakdowns

📈 **Rich Visualizations**
- Regional sales distribution (pie chart)
- Top 10 games by global sales
- Sales trends over time (line chart)
- Genre performance (top 10)
- Publisher rankings
- Sales categories breakdown
- Platform performance
- Franchise analysis

📋 **Data Export**
- View detailed game data in an interactive table
- Download filtered results as CSV

## Data Features

The dashboard calculates the following metrics from your raw data:

- **Game Age**: Classification of games by release date (New Release, Recent, Modern, Established, Classic, Vintage)
- **Decade Released**: Groups games by decade released
- **Sales Category**: Classifies games by sales performance (Blockbuster, Major Hit, Hit, Successful, Moderate, Niche, Low Seller)
- **Franchise**: Automatically identifies popular game franchises
- **Favorite Games**: Highlights your favorite games (Borderlands, Far Cry, Deus Ex, HomeFront)

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone the repository** (or create your own)
   ```bash
   git clone https://github.com/yourusername/video-games-dashboard.git
   cd video-games-dashboard
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare your data**
   - Place your `video_games_sales.csv` file in the same directory as the script
   - The CSV should have these columns: Rank, Name, Platform, Year, Genre, Publisher, NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales

## Usage

Run the dashboard locally:

```bash
streamlit run video_games_dashboard.py
```

The application will open in your default web browser at `http://localhost:8501`

## Deploying to Streamlit Cloud

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository and the `video_games_dashboard.py` file
   - Click "Deploy"

**Note**: Make sure your `video_games_sales.csv` is committed to the GitHub repository.

## Project Structure

```
video-games-dashboard/
├── video_games_dashboard.py    # Main Streamlit application
├── video_games_sales.csv       # Data file (add this)
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## Data Source

The dashboard expects a CSV file with video game sales data. Columns required:
- `Rank`: Game ranking
- `Name`: Game title
- `Platform`: Gaming platform (PS2, X360, DS, etc.)
- `Year`: Release year
- `Genre`: Game genre
- `Publisher`: Game publisher
- `NA_Sales`: North American sales in millions
- `EU_Sales`: European sales in millions
- `JP_Sales`: Japanese sales in millions
- `Other_Sales`: Other regions sales in millions
- `Global_Sales`: Total global sales in millions

## Customization

### Modify Franchises
Edit the `franchise_mapping` dictionary in the `add_calculated_columns()` function to add or modify franchise detection.

### Change Favorite Games
Update the `favorite_games` list in `add_calculated_columns()` to highlight your favorite games:
```python
favorite_games = ['Your Game 1', 'Your Game 2', 'Your Game 3']
```

### Adjust Sales Categories
Modify the thresholds in the `get_sales_category()` function to customize how games are categorized.

### Color Schemes
Change `color_continuous_scale` and `color_discrete_sequence` parameters in chart functions to modify visualization colors.

## Performance Tips

- The dataset is cached on first load using Streamlit's `@st.cache_data` decorator
- Filtering happens in-memory for instant updates
- Large datasets may benefit from reducing the number of games displayed in tables

## Troubleshooting

### "FileNotFoundError: Could not find 'video_games_sales.csv'"
- Ensure `video_games_sales.csv` is in the same directory as `video_games_dashboard.py`
- Check the file name matches exactly (case-sensitive on Linux/Mac)

### Charts not displaying
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Try clearing Streamlit cache: `streamlit cache clear`

### Slow performance
- Try reducing the year range in filters
- Reduce the number of platforms selected

## Requirements

- `streamlit`: Web app framework
- `pandas`: Data manipulation and analysis
- `plotly`: Interactive visualizations
- `numpy`: Numerical computing

See `requirements.txt` for version specifications.

## Future Enhancements

Potential improvements:
- [ ] Add regional comparison charts
- [ ] Implement time-series forecasting
- [ ] Add heatmaps for platform-genre analysis
- [ ] Include game rating/reviews if data available
- [ ] Add export to PDF functionality
- [ ] Implement custom date range picker

## License

This project is open source and available under the MIT License.

## Author

Created as a Streamlit dashboard for video game sales analysis.

## Support

For issues or suggestions, please open an issue on GitHub.

---

**Last Updated**: 2024
**Dashboard Version**: 1.0
