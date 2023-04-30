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


# upload image in first time
def fileUpload():
    file = request.files['photo']
    filename = file.filename
    file.save(os.path.join('customizeimages', filename))
    return 'customizeimages/'+filename

def addCustomizeImages():
    vendorId = request.json.get('vendorId', None)
    imageUrl = request.json.get('imageUrl', None)
    id = request.json.get('id', None)

    try:
        # sql1 = "DELETE FROM customizeitemimage WHERE vendorId = " + vendorId + " " ;
        # mycursor.execute(sql1)


        sql = "INSERT INTO customizeitemimage (vendorId , imageUrl,id) VALUES (%s, %s,%s)"
        val = (vendorId, imageUrl,id)
        mycursor.execute(sql, val)
        mydb.commit()


        return jsonify("success");
    except Exception as e:
        return "unsuccess"


def deleteCustomizeImages():
    vendorId = request.json.get('vendorId', None)
    try:
        sql1 = "DELETE FROM customizeitemimage WHERE vendorId = " + vendorId + " " ;
        mycursor.execute(sql1)
        mydb.commit()


        return jsonify("success");
    except Exception as e:
        return "unsuccess"


def addCustomizeVendor():
    vendorId = request.json.get('vendorId', None)
    type = request.json.get('type', None)
    status = request.json.get('status', None)


    try:
        sql = "INSERT INTO customizevendors (vendorId, type,status) VALUES (%s,%s,%s)"
        val = (vendorId, type, status )
        mycursor.execute(sql, val)
        mydb.commit()
        last=mycursor.lastrowid

        return jsonify(last);
    except:
        return "unsuccess"

def updateCustomizeStatus():
    vendorId = request.json.get('vendorId', None)
    status = request.json.get('status', None)
    type = request.json.get('type', None)

    try:
        sql =  "UPDATE  customizevendors SET status= '" + status + "' , type= '" + type + "' WHERE vendorId = " + vendorId + " " ;

        # val = (vendorId,status)
        mycursor.execute(sql)
        mydb.commit()
        last=mycursor.lastrowid

        return jsonify(last);
    except:
        return "unsuccess"


def checkCustomizeVendorIsThere():
    try:
        vendorId = request.json.get('vendorId', None)
        sql = "SELECT * FROM  customizevendors where  vendorId=" + vendorId + ""

        mycursor.execute(sql)
        myresult = mycursor.fetchall()

        if (len(myresult) != 0):
            sql = "SELECT * FROM  customizevendors where  vendorId=" + vendorId + " and status='Can Make'"

            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            if (len(myresult) != 0):
               return jsonify("Can Make");
            else:
               return jsonify("Cannot Make")
        else:
            return jsonify("No Customize");

    except  Exception as e:
        return "unsuccess"


def getCustomizeImages():
    try:
      userId = request.json.get('vendorId', None)
      sql = "SELECT imageUrl FROM  customizeitemimage where  vendorId =" + userId + " "

      mycursor.execute(sql)

      myresult = mycursor.fetchall()

      return jsonify(myresult);
    except:
      return "unsuccess"

def getCustomizeType():
    try:
      userId = request.json.get('vendorId', None)
      sql = "SELECT type FROM  customizevendors where  vendorId =" + userId + " "

      mycursor.execute(sql)

      myresult = mycursor.fetchall()

      return jsonify(myresult[0]);
    except:
      return "unsuccess"

def getCustomizeShops():
    try:
      sql = "SELECT users.userId,users.name,users.address,customizeitemimage.imageUrl FROM `customizevendors` " \
            " Inner Join users on users.userId=customizevendors.vendorId" \
            " INNER JOIN customizeitemimage on customizeitemimage.vendorId=customizevendors.vendorId where " \
            " customizevendors.status='Can Make' and customizeitemimage.id=1 ORDER by users.userId desc LIMIT 3"

      mycursor.execute(sql)

      myresult = mycursor.fetchall()

      return jsonify(myresult);
    except:
      return "unsuccess"

def getCustomizeByTypeShops():
    try:
      type = request.json.get('type', None)

      sql = "SELECT users.userId,users.name,users.address,customizeitemimage.imageUrl FROM `customizevendors`" \
            "Inner Join users on users.userId=customizevendors.vendorId INNER JOIN customizeitemimage" \
            " on customizeitemimage.vendorId=customizevendors.vendorId where customizevendors.status='Can Make' " \
            "and customizeitemimage.id=1 " \
            "and customizevendors.type='"+type+"' " \
            "ORDER by customizevendors.customizeVendorId"

      mycursor.execute(sql)

      myresult = mycursor.fetchall()

      return jsonify(myresult);
    except:
      return "unsuccess"

