### <b>Flight Buddy - Automated Flight Data Analysis and Personalized Travel Recommendations</b>

Flight Buddy is an advanced Robotic Process Automation (RPA) tool designed to revolutionize flight booking and travel planning. Combining the power of UiPath, Python, and AI-driven insights, Flight Buddy simplifies the process of finding flights, analyzing travel data, and providing users with personalized travel recommendations.

#### Features : 
* Automated flight search and data scraping from MakeMyTrip.
* Python-powered data analysis to identify the most economical and shortest flights.
* Real-time visualization of key insights using Matplotlib.
* Seamless integration with ChatGPT API for personalized travel details.
* Comprehensive reports emailed directly to the user, including:
  * Cheapest and fastest flights.
  * Average fare per airline.
  * Airport amenities like lounge access and restaurant options.

#### Project Workflow:

1. Collect User Details:
  * Gather user information, including travel dates, destinations, and preferences via UiPath workflow.
  
2. Input Data into MakeMyTrip:
  * Automate user detail entry on the MakeMyTrip website using UiPath Browser activities.
  

# Flight Buddy - Automated Flight Data Analysis and Personalized Travel Recommendations

**Flight Buddy** is an advanced Robotic Process Automation (RPA) tool designed to revolutionize flight booking and travel planning. Combining the power of **UiPath**, **Python**, and **AI-driven insights**, Flight Buddy simplifies the process of finding flights, analyzing travel data, and providing users with personalized travel recommendations.

---

## Features
- Automated flight search and data scraping from **MakeMyTrip**.
- **Python-powered data analysis** to identify the most economical and shortest flights.
- Real-time visualization of key insights using **Matplotlib**.
- Seamless integration with **ChatGPT API** for personalized travel details.
- Comprehensive reports emailed directly to the user, including:
  - Cheapest and fastest flights.
  - Average fare per airline.
  - Airport amenities like lounge access and restaurant options.

---

## Project Workflow
1. **Collect User Details**  
   - Gather user information, including travel dates, destinations, and preferences via UiPath workflow.

2. **Input Data into MakeMyTrip**  
   - Automate user detail entry on the MakeMyTrip website using UiPath Browser activities.

3. **Scrape Flight Data**  
   - Extract real-time flight information (e.g., duration, price, airline) and store it in an Excel file.

4. **Export Data to Excel**  
   - Organize and save the scraped data in an Excel sheet for further analysis.

5. **Analyze Data**  
   - Use Python and Pandas to:
     - Find the most economical and shortest flights.
     - Calculate average fares per airline.

6. **Visualize Insights**  
   - Generate detailed graphs using Matplotlib for:
     - Cost comparison.
     - Flight durations.
     - Airline performance.

7. **Leverage LLM (Large Language Model)**  
   - Send the analyzed flight data to ChatGPT via OpenAI API for additional insights, such as:
     - Airport amenities (lounge access, restaurant options).

8. **Compile and Organize**  
   - Combine data analysis, visual representations, and ChatGPT insights into a comprehensive summary.

9. **Email Report**  
   - Deliver the final report to the user via email, providing all relevant travel insights in an easy-to-read format.

---

## Architecture
- **Frontend**: UiPath workflows for automation.
- **Backend**:
  - Python for data processing and analysis.
  - Matplotlib for visualization.
  - OpenAI API for enhanced travel insights.
- **Data Storage**: Excel for intermediate data organization.

---

## Installation and Setup
1. **Clone this repository**:
   ```bash
   git clone https://github.com/your-username/flight-buddy.git
   cd flight-buddy
