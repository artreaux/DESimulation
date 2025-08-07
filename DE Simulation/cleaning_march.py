import pandas as pd

# Function to convert D/M/YYYY to M/D/YYYY (Swap day and month)
def swap_day_month(date_str):
    try:
        # Split the date by '/'
        day, month, year = date_str.split('/')
        
        # Return in M/D/YYYY format
        return f"{month}/{day}/{year}"
    except Exception as e:
        return None  # Return None if there is any issue with the date format

# Path for the October CSV file
input_file_path = r"C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\January-2024.csv"
output_file_path = r"C:\Users\labva\OneDrive\Desktop\DE Simulation\January-2024_clean.csv"

# Read the October CSV file into a DataFrame
df = pd.read_csv(input_file_path)

# Check if 'DATE_BOOKED' and 'DEPARTURE_DATE' columns exist and apply the conversion
if 'DateBooked' in df.columns:
    # Apply the swap function to the 'DATE_BOOKED' column
    df['DateBooked'] = df['DateBooked'].apply(swap_day_month)

if 'DepartureDate' in df.columns:
    # Apply the swap function to the 'DEPARTURE_DATE' column
    df['DepartureDate'] = df['DepartureDate'].apply(swap_day_month)

# Save the cleaned data into the output folder
df.to_csv(output_file_path, index=False)

print(f"Cleaned file saved at: {output_file_path}")
