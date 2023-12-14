from pymongo import MongoClient
def connect():
    mongoClient = MongoClient("mongodb://localhost:27017")
    database = mongoClient["local"]
    collection = database['fruits_info']
    return collection

def insert(collection,dict_fruit):
    collection.insert_one(dict_fruit)
    return

fruit_info = [
    {"name": "사과", "color": "빨강", "taste": "달콤"},
    {"name": "바나나", "color": "노랑", "taste": "달콤"},
    {"name": "포도", "color": "보라", "taste": "달콤한데 약간의 쓴맛이 있음"},
    {"name": "오렌지", "color": "주황", "taste": "달콤하면서 새콤"}
]

for i in range(len(fruit_info)):
    dict_fruit = fruit_info[i]
    collection = connect()
    insert(collection,dict_fruit)

