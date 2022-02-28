from fastapi import FastAPI
from pydantic import BaseModel
from config.internal_functions import *

app = FastAPI(
    title="Address Book",
    description="Store, update and delete address of user")


class createAddress(BaseModel):
    name: str
    addressCoordinateX: float
    addressCoordinateY: float


class modifyAddress(BaseModel):
    addressCoordinateX: float
    addressCoordinateY: float
    id: int


class deleteAddress(BaseModel):
    id: int


class searchAddress(BaseModel):
    addressCoordinateX: float
    addressCoordinateY: float
    distance: int


@app.get("/", tags=["Welcome"])
def root():
    return {"s": "success", "message": "Welcome to Address Book Application"}


# GET - RETRIEVE ADDRESS
@app.get('/address', tags=["Retrieve Address"])
def getAddress():
    res = getAddressInternal()
    return res


# POST - ADD ADDRESS
@app.post('/address', tags=["Add Address"])
def addAddress(addressDet: createAddress):
    res = addAddressInternal(addressDet)
    return res


# PUT - MODIFY ADDRESS
@app.put('/address', tags=["Modify Address"])
def modifyAddress(addressDet: modifyAddress):
    res = modifyAddressInternal(addressDet)
    return res


# DELETE - DELETE ADDRESS
@app.delete('/address', tags=["Delete Address"])
def deleteAddress(addressDet: deleteAddress):
    res = deleteAddressInternal(addressDet)
    return res


# POST - SEARCH ADDRESS
@app.post('/address/search', tags=["Search Address"])
def searchAddress(addressDet: searchAddress):
    res = searchAddressInternal(addressDet)
    return res
