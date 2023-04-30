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


def getOrders():
    try:
        vendorId = request.json.get('vendorId', None)

        sql = "select  orders.orderId,orders.status,orders.Month,orders.Year,orders.day" \
              " from orders WHERE orders.vendorId="+vendorId+" ORDER by orders.orderId desc"

        mycursor.execute(sql)

        myresult = mycursor.fetchall()

        return jsonify(myresult);
    except Exception as e:
        return "unsuccess"



def getCustomizeProductOrders():
    try:
        vendorId = request.json.get('vendorId', None)

        sql =   "SELECT customizeorders.customizeOrderId,customizeorders.status,customizeorders.Month,customizeorders.Year," \
                "customizeorders.day FROM `customizeorders` WHERE vendorId="+vendorId+" and status in('Requested','Images Resent','Ongoing','Accepted','Resend Image')"

        mycursor.execute(sql)

        myresult = mycursor.fetchall()

        return jsonify(myresult);
    except:
        return "unsuccess"




def addCustomizeOrder():

    try:

        customerId  = request.json.get('customerId', None)
        vendorId   = request.json.get('vendorId', None)
        description  = request.json.get('description', None)
        total  = request.json.get('total', None)
        status  = request.json.get('status', None)
        Month  = request.json.get('Month', None)
        Year  = request.json.get('Year', None)
        day= request.json.get('day', None)

        sql = "INSERT INTO customizeorders(customerId ,vendorId,description,total,status,Month,Year,day) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (customerId,vendorId,description,total,status,Month,Year,day)
        mycursor.execute(sql, val)
        mydb.commit()

        last = mycursor.lastrowid


        return jsonify(last);
    except:
        return "unsuccess"




def addCustomizeordersimage():

    try:

        customizeOrderId   = request.json.get('customizeOrderId', None)
        imageUrl   = request.json.get('imageUrl', None)
        id  = request.json.get('id', None)


        sql = "INSERT INTO customizeordersimage(customizeOrderId ,imageUrl,id) VALUES (%s,%s,%s)"
        val = (customizeOrderId,imageUrl,id)
        mycursor.execute(sql, val)
        mydb.commit()

        return jsonify("success");
    except:
        return "unsuccess"



def getCustomizeOrderImages():
    try:
        customizeOrderId  = request.json.get('customizeOrderId', None)

        sql =   "SELECT imageUrl FROM customizeordersimage WHERE customizeOrderId ="+customizeOrderId +" "

        mycursor.execute(sql)

        myresult = mycursor.fetchall()

        return jsonify(myresult);
    except:
        return "unsuccess"

def getCustomizeOrderDetails():
    try:
        customizeOrderId  = request.json.get('customizeOrderId', None)

        sql =   "SELECT customerId,vendorId,description,status,total FROM customizeorders WHERE customizeOrderId ="+customizeOrderId +" "

        mycursor.execute(sql)

        myresult = mycursor.fetchall()

        return jsonify(myresult);
    except:
        return "unsuccess"



def updateCustomizeOrder():
    try:

        customizeOrderId = request.json.get('customizeOrderId', None)
        status = request.json.get('status', None)

        sql ="UPDATE  customizeorders SET status = '" + status + "' WHERE customizeOrderId = " + customizeOrderId
        mycursor.execute(sql)
        mydb.commit()
        return jsonify("success");
    except:
        return "unsuccess"

def updateCustomizePrice():
    try:

        customizeOrderId = request.json.get('customizeOrderId', None)
        total = request.json.get('total', None)

        sql ="UPDATE  customizeorders SET total = '" + total + "' WHERE customizeOrderId = " + customizeOrderId
        mycursor.execute(sql)
        mydb.commit()
        return jsonify("success");
    except:
        return "unsuccess"

def getCustomizeOrdersByCustomerId():
    try:
        customerId  = request.json.get('customerId', None)
        status  = request.json.get('status', None)


        sql ="SELECT customizeOrderId,customerId,vendorId,description,status,Year,month,day FROM customizeorders WHERE customerId  ="+customerId +" and status = '"+status+"'"

        mycursor.execute(sql)

        myresult = mycursor.fetchall()

        return jsonify(myresult);
    except:
        return "unsuccess"



def deleteCustomizeordersimage():

    try:

        customizeOrderId   = request.json.get('customizeOrderId', None)
        sql = "DELETE FROM customizeordersimage WHERE  customizeOrderId = " + customizeOrderId
        mycursor.execute(sql)
        mydb.commit()

        return jsonify("success");
    except:
        return "unsuccess"

def addOrder():
    try:
        customerId  = request.json.get('customerId', None)
        vendorId   = request.json.get('vendorId', None)
        total  = request.json.get('total', None)
        paymentType  = request.json.get('paymentType', None)
        status  = request.json.get('status', None)
        Month  = request.json.get('Month', None)
        Year  = request.json.get('Year', None)
        day= request.json.get('day', None)
        sql = "INSERT INTO orders(customerId ,vendorId,paymentType,total,status,Month,Year,day) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (customerId,vendorId,paymentType,total,status,Month,Year,day)
        mycursor.execute(sql, val)
        mydb.commit()
        last = mycursor.lastrowid
        return jsonify(last);
    except Exception as e:
        return "unsuccess"

def addOrdereditem():
    try:
        orderId  = request.json.get('orderId', None)
        itemId   = request.json.get('itemId', None)
        quantity   = request.json.get('quantity', None)
        price   = request.json.get('price', None)
        total  = request.json.get('total', None)

        sql = "INSERT INTO ordereditem(orderId,itemId,quantity,price,total) VALUES (%s,%s,%s,%s,%s)"
        val = (int(orderId),itemId,quantity,price,total)
        mycursor.execute(sql, val)
        mydb.commit()
        last = mycursor.lastrowid
        return jsonify(last);
    except Exception as e:
        return "unsuccess"

