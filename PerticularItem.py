import os
from flask import Flask, request, jsonify, send_file, send_from_directory, url_for, render_template, json
from flask_cors import CORS
from datetime import datetime

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="hastkala"
)

mycursor = mydb.cursor()


def addRating(userId, itemId,rating):
  try:
    sql = "INSERT INTO rating (itemId ,userId,rating) VALUES (%s,%s,%s)"
    val = (itemId, userId,rating)
    mycursor.execute(sql, val)
    mydb.commit()

    return jsonify("success");
  except:
    return "unsuccess"

def updateRating(userId, itemId,rating):
    try:
      sql = "UPDATE  rating SET rating= "+rating+" WHERE itemId = " + itemId + " and userId = " + userId;
      mycursor.execute(sql)
      mydb.commit()

      return jsonify("success");
    except:
      return "unsuccess"

def makeRatingByUser():
  try:
    itemId = request.json.get('itemId', None)
    userId = request.json.get('userId', None)
    rating = request.json.get('rating', None)
    sql = "SELECT * FROM  rating where  userId=" + userId + " and itemId =" + itemId

    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    if (len(myresult) == 0):
      addRating(userId, itemId,rating);
    else:
      updateRating(userId, itemId, rating)
    return jsonify("Success");
  except:
    return "unsuccess"

def getPerticularRating():
    try:
      itemId = request.json.get('itemId', None)
      userId = request.json.get('userId', None)
      sql = "SELECT * FROM  rating where  userId=" + userId + " and itemId =" + itemId

      mycursor.execute(sql)

      myresult = mycursor.fetchall()

      return jsonify(myresult);
    except:
      return "unsuccess"


def avgRating():
  try:
    itemId = request.json.get('itemId', None)
    sql = "SELECT count(rating),sum(rating)/count(rating) FROM  rating where  itemId =" + itemId

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    return jsonify(myresult);
  except:
    return "unsuccess"

def sendComment():
  try:
    itemId = request.json.get('itemId', None)
    userId = request.json.get('userId', None)
    comment = request.json.get('sendComment', None)
    sql = "INSERT INTO comment (itemId ,userId,comment,sendDate) VALUES (%s,%s,%s,%s)"
    val = (itemId, userId,comment,datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
    mycursor.execute(sql, val)
    mydb.commit()

    return jsonify("success");
  except:
    return "unsuccess"

def getCommentByItem():
  try:
    itemId = request.json.get('itemId', None)
    sql = "SELECT users.name,comment.comment,comment.sendDate FROM comment join users on users.userId=comment.userId where  itemId =" + itemId +" order by comment.commentId desc "

    mycursor.execute(sql)

    myresult = mycursor.fetchall()
    return jsonify(myresult);
  except:
    return "unsuccess"

def addCart(itemId,userId,quantity):
  try:
    itemId = request.json.get('itemId', None)
    userId = request.json.get('userId', None)
    quantity = request.json.get('quantity', None)

    sql = "INSERT INTO cart (itemId ,userId,quantity,status) VALUES (%s,%s,%s,%s)"
    val = (itemId, userId,quantity,'pending')
    mycursor.execute(sql, val)
    mydb.commit()

    return jsonify("success");
  except:
    return "unsuccess"

def updateCart(userId, itemId, quantity):
    try:
      sql = "UPDATE  cart SET quantity= " + quantity + " WHERE itemId = " + itemId + " and userId = " + userId;
      mycursor.execute(sql)
      mydb.commit()
      mydb.commit()

      return jsonify("success");
    except:
      return "unsuccess"



def addOrUpdateCart():
  try:
    itemId = request.json.get('itemId', None)
    userId = request.json.get('userId', None)
    quantity = request.json.get('quantity', None)
    sql = "SELECT * FROM  cart where  status='pending' and  userId=" + userId + " and itemId =" + itemId

    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    if (len(myresult) == 0):
      addCart(userId, itemId,quantity)
    else:
      updateCart(userId, itemId, quantity)
    return jsonify("Success");
  except:
    return "unsuccess"

def getPerticularCartForUser():
    try:
      itemId = request.json.get('itemId', None)
      userId = request.json.get('userId', None)
      sql = "SELECT quantity FROM  cart  where status='pending' and   userId=" + userId + " and itemId =" + itemId

      mycursor.execute(sql)

      myresult = mycursor.fetchall()

      return jsonify(myresult);
    except:
      return "unsuccess"


def getAllCartForUser():
  try:
    userId = request.json.get('userId', None)
    sql = "SELECT cartId,item.itemId,itemName,cart.quantity,imageUrl,price,cart.quantity*price as total,item.userId,users.name " \
          " FROM cart INNER join item on item.itemId=cart.itemId INNER JOIN itemimage on itemimage.itemId=item.itemId" \
          " INNER join users on users.userId=item.userId " \
          " where status='pending' and itemimage.id=1 and   cart.userId=" + userId

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    return jsonify(myresult);
  except:
    return "unsuccess"


def getCountCart():
  try:
    userId = request.json.get('userId', None)
    sql = "SELECT count(*) FROM cart INNER join item on item.itemId=cart.itemId INNER JOIN itemimage on itemimage.itemId=item.itemId where status='pending' and itemimage.id=1 and   cart.userId=" + userId

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    return jsonify(myresult);
  except:
    return "unsuccess"

def deleteCartItems():
    try:
      cartId = request.json.get('cartId', None)
      sql = "UPDATE  cart SET status= 'Ordered' WHERE cartId = " + cartId + " ";
      mycursor.execute(sql)
      mydb.commit()

      return jsonify("success");
    except:
      return "unsuccess"




