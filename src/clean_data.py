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
        raise FileNotFoundError(
            f"\n\n[ERROR] Raw UCI dataset not found at: {file_path}\n"
            "This project requires the real public 'Predict Students' Dropout and Academic Success' dataset "
            "from the UCI Machine Learning Repository.\n"
            "Please download the dataset manually and place it as a CSV file at the correct path:\n"
            f"  -> {file_path}\n"
            "For full details, please refer to data/README.md or data/raw/README.md.\n"
        )
    
    # Detect delimiter (the real UCI dataset is typically semicolon-delimited)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            first_line = f.readline()
        sep = ';' if ';' in first_line else ','
    except Exception:
        sep = ','
        
    df = pd.read_csv(file_path, sep=sep)
    
    # Standardize column names to lowercase snake_case, strip whitespace/quotes/tabs
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(' ', '_')
        .str.replace('(', '')
        .str.replace(')', '')
        .str.replace('/', '_')
        .str.replace('"', '')
        .str.replace("'", "")
    )
    
    # Handle missing values (if any)
    df = df.ffill()
    
    # Check duplicates
    df = df.drop_duplicates()
    
    # Standardize Target column
    if 'target' in df.columns:
        df = df.rename(columns={'target': 'student_status'})
    
    # Map status if needed (UCI often has 'Dropout', 'Enrolled', 'Graduate')
    # Standardize outcomes to ensure correct mapping
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
