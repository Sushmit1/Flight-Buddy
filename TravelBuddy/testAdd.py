import pandas as pd
import matplotlib.pyplot as plt
import io
import smtplib
from email.message import EmailMessage
from fpdf import FPDF
from PIL import Image
import tempfile
import openai
import csv
import numpy as np

def JoinName(firstname, lastname):
    name = firstname + " " + lastname

    file_path = r"D:\VIT\sem_7_fall\RPA\project\TravelBuddy\Data\flightdata.xlsx"
    df = pd.read_excel(file_path, header=None) 

    df.columns = ['Airlines', 'Departure', 'Arrival', 'Duration', 'Fare', 'Stops']

    df['Fare'] = df['Fare'].replace({'₹ ': '', ',': ''}, regex=True)
    df['Fare'] = pd.to_numeric(df['Fare'], errors='coerce')
    df = df.dropna(subset=['Fare'])
    df['Fare'] = df['Fare'].astype(int)

    def format_duration(minutes):
        hours = minutes // 60
        remaining_minutes = minutes % 60
        return f"{hours}h {remaining_minutes}m"

    def duration_to_minutes(duration):
        parts = str(duration).split()  
        total_minutes = 0
        for i in range(len(parts) - 1):
            if parts[i].isdigit():
                if parts[i + 1] == 'h':
                    total_minutes += int(parts[i]) * 60
                elif parts[i + 1] == 'm':
                    total_minutes += int(parts[i])
        return total_minutes

    df['Duration'] = df['Duration'].apply(duration_to_minutes)

    df['Number of Stops'] = df['Stops'].apply(lambda x: len(str(x).split(',')))

    plots = [
        ('Average Cost per Airline', 'avg_cost_per_airline.png'),
        ('Number of Stops vs Airline Name', 'stops_vs_airline.png'),
    ]
    img_buffers = {}

    plt.figure(figsize=(14, 10)) 
    avg_cost_per_airline = df.groupby('Airlines')['Fare'].mean().sort_values()
    avg_cost_per_airline.plot(kind='bar', color='skyblue')
    plt.title('Average Cost per Airline')
    plt.xlabel('Airline Name')
    plt.ylabel('Average Fare (INR)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    img_buffers['avg_cost_per_airline.png'] = io.BytesIO()
    plt.savefig(img_buffers['avg_cost_per_airline.png'], format='png')
    plt.close()

    plt.figure(figsize=(14, 10))
    stops_per_airline = df.groupby('Airlines')['Number of Stops'].mean()
    stops_per_airline.plot(kind='bar', color='orange')
    plt.title('Number of Stops vs Airline')
    plt.xlabel('Airline Name')
    plt.ylabel('Average Number of Stops')
    plt.xticks(rotation=45, ha='right')
    plt.yticks(np.arange(1, stops_per_airline.max()+1, step=1))
    plt.tight_layout()
    img_buffers['stops_vs_airline.png'] = io.BytesIO()
    plt.savefig(img_buffers['stops_vs_airline.png'], format='png')
    plt.close()

    cheapest_flight = df.loc[df['Fare'].idxmin()]
    fastest_flight = df.loc[df['Duration'].idxmin()]



    stops = df['Stops'].tolist()
    airlines = df['Airlines'].tolist()

    # openai.api_key = ""
    # prompt=f"Please provide a table with the following information for each stop in flight {stops} and their respective airline {airlines} This is the format of table Stop Name , Food Options and Nearby Restaurants, Free Lounge Access (Yes/No) The table should have rows corresponding to the number of stops. Please format the output as a single table with the headers: 'Stop Name', 'Food Options and Restaurants', and 'Free Lounge  Note: only return table nothing else no warnings also"
    # response = openai.chat.completions.create(
    #     model="gpt-4o", 
    #     messages=[
    #         {"role": "system", "content": "You are a helpful assistant."},
    #         {"role": "user", "content": prompt}
    #     ],
    #     max_tokens=400,
    #     temperature=0.7
    # )
    # llm_result=response.choices[0].message.content
    # print(llm_result)
    





    llm_result="""| Stop Name                         | Food Options and Restaurants        | Free Lounge Access (Yes/No) |
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
| New Delhi                         | Multiple cuisines, Indian, Fast Food| No"""

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    for plot_title, plot_file in plots:
        pdf.add_page()
        pdf.set_font("Arial", size=12, style='B')
        pdf.cell(200, 10, txt=plot_title, ln=True, align='C')

        img_buffers[plot_file].seek(0)
        
        img = Image.open(img_buffers[plot_file])

        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_img:
            img.save(temp_img, format="PNG")
            temp_img_path = temp_img.name

        pdf.image(temp_img_path, x=10, y=30, w=180)

    pdf.add_page()
    pdf.set_font("Arial", size=14, style='B')
    pdf.cell(200, 10, txt="Cheapest Flight", ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Airline: {cheapest_flight['Airlines']}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Fare: INR {cheapest_flight['Fare']}", ln=True, align='L') 
    pdf.cell(200, 10, txt=f"Departure: {cheapest_flight['Departure']}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Arrival: {cheapest_flight['Arrival']}", ln=True, align='L')

    pdf.add_page()
    pdf.set_font("Arial", size=14, style='B')
    pdf.cell(200, 10, txt="Fastest Flight", ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Airline: {fastest_flight['Airlines']}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Fare: INR {fastest_flight['Fare']}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Duration: {format_duration(fastest_flight['Duration'])}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Departure: {fastest_flight['Departure']}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Arrival: {fastest_flight['Arrival']}", ln=True, align='L')
    
    pdf.add_page()
    pdf.set_font("Arial", size=14, style='B')
    pdf.cell(200, 10, txt="LLM Suggestions", ln=True, align='C')

    pdf.set_font("Arial", size=10)

    lines = llm_result.split('\n')

    for line in lines:
        pdf.multi_cell(0, 10, txt=line, border=1, align='L')

    pdf.ln(10)

    pdf_buffer = io.BytesIO()
    pdf_buffer.write(pdf.output(dest='S').encode('latin1'))
    pdf_buffer.seek(0)

    # Input data as a multiline string
    data = llm_result

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

    email_address = firstname
    sender_email = "dharshanbalajikaruppa18@gmail.com" 
    sender_password = "vpqy tsad nqri rlec"  

    msg = EmailMessage()
    msg['Subject'] = "Flight Data Analysis Report"
    msg['From'] = sender_email
    msg['To'] = email_address
    msg.set_content("Attached is the flight data analysis report in PDF format.")

    msg.add_attachment(pdf_buffer.read(), maintype='application', subtype='pdf', filename='flight_data_analysis.pdf')

    with open(file_path, 'rb') as f:
        file_data = f.read()
        file_name = "flightdata.xlsx"
        msg.add_attachment(file_data, maintype='application', subtype='vnd.ms-excel', filename=file_name)

    csv_file_path = "Data/stops_info.csv"  # Path to your CSV file
    with open(csv_file_path, 'rb') as f:
        file_data = f.read()
        file_name = "stops_info.csv"  # Desired name for the attached file
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)

    return name

JoinName("thamizharasan.mohankumar2021@vitstudent.ac.in", "Project")