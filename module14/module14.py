


import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('weather_tokyo_data.csv.csv')


print(df.head())

average_temperature = df['temperature'].mean()


formatted_average_temperature = round(average_temperature, 2)

print(f"The average temperature is: {formatted_average_temperature}°C")


df['date'] = pd.to_datetime(df['date'])

df['month'] = df['date'].dt.month

monthly_avg_temp = df.groupby('month')['temperature'].mean()

monthly_avg_temp = monthly_avg_temp.round(2)

print("Average temperature for each month:")
print(monthly_avg_temp)


df['date'] = pd.to_datetime(df['date'])


df['month'] = df['date'].dt.month

monthly_avg_temp = df.groupby('month')['temperature'].mean()


monthly_avg_temp = monthly_avg_temp.round(2)


plt.figure(figsize=(10, 6))
monthly_avg_temp.plot(kind='bar', color='skyblue', edgecolor='black')

plt.title('Average Monthly Temperature', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Average Temperature (°C)', fontsize=12)

month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.xticks(ticks=range(12), labels=month_names, rotation=45)

plt.tight_layout()
plt.show()













