import pandas as pd

def decimal_to_time(decimal):
    """Convert decimal time to 12-hour format with AM/PM."""
    # Convert decimal to total seconds
    total_seconds = int(decimal * 24 * 3600)
    # Calculate hours, minutes, and seconds
    hours = (total_seconds // 3600) % 24
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    # Format time to 12-hour format with AM/PM
    time_str = f"{hours:02}:{minutes:02}:{seconds:02}"
    time = pd.to_datetime(time_str, format='%H:%M:%S').strftime('%I:%M:%S %p')
    return time

def clean_and_convert_departure_time(file_path):
    try:
        # Load the CSV file into a DataFrame with latin1 encoding
        df = pd.read_csv(file_path, encoding='latin1')
        
        # Convert DepartureTime from decimal to 12-hour format with AM/PM
        df['DepartureTime'] = df['DepartureTime'].apply(decimal_to_time)
        
        # Update the column headers
        new_headers = [
            'DATE_BOOKED', 'ORIGIN', 'DESTINATION', 'ORDER_REF', 'TICKET_NO', 'SEATNO',
            'DATE_REDEEMED', 'EMAIL', 'MOBILENO', 'FARE', 'CONVENIENCE_FEE', 'DISCOUNT',
            'DEPARTURE_DATE', 'DEPARTURE_TIME', 'BUS_TYPE', 'NUMBER_OF_VOUCHERS_BOOKED'
        ]
        df.columns = new_headers
        
        # Ensure the DESTINATION column is clean and properly encoded
        df['DESTINATION'] = df['DESTINATION'].apply(lambda x: x.encode('latin1').decode('utf-8', 'ignore'))
        
        # Save the cleaned and formatted DataFrame back to CSV with UTF-8 encoding
        df.to_csv(file_path, index=False, encoding='utf-8')
        print(f"Cleaned and formatted {file_path} successfully.")
    
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

# File path for October-2023.csv
file_path = r"C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\October-2023.csv"

# Run the function
clean_and_convert_departure_time(file_path)
