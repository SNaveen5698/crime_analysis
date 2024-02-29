#3difference in crime rates between male and female victims
import pymysql
import matplotlib.pyplot as plt

connection = pymysql.connect(user='root', password='naveen5698', host='127.0.0.1', database='crime')
cursor = connection.cursor()

cursor.execute("SELECT Vict_Sex, COUNT(*) AS Number_of_Crimes FROM crime_data GROUP BY Vict_Sex")
sex_data = cursor.fetchall()

cursor.close()
connection.close()

sex_labels, crime_counts = zip(*sex_data)
'''sex_labels = [row[0] for row in sex_data]
crime_counts = [row[1] for row in sex_data]'''


plt.pie(crime_counts, labels=sex_labels, colors=['blue', 'pink'], autopct='%1.1f%%', startangle=90)
plt.title('Crime Rates Between Male and Female Victims')
plt.show()
