import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r"C:\Users\LENOVO\OneDrive\Desktop\campaign.csv")


df['CAC'] = df['Spend'] / df['Customers']
df['ROI'] = (df['Revenue'] - df['Spend']) / df['Spend'] * 100

print(df.groupby('Channel')[['CAC','ROI']].mean())

print("\nTop Campaigns:\n", df.nlargest(5, 'ROI'))
print("\nWorst Campaigns:\n", df.nsmallest(5, 'ROI'))
df.groupby('Channel')['ROI'].mean().plot(kind='bar')
plt.show()