"""
Data preparation module for GDP analysis.
Functions for loading and initial data inspection.
"""

import pandas as pd
from typing import Tuple


def load_gdp_data(
    file_path: str = "train.csv",
    test_path: str = "test.csv"
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Load GDP data from a CSV file.

    Parameters:
    file_path (str): Path to training CSV file
    test_path (str): Path to test CSV file

    Returns:
    tuple: (train_df, test_df) - Training and test dataframes
    """
    train_df = pd.read_csv(file_path)
    test_df = pd.read_csv(test_path)

    return train_df, test_df


def clean_gdp_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and reshape the GDP data for analysis.

    Parameters:
    df (pd.DataFrame): Raw GDP data

    Returns:
    pd.DataFrame: Cleaned GDP data in long format
    """
    # Keep only the columns we need
    df_clean = df.drop(['Series Name', 'Series Code', 'Country Code'],
                       axis=1)

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
