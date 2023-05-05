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
    file.save(os.path.join('items', filename))
    return 'items/'+filename

def addItemImage():
    itemId = request.json.get('itemId', None)
    imageUrl = request.json.get('imageUrl', None)
    id = request.json.get('id', None)

    try:
        sql = "INSERT INTO itemimage (itemId , imageUrl,id) VALUES (%s, %s,%s)"
        val = (itemId, imageUrl,id)
        mycursor.execute(sql, val)
        mydb.commit()
        last=mycursor.lastrowid

        return jsonify("success");
    except:
        return "unsuccess"


def addItem():
    name = request.json.get('itemName', None)
    price = request.json.get('price', None)
    quantity = request.json.get('quantity', None)
    itemType = request.json.get('itemType', None)
    description = request.json.get('description', None)
    vendorId = request.json.get('vendorId', None)

    try:
        sql = "INSERT INTO item (itemName, price,quantity,itemType,description,userId ) VALUES (%s,%s,%s,%s,%s,%s)"
        val = (name, price, quantity,itemType, description,vendorId )
        mycursor.execute(sql, val)
        mydb.commit()
        last=mycursor.lastrowid

        return jsonify(last);
    except:
        return "unsuccess"





def getItemByVendor():
    try:
        vendorId = request.json.get('vendorId', None)

        sql = "SELECT item.itemId,item.itemName,item.price,item.quantity,item.description,itemimage.itemImageId," \
              "itemimage.imageUrl FROM item JOIN itemimage on itemimage.itemId=item.itemId " \
              "WHERE itemimage.id=1 and item.userId="+vendorId+" ORDER by item.itemId desc"

        mycursor.execute(sql)

        myresult = mycursor.fetchall()

        return jsonify(myresult);
    except Exception as e:
        return "unsuccess"


def getItemByType():
    try:
        itemType = request.json.get('itemType', None)

        sql = "SELECT item.itemId,item.itemName,item.price,item.quantity,item.description,itemimage.itemImageId,itemimage.imageUrl FROM item JOIN itemimage on itemimage.itemId=item.itemId WHERE itemimage.id=1 and item.itemType='"+itemType+"' ORDER by item.itemId desc limit 3"

        mycursor.execute(sql)

        myresult = mycursor.fetchall()

        return jsonify(myresult);
    except:
        return "unsuccess"

def getItemByType2():
    try:
        itemType = request.json.get('itemType', None)

        sql = "SELECT item.itemId,item.itemName,item.price,item.quantity,item.description,itemimage.itemImageId,itemimage.imageUrl FROM item JOIN itemimage on itemimage.itemId=item.itemId WHERE itemimage.id=1 and item.itemType='"+itemType+"' ORDER by item.itemId desc "

        mycursor.execute(sql)

        myresult = mycursor.fetchall()

        return jsonify(myresult);
    except:
        return "unsuccess"

def getItemByType3():
    try:
        itemType = request.json.get('itemType', None)
        itemName = request.json.get('itemName', None)


        sql = "SELECT item.itemId,item.itemName,item.price,item.quantity,item.description," \
              "itemimage.itemImageId,itemimage.imageUrl FROM item JOIN itemimage on itemimage.itemId=item.itemId " \
              "WHERE itemimage.id=1 and item.itemType='"+itemType+"' and item.itemName like  '%"+itemName+"%' ORDER by item.itemId desc "

        mycursor.execute(sql)

        myresult = mycursor.fetchall()

        return jsonify(myresult);
    except:
        return "unsuccess"

def getItemByType4():
    try:
        itemType = request.json.get('itemType', None)
        type = request.json.get('type', None)


        sql = "SELECT item.itemId,item.itemName,item.price,item.quantity,item.description," \
              " itemimage.itemImageId,itemimage.imageUrl FROM item " \
              " JOIN itemimage on itemimage.itemId=item.itemId " \
              " JOIN machinelearningimages on machinelearningimages.itemId=item.itemId " \
              " WHERE itemimage.id=1 and item.itemType='"+itemType+"' " \
              " and machinelearningimages.type='" + type + "' " \
              " ORDER by item.itemId desc "

        mycursor.execute(sql)

        myresult = mycursor.fetchall()

        return jsonify(myresult);
    except:
        return "unsuccess"



def makeFavourite(userId,itemId):

    try:
        sql = "INSERT INTO favourites (itemId ,userId) VALUES (%s,%s)"
        val = (itemId,userId )
        mycursor.execute(sql, val)
        mydb.commit()

        return jsonify("success");
    except:
        return "unsuccess"

def deleteFavourite(userId,itemId):
    try:
        sql = "DELETE FROM favourites WHERE itemId = "+itemId+" and userId = "+userId;
        mycursor.execute(sql)
        mydb.commit()

        return jsonify("success");
    except:
        return "unsuccess"


def getItemByUserIdAndItemId():
    try:
        itemId = request.json.get('itemId', None)
        userId = request.json.get('userId', None)
        sql = "SELECT * FROM  favourites where  userId="+userId+" and itemId ="+itemId+" "

        mycursor.execute(sql)
        myresult = mycursor.fetchall()

        if(len(myresult)==0):
            makeFavourite(userId,itemId);
        else:
            deleteFavourite(userId,itemId)
        return jsonify("Success");
    except:
        return "unsuccess"




def getItemByFavourites():
    try:
        userId = request.json.get('userId', None)

        sql = "SELECT item.itemId,item.itemName,item.price,item.quantity,item.description,itemimage.itemImageId,itemimage.imageUrl FROM " \
              "item JOIN itemimage on itemimage.itemId=item.itemId" \
              " JOIN Favourites on item.itemId=Favourites.itemId" \
              " WHERE itemimage.id=1 and Favourites.userId="+userId+" ORDER by item.itemId desc "



        mycursor.execute(sql)

        myresult = mycursor.fetchall()

        return jsonify(myresult);
    except:
        return "unsuccess"


def getItemByItemId():
    try:
        itemId = request.json.get('itemId', None)

        sql = "SELECT item.itemId,item.itemName,item.price,item.quantity,item.description,itemimage.itemImageId,itemimage.imageUrl FROM item JOIN itemimage on itemimage.itemId=item.itemId WHERE  item.itemId="+itemId+" "

        mycursor.execute(sql)

        myresult = mycursor.fetchall()

        return jsonify(myresult);
    except:
        return "unsuccess"


def getItems():
    try:


        sql = "SELECT item.itemId,item.itemName,item.price,item.quantity,item.description,itemimage.itemImageId,itemimage.imageUrl FROM item JOIN itemimage on itemimage.itemId=item.itemId WHERE itemimage.id=1  ORDER by item.itemId desc limit 3"

        mycursor.execute(sql)

        myresult = mycursor.fetchall()

        return jsonify(myresult);
    except:
        return "unsuccess"


def machinelearningimages():
    itemId = request.json.get('itemId', None)
    type = request.json.get('type', None)

    try:
        sql = "INSERT INTO machinelearningimages(itemId,type) VALUES (%s,%s)"
        val = (itemId ,type)
        mycursor.execute(sql, val)
        mydb.commit()
        last=mycursor.lastrowid

        return jsonify(last);
    except:
        return "unsuccess"



