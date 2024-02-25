import json
from fastapi import APIRouter
from fastapi import Form, File, UploadFile, Response
import random
from typing import Optional
import datetime
# Import something related to the Databases
import getpass
import subprocess
import os
# from PIL import Image
import hashlib
from fastapi.responses import FileResponse
import pymongo
import boto3
import requests
import mimetypes
from botocore.client import Config
import bson
import configparser


config = configparser.ConfigParser()
config.read('config.ini')




router = APIRouter()



URI = config.get('mongodb', 'uri')
CLIENT = pymongo.MongoClient(URI, authsource='admin')
db = CLIENT[config.get('mongodb', 'db')]

# FOR S3 CLIENT
#Creating Session With Boto3.
session = boto3.Session(
    aws_access_key_id=config.get('aws', 'aws_access_key_id'),
    aws_secret_access_key=config.get('aws', 'aws_secret_access_key'),
)
me_s3 = session.client(
    's3',
    aws_access_key_id=config.get('aws', 'aws_access_key_id'),
    aws_secret_access_key=config.get('aws', 'aws_secret_access_key'),
    region_name=config.get('aws', 'aws_region_name'),
    config=Config(signature_version='s3v4')
)
#Creating S3 Resource From the Session.
MYS3_CLIENT = session.resource('s3')

MYS3_CLIENT2 = session.client('s3')



@router.get("/")
def index():
    return {"msg": f"Backend Running Successfully..."}


@router.post("/register")
def register(email: str=Form(...), pwd: str=Form(...), name: str=Form(...), role: str=Form(...), sq: str=Form(...), sqa: str=Form(...)):
    collection = db[config.get('mongodb', 'user_collection')]

    chk_data = collection.find_one({"_id": email})
    if chk_data is None:
        pass
    else:
        return {"msg": "EmailExist"}

    data = collection.find()
    data = {
        "_id": email,
        "name": name, 
        "email": email, 
        "pwd": hashlib.md5(pwd.encode()).hexdigest(),
        "role": role,
        "sq": str(sq).lower(),
        "sqa": str(sqa).lower(),
        "status": "Activate",

    }        
    result = collection.insert_one(data)
    if result.acknowledged == True:
        return {"msg": "done"}
    else:
        return {"msg": "error"}



@router.post("/org_register")
def org_register(tmSize: str=Form(...), industry: str=Form(...), email: str=Form(...), pwd: str=Form(...), name: str=Form(...), role: str=Form(...), sq: str=Form(...), sqa: str=Form(...)):
    # client = pymongo.MongoClient("mongodb://localhost:27017/")

    
    collection = db[config.get('mongodb', 'org_collection')] 
    chk_data = collection.find_one({"email": email})
    if chk_data:
        return {"msg": "error", "err_msg":"Email already exist with an another organization..."}
    data = {
        "name": name, 
        "email": email, 
        "pwd": hashlib.md5(pwd.encode()).hexdigest(),
        "role": role,
        "sq": str(sq).lower(),
        "sqa": str(sqa).lower(),
        "tmSize": tmSize,
        "industry": industry,
    }     
    # print(data)
    # return {"msg": "done"}
    result = collection.insert_one(data)
    if result.acknowledged == True:
        return {"msg": "done"}
    else:
        return {"msg": "error", "err_msg": "Something went wrong, try again!!!"}


@router.post("/emp_register")
def emp_register(emp_email: str=Form(...), email: str=Form(...), pwd: str=Form(...), name: str=Form(...), role: str=Form(...), sq: str=Form(...), sqa: str=Form(...)):
    # client = pymongo.MongoClient("mongodb://localhost:27017/")
    
    if email == "not applicable":
        emp = emp_email.index("@")
        empDomain = emp_email[emp+1:]

        collection_getOrgMail = db[config.get('mongodb', 'org_collection')]
        dbData_getOrgMail = collection_getOrgMail.find({})
        myData_getOrgMail = [i['email'] for i in dbData_getOrgMail]

        
        for i in myData_getOrgMail:
            org = i.index("@")
            orgDomain = i[org+1:]

            if empDomain == orgDomain:
                orgaMail = i
                break
        else:
            orgDomain = "not found"

        if orgDomain != "not found":
            email = orgaMail
        else:
            return {"msg": "error", "err_msg": "Invalid employee Email, Organization doesn't exist."}

    
    org_collection = db[config.get('mongodb', 'org_collection')]
    chk_data = org_collection.find_one({"email": email})
    
    if chk_data:
        pass
    else:
        return {"msg": "error", "err_msg": "Invalid Organization Email, doesn't exist."}

    collection = db[config.get('mongodb', 'emp_collection')]
    chk_data = collection.find_one({"email": email})
    if chk_data:
        return {"msg": "error", "err_msg": "Your email address already exist, use different."}

    data = {
        "name": name, 
        "org_email": email, 
        "emp_email": emp_email, 
        "pwd": hashlib.md5(pwd.encode()).hexdigest(),
        "role": role,
        "sq": str(sq).lower(),
        "sqa": str(sqa).lower()
    }          
    result = collection.insert_one(data)
    if result.acknowledged == True:
        return {"msg": "done"}
    else:
        return {"msg": "error", "err_msg":"Something went wrong, try again !!!."}


@router.post("/makePayment")
def makePayment(sId: str=Form(...), uid: str=Form(...), price: str=Form(...), number: str=Form(...)):
    url = "https://api.cashfree.com/api/v2/cftoken/order"
    headers = {
        "Accept": "application/json",
        "x-api-version": "2022-01-01",
        "Content-Type": "application/json",
        "x-client-id": db[config.get('cashfree', 'x-client-id')],
        "x-client-secret": db[config.get('cashfree', 'x-client-secret')],
    }
    orderId = str(random.randint(10000, 99999))
    body = {
        "orderId": orderId,
        "orderAmount": price,
        "orderCurrency": "INR"
    }

    response = requests.post(url=url, data=json.dumps(body), headers=headers)
    responseData = json.loads(response.text)
    if responseData['status'] == "OK":
        cftokenRes = responseData['cftoken'] 
        ptLink = genPaymentLink(cftokenRes, orderId, price, uid, number)
        return {"msg": "done", "link": ptLink}
    else:
        return {"msg": "nope"}


