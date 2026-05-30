import pandas as pd

# Read the CSV with error handling
try:
    # Try reading with different parameters
    df = pd.read_csv('data/faqs.csv', on_bad_lines='skip', engine='python')
    print(f"Loaded {len(df)} rows with skip bad lines")
    
    # Save the cleaned version
    df.to_csv('data/faqs_clean.csv', index=False, quoting=1)  # quoting=1 means QUOTE_ALL
    print("Saved cleaned CSV to data/faqs_clean.csv")
    
    # Verify it can be read
    df_test = pd.read_csv('data/faqs_clean.csv')
    print(f"Verification: Successfully read {len(df_test)} rows from cleaned file")
    print("\nFirst few rows:")
    print(df_test.head())
    
except Exception as e:
    print(f"Error: {e}")
