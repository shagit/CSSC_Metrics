import csv
import psycopg2

conn_string = "dbname='deaup6nh066ma2' user='xibtwlbzmsbctw' password='PDfZm6nQ2bHXjNNPwrnEKFQGoa' host='ec2-54-217-202-110.eu-west-1.compute.amazonaws.com' port='5432'"
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()
reader = csv.reader(open('/app/OE_TAT3.txt','rb'))

for row in reader :
	statement = "INSERT INTO test_oe (document,time_ist,tat,name) VALUES ('"+row[0]+"','"+row[1]+"','"+row[2]+"','"+row[3]+"')";
	cursor.execute(statement)
	conn.commit()
