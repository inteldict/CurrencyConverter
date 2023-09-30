import csv

# Define the conversion rates dictionary
# conversion_rates = {
#     "AUD": {
#         1: 1.5770,
#         2: 1.5825,
#         # ... Add conversion rates for all months
#     },
#     "BRL": {
#         1: 6.2673,
#         2: 5.8903,
#         # ... Add conversion rates for all months
#     },
#     # Add entries for other currencies
# }
conversion_rates = {}

# Load data from the CSV file
# 'utf-8'
with open('data/2022_Umsatzsteuer_Umrechnungskurse.csv', newline='', encoding='iso-8859-1') as csvfile:
    reader = csv.reader(csvfile)
    # Skip the header row
    next(reader)

    for row in reader:
        # Extract data from each row
        country = row[0]
        # in row[1] is always the same value:
        # currency = row[1]
        rates = []
        for index, rate_str in enumerate(row[2:]):
            if not rate_str:
                continue
            rate, currency = rate_str.split()
            rates.append(float(rate.replace('.', '').replace(",", ".")))
            assert index < 12

        # rates = [float(rate.replace(",", ".")) for rate in ]  # Convert comma to dot for decimals

        # Store data in the dictionary
        conversion_rates[currency] = {
            'country': country,
            # 'currency': currency,
            'rates': rates
        }


# Function to convert nominal amount to Euros
def convert_to_euros(amount, currency, month):
    if currency in conversion_rates:
        conversion_rate = conversion_rates[currency]["rates"][month]
        euros = amount / conversion_rate
        return euros
    else:
        return None  # Handle cases where currency or month is not found


# # Input from the user
# amount = float(input("Enter the nominal amount: "))
# currency = input("Enter the currency abbreviation (e.g., AUD): ")
# month = int(input("Enter the month (1-12): "))
#
# # Perform the conversion
# euros = convert_to_euros(amount, currency, month)
#
# # Display the result
# if euros is not None:
#     print(f"{amount} {currency} is approximately {euros:.2f} Euros.")
# else:
#     print("Invalid currency or month.")

while True:
    # Input from the user
    amount = float(input("Enter the nominal amount (or 0 to exit): "))

    # Check if the user wants to exit
    if amount == 0:
        print("Goodbye!")
        break

    currency = input("Enter the currency abbreviation (e.g., AUD): ")
    month = int(input("Enter the month (1-12): "))
    assert 0 < month < 13
    month = month - 1

    # Perform the conversion
    euros = convert_to_euros(amount, currency, month)

    # Display the result
    if euros is not None:
        print(f"{amount} {currency} is approximately {euros:.2f} Euros.")
    else:
        print("Invalid currency or month.")
