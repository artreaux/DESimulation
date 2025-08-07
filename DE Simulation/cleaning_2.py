import pandas as pd
import glob

def clean_data(file_pattern, output_pattern):
    file_paths = glob.glob(file_pattern)
    
    for file_path in file_paths:
        try:
            df = pd.read_csv(file_path)
            
            # Convert DATE_BOOKED to datetime, coerce errors to NaT, then drop NaT rows
            df['DATE_BOOKED'] = pd.to_datetime(df['DATE_BOOKED'], errors='coerce', format='%Y-%m-%d %H:%M:%S')
            df = df.dropna(subset=['DATE_BOOKED'])
            
            # Convert DEPARTURE_DATE to datetime, coerce errors to NaT, then drop NaT rows
            df['DEPARTURE_DATE'] = pd.to_datetime(df['DEPARTURE_DATE'], errors='coerce', format='%Y-%m-%d')
            df = df.dropna(subset=['DEPARTURE_DATE'])
            
            # Convert DEPARTURE_TIME to time, coerce errors to NaT, then drop NaT rows
            df['DEPARTURE_TIME'] = pd.to_datetime(df['DEPARTURE_TIME'], errors='coerce', format='%H:%M:%S').dt.time
            df = df.dropna(subset=['DEPARTURE_TIME'])
            
            # Save cleaned data to new CSV
            output_file = output_pattern.format(file_path.split("\\")[-1])
            df.to_csv(output_file, index=False)
            print(f"Cleaned and saved to {output_file}.")
        
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")

# Clean and save CSV files
file_pattern = r"C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\Data\*-2023.csv"
output_pattern = r"C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\Data\cleaned_{}"
clean_data(file_pattern, output_pattern)
