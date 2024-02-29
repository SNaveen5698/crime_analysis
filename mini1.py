#1 geographical hotspots for reported crimes

import pymysql
import matplotlib.pyplot as plt

host = '127.0.0.1'
user = 'root'
password = 'naveen5698'
database = 'crime'

conn = pymysql.connect(host=host, user=user, password=password, database=database)

query = "SELECT LAT, LON FROM crime_data"

cursor = conn.cursor()
cursor.execute(query)
data = cursor.fetchall()

conn.close()

latitudes, longitudes = zip(*data)
'''latitudes = [row[0] for row in data]
longitudes = [row[1] for row in data]'''

plt.figure(figsize=(10, 8))
plt.scatter(longitudes, latitudes, alpha=0.5, marker='o', color='red')
plt.title('Geographical Hotspots for Reported Crimes')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)
plt.show()





