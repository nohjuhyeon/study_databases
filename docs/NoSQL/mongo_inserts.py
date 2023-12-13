from pymongo import MongoClient
# mongodb에 접속 -> 자원에 대한 class 
mongoClient = MongoClient("mongodb://localhost:27017")

# database 연결
database = mongoClient["local"]

# collection 작업
collection = database['fruits']

# insert 작업 
collection.insert_one({"name": "키위", 
                        "color": "갈색", 
                        "origin":"뉴질랜드"})

pass