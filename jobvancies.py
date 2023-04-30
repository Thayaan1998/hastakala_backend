import os
from flask import Flask, request, jsonify, send_file, send_from_directory, url_for, render_template, json
from flask_cors import CORS

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="hastkala"
)

mycursor = mydb.cursor()


app = Flask(__name__)
CORS(app)


def addJobVacancies():
    try:
        vendorId   = request.json.get('vendorId', None)
        description  = request.json.get('description', None)
        category  = request.json.get('category', None)
        jobTitle = request.json.get('jobTitle', None)
        status  = request.json.get('status', None)
        Month  = request.json.get('Month', None)
        Year  = request.json.get('Year', None)
        day= request.json.get('day', None)
        sql = "INSERT INTO jobdescription(vendorId,description,category,jobTitle,year,month,day,status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (vendorId,description,category,jobTitle,Year,Month,day,status)
        mycursor.execute(sql, val)
        mydb.commit()
        last = mycursor.lastrowid
        return jsonify(last);
    except:
        return "unsuccess"

def getVacanciesByJobDescriptionId():
  try:
    JobDescriptionId = request.json.get('jobDescriptionId', None)

    sql = "select  JobDescriptionId,vendorId,category,jobTitle,description  " \
          " from jobdescription WHERE status= 'Active' and JobDescriptionId = "+JobDescriptionId+" ORDER by JobDescriptionId  desc"
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    return jsonify(myresult);
  except:
    return "unsuccess"

def getVacanciesByJobCategory():
  try:
    category  = request.json.get('category', None)

    sql = " select JobDescriptionId,vendorId,category,jobTitle,year,month,day,users.name " \
          " from jobdescription INNER JOIN users on users.userId=jobdescription.vendorId  " \
          " WHERE status= 'Active' and category  = '"+category +"' ORDER by JobDescriptionId  desc"
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    return jsonify(myresult);
  except:
    return "unsuccess"

def getVacanciesByVendorId():
  try:
    vendorId  = request.json.get('vendorId', None)

    sql = " select JobDescriptionId,vendorId,category,jobTitle,year,month,day,users.name " \
          " from jobdescription INNER JOIN users on users.userId=jobdescription.vendorId  " \
          " WHERE status= 'Active' and jobdescription.vendorId  = '"+vendorId +"' ORDER by JobDescriptionId  desc"
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    return jsonify(myresult);
  except:
    return "unsuccess"

def getJobTitle():
  try:
    category  = request.json.get('category', None)

    sql = "select  jobTitle " \
          " from jobtitle WHERE category  = '"+category +"' "
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    return jsonify(myresult);
  except:
    return "unsuccess"

def addJobcvs():
    try:
        customerId   = request.json.get('customerId', None)
        JobDescriptionId   = request.json.get('JobDescriptionId', None)
        fileUrl  = request.json.get('fileUrl', None)

        sql = "INSERT INTO jobcvs(customerId,JobDescriptionId,fileUrl) VALUES (%s,%s,%s)"
        val = (customerId,JobDescriptionId,fileUrl)
        mycursor.execute(sql, val)
        mydb.commit()
        last = mycursor.lastrowid
        return jsonify(last);
    except:
        return "unsuccess"

def getAppliedPeople():
  try:
    JobDescriptionId = request.json.get('jobDescriptionId', None)

    sql = "SELECT users.userId,users.name,users.address,users.phoneNumber,fileUrl FROM `jobcvs` " \
          "INNER JOIN users on users.userId=jobcvs.customerId " \
          "INNER JOIN jobdescription on jobdescription.JobDescriptionId=jobcvs.JobDescriptionId " \
          "where jobcvs.JobDescriptionId="+JobDescriptionId

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    return jsonify(myresult);
  except:
    return "unsuccess"

def updateVacancies():
    try:
      JobDescriptionId = request.json.get('jobDescriptionId', None)
      sql = "UPDATE  jobdescription SET status= 'inactive' WHERE JobDescriptionId  = " + JobDescriptionId ;
      mycursor.execute(sql)
      mydb.commit()

      return jsonify("success");
    except:
      return "unsuccess"


def fileUpload():
    file = request.files['photo']
    filename = file.filename
    file.save(os.path.join('cvs', filename))
    return 'cvs/'+filename