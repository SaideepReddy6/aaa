
import os
import xlrd
import pyodbc
import datetime

def data_load(test):
	local_path=os.path.abspath(os.path.curdir)
	book=xlrd.open_workbook(os.path.join(local_path,'uploads/',test))
	sheet=book.sheet_by_name("Sheet1")
	server = 'r-d-credit-server-a.database.windows.net'
	database = 'r-d-credit-sql-q'
	username = 'azurewebapp'
	password = 'Bw4KC8OxlNy3tyoCzC'
	driver= '{ODBC Driver 17 for SQL Server}'
	cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
	cursor = cnxn.cursor()
	query="""INSERT INTO Employees (Employee_Number, Employee_Name, Job_Title, Hire_Date, Term_Date, State_ID, Time_stamp) VALUES (?,?,?,?,?,?,?)"""
	for r in range(1,10):
		Employee_Number= int(sheet.cell(r,0).value)
		Employee_Name= sheet.cell(r,1).value
		Job_Title= sheet.cell(r,2).value
		Hire= sheet.cell(r,4).value
		if Hire=='':
    			Hire_Date='1-1-1900'
		else:
			y, m, d, h, i, s= xlrd.xldate_as_tuple(sheet.cell(r,4).value,book.datemode)
			Hire_Date=("{1}-{2}-{0}".format(y, m, d))
		Term=sheet.cell(r,5).value
		if Term=='':
			Term_Date='12-31-2299'
		else:
			y, m, d, h, i, s= xlrd.xldate_as_tuple(sheet.cell(r,5).value,book.datemode)
			Term_Date= ("{1}-{2}-{0}".format(y, m, d))
		State_ID= sheet.cell(r,6).value
		Time_stamp=str(datetime.datetime.now())[0:-3]
		values = (Employee_Number, Employee_Name, Job_Title, Hire_Date, Term_Date, State_ID, Time_stamp)
		cursor.execute(query,values)
	cursor.close()
	cnxn.commit()
	cnxn.close()
	return ('done')