
def connect(mongo_server_link,database_name,collection_name):                                                   # collection에 연결하는 함수 작성
    from pymongo import MongoClient
    mongoClient = MongoClient(mongo_server_link)                                                                # mongo DB 서버에 연결
    database = mongoClient[database_name]                                                                       # 데이터 베이스에 연결
    collection = database[collection_name]                                                                      # collection에 연결
    return collection

def insert_list(collection,list_items):                                                                         # 리스트의 dict들을 모두 추가하는 함수 작성
    for i in range(len(list_items)):                                                                            # 리스트의 dict들이 모두 추가될 때까지 반복
        dict_quiz = list_items[i]                                              
        collection.insert_one(dict_quiz)                                                                            # 리스트의 dict 추가

def user_answer(collection,list_items,user_name):                                                                         # 리스트의 dict들을 모두 추가하는 함수 작성
    for i in range(len(list_items)):                                                                            # 리스트의 dict들이 모두 추가될 때까지 반복
        dict_quiz = list_items[i][user_name]                                              
        collection.insert_one(dict_quiz)
def db_question():                                                                                              # collection에서 question 데이터를 가져와 리스트 작성
    quiz = collection.find({},{"_id":0,"question":1, "choices":1,"answer":1,"answer_number":1,"score":1})
    list_question = []   
    for i in quiz:
        list_question.append(i["question"])
    return list_question
def db_choices():                                                                                               # collection에서 choice 데이터를 가져와 리스트 작성
    quiz = collection.find({},{"_id":0,"question":1, "choices":1,"answer":1,"answer_number":1,"score":1})
    list_choices = []   
    for i in quiz:
        list_choices.append(i["choices"])
    return list_choices
def db_answer():                                                                                                # collection에서answer 데이터를 가져와 리스트 작성
    quiz = collection.find({},{"_id":0,"question":1, "choices":1,"answer":1,"answer_number":1,"score":1})
    list_answer = []   
    for i in quiz:
        list_answer.append(i["answer"])
    return list_answer 
def db_answer_number():                                                                                         # collection에서 answer_number 데이터를 가져와 리스트 작성
    quiz = collection.find({},{"_id":0,"question":1, "choices":1,"answer":1,"answer_number":1,"score":1})
    list_answer_number = []   
    for i in quiz:
        list_answer_number.append(i["answer_number"])
    return list_answer_number
def db_score():                                                                                         # collection에서 answer_number 데이터를 가져와 리스트 작성
    quiz = collection.find({},{"_id":0,"question":1, "choices":1,"answer":1,"answer_number":1,"score":1})
    list_score = []   
    for i in quiz:
        list_score.append(i["score"])
    return list_score
def user_name():
    user_name = input()
    return user_name

def question_print(list_question, list_choices,list_answer_number,list_input):                                  # 질문지 출력과 정답 입력 프린트
    for i in range(len(list_question)):                                                 
        print(list_question[i])
        for j in range(len(list_choices[i])):
            print("{}. {} ".format(j+1,list_choices[i][j]))
        input_answer = int(input("답을 입력하세요.:"))
        if int(input_answer) == list_answer_number[i]:
            print("정답입니다!")
        list_input.append(input_answer)
    return list_input

def score_sum(list_input,list_answer_number,list_score):
    score_sum = 0
    for i in range(len(list_input)):
        if list_input[i] == list_answer_number[i]:
            score_sum = score_sum + list_score[i]
    print("최종 점수 : {}".format(score_sum))
    return score_sum

def update_data(quiz_list,list_input,user_name,collection):
    for i in range(len(quiz_list)):                                                                            # 리스트의 dict들이 모두 추가될 때까지 반복
        quiz_list[i][user_name] = list_input[i]
    for i in range(len(quiz_list)):
        collection.update_one({"question": quiz_list[i]["question"]},{'$set': {user_name : list_input[i]}})

quiz_list = [                                                                  #추가할 리스트 작성
    {
        "question": "Python의 생성자 함수 이름은 무엇인가요?",
        "choices": ["__init__", "__main__", "__str__", "__del__"],
        "answer": "__init__",
        "answer_number":1,
        "score": 20
    },
    {
        "question": "Python에서 'Hello, World!'를 출력하는 코드는 무엇인가요?",
        "choices": ["print('Hello, World!')", "console.log('Hello, World!')", "printf('Hello, World!')", "echo 'Hello, World!'"],
        "answer": "print('Hello, World!')",
        "answer_number":1,
        "score": 20
    },
    {
        "question": "Python의 주석을 나타내는 기호는 무엇인가요?",
        "choices": ["//", "/* */", "#", "--"],
        "answer": "#",
        "answer_number":3,
        "score": 20
    },
    {
        "question": "Python에서 리스트의 길이를 반환하는 함수는 무엇인가요?",
        "choices": ["size()", "length()", "len()", "sizeof()"],
        "answer": "len()",
        "answer_number":3,
        "score": 20
    },
    {
        "question": "Python에서 문자열을 숫자로 변환하는 함수는 무엇인가요?",
        "choices": ["str()", "int()", "char()", "float()"],
        "answer": "int()",
        "answer_number":2,
        "score": 20
    }
]


mongo_server_link = "mongodb://localhost:27017"                                 # mongoDB 서버 입력
database_name ="local"                                                          # 데이터 베이스 이름 입력
collection_name = 'solvingProblem'                                                 # collection 이름 입력

collection = connect(mongo_server_link,database_name,collection_name)                        # 추가하고자 하는 collection에 연결
collection.delete_many({})
insert_list(collection,quiz_list)
list_input = []
question_index = db_question()
choices_index = db_choices()
answer_index = db_answer()
answer_number_index = db_answer_number()
score_index = db_score()
str_user_name = user_name()
list_input = question_print(question_index,choices_index,answer_number_index,list_input)
score_sum(list_input,answer_number_index,score_index)
update_data(quiz_list,list_input,str_user_name,collection)