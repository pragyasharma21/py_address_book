import sqlite3
import geopy
import geopy.distance


def getAddressInternal():
    '''
    Retrieve all the address from database
    :return: {s=error/success, message, data}
    '''
    try:
        db = sqlite3.connect("addressData.db")
        cursor = db.cursor()
        queryRes = cursor.execute('''SELECT * FROM ADDRESS_DATA;''')
        queryRes = queryRes.fetchall()
        db.close()
        return {"s": "success", "message": "", "data": queryRes}
    except Exception as e:
        return {"s": "error", "message": "db connection error."}


def addAddressInternal(addressDet):
    '''
    Adding the new address to database
    :param addressDet: body -> {name, addressCoordinateX, addressCoordinateY}
    :return: {s=error/success, message}
    '''
    try:
        db = sqlite3.connect("addressData.db")
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS ADDRESS_DATA (ADDRESS_ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, ADDRESS_COORDINATE_X FLOAT NOT NULL, ADDRESS_COORDINATE_Y FLOAT NOT NULL);''')
        cursor.execute('''INSERT INTO ADDRESS_DATA (NAME, ADDRESS_COORDINATE_X, ADDRESS_COORDINATE_Y) VALUES ('%s', %f, %f);''' % (addressDet.name, addressDet.addressCoordinateX, addressDet.addressCoordinateY))
        db.commit()
        db.close()
        return {"s": "success", "message": "Address is added to db."}
    except Exception as e:
        return {"s": "error", "message": "db connection error."}


def modifyAddressInternal(addressDet):
    '''
    Modify=ing the existing address
    :param addressDet: {id, addressCoordinateX, addressCoordinateY}
    :return: {s=error/success, message}
    '''
    try:
        db = sqlite3.connect("addressData.db")
        cursor = db.cursor()
        cursor.execute('''UPDATE ADDRESS_DATA SET ADDRESS_COORDINATE_X = %f, ADDRESS_COORDINATE_Y = %f WHERE ADDRESS_ID = %d;''' % (addressDet.addressCoordinateX, addressDet.addressCoordinateY, addressDet.id))
        db.commit()
        db.close()
        return {"s": "success", "message": "Address is modified."}
    except Exception as e:
        return {"s": "error", "message": "db connection error."}


def deleteAddressInternal(addressDet):
    '''
    Deleting address
    :param addressDet: {id}
    :return: {s=error/success, message}
    '''
    try:
        db = sqlite3.connect("addressData.db")
        cursor = db.cursor()
        cursor.execute('''DELETE FROM ADDRESS_DATA WHERE ADDRESS_ID = %d;''' % (addressDet.id))
        db.commit()
        db.close()
        return {"s": "success", "message": "Address is added to db."}
    except Exception as e:
        return {"s": "error", "message": "db connection error."}


def searchAddressInternal(addressDet):
    '''
    Searching the addresses that fall within the given radius of coordinates
    :param addressDet: {addressCoordinateX, addressCoordinateY, distance}
    :return: {s=error/success, message, data}
    '''
    try:
        db = sqlite3.connect("addressData.db")
        cursor = db.cursor()
        pt1 = geopy.Point(addressDet.addressCoordinateX, addressDet.addressCoordinateY)
        queryRes = cursor.execute('''SELECT * FROM ADDRESS_DATA;''')
        queryRes = queryRes.fetchall()
        searchRes = []
        for i in queryRes:
            # idDist = i[0]
            # name = i[1]
            cordX = i[2]
            cordY = i[3]
            pt2 = geopy.Point(cordX, cordY)
            dist = geopy.distance.distance(pt1, pt2).km
            print("distance ", dist)
            if dist <= addressDet.distance:
                searchRes.append(i)
        return {"s": "success", "message":"", "data": searchRes}
    except Exception as e:
        return {"s": "error", "message": "db connection error."}


