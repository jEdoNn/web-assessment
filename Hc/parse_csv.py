import csv
import sqlite3

# open the connection to the database
conn = sqlite3.connect('Hc/HC_data.db')
cur = conn.cursor()

# drop the data from the table so that if we rerun the file, we don't repeat values
conn.execute('DROP TABLE IF EXISTS deployments')
print("table dropped successfully");
# create table again
conn.execute('CREATE TABLE deployments (Health_Camp_ID INTEGER, Camp_Start_Date TEXT, Camp_End_Date TEXT, Category1 TEXT, Category2 TEXT, Category3 INTEGER)')
print("table created successfully");

conn.execute('DROP TABLE IF EXISTS status')
print("table dropped successfully");
# create the status table again  
conn.execute('CREATE TABLE status (Patient_ID INTEGER PRIMAR KEY, deployID INTEGRER, Donation INTEGRER, Health_Score REAL)')
print("table created successfully");

# open the file to read it into the database
with open('/home/codio/workspace/Hc/Health_Care_Analytics/Health_Camp_Detail.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    for row in reader:
        print(row)
        # check if the row starts with empty string (avoid reading empty lines after the data)
        if row[0]:
            try:

              Health_Camp_ID = int(row[0])
              Camp_Start_Date = row[1]
              Camp_End_Date = row[2]
              Category1 = row[3]
              Category2 = row[4]
              Category3 = int(row[5])

              cur.execute('INSERT INTO deployments VALUES (?,?,?,?,?,?)', (Health_Camp_ID, Camp_Start_Date, Camp_End_Date, Category1, Category2, Category3))
              conn.commit()
            except Exception: # if there are missing values, go to the next row
              pass
        else: # stop reading when reaching empty lines.
            break

print("data parsed successfully");


# open the file to read it into the database
with open('/home/codio/workspace/Hc/Health_Care_Analytics/First_Health_Camp_Attended.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    print('start to work on the status table')
    for row in reader:
        print(row)
        # check if the row starts with empty string (avoid reading empty lines after the data)
        if row[0]: 
            try:
              deployID = int(row[0])
              print('Health_Camp_ID', deployID)
              # link between two tables
              cur.execute('SELECT * from deployments WHERE Health_Camp_ID=?', (deployID,))
              temp_row = cur.fetchall() #temp_row is a tuple, and not an array, so need first item from first item
              
              Patient_ID = int(row[1])
              Donation = int(row[2])
              Health_Score = float(row[3])

              # print(temperature)
              cur.execute('INSERT INTO status (Patient_ID, deployID, Donation, Health_Score) VALUES ( ?,?,?,?)', (Patient_ID, deployID, Donation, Health_Score))
              conn.commit()
            except Exception: # if there are missing values, go to the next row
              pass
        else: # stop reading when reaching empty lines.
            break


print("data parsed successfully");



conn.close()