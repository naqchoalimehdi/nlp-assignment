import csv

# Read the original file and fix it
with open('data/faqs.csv', 'r', encoding='utf-8') as infile:
    lines = infile.readlines()

# Write properly formatted CSV
with open('data/faqs_proper.csv', 'w', encoding='utf-8', newline='') as outfile:
    writer = csv.writer(outfile, quoting=csv.QUOTE_MINIMAL)
    
    # Write header
    writer.writerow(['question', 'answer', 'category'])
    
    # Process each line (skip header)
    for i, line in enumerate(lines[1:], start=2):
        line = line.strip()
        if not line:
            continue
            
        # Find the last comma (category separator)
        last_comma = line.rfind(',')
        if last_comma == -1:
            print(f"Skipping line {i}: No comma found")
            continue
            
        category = line[last_comma+1:].strip()
        rest = line[:last_comma]
        
        # Find the first comma (question-answer separator)
        first_comma = rest.find(',')
        if first_comma == -1:
            print(f"Skipping line {i}: Only one comma found")
            continue
            
        question = rest[:first_comma].strip()
        answer = rest[first_comma+1:].strip()
        
        writer.writerow([question, answer, category])
        
print("Fixed CSV saved to data/faqs_proper.csv")

# Verify
import pandas as pd
df = pd.read_csv('data/faqs_proper.csv')
print(f"Verification: Successfully loaded {len(df)} rows")
print(df.head())
