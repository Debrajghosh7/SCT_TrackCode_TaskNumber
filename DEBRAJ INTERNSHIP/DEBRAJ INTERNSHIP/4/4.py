r"""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = r"C:/Users/user/Desktop/DEBRAJ INTERNSHIP/4/us-accidents-metadata.json"
df = pd.read_json(file_path)

# Display basic info about the dataset
print(df.info())

# Select relevant columns
columns_of_interest = ['Start_Time', 'End_Time', 'Severity', 'City', 'State', 'Temperature(F)', 'Weather_Condition', 'Visibility(mi)', 'Humidity(%)', 'Wind_Speed(mph)', 'Sunrise_Sunset', 'Street']
df = df[columns_of_interest]

# Convert Start_Time to datetime format
df['Start_Time'] = pd.to_datetime(df['Start_Time'])
df['Hour'] = df['Start_Time'].dt.hour
df['DayOfWeek'] = df['Start_Time'].dt.day_name()

# Accident count by time of day
plt.figure(figsize=(12, 6))
sns.countplot(x='Hour', data=df, palette='coolwarm')
plt.title('Accident Frequency by Hour of the Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()

# Accident count by weather condition
plt.figure(figsize=(14, 6))
top_weather_conditions = df['Weather_Condition'].value_counts().nlargest(10).index
sns.countplot(y=df[df['Weather_Condition'].isin(top_weather_conditions)]['Weather_Condition'], palette='viridis')
plt.title('Top 10 Weather Conditions Leading to Accidents')
plt.xlabel('Number of Accidents')
plt.ylabel('Weather Condition')
plt.show()

# Accident severity distribution
plt.figure(figsize=(8, 5))
sns.countplot(x='Severity', data=df, palette='magma')
plt.title('Distribution of Accident Severity')
plt.xlabel('Severity Level')
plt.ylabel('Number of Accidents')
plt.show()

# Accident count by day of the week
plt.figure(figsize=(10, 5))
sns.countplot(x='DayOfWeek', data=df, order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], palette='muted')
plt.title('Accidents by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Accidents')
plt.show()

print("Analysis complete.")"""


r"""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = r"C:/Users/user/Desktop/DEBRAJ INTERNSHIP/4/us-accidents-metadata.json"
try:
    df = pd.read_json(file_path)
except FileNotFoundError:
    print("File not found. Please check the file path.")
    exit()

# Display basic info about the dataset
print(df.info())

# Select relevant columns
columns_of_interest = ['Start_Time', 'End_Time', 'Severity', 'City', 'State', 'Temperature(F)', 'Weather_Condition', 'Visibility(mi)', 'Humidity(%)', 'Wind_Speed(mph)', 'Sunrise_Sunset', 'Street']
df = df[columns_of_interest]

# Handle missing data
df = df.dropna(subset=columns_of_interest)

# Convert columns to appropriate data types
df['Temperature(F)'] = pd.to_numeric(df['Temperature(F)'], errors='coerce')
df['Visibility(mi)'] = pd.to_numeric(df['Visibility(mi)'], errors='coerce')
df['Humidity(%)'] = pd.to_numeric(df['Humidity(%)'], errors='coerce')
df['Wind_Speed(mph)'] = pd.to_numeric(df['Wind_Speed(mph)'], errors='coerce')

# Convert Start_Time to datetime format
df['Start_Time'] = pd.to_datetime(df['Start_Time'])
df['Hour'] = df['Start_Time'].dt.hour
df['DayOfWeek'] = df['Start_Time'].dt.day_name()

# Accident count by time of day
plt.figure(figsize=(12, 6))
sns.countplot(x='Hour', data=df, palette='coolwarm')
plt.title('Accident Frequency by Hour of the Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()

# Accident count by weather condition
plt.figure(figsize=(14, 6))
top_weather_conditions = df['Weather_Condition'].value_counts().nlargest(10).index
sns.countplot(y=df[df['Weather_Condition'].isin(top_weather_conditions)]['Weather_Condition'], 
              palette='viridis', order=top_weather_conditions)
plt.title('Top 10 Weather Conditions Leading to Accidents')
plt.xlabel('Number of Accidents')
plt.ylabel('Weather Condition')
plt.show()

# Accident severity distribution
plt.figure(figsize=(8, 5))
sns.countplot(x='Severity', data=df, palette='magma')
plt.title('Distribution of Accident Severity')
plt.xlabel('Severity Level')
plt.ylabel('Number of Accidents')
plt.show()

# Accident count by day of the week
plt.figure(figsize=(10, 5))
sns.countplot(x='DayOfWeek', data=df, order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], palette='muted')
plt.title('Accidents by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Accidents')
plt.show()

print("Analysis complete.")"""



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = r"C:\Users\HP\OneDrive\Desktop\DEBRAJ INTERNSHIP\DEBRAJ INTERNSHIP\4\US_Accidents_March23.csv"  # Replace with the actual path to your CSV file
df = pd.read_csv(file_path)

# Display basic info about the dataset
print(df.info())

# Display the first few rows of the dataset
print(df.head())

# Convert Start_Time to datetime format
df['Start_Time'] = pd.to_datetime(df['Start_Time'])

# Extract hour and day of the week
df['Hour'] = df['Start_Time'].dt.hour
df['DayOfWeek'] = df['Start_Time'].dt.day_name()

# Accident count by time of day
plt.figure(figsize=(12, 6))
sns.countplot(x='Hour', data=df, palette='coolwarm')
plt.title('Accident Frequency by Hour of the Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()

# Accident count by day of the week
plt.figure(figsize=(10, 5))
sns.countplot(x='DayOfWeek', data=df, order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], palette='muted')
plt.title('Accidents by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Accidents')
plt.show()

# Accident count by weather condition
plt.figure(figsize=(14, 6))
top_weather_conditions = df['Weather_Condition'].value_counts().nlargest(10).index
sns.countplot(y=df[df['Weather_Condition'].isin(top_weather_conditions)]['Weather_Condition'], palette='viridis', order=top_weather_conditions)
plt.title('Top 10 Weather Conditions Leading to Accidents')
plt.xlabel('Number of Accidents')
plt.ylabel('Weather Condition')
plt.show()

# Accident severity distribution
plt.figure(figsize=(8, 5))
sns.countplot(x='Severity', data=df, palette='magma')
plt.title('Distribution of Accident Severity')
plt.xlabel('Severity Level')
plt.ylabel('Number of Accidents')
plt.show()

# Visualize accident hotspots
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Start_Lng', y='Start_Lat', data=df, hue='Severity', palette='coolwarm', alpha=0.6)
plt.title('Accident Hotspots')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

print("Analysis complete.")
