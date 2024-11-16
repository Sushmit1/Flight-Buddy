import csv

data = """| Stop Name                         | Food Options and Restaurants        | Free Lounge Access (Yes/No) |
|-----------------------------------|-------------------------------------|-----------------------------|
| New Delhi                         | Multiple cuisines, Indian, Fast Food| No                          |
| Hong Kong                         | Asian, International, Fast Food     | No                          |
| New Delhi                         | Multiple cuisines, Indian, Fast Food| No                          |
| Hong Kong                         | Asian, International, Fast Food     | No                          |
| New Delhi                         | Multiple cuisines, Indian, Fast Food| No                          |
| Hong Kong                         | Asian, International, Fast Food     | No                          |
| New Delhi                         | Multiple cuisines, Indian, Fast Food| No                          |
| Hong Kong                         | Asian, International, Fast Food     | No                          |
| Singapore                         | International, Asian, Fast Food     | No                          |
| Hong Kong                         | Asian, International, Fast Food     | No                          |
| Hong Kong                         | Asian, International, Fast Food     | No                          |
| Tokyo-Haneda Airport              | Japanese, International, Fast Food  | No                          |
| Kuala Lumpur                      | Malaysian, International, Fast Food | No                          |
| Osaka                             | Japanese, International             | No                          |
| Kuala Lumpur                      | Malaysian, International, Fast Food | No                          |
| Tokyo - Narita Apt                | Japanese, International, Fast Food  | No                          |
| Kuala Lumpur                      | Malaysian, International, Fast Food | No                          |
| Tokyo - Narita Apt                | Japanese, International, Fast Food  | No                          |
| Kuala Lumpur                      | Malaysian, International, Fast Food | No                          |
| Hong Kong                         | Asian, International, Fast Food     | No                          |
| New Delhi                         | Multiple cuisines, Indian, Fast Food| No                          |
| Tokyo-Haneda Airport              | Japanese, International, Fast Food  | No                          |
| New Delhi                         | Multiple cuisines, Indian, Fast Food| No
"""

# Split data into lines and remove lines with separators
lines = [line.strip("|").strip() for line in data.split("\n") if "----" not in line and line.strip()]

# Separate header and rows
header = [col.strip() for col in lines[0].split("|")]
rows = [line.split("|") for line in lines[1:]]

# Clean rows by stripping extra spaces
cleaned_rows = [[col.strip() for col in row] for row in rows]

# Write to CSV file
with open("Data/stops_info.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(header)  # Write header
    writer.writerows(cleaned_rows)  # Write rows

print("CSV file 'stops_info.csv' created successfully.")