import os
import pandas as pd
import re

def clean_datetime(value):
    """
    Cleans datetime values to make sure that the time is in proper HH:MM:SS format.
    Fixes single digit hours and minutes, and appends default time if missing.
    """
    if not isinstance(value, str):
        return value

    # If the value is a date-only (MM/DD/YY), append default time '00:00:00'
    if len(value) == 10:  # Format: MM/DD/YY (just a date)
        return value + ' 00:00:00'

    # Fix cases like '01/02/23 0:00' to '01/02/23 00:00:00'
    value = re.sub(r'(\d{1,2}):(\d{1})$', r'\1:\2:00', value)  # e.g., 0:2 -> 0:02:00
    value = re.sub(r'(\d{1,2}):(\d{1,2}):(\d{1})$', r'\1:\2:\3', value)  # e.g., 12:2:1 -> 12:02:01

    # Ensure time is correctly padded (HH:MM:SS)
    value = re.sub(r'(\d{1,2})\s*[:.]\s*(\d{1,2})$', r'\1:\2:00', value)  # e.g., '12:2' -> '12:02:00'

    # Ensure the datetime format is consistent: MM/DD/YY HH:MM:SS
    if re.match(r'\d{2}/\d{2}/\d{2} \d{1,2}:\d{1,2}:\d{1,2}', value):  # Looks like MM/DD/YY HH:MM:SS
        return value

    return value

def clean_csv(input_csv, output_csv):
    """
    Reads a CSV file, cleans it, and saves the cleaned data to a new CSV file.
    """
    try:
        # Read CSV into a DataFrame
        df = pd.read_csv(input_csv)

        # Apply cleaning to the 'DATE_BOOKED' column (or any datetime column)
        if 'DATE_BOOKED' in df.columns:
            df['DATE_BOOKED'] = df['DATE_BOOKED'].apply(clean_datetime)

        # If you have other datetime columns (like 'DEPARTURE_TIME'), apply clean_datetime to those as well
        if 'DEPARTURE_TIME' in df.columns:
            df['DEPARTURE_TIME'] = df['DEPARTURE_TIME'].apply(clean_datetime)

        # Save the cleaned data to a new CSV file
        df.to_csv(output_csv, index=False)
        print(f"Data cleaned and saved to {output_csv}")
    
    except Exception as e:
        print(f"Error processing file {input_csv}: {e}")

def clean_all_csv_in_directory(directory_path):
    """
    Cleans all CSV files in a specified directory.
    """
    # List all files in the directory
    files = os.listdir(directory_path)

    # Filter only .csv files
    csv_files = [file for file in files if file.endswith('.csv')]

    for file in csv_files:
        input_file = os.path.join(directory_path, file)
        output_file = os.path.join(directory_path, file.replace('.csv', '_cleaned.csv'))

        # Clean each CSV file
        clean_csv(input_file, output_file)

# Specify the directory containing the CSV files
directory_path = r"C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\Data"

# Clean all CSV files in the specified directory
clean_all_csv_in_directory(directory_path)
