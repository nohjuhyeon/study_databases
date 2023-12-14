from pymongo import MongoClient
def connect(mongo_server_link,database_name,collection_name):                # collection에 연결하는 함수 작성
    mongoClient = MongoClient(mongo_server_link)                             # mongo DB 서버에 연결
    database = mongoClient[database_name]                                    # 데이터 베이스에 연결
    collection = database[collection_name]                                   # collection에 연결
    return collection

def insert(collection,dict_quiz):                                      # 리스트를 추가하는 함수 작성
    collection.insert_one(dict_quiz)                                   
    return

def insert_list(collection,list_items):                                                    #리스트의 dict들을 모두 추가하는 함수 작성
    for i in range(len(list_items)):                                            # 리스트의 dict들이 모두 추가될 때까지 반복
        dict_quiz = list_items[i]                                              
        insert(collection,dict_quiz)                                           # 리스트의 dict 추가

def question_print():
    for i in range(len(list_question)):
        print(list_question[i])
        for j in range(len(list_choices[i])):
            print("{}. {} ".format(j+1,list_choices[i][j]))
        A = input("답을 입력하세요.:")

quiz_list = [                                                                  #추가할 리스트 작성
    {
        "question": "Python의 생성자 함수 이름은 무엇인가요?",
        "choices": ["__init__", "__main__", "__str__", "__del__"],
        "answer": "__init__",
        "score": 20
    },
    {
        "question": "Python에서 'Hello, World!'를 출력하는 코드는 무엇인가요?",
        "choices": ["print('Hello, World!')", "console.log('Hello, World!')", "printf('Hello, World!')", "echo 'Hello, World!'"],
        "answer": "print('Hello, World!')",
        "score": 20
    },
    {
        "question": "Python의 주석을 나타내는 기호는 무엇인가요?",
        "choices": ["//", "/* */", "#", "--"],
        "answer": "#",
        "score": 20
    },
    {
        "question": "Python에서 리스트의 길이를 반환하는 함수는 무엇인가요?",
        "choices": ["size()", "length()", "len()", "sizeof()"],
        "answer": "len()",
        "score": 20
    },
    {
        "question": "Python에서 문자열을 숫자로 변환하는 함수는 무엇인가요?",
        "choices": ["str()", "int()", "char()", "float()"],
        "answer": "int()",
        "score": 20
    }
]


mongo_server_link = "mongodb://localhost:27017"                                 # mongoDB 서버 입력
database_name ="local"                                                          # 데이터 베이스 이름 입력
collection_name = 'solvingProblem'                                                 # collection 이름 입력

collection = connect(mongo_server_link,database_name,collection_name)                        # 추가하고자 하는 collection에 연결
# insert_list(collection,quiz_list)

question = collection.find({},{"_id":0,"question":1,})
choices = collection.find({},{"_id":0,"choices":1 })
answer = collection.find({},{"_id":0,"answer":1 })
score = collection.find({},{"_id":0,"score":1 })
list_question = []
list_choices = []
list_answer = []
list_score = []
for i in question:
    list_question.append(i["question"])
for i in choices:
    list_choices.append(i["choices"])
for i in answer:
    list_answer.append(i["answer"])
for i in score:
    list_score.append(i["score"])    

question_print()