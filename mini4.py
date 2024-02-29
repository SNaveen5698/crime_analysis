#4most crimes occur based on the "Location"
import pymysql
import matplotlib.pyplot as plt
import pandas as pd

connection = pymysql.connect(user='root', password='naveen5698', host='127.0.0.1', database='crime')
cursor = connection.cursor()

cursor.execute("SELECT Location, COUNT(*) AS Crime_Count FROM crime_data GROUP BY Location ORDER BY Crime_Count DESC LIMIT 10")
location_data = cursor.fetchall()

cursor.close()
connection.close()

df_location = pd.DataFrame(location_data, columns=['Location', 'Crime_Count'])
plt.figure(figsize=(2, 2))
plt.bar(df_location['Location'], df_location['Crime_Count'], color='orange')
plt.title('Top 10 Locations with the Most Crimes')
plt.xlabel('Location')
plt.ylabel('Crime Count')
plt.xticks(rotation=45, ha='right')
plt.show()
