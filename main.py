import os
from flask import Flask, request, jsonify, send_file, send_from_directory, url_for, render_template
from flask_cors import CORS
from flask import send_from_directory, current_app as app


import PerticularItem

app = Flask(__name__)
CORS(app)
import Items
import Orders
import Users
import PerticularItem
import Customizeshop
import jobvancies

# Item Part
@app.route('/uploadImage', methods=['POST'])
def fileUpload():
    return Items.fileUpload();

@app.route('/getItems', methods=['POST'])
def getItems():
    return Items.getItems();

@app.route('/addItem', methods=['GET', 'POST'])
def addItem():
    return Items.addItem();

@app.route('/addItemImage', methods=['GET', 'POST'])
def addItemImage():
    return Items.addItemImage();

@app.route('/getItemByVendor', methods=['GET', 'POST'])
def getItemByVendor():
    return Items.getItemByVendor();

@app.route('/getItemType', methods=['GET', 'POST'])
def getItemType():
    return Items.getItemByType();

@app.route('/getItemType2', methods=['GET', 'POST'])
def getItemType2():
    return Items.getItemByType2();

@app.route('/getItemByItemId', methods=['GET', 'POST'])
def getItemByItemId():
    return Items.getItemByItemId();

@app.route('/getItemByUserIdAndItemId', methods=['GET', 'POST'])
def getItemByUserIdAndItemId():
    return Items.getItemByUserIdAndItemId();


@app.route('/getItemByFavourites', methods=['GET', 'POST'])
def getItemByFavourites():
    return Items.getItemByFavourites();

@app.route('/getFile')
def getFile ():
    args = request.args
    name = args.get('path')


    return send_file(name, mimetype='image/gif')


@app.route('/getFile2')
def getFile2 ():
    args = request.args
    name = args.get('path').split("/")

    return send_from_directory(name[0],name[1])

    # return send_file(name, mimetype='pdf')



#User Part
@app.route('/uploadUserImage', methods=['POST'])
def fileUserUpload():
    return Users.fileUpload();

@app.route('/addUser', methods=['GET', 'POST'])
def addUser():
    return Users.addUser();

@app.route('/addUserImage', methods=['GET', 'POST'])
def addUserImage():
    return Users.addUserImage();

@app.route('/getUserByPhonenumber', methods=['GET', 'POST'])
def getUserByPhonenumber():
    return Users.getUserByPhonenumber();

@app.route('/getUserDetailsByUserId', methods=['GET', 'POST'])
def getUserDetailsByUserId():
    return Users.getUserDetailsByUserId()


@app.route('/getShops', methods=['GET', 'POST'])
def getShops():
    return Users.getShops()

@app.route('/getDrivers', methods=['GET', 'POST'])
def getDrivers():
    return Users.getDrivers()


#Rating Part
@app.route('/makeRatingByUser', methods=['GET', 'POST'])
def makeRatingByUser():
    return PerticularItem.makeRatingByUser();

@app.route('/getPerticularRating', methods=['GET', 'POST'])
def getPerticularRating():
    return PerticularItem.getPerticularRating();

@app.route('/avgRating', methods=['GET', 'POST'])
def avgRating():
    return  PerticularItem.avgRating();



#Comments Part
@app.route('/sendComment', methods=['GET', 'POST'])
def sendComment():
    return PerticularItem.sendComment();

@app.route('/getCommentByItem', methods=['GET', 'POST'])
def getCommentByItem():
    return PerticularItem.getCommentByItem();

#cart
@app.route('/addOrUpdateCart', methods=['GET', 'POST'])
def addOrUpdateCart():
    return PerticularItem.addOrUpdateCart();


@app.route('/getPerticularCartForUser', methods=['GET', 'POST'])
def getPerticularCartForUser():
    return PerticularItem.getPerticularCartForUser();

@app.route('/getAllCartForUser', methods=['GET', 'POST'])
def getAllCartForUser():
    return PerticularItem.getAllCartForUser();

@app.route('/getCountCart', methods=['GET', 'POST'])
def getCountCart():
    return PerticularItem.getCountCart();


#Customize Part
@app.route('/addCustomizeImage', methods=['GET', 'POST'])
def addCustomizeImage():
    return Customizeshop.fileUpload()

@app.route('/deleteCustomizeImages', methods=['GET', 'POST'])
def deleteCustomizeImages():
    return Customizeshop.deleteCustomizeImages()

@app.route('/addCustomizeImages', methods=['GET', 'POST'])
def addCustomizeImages():
    return Customizeshop.addCustomizeImages()

@app.route('/addCustomizeVendor', methods=['GET', 'POST'])
def addCustomizeVendor():
    return Customizeshop.addCustomizeVendor()


@app.route('/updateCustomizeStatus', methods=['GET', 'POST'])
def updateCustomizeStatus():
    return Customizeshop.updateCustomizeStatus()

@app.route('/checkCustomizeVendorIsThere', methods=['GET', 'POST'])
def checkCustomizeVendorIsThere():
    return Customizeshop.checkCustomizeVendorIsThere()

@app.route('/getCustomizeImages', methods=['GET', 'POST'])
def getCustomizeImages():
    return Customizeshop.getCustomizeImages()

@app.route('/getCustomizeType', methods=['GET', 'POST'])
def getCustomizeType():
    return Customizeshop.getCustomizeType()


