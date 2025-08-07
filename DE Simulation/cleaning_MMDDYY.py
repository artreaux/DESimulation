import pandas as pd
import glob

def format_date(date_str):
    """Convert date from 'YYYY-MM-DD' to 'MM/DD/YY' format."""
    try:
        date = pd.to_datetime(date_str, format='%Y-%m-%d', errors='coerce')
        return date.strftime('%m/%d/%y')
    except Exception as e:
        return date_str

def process_files(file_pattern):
    # Get the list of CSV files
    file_paths = glob.glob(file_pattern)
    
    for file_path in file_paths:
        try:
            # Load the CSV file into a DataFrame
            df = pd.read_csv(file_path)
            
            # Convert DATE_BOOKED and DEPARTURE_DATE to 'MM/DD/YY' format
            if 'DATE_BOOKED' in df.columns:
                df['DATE_BOOKED'] = df['DATE_BOOKED'].astype(str).apply(format_date)
            if 'DEPARTURE_DATE' in df.columns:
                df['DEPARTURE_DATE'] = df['DEPARTURE_DATE'].astype(str).apply(format_date)
            
            # Save the formatted DataFrame back to CSV
            df.to_csv(file_path, index=False)
            print(f"Formatted {file_path} successfully.")
        
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")

# Pattern to match all month-2023 CSV files
file_pattern = r"C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\Data\*-2023.csv"

# Run the function
process_files(file_pattern)
