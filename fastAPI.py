from fastapi import FastAPI, Form, Request, Depends, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import pymongo
from fastapi.responses import JSONResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Định nghĩa tài khoản và mật khẩu
username = "truc"
password = "1234"

myclient=pymongo.MongoClient('mongodb+srv://test:12345@test.ngmfdui.mongodb.net/?retryWrites=true&w=majority')
mydb= myclient["mydatabase"]
mycol=mydb["Master"]
mycol1=mydb["IotGateWay"]
mycol2=mydb["IotNode"]
mycol3=mydb["Button"]

class Master(BaseModel):
    _id: int
    led1_status: int
    led2_status: int
    temp: float
    humi: float
    timestamp: str


class IotGateWay(BaseModel):
    _id: int
    lamp: int
    siren: int
    temp: float
    timestamp: str


class IotNode (BaseModel):
    _id: int
    vibration: int
    relay: int
    Light_Sensor: float
    Distance_Sensor: float 
    timestamp: str 
    

class Button(BaseModel):
    _id: int
    Toggle_Lamp : int
    Toggle_Siren: int
    Toggle_Vibration: int
    Toggle_Relay: int
    Toggle_LED1: int
    Toggle_LED2: int
    timestamp: str 


app.mount("/static", StaticFiles(directory="D:/HOC/HKI_N4/IOT/giao dien/cqq-main/templates"), name="static")
@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("login3.html", {"request": request})

@app.post("/login")
async def login(request: Request, username_form: str = Form(...), password_form: str = Form(...)):
    if username_form == username and password_form == password:
        response = RedirectResponse("/welcome")
        return response
    else:
        return HTTPException(status_code=400, detail="Incorrect username or password")

@app.get("/welcome", response_class=HTMLResponse)
async def welcome(request: Request):
    return templates.TemplateResponse("new.html", {"request": request})
    
@app.get("/interface", response_class=HTMLResponse)

async def interface(request: Request):
    return templates.TemplateResponse("Interface.html", {"request": request})

@app.get("/graph", response_class=HTMLResponse)
async def graph(request: Request):
    return templates.TemplateResponse("graph.html", {"request": request})

@app.get("/get_master_data")
def get_master_data():
    latest_data = mycol.find_one(sort=[("timestamp", pymongo.DESCENDING)])
    if latest_data:
        return {
            "_id": latest_data["_id"],
            "led1_status": latest_data["led1_status"],
            "led2_status": latest_data["led2_status"],
            "temp": latest_data["temp"],
            "humi": latest_data["humi"],
            "timestamp": latest_data["timestamp"]
        }
    return {"message": "Không có dữ liệu Master."}


@app.get("/get_gateway_data")
def get_gateway_data():
    latest_data = mycol1.find_one(sort=[("timestamp", pymongo.DESCENDING)])
    if latest_data:
        return {
            "_id": latest_data["_id"],
            "lamp": latest_data["lamp"],
            "siren": latest_data["siren"],
            "temp": latest_data["temp"],
            "timestamp": latest_data["timestamp"]
        }
    return {"message": "Không có dữ liệu Gateway."}

@app.get("/get_node_data")
def get_node_data():
    latest_data = mycol2.find_one(sort=[("timestamp", pymongo.DESCENDING)])
    if latest_data:
        return {
            "_id": latest_data["_id"],
            "vibration": latest_data["vibration"],
            "relay": latest_data["relay"],
            "Light_Sensor": latest_data["Light_Sensor"],
            "Distance_Sensor": latest_data["Distance_Sensor"],
            "timestamp": latest_data["timestamp"]
        }
    return {"message": "Không có dữ liệu Node."}

@app.get("/get_button_data")
def get_button_data():
    latest_data = mycol3.find_one(sort=[("timestamp", pymongo.DESCENDING)])
    if latest_data:
        return {
            "_id": latest_data["_id"],
            "Toggle_Lamp": latest_data["Toggle_Lamp"],
            "Toggle_Siren": latest_data["Toggle_Siren"],
            "Toggle_Vibration": latest_data["Toggle_Vibration"],
            "Toggle_Relay": latest_data["Toggle_Relay"],
            "Toggle_LED1": latest_data["Toggle_LED1"],
            "Toggle_LED2": latest_data["Toggle_LED2"],
            "timestamp": latest_data["timestamp"]
        }
    return {"message": "Không có dữ liệu Button."}

# API POST để cập nhật dữ liệu cho các class
@app.post("/update_master_data")
async def update_data_post(item: Master):
    Master = {
        "_id" : item._id,
        "led1_status": item.led1_status,
        "led2_status": item.led2_status,
        "temp": item.temp,
        "humi": item.humi,
        "timestamp": item.timestamp,   
    }
    mycol.insert_one(Master)
    return {"message": "Dữ liệu Master đã được cập nhật"}


@app.post("/update_gateway_data")
async def update_data_post(item: IotGateWay):
    GateWay = {
         "_id" : item._id,
        "lamp": item.lamp,
        "siren": item.siren,
        "temp": item.temp,
        "timestamp": item.timestamp
    }
    mycol1.insert_one(GateWay)
    return {"message": "Dữ liệu Gateway đã được cập nhật"}

@app.post("/update_node_data")
async def update_data_post(item: IotNode):
    Node = {
         "_id" : item._id,
        "vibration": item.vibration,
        "relay": item.relay,
        "Light_Sensor": item.Light_Sensor,
        "Distance_Sensor": item.Distance_Sensor,
        "timestamp": item.timestamp
    }
    mycol2.insert_one(Node)
    return {"message": "Dữ liệu Node đã được cập nhật"}

@app.post("/update_button_data")
async def update_data_post(item: Button):
    BT = {
         "_id" : item._id,
        "Toggle_Lamp": item.Toggle_Lamp,
        "Toggle_Siren": item.Toggle_Siren,
        "Toggle_Vibration": item.Toggle_Vibration,
        "Toggle_Relay": item.Toggle_Relay,
        "Toggle_LED1": item.Toggle_LED1,
        "Toggle_LED2": item.Toggle_LED2,
        "timestamp": item.timestamp
    }
    mycol3.insert_one(BT)
    return { "message": "Dữ liệu các Button đã được cập nhật"}