def genPaymentLink(cftokenRes, orderId, price, uid, number):
    
    adminCollection = db[config.get('mongodb', 'user_collection')]
    db_data = adminCollection.find_one({"_id": uid})
    cus_id="".join(c for c in str(uid) if c.isalpha())
    cus_id = str(cus_id).replace(" ", "")   

    url = "https://api.cashfree.com/pg/orders"

    payload = {
        "appId": db[config.get('cashfree', 'x-client-id')],
        "secretKey": db[config.get('cashfree', 'x-client-secret')],
        "customer_details": {
            "customer_name": db_data['name'],
            "customer_id": cus_id,
            "customer_email": uid,
            "customer_phone": number
        },
        "order_id": orderId,
        "order_token": cftokenRes,
        "order_amount": price,
        "order_currency": "INR",
        "order_meta": {
            "return_url": "https://www.taskstore.in/AfterPayment?order_id={order_id}&order_token={order_token}"
        }
    }
    headers = {
        "Accept": "application/json",
        "x-client-id": db[config.get('cashfree', 'x-client-id')],
        "x-client-secret": db[config.get('cashfree', 'x-client-secret')],
        "x-api-version": "2022-01-01",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    responseData = json.loads(response.text)
    print(responseData)
    return responseData['payment_link']



@router.post("/checkPayment")
def checkPayment(oId: str=Form(...), oTok: str=Form(...), uid: str=Form(...), paySid: str=Form(...)):
    url = "https://api.cashfree.com/api/v2/cftoken/order"
    headers = {
        "Accept": "application/json",
        "x-api-version": "2022-01-01",
        "Content-Type": "application/json",
        "x-client-id": db[config.get('cashfree', 'x-client-id')],
        "x-client-secret": db[config.get('cashfree', 'x-client-secret')],
    }
    url = f"https://api.cashfree.com/pg/orders/{oId}"

    response = requests.get(url, headers=headers)
    responseData = json.loads(response.text)
    if responseData['order_status'] == "PAID":
        if oTok == responseData['order_token']:
            res = sendToSetting_paid(paySid, uid)
            if res == "done":
                return {"msg": "done"}
            else:
                return {"msg": "notdone"}
        else:
            return {"msg": "nope"}
    else:
        return {"msg": "nope"}



@router.post("/create_org")
def create_org(org_name: str=Form(...), tmSize: str=Form(...), industry: str=Form(...), manager_email: str=Form(...)):
    adminCollection = db['AdminUser']
    db_data = adminCollection.find()
    all_dict = []
    for i in db_data:
        all_dict.append(dict(i))
    last_id = len(all_dict)
    
    
    collection = db['Organizations']
    db_data = collection.find()
    all_dict = []
    for i in db_data:
        all_dict.append(dict(i))
    _id = len(all_dict)+1
    
    
    data = {"_id":_id,"admin_id":last_id, "org_name":org_name, "tmSize":tmSize, "industry":industry, "manager_email":manager_email}
    collection.insert_one(data)

    
    return {"msg": True}




@router.post("/login")
def login(email: str=Form(...), pwd: str=Form(...), role: str=Form(...)):
    if role == "organization":
        collection = db[config.get('mongodb', 'org_collection')]
    elif role == "employee":
        collection = db[config.get('mongodb', 'emp_collection')]
    else:
        collection = db[config.get('mongodb', 'user_collection')]

    data = collection.find_one({"email": email, "pwd": hashlib.md5(pwd.encode()).hexdigest()})

    
    if data != None:
        userId = str(data['_id'])
        userRole = data['role']
        return {"msg": True, "uid": userId, "role": userRole}
    else:
        return {"msg": False}
    
    
    
@router.post("/loginOwner")
def loginOwner(email: str=Form(...), pwd: str=Form(...)):
    collection = db['AdminUser']
    
    data = collection.find_one({"email": email, "pwd": pwd})
    
    if data:
        return {"msg": True}
    else:
        return {"msg": False}
    
    
@router.post("/script_upload")
async def script_upload(price: str=Form(...), youtubelink: str=Form(...), userId: str=Form(...), authorName: str=Form(...), scriptFile: UploadFile=File(...), scriptIcon: UploadFile=File(...), scriptName: str=Form(...), scriptDesc: str=Form(...), upldDep: UploadFile=File(...), cat: str=Form(...), lang: str=Form(...), os: str=Form(...)):
    # SAVE TO DATABASE
    collection = db[config.get('mongodb', 'script_collection')]
    db_data = collection.find()
    all_dict = []
    for i in db_data:
        all_dict.append(dict(i))
    _id = len(all_dict)+1
    
    ScriptFileName1 = str(_id)+"_"+str(scriptFile.filename)
    ScriptDependency1 = str(_id)+"_"+str(upldDep.filename)
    scriptIcon1 = str(_id)+"_"+str(scriptIcon.filename)

    strDate = str(datetime.datetime.today().date()).split("-")
    strDate.reverse()
    strDate = "/".join(strDate)

    # Make the youtube link
    # https://www.youtube.com/embed/-HC2Rooa7Gg?autoplay=1&mute=1
    # https://www.youtube.com/embed/-poXZLDQaOg
    # https://www.youtube.com/watch?v=5rUE4gAfCpI
    # https://www.youtube.com/watch?v=-HC2Rooa7Gg
    newYoutubeLink = str(youtubelink).replace("watch", "embed")
    newYoutubeLink = str(newYoutubeLink).replace("?v=", "/")
    newYoutubeLink = newYoutubeLink + "?autoplay=1&mute=1"
    youtubelink = newYoutubeLink
    # End the youtube link
    
    data = {
        "_id":_id,
        "ScriptName":scriptName, 
        "ScriptFileName":ScriptFileName1, 
        "Description":scriptDesc, 
        "Dependency":ScriptDependency1,
        "ScriptIcon":scriptIcon1,
        "AuthorName": authorName,
        "cat": cat,
        "lang": lang,
        "os": os,
        "userId": userId,
        "status": "Deactivate",
        "installed": 0,
        "youtubelink": youtubelink, 
        "price": price,
        "date": strDate,
        "updated": 0
    }


    collection.insert_one(data) 

    
    # SCRIPT UPLOAD
    content_type = mimetypes.guess_type(ScriptFileName1)
    content_type = str(content_type).lstrip('(')
    content_type = str(content_type).rstrip(', None)')
    scriptfile = await scriptFile.read()
    signed_url = me_s3.generate_presigned_url(
        ClientMethod ='put_object',
        Params = {
            'Bucket': "scriptstore-fastapi",
            'Key':f'All_Script/ScriptID_{_id}/Script/{ScriptFileName1}',
        },
        ExpiresIn=36000
    )
    response = requests.put(signed_url, data=scriptfile)

    # DEPENDENCY UPLOAD
    scriptfile = await upldDep.read()
    signed_url = me_s3.generate_presigned_url(
        ClientMethod ='put_object',
        Params = {
            'Bucket': "scriptstore-fastapi",
            'Key':f'All_Script/ScriptID_{_id}/Dependency/{ScriptDependency1}',
        },
        ExpiresIn=36000
    )
    response = requests.put(signed_url, data=scriptfile)
    content_type = "text/plain"

    # UPLOAD SCRIPT ICON
    content_type = mimetypes.guess_type(scriptIcon1)
    content_type = str(content_type).lstrip('(')
    content_type = str(content_type).rstrip(', None)')
    scriptfile = await scriptIcon.read()
    signed_url = me_s3.generate_presigned_url(
        ClientMethod ='put_object',
        Params = {
            'Bucket': "scriptstore-fastapi",
            'Key':f'All_Script/ScriptID_{_id}/ScriptIcon/{scriptIcon1}',
        },
        ExpiresIn=36000
    )
    
    response = requests.put(signed_url, data=scriptfile)


    return {"msg":True}



@router.post("/get_script")
def get_script(ScriptId: str=Form(...)):
    allScripts = os.listdir("./All_Script/Script")
    myScript = ""
    for i in allScripts:
        if str(i).startswith(str(ScriptId)+"_"):
            myScript = i
            break
    else:
        myScript = "Script Not Found"

    return {"msg": f"http://127.0.0.1:8000/All_Script/Script/{myScript}"}


@router.get("/All_Script/{scriptID}/ScriptIcon/{scriptIconName}")
def get_image(scriptID, scriptIconName):
    myfile = f"./app/api/api_v1/endpoints/All_Script/{scriptID}/ScriptIcon/{scriptIconName}"
    return FileResponse(myfile)

@router.post("/scriptList")
def scriptList(os: str=Form(...), uid: str=Form(...)):
    # DATABASE
    collection = db[config.get('mongodb', 'script_collection')]
    db_data = collection.find()
    data = []
    _idCount = 1
    for i in db_data:
        temp = {}
        if i['status'] == "Activate" and (i['os'] == os):
            for k, v in i.items():
                if k == "_id":
                    _idCount = v
                    InstalledCollection = db[config.get('mongodb', 'installed_collection')]
                    InstalledCollection_db_data = InstalledCollection.find_one({"uid": uid})
                    if InstalledCollection_db_data == None:
                        temp["exist"] = "NotExist"
                    elif str(v) in InstalledCollection_db_data['sId']:
                        temp["exist"] = "Exist"
                    else:
                        temp["exist"] = "NotExist"
                if str(k) == "ScriptIcon":
                    s3key = f'All_Script/ScriptID_{_idCount}/ScriptIcon/{v}'
                    s3img = MYS3_CLIENT.Object("scriptstore-fastapi", s3key)
                    res = f'https://scriptstore-fastapi.s3.ap-south-1.amazonaws.com/All_Script/ScriptID_{_idCount}/ScriptIcon/{v}'
                    temp[k] = res
                else:
                    temp[k] = v
            data.append(temp)
    return {"msg": data}


@router.post("/scriptListWithAll")
def scriptListWithAll(os: str=Form(...), uid: str=Form(...)):
    # DATABASE
    collection = db[config.get('mongodb', 'script_collection')]
    db_data = collection.find()
    data = []
    _idCount = 1
    for i in db_data:
        temp = {}
        if i['status'] == "Activate" and (i['os'] == os or i['os'] == "All"):
            for k, v in i.items():
                if k == "_id":
                    _idCount = v
                    InstalledCollection = db[config.get('mongodb', 'installed_collection')]
                    InstalledCollection_db_data = InstalledCollection.find_one({"uid": uid})
                    if InstalledCollection_db_data == None:
                        temp["exist"] = "NotExist"
                    elif str(v) in InstalledCollection_db_data['sId']:
                        temp["exist"] = "Exist"
                    else:
                        temp["exist"] = "NotExist"
                if str(k) == "ScriptIcon":
                    s3key = f'All_Script/ScriptID_{_idCount}/ScriptIcon/{v}'
                    s3img = MYS3_CLIENT.Object("scriptstore-fastapi", s3key)
                    res = f'https://scriptstore-fastapi.s3.ap-south-1.amazonaws.com/All_Script/ScriptID_{_idCount}/ScriptIcon/{v}'
                    temp[k] = res
                else:
                    temp[k] = v
            data.append(temp)
    return {"msg": data}



@router.get("/reqScript")
def reqScript():
    # DATABASE
    
    collection = db[config.get('mongodb', 'script_collection')]
    db_data = collection.find()
    data = []
    _idCount = 1
    for i in db_data:
        temp = {}
        for k, v in i.items():
            if k == "_id":
                _idCount = v
            if str(k) == "ScriptIcon":
                s3key = f'All_Script/ScriptID_{_idCount}/ScriptIcon/{v}'
                s3img = MYS3_CLIENT.Object("scriptstore-fastapi", s3key)
                res = f'https://scriptstore-fastapi.s3.ap-south-1.amazonaws.com/All_Script/ScriptID_{_idCount}/ScriptIcon/{v}'
                temp[k] = res
            else:
                if k == "status":
                    if v == "Activate":
                        v = "Deactivate"
                    else:
                        v = "Activate"
                temp[k] = v
        data.append(temp)
    return {"msg": data}

@router.get("/reqScriptDetail/{id}")
def reqScriptDetail(id):
    # DATABASE
    
    collection = db[config.get('mongodb', 'script_collection')]
    db_data = collection.find_one({"_id": int(id)})
    scriptDbData = db_data
    data = []
    temp = {}

    # GET SCRIPT DETAILS
    temp['_id'] = db_data['_id']
    temp['ScriptName'] = db_data['ScriptName']
    temp['ScriptFileName'] =f"https://scriptstore-fastapi.s3.ap-south-1.amazonaws.com/All_Script/ScriptID_{id}/Script/"+str(db_data['ScriptFileName'])
    temp['Description'] = db_data['Description']
    temp['Dependency'] = db_data['Dependency']
    temp['ScriptIcon'] = f"https://scriptstore-fastapi.s3.ap-south-1.amazonaws.com/All_Script/ScriptID_{id}/ScriptIcon/"+str(db_data['ScriptIcon'])
    temp['AuthorName'] = db_data['AuthorName']
    temp['cat'] = db_data['cat']
    temp['lang'] = db_data['lang']
    temp['status'] = db_data['status']
    temp['price'] = db_data['price']
    temp['date'] = db_data['date']
    temp['video'] = db_data['youtubelink']

    # GET DEVELOPER DETAILS
    userId = db_data['userId']
    collection = db[config.get('mongodb', 'user_collection')]
    db_data = collection.find_one({"_id": userId})
    temp['dev_email'] = db_data['email']

    # APPEND THE TEMP 
    data.append(temp)
    return {"msg": data, "alldata": scriptDbData}

@router.post("/sendToSetting")
def sendToSetting(sId: str=Form(...), uid: str=Form(...)):
    sId2 = [sId]
    
    InstalledCollection = db[config.get('mongodb', 'installed_collection')]
    db_data = InstalledCollection.find_one({"uid": uid})
    if db_data == None:
        db_data = InstalledCollection.find()
        all_dict = []
        for i in db_data:
            all_dict.append(dict(i))
        _id = len(all_dict)+1
        data = {
            "_id":_id,
            "sId":list(sId2), 
            "uid":uid
        }
        result = InstalledCollection.insert_one(data)

        # UPDATE INSTALLATION NUMBER
        InstalledCollection = db[config.get('mongodb', 'script_collection')]
        db_data = InstalledCollection.find_one({"_id": int(sId)})
        installation_number = int(db_data['installed'])+1
        data = { "$set": {"installed": installation_number}}
        filter = {"_id": int(sId)}
        result = InstalledCollection.update_one(filter, data)

        if result.acknowledged == True:
            return {"msg": "done"}
        else:
            return {"msg": "error"}
    else:
        if sId in db_data['sId']:
            return{"msg":"exist"}

        dbSid = db_data['sId']
        newSid = list(dbSid)+list(sId2)
        data = { "$set": {"sId": newSid}}
        filter = {"uid": uid}
        result = InstalledCollection.update_one(filter, data)

        # UPDATE INSTALLATION NUMBER
        InstalledCollection = db[config.get('mongodb', 'script_collection')]
        db_data = InstalledCollection.find_one({"_id": int(sId)})
        installation_number = int(db_data['installed'])+1
        data = { "$set": {"installed": installation_number}}
        filter = {"_id": int(sId)}
        result = InstalledCollection.update_one(filter, data)
        if result.acknowledged == True:
            return {"msg": "done"}
        else:
            return {"msg": "error"}


def sendToSetting_paid(sId, uid):
    sId2 = [sId]
    
    InstalledCollection = db[config.get('mongodb', 'installed_collection')]
    db_data = InstalledCollection.find_one({"uid": uid})
    if db_data == None:
        db_data = InstalledCollection.find()
        all_dict = []
        for i in db_data:
            all_dict.append(dict(i))
        _id = len(all_dict)+1
        data = {
            "_id":_id,
            "sId":list(sId2), 
            "uid":uid
        }
        result = InstalledCollection.insert_one(data)

        # UPDATE INSTALLATION NUMBER
        InstalledCollection = db[config.get('mongodb', 'script_collection')]
        db_data = InstalledCollection.find_one({"_id": int(sId)})
        installation_number = int(db_data['installed'])+1
        data = { "$set": {"installed": installation_number}}
        filter = {"_id": int(sId)}
        result = InstalledCollection.update_one(filter, data)

        if result.acknowledged == True:
            return "done"
        else:
            return "nope"
    else:
        if sId in db_data['sId']:
            return{"msg":"exist"}

        dbSid = db_data['sId']
        newSid = list(dbSid)+list(sId2)
        data = { "$set": {"sId": newSid}}
        filter = {"uid": uid}
        result = InstalledCollection.update_one(filter, data)

        # UPDATE INSTALLATION NUMBER
        InstalledCollection = db[config.get('mongodb', 'script_collection')]
        db_data = InstalledCollection.find_one({"_id": int(sId)})
        installation_number = int(db_data['installed'])+1
        data = { "$set": {"installed": installation_number}}
        filter = {"_id": int(sId)}
        result = InstalledCollection.update_one(filter, data)
        if result.acknowledged == True:
            return "done"
        else:
            return "nope"



@router.post("/checkinstalled")
def checkinstalled(sId: str=Form(...), uid: str=Form(...)):
    sId2 = [sId]
    
    InstalledCollection = db[config.get('mongodb', 'installed_collection')]
    db_data = InstalledCollection.find_one({"uid": uid})
    if db_data == None:
        print(sId, "Not exist", db_data['sId'])
        return {"msg": "done"}
    elif sId in db_data['sId']:
        print(sId, "exist", db_data['sId'])
        return{"msg":"exist"}
    else:
        print(sId, "Not exist", db_data['sId'])
        return{"msg":"done"}


@router.post("/testUserInstall")
def testUserInstall(uid: str=Form(...)):

    scriptCollection = db[config.get('mongodb', 'script_collection')]
    db_data = scriptCollection.find({"status":"Activate"})

    all_id = []
    for i in db_data:
        all_id.append(str(i['_id']))

    InstalledCollection = db[config.get('mongodb', 'installed_collection')]
    db_data = InstalledCollection.find_one({"uid": uid})
    if db_data == None:
        db_data = InstalledCollection.find()
        all_dict = []
        for i in db_data:
            all_dict.append(dict(i))
        _id = len(all_dict)+1
        data = {
            "_id":_id,
            "sId":all_id, 
            "uid":uid
        }
        result = InstalledCollection.insert_one(data)
    else:
        InstalledCollection = db[config.get('mongodb', 'installed_collection')]
        data = {"$set": {"sId":all_id}}
        filter = {"uid": uid}
        result = InstalledCollection.update_one(filter, data)

    if result.acknowledged == True:
        return {"msg": "done"}
    else:
        return {"msg": "error"}


@router.post("/changeStatus")
def changeStatus(sId: str=Form(...)):
    
    
    InstalledCollection = db[config.get('mongodb', 'script_collection')]
    db_data = InstalledCollection.find_one({"_id": int(sId)})

    cur_status = db_data['status']

    if cur_status == "Activate":
        new_status = "Deactivate"
    else:
        new_status = "Activate"
   
    data = { "$set": {"status": new_status}}
    filter = {"_id": int(sId)}
    result = InstalledCollection.update_one(filter, data)

    if result.acknowledged == True:
        return {"msg": "done"}
    else:
        return {"msg": "error"}



@router.post("/getScirptForSetting")
def getScirptForSetting(uid: str=Form(...)):
    
    
    
    collection = db[config.get('mongodb', 'installed_collection')]
    
    data = collection.find_one({"uid": uid})
    if data == None:
        return {"msg": "empty"}
    else:
        sId = data['sId']
        if sId:
            respData = {}
            respCollection = db[config.get('mongodb', 'script_collection')]
            scriptName = []
            authorName = []
            scriptId = []
            for i in sId:
                respDbData = respCollection.find_one({"_id": int(float((i)))})
                
                scriptName.append(respDbData['ScriptName'])
                authorName.append(respDbData['AuthorName'])
                scriptId.append(respDbData['_id'])
            respData['scriptName'] = scriptName
            respData['authorName'] = authorName
            respData['scriptId'] = scriptId
            print(respData)
            return {"msg": True, "data": respData}
        else:
            return {"msg": "empty"}



@router.post("/delScript")
def delScript(sId: str=Form(...), uid: str=Form(...)):
    
    
    
    collection = db[config.get('mongodb', 'installed_collection')]
    data = collection.find_one({"uid": uid})
    allScriptId = data['sId']
    allScriptId.remove(sId)
    data = { "$set": {"sId": allScriptId}}
    filter = {"uid": uid}
    result = collection.update_one(filter, data)

    # Decrease installation number
    collection = db[config.get('mongodb', 'script_collection')]
    data = collection.find_one({"_id": int(sId)})
    updateInstallationNumber = int(data['installed'])-1
    if updateInstallationNumber<=0:
        updateInstallationNumber = 0
    data = { "$set": {"installed": updateInstallationNumber}}
    filter = {"_id": int(sId)}
    result = collection.update_one(filter, data)

    if result.acknowledged == True:
        return {"msg": "done"}
    else:
        return {"msg": "error"}



@router.post("/getScriptDetails")
def getScriptDetails(sId: str=Form(...)):
    
    
    
    collection = db[config.get('mongodb', 'script_collection')]
    
    data = collection.find_one({"_id": int(sId)})
    if data:
        respData = {}
        respData['id'] = data['_id']
        respData['ScriptName'] = data['ScriptName']
        respData['Description'] = data['Description']
        res = f"https://scriptstore-fastapi.s3.ap-south-1.amazonaws.com/All_Script/ScriptID_{data['_id']}/ScriptIcon/{data['ScriptIcon']}"
        respData['ScriptIcon'] = res
        respData['AuthorName'] = data['AuthorName']
        return {"msg": True, "data": respData}
    else:
        return {"msg": False}

@router.post("/scriptDetailsForEdit")
def scriptDetailsForEdit(id: str=Form(...)):
    
    collection = db[config.get('mongodb', 'script_collection')]
    data = collection.find_one({"_id": int(id)})
    return {"msg": True, "data": data}

@router.get("/getScriptIcon/{scriptIcon}/{scriptid}")
def getScriptIcon(scriptIcon, scriptid):
    myfile = "Nothing"
    return FileResponse(myfile)


@router.post("/getSelectedScriptId")
def getSelectedScriptId(uid: str=Form(...)):
    
    
    collection = db[config.get('mongodb', 'installed_collection')]
    data = collection.find_one({"uid": uid})

    if data:
        return {"msg": True, "sId": data['sId']}
    else:
        return {"msg": False}

@router.get("/getSelectedScript/{scrId}")
def getSelectedScript(scrId):
    
    
    collection = db[config.get('mongodb', 'script_collection')]
    data = collection.find_one({"_id": int(scrId)})

    if data:
        return {"msg": True, "name": data['ScriptName'], "id": data['_id']}
    else:
        return {"msg": False}

@router.post("/downRun")
def downRun(sId: str=Form(...)):
    if int(sId) == 0:
        myfile = f"./All_Script/DefaultKeyLog/def_kl.py"
        return FileResponse(myfile)
    else:
        
        
        collection = db[config.get('mongodb', 'script_collection')]
        data = collection.find_one({"_id": int(sId)})
        scrName = data['ScriptFileName']
        if data:
            myfile = f"./All_Script/Script/{scrName}"
            return FileResponse(myfile)
        else:
            return {"msg": False}


@router.post("/storeLog")
async def downRun(uid: str=Form(...), logFile: UploadFile=File(...)):
    checkPath = f"./All_Script/Log/"
    allLogFile = []
    uidLogFile = []
    allLogFile = os.listdir(checkPath)
    for i in allLogFile:
        if str(i).startswith(f"id_{uid}"):
            uidLogFile.append(i)
    count = len(uidLogFile)+1
    completePath = f"./All_Script/Log/id_{uid}_logfile({count}).txt"
    contents = await logFile.read()
    with open(f"{completePath}", "wb") as f:
        f.write(contents) 

    return {"msg": "done"}

@router.post("/fetchLogFile")
async def fetchLogFile(uid: str=Form(...)):
    checkPath = f"./All_Script/Log/"
    allLogFile = []
    uidLogFile = []
    allLogFile = os.listdir(checkPath)
    for i in allLogFile:
        if str(i).startswith(f"id_{uid}"):
            uidLogFile.append(i)
    responseData = []
    for i in uidLogFile:
        responseData.append(f"{i}") 

    if len(uidLogFile) > 0:       
        return {"msg": "done", "data": responseData}
    else:
        return {"msg": "empty"}



@router.get("/downloadLogFile/{logFileName}")
async def downloadLogFile(logFileName):
    myfile = f"./All_Script/Log/{logFileName}"
    return FileResponse(myfile)

@router.post("/downloadLogFile")
async def downloadLogFile(logFileName: str=Form(...)):
    myfile = f"./All_Script/Log/{logFileName}"
    return FileResponse(myfile)


@router.get("/panel/getScriptTest")
async def getScriptTest():
    URL = f"https://scriptstore-fastapi.s3.ap-south-1.amazonaws.com/All_Script/ScriptID_5/Script/5_hello.py"
  
    r = requests.get(url = URL)
    open('./myScriptFile.py', 'wb').write(r.content)


@router.post("/newScriptCat")
def newScriptCat(cat: str=Form(...)):
    
    
    collection = db[config.get('mongodb', 'cat_collection')]
    cursor = collection.find().sort('_id', -1).limit(1)
    for document in cursor:
        _id = int(document['_id'])
    data = {
        "_id":_id+1,
        "cat": cat
    }        
    result = collection.insert_one(data)
    if result.acknowledged == True:
        return {"msg": True}
    else:
        return {"msg": "error"}



@router.post("/newScriptlang")
def newScriptlang(lang: str=Form(...)):
    
    collection = db[config.get('mongodb', 'lang_collection')]
    cursor = collection.find()
    checkExist = []
    for i in cursor:
        checkExist.append(i)
    if len(checkExist)>0:
        cursor = collection.find().sort('_id', -1).limit(1)
        for document in cursor:
            _id = int(document['_id'])
        data = {
            "_id":_id+1,
            "lang": lang
        }        
        result = collection.insert_one(data)
        if result.acknowledged == True:
            return {"msg": True}
        else:
            return {"msg": "error"}
    else:
        data = {
            "_id": 1,
            "lang": lang
        }        
        result = collection.insert_one(data)
        if result.acknowledged == True:
            return {"msg": True}
        else:
            return {"msg": "error"}


@router.get("/getCat")
async def getCat():
    
    collection = db[config.get('mongodb', 'cat_collection')]
    data = collection.find()
    resData = []
    for i in data:
        resData.append(i)
    return {"msg": True, "data": resData}

@router.get("/getLang")
async def getLang():
    
    collection = db[config.get('mongodb', 'lang_collection')]
    data = collection.find()
    resData = []
    for i in data:
        resData.append(i)
    return {"msg": True, "data": resData}


@router.get("/getUser")
async def getUser():
    
    collection = db[config.get('mongodb', 'user_collection')]
    data = collection.find()
    resData = []
    for i in data:
        resData.append(i)
    totalUser = len(resData)
    
    return {"msg": True, "data": list(resData), "totalUser": totalUser}
    # 
    # collection = db[config.get('mongodb', 'user_collection')]
    # collection.update_many({}, {"$set": {"status": "Activate"}}, upsert=False, array_filters=None)
    # return {"msg":"hi"}

@router.post("/filterUser")
async def filterUser(desired: str=Form(...), col: str=Form(...)):
    
    collection = db[config.get('mongodb', 'user_collection')]
    data = collection.find({col: desired})
    resData = []
    for i in data:
        resData.append(i)
    totalUser = len(resData)
    
    return {"msg": True, "data": list(resData), "totalUser": totalUser}


@router.post("/userStatusChange")
async def userStatusChange(uid: str=Form(...), status_to: str=Form(...)):
    
    collection = db[config.get('mongodb', 'user_collection')]
    data = { "$set": {"status": status_to}}
    filter = {"_id": uid}
    collection.update_one(filter, data)
    return {"msg": True}



@router.post("/editUserRole")
async def editUserRole(role: str=Form(...), userId: str=Form(...)):
    
    collection = db[config.get('mongodb', 'user_collection')]
    data = { "$set": {"role": role}}
    filter = {"_id": userId}
    collection.update_one(filter, data)
    return {"msg": True}


@router.post("/userDelete")
async def userDelete(uid: str=Form(...)):
    
    collection = db[config.get('mongodb', 'user_collection')]
    collection.delete_one({'_id': uid})
    return {"msg": True}


    


@router.post("/delCat")
async def delCat(catId: str=Form(...)):
    
    collection = db[config.get('mongodb', 'cat_collection')]
    collection.delete_one({'_id': int(catId)})
    return {"msg": True}

@router.post("/delLang")
async def delLang(langId: str=Form(...)):
    
    collection = db[config.get('mongodb', 'lang_collection')]
    collection.delete_one({'_id': int(langId)})
    return {"msg": True}

@router.post("/editCat")
async def editCat(ecatId: str=Form(...), ecat: str=Form(...)):
    
    collection = db[config.get('mongodb', 'cat_collection')]
    data = { "$set": {"cat": ecat}}
    filter = {"_id": int(ecatId)}
    collection.update_one(filter, data)
    return {"msg": True}

@router.post("/editLang")
async def editLang(elangId: str=Form(...), elang: str=Form(...)):
    
    collection = db[config.get('mongodb', 'lang_collection')]
    data = { "$set": {"lang": elang}}
    filter = {"_id": int(elangId)}
    collection.update_one(filter, data)
    return {"msg": True}

@router.get("/getScriptCatList")
def getScriptCatList():
    
    
    # GET CATEGORY LIST
    collection = db[config.get('mongodb', 'cat_collection')]
    data = collection.find()
    res_data = []
    for i in data:
        res_data.append(i['cat'])

    # GET SCRIPT LANGUAGE LIST
    collection = db[config.get('mongodb', 'lang_collection')]
    l_data = collection.find()
    l_res_data = []
    for i in l_data:
        l_res_data.append(i['lang'])
    return{"msg": True, "data": res_data, "l_data": l_res_data}


@router.get("/getUserName/{userid}/{role}")
def getUserName(userid, role):

    if str(userid) == "null":
        return {"msg": "Guest"}
    else:
        

        if role == "organization":
            collection = db[config.get('mongodb', 'org_collection')]
    
            data = collection.find_one({"_id": bson.ObjectId(userid)})
            print("Userid:",userid)
            print("Data:",data)

        elif role == "employee":
            collection = db[config.get('mongodb', 'emp_collection')]
            data = collection.find_one({"_id": bson.ObjectId(userid)})
        else:
            collection = db[config.get('mongodb', 'user_collection')]
            data = collection.find_one({"_id": userid})

        name = data['name']
        return {"msg": name}


@router.post("/checkCurPwd")
def checkCurPwd(currpwd: str=Form(...), uid: str=Form(...)):
    
    collection = db[config.get('mongodb', 'user_collection')]
    data = collection.find_one({"_id": uid})
    pwd = data['pwd']
    if(hashlib.md5(currpwd.encode()).hexdigest() == pwd):
        return {"msg": True, "data": {"email": data['email'], "pwd": currpwd}}    
    else:
        return {"msg": False}
    


@router.post("/resetPass")
def resetPass(pwd: str=Form(...), uid: str=Form(...), email: str=Form(...)):
    
    
    collection = db[config.get('mongodb', 'user_collection')]
    # data = collection.find_one({"_id": uid})
    data = { "$set": {"pwd": hashlib.md5(pwd.encode()).hexdigest(), "email": email}}
    filter = {"_id": uid}
    result = collection.update_one(filter, data)
    return {"msg": True}


@router.post("/getSecQue")
def getSecQue(mail: str=Form(...)):
    
    collection = db[config.get('mongodb', 'user_collection')]
    data = collection.find_one({"email": mail})
    if data is not None:
        sq = data['sq']
        sqa = data['sqa']
        return {"msg": True, "data": {"sq": sq, "sqa": sqa}}
    else:
        return {"msg": False}

@router.post("/forgotPwd")
def forgotPwd(pwd: str=Form(...), mail: str=Form(...)):
    
    
    collection = db[config.get('mongodb', 'user_collection')]
    # data = collection.find_one({"_id": uid})
    data = { "$set": {"pwd": hashlib.md5(pwd.encode()).hexdigest()}}
    filter = {"email": mail}
    result = collection.update_one(filter, data)
    return {"msg": True}

@router.get("/howtoinstall")
def howtoinstall():
    

    collection = db[config.get('mongodb', 'user_collection')]
    usersData = collection.find()
    users = [i for i in usersData]
    users = len(users)

    collection = db[config.get('mongodb', 'script_collection')]
    scriptData = collection.find()
    script = [i for i in scriptData]
    script = len(script)

    collection = db[config.get('mongodb', 'script_collection')]
    myquery = { "installed": 0}
    scriptData = collection.find(myquery)
    installed_script = [i for i in scriptData]
    installed_script = script - len(installed_script)

    data = {}
    data['users'] = users
    data['script'] = script
    data['installed_script'] = installed_script

    return{"msg": True, "data": data}


@router.post("/fav_script")
def fav_script(sId: str=Form(...), like: str=Form(...)):
    
    collection = db[config.get('mongodb', 'script_collection')]
    db_script = collection.find_one({"_id": int(sId)})
    if like == "true":
        try:
            existing_fav = int(db_script['fav'])+1
        except:
            existing_fav = 1
    else:
        try:
            existing_fav = int(db_script['fav'])-1
        except:
            existing_fav = 0
    data = { "$set": {"fav": existing_fav}}
    filter = {"_id": int(sId)}
    result = collection.update_one(filter, data)
    if result.acknowledged == True:
        return {"msg": "done"}
    else:
        return {"msg": "error"}

@router.get("/getAllOrg")
def getAllOrg():
    
    collection = db[config.get('mongodb', 'org_collection')]
    dbData = collection.find({})
    myData = [i['email'] for i in dbData]
    
        
    return {"msg": "done", "data": myData}




@router.post("/edit_script_upload")
async def edit_script_upload(sid: str=Form(...), price: str=Form(...), youtubelink: str=Form(...), userId: str=Form(...), authorName: str=Form(...), 
    scriptFile: Optional[UploadFile]=None, 
    upldDep: Optional[UploadFile]=None,  
    scriptIcon: Optional[UploadFile]=None, 
    scriptName: str=Form(...), scriptDesc: str=Form(...), cat: str=Form(...), lang: str=Form(...), os: str=Form(...)):
    

    
    collection = db[config.get('mongodb', 'script_collection')]

    if not scriptFile:
        db_data = collection.find_one({"_id": int(sid)})
        ScriptFileName1 = db_data['ScriptFileName']
    else:
        ScriptFileName1 = str(sid)+"_"+str(scriptFile.filename)

    if not upldDep:
        db_data = collection.find_one({"_id": int(sid)})
        ScriptDependency1 = db_data['Dependency']
    else:
        ScriptDependency1 = str(sid)+"_"+str(upldDep.filename)

    if not scriptIcon:
        db_data = collection.find_one({"_id": int(sid)})
        scriptIcon1 = db_data['ScriptIcon']
    else:
        scriptIcon1 = str(sid)+"_"+str(scriptIcon.filename)
    

    strDate = str(datetime.datetime.today().date()).split("-")
    strDate.reverse()
    strDate = "/".join(strDate)
    
    data = { "$set": {
        "ScriptName":scriptName, 
        "ScriptFileName":ScriptFileName1, 
        "Description":scriptDesc, 
        "Dependency":ScriptDependency1,
        "ScriptIcon":scriptIcon1,
        "AuthorName": authorName,
        "cat": cat,
        "lang": lang,
        "os": os,
        "userId": userId,
        "status": "Deactivate",
        "installed": 0,
        "youtubelink": youtubelink, 
        "price": price,
        "date": strDate,
        "updated": int(db_data['updated'])+1
        }}
    filter = {"_id": int(sid)}
    result = collection.update_one(filter, data)

    # Update to S3

    if not scriptFile:
        pass
    else:
        scriptfile = await scriptFile.read()
        signed_url = me_s3.generate_presigned_url(
            ClientMethod ='put_object',
            Params = {
                'Bucket': "scriptstore-fastapi",
                'Key':f'All_Script/ScriptID_{sid}/Script/{ScriptFileName1}',
            },
            ExpiresIn=36000
        )
        response = requests.put(signed_url, data=scriptfile)


    if not upldDep:
        pass
    else:
        scriptfile = await upldDep.read()
        signed_url = me_s3.generate_presigned_url(
            ClientMethod ='put_object',
            Params = {
                'Bucket': "scriptstore-fastapi",
                'Key':f'All_Script/ScriptID_{sid}/Dependency/{ScriptDependency1}',
            },
            ExpiresIn=36000
        )
        response = requests.put(signed_url, data=scriptfile)

    if not scriptIcon:
        pass
    else:
        scriptfile = await scriptIcon.read()
        signed_url = me_s3.generate_presigned_url(
            ClientMethod ='put_object',
            Params = {
                'Bucket': "scriptstore-fastapi",
                'Key':f'All_Script/ScriptID_{sid}/ScriptIcon/{scriptIcon1}',
            },
            ExpiresIn=36000
        )
        response = requests.put(signed_url, data=scriptfile)
    return {"msg":True}


@router.post("/feedback_script")
async def feedback_script(feedback_msg: str=Form(...), script_id: str=Form(...), uid: str=Form(...)):
    
    collection = db[config.get('mongodb', 'feedback_collection')]
    data = {
        "feedback_msg": feedback_msg,
        "script_id": script_id,
        "uid": uid,
    }        
    result = collection.insert_one(data)
    
    if result.acknowledged == True:
        return {"msg": True}
    else:
        return {"msg": False}



@router.post("/commentScriptReq")
def commentScriptReq(scTit: str=Form(...), scDesc: str=Form(...), uid: str=Form(...), role: str=Form(...)):
    
        
    
    collection = db[config.get('mongodb', 'req_collection')]
    
    
    data = {
        "title":scTit, 
        "desc":scDesc, 
        "upvote":1, 
        "workingStatus": 10, 
        "userRole":role, 
        "uid": uid,
        "initiateAt":str(datetime.datetime.today()), 
        "upvoteList": [uid]        
        }
    ack = collection.insert_one(data)

    if ack.acknowledged == True:
        return {"msg": True}
    else:
        return {"msg": False}


@router.get("/fetchCommentScriptReq")
def fetchCommentScriptReq():
    
        
    
    collection = db[config.get('mongodb', 'req_collection')]
    
    db_data = collection.find()

    acData = []

    for i in db_data:
        i["_id"] = str(i['_id'])
        acData.append(i)

    return {"msg": True, "data": acData}


@router.post("/updateCommentReqSt")
def updateCommentReqSt(scId: str=Form(...), value: str=Form(...)):
    
        
    collection = db[config.get('mongodb', 'req_collection')]
    # db_data = collection.find_one({"_id": bson.ObjectId(scId)})
    data = { "$set": {"workingStatus": value}}
    filter = {"_id": bson.ObjectId(scId)}
    result = collection.update_one(filter, data)


    # NOW TRY TO GET LATEST DATA(mountedAlter)
    db_data = collection.find()
    acData = []
    for i in db_data:
        i["_id"] = str(i['_id'])
        acData.append(i)

    if result.acknowledged == True:
        return {"msg": True, "data": acData}
    else:
        return {"msg": False}

@router.post("/updateUpvote")
def updateUpvote(scId: str=Form(...), value: str=Form(...), uid: str=Form(...)):
    
        
    collection = db[config.get('mongodb', 'req_collection')]
    # CHECK ALREADY VOTE OR NOT
    db_data = collection.find_one({"_id": bson.ObjectId(scId)})
    if str(uid) in db_data['upvoteList']:
        return {"msg": True, "data": "exist"}


    l = db_data['upvoteList']
    l.append(uid)
    data = { "$set": {
        "upvote": int(value)+1, 
        "upvoteList":l,
    }}
    filter = {"_id": bson.ObjectId(scId)}
    result = collection.update_one(filter, data)
    

    # NOW TRY TO GET LATEST DATA(mountedAlter)
    db_data = collection.find()
    acData = []
    for i in db_data:
        i["_id"] = str(i['_id'])
        acData.append(i)


    if result.acknowledged == True:
        return {"msg": True, "data": acData}
    else:
        return {"msg": False}
    




















@router.get("/sayed")
def sayed():
    return{"msg": "Hello Sayed!!!"}
































@router.get("/runningScript")
def runningScript():
    #  RUN WITH DOWNLOADS

    username = getpass.getuser()
    all_file = os.listdir("/home/"+username+"/Downloads")
    for i in all_file:
        if str(i).endswith(".py"):
            print("""
░██████╗░█████╗░██████╗░██╗██████╗░████████╗  ░██████╗████████╗░█████╗░██████╗░███████╗
██╔════╝██╔══██╗██╔══██╗██║██╔══██╗╚══██╔══╝  ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝
╚█████╗░██║░░╚═╝██████╔╝██║██████╔╝░░░██║░░░  ╚█████╗░░░░██║░░░██║░░██║██████╔╝█████╗░░
░╚═══██╗██║░░██╗██╔══██╗██║██╔═══╝░░░░██║░░░  ░╚═══██╗░░░██║░░░██║░░██║██╔══██╗██╔══╝░░
██████╔╝╚█████╔╝██║░░██║██║██║░░░░░░░░██║░░░  ██████╔╝░░░██║░░░╚█████╔╝██║░░██║███████╗
╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░  ╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝ """)


            print("=========================================================================================================")
            print("=========================================================================================================")
            subprocess.call(["python3", "/home/"+username+"/Downloads/"+str(i)])
            print("=========================================================================================================")
            print("=========================================================================================================")
            print("""
        ░█▀▀▀ ░█▄─░█ ░█▀▀▄ 
        ░█▀▀▀ ░█░█░█ ░█─░█ 
        ░█▄▄▄ ░█──▀█ ░█▄▄▀\n""")
            break

    return {"msg": "Done !"}



@router.get("/runThisScript/")
def runThisScriptWithOutDownload(sId: str='0'):
    
    
    # dbObj = DB_Conn()
    # db = dbObj.Conn()
    collection = db[config.get('mongodb', 'script_collection')]
    db_data = collection.find_one({"_id": int(sId)})
    scriptName = db_data['ScriptFileName']
    myfile = f"./All_Script/Script/{scriptName}"
    print("""
░██████╗░█████╗░██████╗░██╗██████╗░████████╗  ░██████╗████████╗░█████╗░██████╗░███████╗
██╔════╝██╔══██╗██╔══██╗██║██╔══██╗╚══██╔══╝  ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝
╚█████╗░██║░░╚═╝██████╔╝██║██████╔╝░░░██║░░░  ╚█████╗░░░░██║░░░██║░░██║██████╔╝█████╗░░
░╚═══██╗██║░░██╗██╔══██╗██║██╔═══╝░░░░██║░░░  ░╚═══██╗░░░██║░░░██║░░██║██╔══██╗██╔══╝░░
██████╔╝╚█████╔╝██║░░██║██║██║░░░░░░░░██║░░░  ██████╔╝░░░██║░░░╚█████╔╝██║░░██║███████╗
╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░  ╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝ \n""")

    print("=========================================================================================================")
    print("=========================================================================================================")
    subprocess.call(["python3", f"{myfile}"])
    print("=========================================================================================================")
    print("=========================================================================================================")
    print("""
░█▀▀▀ ░█▄─░█ ░█▀▀▄ 
░█▀▀▀ ░█░█░█ ░█─░█ 
░█▄▄▄ ░█──▀█ ░█▄▄▀\n""")

    return {"msg": "Successfully Executed !"}
