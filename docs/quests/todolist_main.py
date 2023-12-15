class quest():
    def __init__(self,mongo_server_link,database_name):                                                   # collection에 연결하는 함수 작성
        from pymongo import MongoClient
        self.mongoClient = MongoClient(mongo_server_link)                                                                # mongo DB 서버에 연결
        self.database = self.mongoClient[database_name]                                                                       # 데이터 베이스에 연결

    def todo_list_upload(self,list):
        self.collection = self.database["todos_list"]
        self.collection.delete_many({})
        self.collection.insert_many(list)
    
    def participate_upload(self):
        self.collection = self.database["participants"]
        self.collection.delete_many({})
        participate_list = [{},{},{}]
        for participate in participate_list:
            str_participate =input("input Your Name : ")
            participate["name"] =str_participate
        self.collection.insert_many(participate_list)
        






# mongodb에 접속 -> 자원에 대한 class 

mongo_server_link = "mongodb://localhost:27017"                                                                       # mongoDB 서버 입력
database_name ="local"                                                                                                # 데이터 베이스 이름 입력

quest_todo = quest(mongo_server_link,database_name)
todo_list = [
    {"title": "주간 보고서 작성", "description": "팀의 주간 성과와 진행 상황에 대한 보고서를 작성합니다."},
    {"title": "이메일 확인 및 응답", "description": "미처 확인하지 못한 이메일을 확인하고 필요한 이메일에 대해 응답합니다."},
    {"title": "회의 준비", "description": "다가오는 회의에 대해 준비합니다. 주제 연구, 발표 자료 준비 등이 포함될 수 있습니다."},
    {"title": "프로젝트 계획서 수정", "description": "현재 진행 중인 프로젝트의 계획서를 검토하고 필요한 부분을 수정합니다."},
    {"title": "팀 멤버와의 1:1 면담", "description": "팀 멤버와 개별적으로 만나서 그들의 업무 진행 상황, 이슈, 우려사항 등을 논의합니다."},
]
quest_todo.todo_list_upload(todo_list)
quest_todo.participate_upload()

while True:
    try: 
        print("ToDo List 중 하나 선택 하세요 !")
        print("1. 주간 보고서 작성, 2. 이메일 확인 및 응답, 3. 회의 준비, 4. 프로젝트 계획서 수정, 팀 멤버와의 1:1 면담")
        num_title = input("Title 번호(종료를 원할 경우 \"C\"를 누르세요.) : ").lower()
        if num_title != "c":
            pass
        else:
            break

    except:
        pass