def getOrdersByCustomerId():
    try:
        customerId = request.json.get('customerId', None)
        status  = request.json.get('status', None)


        sql = "select  orders.orderId,orders.customerId,orders.vendorId,orders.paymentType,orders.status,orders.Year,orders.Month,orders.day" \
              " from orders WHERE orders.customerId="+customerId+" and status = '"+status+"' ORDER by orderId desc"

        mycursor.execute(sql)

        myresult = mycursor.fetchall()

        return jsonify(myresult);
    except:
        return "unsuccess"


def getOrderDetails():
    try:
        orderId   = request.json.get('orderId', None)

        sql =   "SELECT customerId,vendorId,paymentType,status,total FROM orders WHERE orderId  ="+orderId  +" "

        mycursor.execute(sql)

        myresult = mycursor.fetchall()

        return jsonify(myresult);
    except:
        return "unsuccess"

def getPeticularOrderDetails():
  try:
    orderId  = request.json.get('orderId', None)


    sql = "SELECT orderId ,item.itemId,itemName,ordereditem.quantity,imageUrl," \
          " ordereditem.price,ordereditem.quantity*ordereditem.price as total,item.userId,users.name  " \
          " FROM ordereditem INNER join item on item.itemId=ordereditem.itemId" \
          " INNER JOIN itemimage on itemimage.itemId=item.itemId" \
          "  INNER join users on users.userId=item.userId"  \
          "  where  itemimage.id=1 and   ordereditem.orderId =" + orderId

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    return jsonify(myresult);
  except:
    return "unsuccess"

def getPeticularOrderDetailsByStatus():
  try:
    # orderId  = request.json.get('orderId', None)


    sql = "select  orders.orderId" \
          " from orders WHERE orders.status='Ongoing' ORDER by orders.orderId desc"
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    return jsonify(myresult);
  except:
    return "unsuccess"

def getPeticularCustomozeOrderDetailsByStatus():
  try:
    # orderId  = request.json.get('orderId', None)

    sql = "select  customizeorders.customizeOrderId " \
          " from customizeorders WHERE customizeorders.status='Ongoing' ORDER by customizeorders.customizeOrderId desc"
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    return jsonify(myresult);
  except:
    return "unsuccess"

def updateOrders():
    try:

        orderId = request.json.get('orderId', None)
        status = request.json.get('status', None)

        sql ="UPDATE  orders SET status = '" + status + "' WHERE orderId = " + orderId
        mycursor.execute(sql)
        mydb.commit()
        return jsonify("success");
    except:
        return "unsuccess"

def addDeliver():

    try:

        driverId= request.json.get('driverId', None)
        vendorId= request.json.get('vendorId', None)
        normalItems= request.json.get('normalItems', None)
        customizeItems = request.json.get('customizeItems', None)
        status = request.json.get('status', None)
        year = request.json.get('year', None)
        month = request.json.get('month', None)
        day = request.json.get('day', None)
        deliveryCost = request.json.get('deliveryCost', None)


        sql = "INSERT INTO deliver(driverId ,vendorId,normalItems,customizeItems,status,year,month,day,deliveryCost) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (driverId ,vendorId,normalItems,customizeItems,status,year,month,day,deliveryCost)
        mycursor.execute(sql, val)
        mydb.commit()

        return jsonify("success");
    except:
        return "unsuccess"

def getDeliveryItemssByStatus():
  try:
    status  = request.json.get('status', None)
    driverId  = request.json.get('driverId', None)


    sql = "select  deliverId,year,month,day " \
          " from deliver WHERE deliver.status= '"+status+"' and driverId = "+driverId+" ORDER by deliverId desc"
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    return jsonify(myresult);
  except:
    return "unsuccess"

def getPeticularDeliveryItem():
  try:
    deliveryId  = request.json.get('deliverId', None)
    sql = "select  * from deliver WHERE deliverId= '"+deliveryId+"' "
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    return jsonify(myresult);
  except:
    return "unsuccess"

def updateDeliveryItem():
    try:
        deliverId = request.json.get('deliverId', None)
        status = request.json.get('status', None)
        sql ="UPDATE  deliver SET status = '" + status + "' WHERE deliverId = " + deliverId
        mycursor.execute(sql)
        mydb.commit()
        return jsonify("success");
    except:
        return "unsuccess"

def addDamageItem1():

    try:

        customerId= request.json.get('customerId', None)
        vendorId= request.json.get('vendorId', None)
        type= request.json.get('type', None)
        imageurl= request.json.get('imageurl', None)

        sql = "INSERT INTO damageitem1(customerId,vendorId,type,imageurl) VALUES (%s,%s,%s,%s)"
        val = (customerId,vendorId,type,imageurl)
        mycursor.execute(sql, val)
        mydb.commit()

        return jsonify("success");
    except:
        return "unsuccess"


def addDamageItem2():

    try:

        driverId= request.json.get('driverId', None)
        vendorId= request.json.get('vendorId', None)
        imageurl= request.json.get('imageurl', None)
        sql = "INSERT INTO damageitem2(driverId,vendorId,imageurl) VALUES (%s,%s,%s)"
        val = (driverId ,vendorId,imageurl)
        mycursor.execute(sql, val)
        mydb.commit()

        return jsonify("success");
    except:
        return "unsuccess"




def fileUpload():
    file = request.files['photo']
    filename = file.filename
    file.save(os.path.join('customizeorders', filename))
    return 'customizeorders/'+filename
