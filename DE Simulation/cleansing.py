import pandas as pd

# Read the CSV file with the correct encoding
df = pd.read_csv(r'C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\Data\October-2023.csv', encoding='ISO-8859-1')

# Print original column names to verify their exact names
print("Original Columns:", df.columns)

# Rename columns to match MySQL table's column names
df.rename(columns={
    'DateBooked': 'DATE_BOOKED',
    'Origin': 'ORIGIN',
    'Destination': 'DESTINATION',
    'OrderRef': 'ORDER_REF',
    'TicketNo': 'TICKET_NO',
    'SeatNo': 'SEATNO',
    'DateRedeemed': 'DATE_REDEEMED',
    'Email': 'EMAIL',
    'MobileNo': 'MOBILENO',
    'Fare': 'FARE',
    'ConvenienceFee': 'CONVENIENCE_FEE',
    'Discount': 'DISCOUNT',
    'DepartureDate': 'DEPARTURE_DATE',
    'DepartureTime': 'DEPARTURE_TIME',
    'BusType': 'BUS_TYPE',
    'NumberOfVouchersBooked': 'NUMBER_OF_VOUCHERS_BOOKED'
}, inplace=True)

# Convert the DEPARTURE_DATE from Excel numeric to date
df['DEPARTURE_DATE'] = pd.to_datetime(df['DEPARTURE_DATE'], origin='1899-12-30', unit='D').dt.strftime('%Y-%m-%d')

# Convert the DEPARTURE_TIME from decimal to time
def convert_decimal_time(value):
    try:
        return pd.to_datetime(value * 86400, unit='s').strftime('%H:%M:%S')
    except Exception:
        return None

df['DEPARTURE_TIME'] = df['DEPARTURE_TIME'].apply(convert_decimal_time)

# Save the cleaned CSV file with utf-8 encoding
df.to_csv(r'C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\Data\October-2023-cleaned.csv', index=False, encoding='utf-8')

# Print renamed columns to verify
print("Renamed Columns:", df.columns)
