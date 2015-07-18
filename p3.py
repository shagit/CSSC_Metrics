from p2 import *
def Count(dateval):
	#if request.method=='POST':
		#dateval2 = request.form['datepick']
		#dateval = dateval2.encode('utf-8')
	#else:
		#dateval2 = request.form['datepick']
		#dateval = dateval2.encode('utf-8')
	conn_string = "dbname='deaup6nh066ma2' user='xibtwlbzmsbctw' password='PDfZm6nQ2bHXjNNPwrnEKFQGoa' host='ec2-54-217-202-110.eu-west-1.compute.amazonaws.com' port='5432'"
	connection = psycopg2.connect(conn_string)
	cursor = connection.cursor()
	result2 = "SELECT * FROM View_1 where convert(date,Time_IST)=? and Region_CSSC='CSSC'" 
	df2 = pd.read_sql_query(result2,connection, params=(dateval,))
	if df2.empty:
		table2 = pandas.DataFrame({'No Data Available': ['']})
	else:
		table2 = pivot_table(df2, values=["Count"], index=["Name"],columns=["type","Order_Type"], aggfunc=lambda x: sum(x), margins=True, dropna=True)
		table2 = table2.fillna('')
		table2 = table2.rename(columns = {'All':'Total'})
		table2 = table2.rename(index = {'All':'Total'})
	dir = 'C:\\Users\\TE236863\\Desktop\\proj\\templates\\my_file2.html'
	if os.path.isfile(dir):
		os.remove('C:\\Users\\TE236863\\Desktop\\proj\\templates\\my_file2.html')
		Data2 = table2.to_html(open('C:\\Users\\TE236863\\Desktop\\proj\\templates\\my_file2.html', 'w'))
	else:
		Data2 = table2.to_html(open('C:\\Users\\TE236863\\Desktop\\proj\\templates\\my_file2.html', 'w'))
	os.chdir("C:\\Users\\TE236863\\Desktop\\proj\\templates")
	
	#with open("ph1.html") as index:
		#index_text = index.read()
	#with open("my_file2.html") as menu:
		#menu_text = menu.read()
		# I called it index2 so it doesn't overwrite... you can change that
	#with open("index2.html", "w") as index2:
		#index2.write(index_text.replace('<!-- EOD Count -->', menu_text))
	#return render_template('index2.html')