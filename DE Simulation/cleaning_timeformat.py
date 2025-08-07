import pandas as pd
import glob
import re

def format_time(time_str):
    """Standardize time format to HH:MM."""
    # Replace formats like 'x:xx' and 'xxx:xx' with 'xx:xx'
    if re.match(r'^\d{1,2}:\d{2}$', time_str):
        return f"{int(time_str.split(':')[0]):02}:{time_str.split(':')[1]}"
    if re.match(r'^\d{3}:\d{2}$', time_str):
        return f"{int(time_str[:2]):02}:{time_str[-2:]}"
    return time_str

def process_files(file_pattern):
    # Get the list of CSV files
    file_paths = glob.glob(file_pattern)
    
    for file_path in file_paths:
        try:
            # Load the CSV file into a DataFrame
            df = pd.read_csv(file_path)
            
            # Standardize time format in DATE_BOOKED and DEPARTURE_TIME columns
            if 'DATE_BOOKED' in df.columns:
                df['DATE_BOOKED'] = df['DATE_BOOKED'].astype(str).apply(lambda x: format_time(x) if ':' in x else x)
            if 'DEPARTURE_TIME' in df.columns:
                df['DEPARTURE_TIME'] = df['DEPARTURE_TIME'].astype(str).apply(lambda x: format_time(x) if ':' in x else x)
            
            # Save the formatted DataFrame back to CSV
            df.to_csv(file_path, index=False)
            print(f"Formatted {file_path} successfully.")
        
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")

# Pattern to match all month-2023 CSV files
file_pattern = r"C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\Data\*-2023.csv"

# Run the function
process_files(file_pattern)
