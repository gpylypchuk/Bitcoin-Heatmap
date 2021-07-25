import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("BCHAIN-MKPRU.csv")
df = df.iloc[::-1]
df["200wma"] = df['Value'].rolling(window = 1400).mean()
df = df[1400:]
dates = pd.to_datetime(df['Date'])

monthly = df[::30]
distance = monthly['200wma'].pct_change() * 100

plt.style.use("dark_background")
plt.figure('Heatmap and Logarithmic Graph of Bitcoin')
plt.semilogy(dates, df['Value'], color = 'yellow', zorder=1)
plt.semilogy(dates, df['200wma'], color = 'red', zorder=2)
plt.scatter(monthly['Date'], monthly['Value'], c=distance, cmap='rainbow', vmin=0, vmax=16, zorder=3)
cbar = plt.colorbar()
cbar.set_label("% Monthly increase in 200wma")
cbar.ax.yaxis.set_label_position("left")
plt.show()