# Import Required Libraries
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# API Setup
API_KEY = 'f705b8d068bc3277b55e179cc7c33e33' 
CITY = 'London'
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetch Data from OpenWeatherMap API
response = requests.get(URL)
data = response.json()

# Error handling: Check if API response is successful
if response.status_code != 200 or 'list' not in data:
    print("Failed to retrieve data. Check your API key and city name.")
    exit()

# Extract and Organize Relevant Data
forecast_list = data['list']
weather_data = []

for item in forecast_list:
    timestamp = item['dt_txt']
    temperature = item['main']['temp']
    humidity = item['main']['humidity']
    weather_data.append({
        'DateTime': timestamp,
        'Temperature (°C)': temperature,
        'Humidity (%)': humidity
    })

# Convert to DataFrame
df = pd.DataFrame(weather_data)
df['DateTime'] = pd.to_datetime(df['DateTime'])

# Create Visualizations
plt.figure(figsize=(14, 6))
sns.lineplot(x='DateTime', y='Temperature (°C)', data=df, label='Temperature', color='tomato')
sns.lineplot(x='DateTime', y='Humidity (%)', data=df, label='Humidity', color='royalblue')
plt.title(f'5-Day Weather Forecast for {CITY}', fontsize=16)
plt.xlabel('Date and Time')
plt.ylabel('Values')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
