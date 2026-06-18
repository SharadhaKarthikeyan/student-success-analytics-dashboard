import pandas as pd
import numpy as np
import os

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(BASE_DIR, 'data', 'raw')
PROCESSED_DIR = os.path.join(BASE_DIR, 'data', 'processed')

os.makedirs(PROCESSED_DIR, exist_ok=True)

def clean_uci_data():
    file_path = os.path.join(RAW_DIR, 'student_success_uci.csv')
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return
    
    df = pd.read_csv(file_path)
    
    # Standardize column names to lowercase snake_case
    df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('/', '_')
    
    # Handle missing values (if any)
    df = df.fillna(method='ffill')
    
    # Check duplicates
    df = df.drop_duplicates()
    
    # Standardize Target column
    if 'target' in df.columns:
        df = df.rename(columns={'target': 'student_status'})
    
    # Map status if needed (UCI often has 'Dropout', 'Enrolled', 'Graduate')
    # Our mock already uses these, but let's be safe
    status_map = {
        'Dropout': 'Dropout',
        'Enrolled': 'Enrolled',
        'Graduate': 'Graduate'
    }
    df['student_status'] = df['student_status'].map(status_map).fillna(df['student_status'])
    
    output_path = os.path.join(PROCESSED_DIR, 'student_success_clean.csv')
    df.to_csv(output_path, index=False)
    print(f"Cleaned UCI data saved to {output_path}")

if __name__ == "__main__":
    print("Running data cleaning...")
    clean_uci_data()
    print("Data cleaning completed!")
