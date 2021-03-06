# Fastapi address book

Purpose of this project is to make address book application where users can create, modify and delete addresses. Users can search address that falls under N km radius of a given coordinates of latitude and longitude.

Language = Python 3.7.7

Server = localhost:8000

## Clone the repo in your local machine

```
sudo apt-get update
sudo apt-get install git
git clone https://github.com/pragyasharma21/py_address_book.git
```

## How to run

Install the requirements for this projects

```
cd py_address_book
pip3 install -r requirements.txt
```

Run fastapi server

```
cd py_address_book
uvicorn main:app --reload
```

For running the address book apis, open web browser and search for following website

```
http://localhost:8000/docs
```

You can test the apis from this Swagger doc.
