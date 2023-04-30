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


def fileUpload():
    file = request.files['photo']
    filename = file.filename
    file.save(os.path.join('users', filename))
    return 'users/'+filename


def addUserImage():
    itemId = request.json.get('userId', None)
    imageUrl = request.json.get('imageUrl', None)

    try:
        sql = "INSERT INTO userimage (userId , imageUrl) VALUES (%s, %s)"
        val = (itemId, imageUrl)
        mycursor.execute(sql, val)
        mydb.commit()
        return jsonify("success");
    except:
        return "unsuccess"


def addUser():
    name = request.json.get('name', None)
    phoneNumber = request.json.get('phoneNumber', None)
    address = request.json.get('address', None)
    type = request.json.get('type', None)

    try:
        sql = "INSERT INTO users (name, phoneNumber,address,type) VALUES (%s, %s,%s,%s)"
        val = (name, phoneNumber,address,type )
        mycursor.execute(sql, val)
        mydb.commit()
        last=mycursor.lastrowid

        return jsonify(last);
    except:
        return "unsuccess"


def getUserByPhonenumber():
    try:
        phonenumber = request.json.get('phoneNumber', None)

        sql = "SELECT userId,type FROM users  WHERE phoneNumber= "+phonenumber+" "

        mycursor.execute(sql)

        myresult = mycursor.fetchall()

        return jsonify(myresult[0]);
    except:
        return "unsuccess"

def getUserDetailsByUserId():
    try:
        userId = request.json.get('userId', None)

        sql = "SELECT users.*,userImage.imageUrl FROM users INNER JOIN userImage on userImage.userId=users.userId  WHERE users.userId= "+userId+" "

        mycursor.execute(sql)

        myresult = mycursor.fetchall()

        return jsonify(myresult[0]);
    except:
        return "unsuccess"


def getShops():
    try:
        sql = "SELECT users.userId,users.name,users.address,userImage.imageUrl FROM users INNER JOIN userImage on userImage.userId=users.userId where users.type='vendor' "
        mycursor.execute(sql)

        myresult = mycursor.fetchall()

        return jsonify(myresult);
    except:
        return "unsuccess"

def getDrivers():
    try:
        sql = "SELECT users.userId,users.name,users.address,users.phoneNumber,userImage.imageUrl FROM users INNER JOIN userImage on userImage.userId=users.userId where users.type='driver' "
        mycursor.execute(sql)

        myresult = mycursor.fetchall()

        return jsonify(myresult);
    except:
        return "unsuccess"

