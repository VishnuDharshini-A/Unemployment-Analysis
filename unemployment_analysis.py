import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("seaborn-v0_8")

#loading data set

df = pd.read_csv("Unemployment in India.csv")

print(df.head())
print(df.info())

#fixing column names

df.columns = df.columns.str.strip()

#converting date to time

df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

#checking missing values

print(df.isnull().sum())

#data exploration

print(df.describe())


#overall unemployment

india_trend = df.groupby('Date')['Estimated Unemployment Rate (%)'].mean()

plt.figure(figsize=(12,5))
plt.plot(india_trend.index, india_trend.values, marker='o')
plt.title("Average Unemployment Rate in India Over Time")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.show()

#covid 19 impact analysis
#separating pre-covid and covid periods

pre_covid = df[df['Date'] < '2020-03-01']
covid = df[df['Date'] >= '2020-03-01']

#comparing average unemployment

print("Pre-COVID Average Unemployment:",
      pre_covid['Estimated Unemployment Rate (%)'].mean())

print("COVID Period Average Unemployment:",
      covid['Estimated Unemployment Rate (%)'].mean())


#statewise unemployment analysis

state_avg = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean().sort_values(ascending=False)

plt.figure(figsize=(10,6))
sns.barplot(x=state_avg.values, y=state_avg.index)
plt.title("Average Unemployment Rate by State")
plt.xlabel("Unemployment Rate (%)")
plt.ylabel("State")
plt.show()

#rural vs urban analysis

area_trend = df.groupby(['Date','Area'])['Estimated Unemployment Rate (%)'].mean().reset_index()

plt.figure(figsize=(12,5))
sns.lineplot(data=area_trend, x='Date', y='Estimated Unemployment Rate (%)', hue='Area')
plt.title("Unemployment Trend: Rural vs Urban")
plt.show()

#seasonal and monthly trends

df['Month'] = df['Date'].dt.month

monthly_avg = df.groupby('Month')['Estimated Unemployment Rate (%)'].mean()

plt.figure(figsize=(8,4))
monthly_avg.plot(kind='bar')
plt.title("Average Monthly Unemployment Rate")
plt.xlabel("Month")
plt.ylabel("Unemployment Rate (%)")
plt.show()



