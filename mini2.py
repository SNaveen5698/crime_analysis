#2distribution of victim ages in reported crimes
import pymysql
import matplotlib.pyplot as plt

connection = pymysql.connect(user='root', password='naveen5698', host='127.0.0.1', database='crime')
cursor = connection.cursor()

cursor.execute("SELECT Vict_Age FROM crime_data WHERE Vict_Age > 0")
age_data = cursor.fetchall()

cursor.close()
connection.close()

ages = [age[0] for age in age_data]

plt.hist(ages, bins=20, edgecolor='black')
plt.title('Distribution of Victim Ages in Reported Crimes')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
