import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r"C:\Users\HP\OneDrive\Desktop\DEBRAJ INTERNSHIP\DEBRAJ INTERNSHIP\1\API_SP.POP.TOTL_DS2_en_csv_v2_76253.csv"
df = pd.read_csv(file_path, skiprows=4)

# Extract India's population data for 2022
india_population = df[df["Country Name"] == "India"]["2022"].values[0]

# Define age group distribution percentages from the given image
age_groups = ["0-20 Years", "21-44 Years", "45+ Years"]
percentages = [36.1, 57.0, 6.9]

# Calculate the population in millions for each age group
populations = [(india_population * p) / 100 for p in percentages]

# Plot the bar chart
plt.figure(figsize=(8, 5))
plt.bar(age_groups, populations, color=["yellow", "blue", "purple"])

# Labels and title
plt.xlabel("Age Groups")
plt.ylabel("Population (Millions)")
plt.title("India's Population Distribution by Age in 2022")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show the chart
plt.show()

