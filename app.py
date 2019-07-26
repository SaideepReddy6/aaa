import os

from flask import  Flask,flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import xlrd
import pandas as pd
import pyodbc
import datetime
import loading
import storage

app=Flask(__name__)

@app.route('/')
def upload_form():
	return render_template('upload.html')


@app.route('/handleUpload', methods=['POST'])
def upload_file():
		file = request.files['file']
		filename = secure_filename(file.filename)
		file.save(os.path.join("uploads/", filename))
		return render_template('next.html',data=filename)

@app.route('/handle', methods=['POST'])
def next_process():
	test=request.form['text']
	local_path=os.path.abspath(os.path.curdir)
	book=xlrd.open_workbook(os.path.join(local_path,'uploads/',test))
	x=book.sheet_by_name("Sheet1")
	c=0
	for i in range(x.ncols):
    		for j in range(x.nrows):
    				if x.cell(j,i).value=="":
    						c=c+1
	if c>0:
		x="MISSING "+str(c)+" "+"Values"					
		return render_template('complete.html',data=x)
	else:
		x="No missing Values"
		l=[x,test]					
		return render_template('complete2.html',data=l)

@app.route('/completed', methods=['POST'])
def file_storage():
	test=request.form['text']
	x=storage.run_sample(test)
	return render_template('final.html',data=x)