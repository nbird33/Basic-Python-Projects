import csv

mobile_numbers = []

# Open the input CSV file
with open('input.csv', 'r') as f:
    reader = csv.DictReader(f)
   
    # Loop through each row in the CSV file
    for row in reader:
        # Check if any of the phone types contain "Mobile"
        if "Mobile" in row['Phone 1 Type'] or "Mobile" in row['Phone 2 Type'] or "Mobile" in row['Phone 3 Type']:
            # Get the corresponding mobile phone number from the same row
            if "Mobile" in row['Phone 1 Type']:
                mobile_numbers.append(row['Phone 1'])
            elif "Mobile" in row['Phone 2 Type']:
                mobile_numbers.append(row['Phone 2'])
            else:
                mobile_numbers.append(row['Phone 3'])

# Write the mobile numbers to a new text file
with open('output.txt', 'w') as f:
    for number in mobile_numbers:
        f.write(number + '\n')