import matplotlib.pyplot as plt

def plot_gdp_comparison(df, countries=None):
    """
    Plot GDP comparison over time for multiple countries.
    
    Parameters:
    df (pd.DataFrame): Cleaned GDP data
    countries (list): List of countries to plot (optional, plots all if None)
    """
    if countries:
        df_plot = df[df['Country Name'].isin(countries)]
    else:
        df_plot = df
    
    plt.figure(figsize=(12, 6))
    
    for country in df_plot['Country Name'].unique():
        country_data = df_plot[df_plot['Country Name'] == country]
        plt.plot(country_data['Year'], country_data['GDP_Trillions'], 
                marker='o', label=country)
    
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('GDP (Trillions USD)', fontsize=12)
    plt.title('GDP Comparison Across Countries (2002-2022)', fontsize=14)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    return plt

def plot_gdp_growth_rate(df):
    """
    Plot GDP growth rate over time for each country.
    
    Parameters:
    df (pd.DataFrame): Cleaned GDP data
    """
    plt.figure(figsize=(12, 6))
    
    for country in df['Country Name'].unique():
        country_data = df[df['Country Name'] == country].sort_values('Year')
        
        # Calculate year-over-year growth rate
        growth_rate = country_data['GDP_Trillions'].pct_change() * 100
        
        plt.plot(country_data['Year'].iloc[1:], growth_rate.iloc[1:], 
                marker='o', label=country, alpha=0.7)
    
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('GDP Growth Rate (%)', fontsize=12)
    plt.title('Year-over-Year GDP Growth Rate (2002-2022)', fontsize=14)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='black', linestyle='--', linewidth=0.8)
    plt.tight_layout()
    
    return plt