class quest():
    def __init__(self,mongo_server_link,database_name):                                                   # collection에 연결하는 함수 작성
        from pymongo import MongoClient
        self.mongoClient = MongoClient(mongo_server_link)                                                                # mongo DB 서버에 연결
        self.database = self.mongoClient[database_name]                                                                       # 데이터 베이스에 연결
        self.todos_list = self.database["todos_list"]
        self.participants = self.database["participants"]
        self.participants_todo = self.database["participants_todo"]
        self.dict_participate_todo = {}
        self.check_finish = ""
    
    def todo_list_upload(self,list):
        self.todos_list.delete_many({})
        self.todos_list.insert_many(list)
    
    def participate_upload(self):
        self.participants.delete_many({})
        participate_list = []
        for i in range(3):
            participate_dict = {}
            str_participate =input("input Your Name : ")
            participate_dict["name"] =str_participate
            participate_list.append(participate_dict)
        self.participants.insert_many(participate_list)
        user_name = self.participants.find({},{"_id":1,"name":1})
        list_user_name = []   
        for i in user_name:
            list_user_name.append(i["_id"])
        return list_user_name
         
    def input_participate_todo_list(self):
        print("ToDo List 중 하나 선택 하세요 !")
        print("1. 주간 보고서 작성, 2. 이메일 확인 및 응답, 3. 회의 준비, 4. 프로젝트 계획서 수정, 팀 멤버와의 1:1 면담")
        dict_participate_todo = {}
        while True:
            num_title = input("Title 번호 : ").lower()
            if num_title == "1" or num_title == "2" or num_title == "3" or num_title == "4":
                dict_participate_todo["title"] = num_title     
                break
            else:
                print("'1','2','3','4' 중 하나를 입력해주세요.")
        while True:
            print("'완료' 또는 '진행중'을 입력해주세요.")
            str_status = input("Status : ")
            if str_status == "완료" or str_status == "진행중":
                dict_participate_todo["status"] = str_status
                break
        return dict_participate_todo

    def if_input_finish(self):     
        while True:
            print("todo list 추가 시 'c', 다음 사용자 입력 시 'q', 모든 입력을 종료할 시 'x'를 입력하세요")
            input_finish = input("종료 여부 : ")
            if input_finish == "c":
                self.check_finish = "c"
                break
            elif input_finish == "q":
                self.check_finish = "q"
                break
            elif input_finish == "x":
                self.check_finish = "x"
                break
        return self.check_finish
    
    def participant_todo_upload(self,list_user_name):
        list_participants_todo = []
        self.participants_todo.delete_many({})
        for i in range(len(list_user_name)):
            while True:
                dict_participate_todo = self.input_participate_todo_list()
                print(dict_participate_todo)
                dict_participate_todo["user_id"] = list_user_name[i]
                check_finish = self.if_input_finish()
                if check_finish == "c":
                    list_participants_todo.append(dict_participate_todo)
                    pass
                else:
                    list_participants_todo.append(dict_participate_todo)
                    break
            if check_finish == "x":
                break
        self.participants_todo.insert_many(list_participants_todo)

