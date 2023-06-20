import pandas as pd
import sqlite3

def extract_data(db_path, query):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def check_data_quality(df):
    result = {}

    # Check for missing values
    result['missing_values'] = df.isnull().sum().to_dict()

    # Check for duplicates
    result['duplicates'] = df.duplicated().sum()

    # Check ranges of numerical columns
    for col in ['year', 'mileage', 'price']:
        if col in df.columns:
            result[col + '_range'] = [df[col].min(), df[col].max()]

    # Check for empty strings in string columns
    for col in ['make', 'model']:
        if col in df.columns:
            result['empty_strings_in_' + col] = df[df[col] == ''].shape[0]

    return result