@app.route('/getCustomizeShops', methods=['GET', 'POST'])
def getCustomizeShops():
    return Customizeshop.getCustomizeShops()

@app.route('/getCustomizeByTypeShops', methods=['GET', 'POST'])
def getCustomizeByTypeShops():
    return Customizeshop.getCustomizeByTypeShops()


#Order Part
@app.route('/getOrders', methods=['GET', 'POST'])
def getOrders():
    return Orders.getOrders();

@app.route('/getCustomizeProductOrders', methods=['GET', 'POST'])
def getCustomizeProductOrders():
    return Orders.getCustomizeProductOrders();

@app.route('/addCustomizeOrder', methods=['GET', 'POST'])
def addCustomizeOrder():
    return Orders.addCustomizeOrder();

@app.route('/addCustomizeordersimage', methods=['GET', 'POST'])
def addCustomizeordersimage():
    return Orders.addCustomizeordersimage();

@app.route('/uploadCustomizeOrderImage', methods=['POST'])
def uploadCustomizeOrderImage():
    return Orders.fileUpload();

@app.route('/getCustomizeOrderImages', methods=['POST'])
def getCustomizeOrderImages():
    return Orders.getCustomizeOrderImages();

@app.route('/getCustomizeOrderDetails', methods=['POST'])
def getCustomizeOrderDetails():
    return Orders.getCustomizeOrderDetails();

@app.route('/updateCustomizeOrder', methods=['POST'])
def updateCustomizeOrder():
    return Orders.updateCustomizeOrder();

@app.route('/updateCustomizePrice', methods=['POST'])
def updateCustomizePrice():
    return Orders.updateCustomizePrice();

@app.route('/getCustomizeOrdersByCustomerId', methods=['POST'])
def getCustomizeOrdersByCustomerId():
    return Orders.getCustomizeOrdersByCustomerId();

@app.route('/deleteCustomizeordersimage', methods=['POST'])
def deleteCustomizeordersimage():
    return Orders.deleteCustomizeordersimage();

@app.route('/addOrder', methods=['POST'])
def addOrder():
    return Orders.addOrder();

@app.route('/addOrdereditem', methods=['POST'])
def addOrdereditem():
    return Orders.addOrdereditem();

@app.route('/deleteCartItems', methods=['POST'])
def deleteCartItems():
    return PerticularItem.deleteCartItems();


@app.route('/getOrdersByCustomerId', methods=['POST'])
def getOrdersByCustomerId():
    return Orders.getOrdersByCustomerId();

@app.route('/getPeticularOrderDetails', methods=['POST'])
def getPeticularOrderDetails():
    return Orders.getPeticularOrderDetails();

@app.route('/getOrderDetails', methods=['POST'])
def getOrderDetails():
    return Orders.getOrderDetails();

@app.route('/updateOrders', methods=['POST'])
def updateOrders():
    return Orders.updateOrders();

@app.route('/getPeticularOrderDetailsByStatus', methods=['POST'])
def getPeticularOrderDetailsByStatus():
    return Orders.getPeticularOrderDetailsByStatus();

@app.route('/getPeticularCustomozeOrderDetailsByStatus', methods=['POST'])
def getPeticularCustomozeOrderDetailsByStatus():
    return Orders.getPeticularCustomozeOrderDetailsByStatus();

@app.route('/addDeliver', methods=['POST'])
def addDeliver():
    return Orders.addDeliver();

@app.route('/getDeliveryItemssByStatus', methods=['POST'])
def getDeliveryItemssByStatus():
    return Orders.getDeliveryItemssByStatus();

@app.route('/getPeticularDeliveryItem', methods=['POST'])
def getPeticularDeliveryItem():
    return Orders.getPeticularDeliveryItem();

@app.route('/updateDeliveryItem', methods=['POST'])
def updateDeliveryItem():
    return Orders.updateDeliveryItem();

@app.route('/addDamageItem1', methods=['POST'])
def addDamageItem1():
    return Orders.addDamageItem1();

@app.route('/addDamageItem2', methods=['POST'])
def addDamageItem2():
    return Orders.addDamageItem2();


#Job Vacancies
@app.route('/addJobVacancies', methods=['POST'])
def addJobVacancies():
    return jobvancies.addJobVacancies()

@app.route('/getJobTitle', methods=['POST'])
def getJobTitle():
    return jobvancies.getJobTitle()

@app.route('/getVacanciesByJobCategory', methods=['POST'])
def getVacanciesByJobCategory():
    return jobvancies.getVacanciesByJobCategory()

@app.route('/getVacanciesByJobDescriptionId', methods=['POST'])
def getVacanciesByJobDescriptionId():
    return jobvancies.getVacanciesByJobDescriptionId()

@app.route('/cvUpload', methods=['POST'])
def cvUpload():
    return jobvancies.fileUpload()

@app.route('/addJobcvs', methods=['POST'])
def addJobcvs():
    return jobvancies.addJobcvs()

@app.route('/getVacanciesByVendorId', methods=['POST'])
def getVacanciesByVendorId():
    return jobvancies.getVacanciesByVendorId()

@app.route('/getAppliedPeople', methods=['POST'])
def getAppliedPeople():
    return jobvancies.getAppliedPeople()

@app.route('/updateVacancies', methods=['POST'])
def updateVacancies():
    return jobvancies.updateVacancies()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(debug=True, host="192.168.1.185", use_reloader=True)


