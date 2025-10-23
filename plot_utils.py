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