import pandas as pd

def load_gdp_data(file_path):
    """
    Load GDP data from a CSV file.
    
    Parameters:
    file_path (str): Path to the CSV file
    
    Returns:
    pd.DataFrame: Raw GDP data
    """
    df = pd.read_csv(file_path)
    return df

def clean_gdp_data(df):
    """
    Clean and reshape the GDP data for analysis.
    
    Parameters:
    df (pd.DataFrame): Raw GDP data
    
    Returns:
    pd.DataFrame: Cleaned GDP data in long format
    """
    # Keep only the columns we need
    # Drop the first two columns (Series Name and Series Code)
    df_clean = df.drop(['Series Name', 'Series Code', 'Country Code'], axis=1)
    
    # Melt the dataframe to convert years from columns to rows
    df_long = df_clean.melt(id_vars=['Country Name'], 
                             var_name='Year', 
                             value_name='GDP')
    
    # Clean the year column - remove the "[YR2002]" format
    df_long['Year'] = df_long['Year'].str.extract(r'(\d{4})')[0].astype(int)

    # Convert GDP to numeric (in case there are any issues)
    df_long['GDP'] = pd.to_numeric(df_long['GDP'], errors='coerce')

    # Drop any rows with missing GDP values
    df_long = df_long.dropna(subset=['GDP'])

    # Convert GDP from current US$ to trillions for easier reading
    df_long['GDP_Trillions'] = df_long['GDP'] / 1e12
    
    return df_long