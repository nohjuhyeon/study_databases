                                                                           # todo list를 todos_list collection에 추가
# list_user_name = quest_todo.participate_upload()                                                                    # 참여자의 정보를 participants에 collection에 추가
class quest():
    def __init__(self,mongo_server_link,database_name):                                                                   # collection에 연결하는 함수 
        from pymongo import MongoClient
        self.mongoClient = MongoClient(mongo_server_link)                                                                 # mongo DB 서버에 연결
        self.database = self.mongoClient[database_name]                                                                   # 데이터 베이스에 연결
        self.todos_list = self.database["todos_list"]                                                                     # collection "todos_list"에 연결
        self.participants = self.database["participants"]                                                                 # collection "participants"에 연결
        self.participants_todo = self.database["participants_todo"]                                                       # collection "participants_todo"에 연결
    
    def todo_list_upload(self,list):    
        self.todos_list.delete_many({})                                                                                 
        self.todos_list.insert_many(list)                                                                                # todolist 업로드 
    
    def user_name_input(self):
        self.participants.delete_many({})   
        participate_dict = {}                                                                                      # 참여자의 dictionary 구성
        str_participate =input("input Your Name : ")                                                               # 참여자의 이름 입력
        participate_dict["name"] =str_participate                                       
        self.participants.insert_one(participate_dict)                                                               # 참여자 리스트 업로드
        pass
        user_name = self.participants.find({},{"_id":1,"name":1})                                                     # 참여자의 이름과 ID  가져오기 
        # for i in user_name:
        list_user_name = []
        for i in user_name:
            list_user_name.append(i["_id"])
            list_user_name.append(i["name"])
        return list_user_name


    def participate_todo(self):
        dict_todo = {}
        print("ToDo List 중 하나 선택 하세요 !")
        print("1. 주간 보고서 작성, 2. 이메일 확인 및 응답, 3. 회의 준비, 4. 프로젝트 계획서 수정, 팀 멤버와의 1:1 면담")    # todolist 출력
        while True:                                                                                                    # 원하는 값이 입력될 때까지 반복 
            num_title = input("Title 번호 : ")                                                                         # title 번호 입력
            if num_title == "1" or num_title == "2" or num_title == "3" or num_title == "4":                           # 번호가 1,2,3,4 중 하나일 경우
                dict_todo["title"] = num_title                                                             # dict_participate_todo 에 추가
                break                                                                                                  # 반복문 finish
            else:                                                                                                      # 아닐 경우
                print("'1','2','3','4' 중 하나를 입력해주세요.")                                                         # "'1','2','3','4' 중 하나를 입력해주세요." 출력 후, 반복
        while True:                                                                                                    # 원하는 값이 입력될 때까지 반복
            print("'완료' 또는 '진행중'을 입력해주세요.")
            str_status = input("Status : ")                                                                            # status 입력
            if str_status == "완료" or str_status == "진행중":                                                          # status 입력값이 '입력' 또는 '진행중'일 경우
                dict_todo["status"] = str_status                                                           # dict_participate_todo에 추가
                break                                                                                                  # 반복문 finish
        return dict_todo

    def if_input_finish(self):     
        while True:                                                                                                   # 원하는 값이 나올 때까지 반복
            print("todo list 추가 시 'c', 다음 사용자 입력 시 'q', 모든 입력을 종료할 시 'x'를 입력하세요")
            input_finish = input("종료 여부 : ").lower                                                                 # 종료 여부 입력
            if input_finish == "c":                                                                                   # 종료 여부가 c 일 경우
                check_finish = "c"                                                                                    # check_finish = c로 지정
                break
            elif input_finish == "q":                                                                                 # 종료 여부가 q 일 경우
                check_finish = "q"                                                                                    # check_finish = q로 지정
                break
            elif input_finish == "x":                                                                                 # 종료 여부가 x 일 경우
                check_finish = "x"                                                                                    # check_finish = x로 지정
                break
        return check_finish

    def final(self):
        list_participants_todo = []
        while True:
            dict_participate_todo = {}
            while True:
                list_user_name = self.user_name_input()
                dict_participate_todo["user_id"] = list_user_name[0]
                dict_participate_todo["user_name"] = list_user_name[1]
                dict_todo = self.participate_todo()
                dict_participate_todo["title"] = dict_todo["title"]
                dict_participate_todo["status"] = dict_todo["status"]
                check_finish = self.if_input_finish()
                if check_finish == "c":
                    list_participants_todo.append(dict_participate_todo)
                    pass
                else:
                    list_participants_todo.append(dict_participate_todo)
                    break
            if check_finish =="x":
                pass
            else:
                break
        print(list_participants_todo)
    # if check_finish == "q":
    #     list_participants_todo.append(dict_participate_todo)
    #     pass
    # else:
    #     break


# self.participants_todo.insert_many(list_participants_todo)                                                    # 모든 참여자의 입력이 끝나면, participants_todo collection에 추가 


# list_participants_todo = []                                                                                   # 참여자의 todo 리스트와 완료 여부를 리스트로 구성
# quest_todo.participants_todo.delete_many({})                                                                        
# while True:
#     dict_participate_todo = quest_todo.input_participate_todo_list()    
#     if quest_todo.if_input_finish() == "c":                                                                               # 종료 여부가 c일 경우
#         list_participants_todo.append(dict_participate_todo)                                              # list_participants_todo에 dictionary 추가 후,
#         dict_participate_todo = quest_todo.input_participate_todo_list()    
#         pass                                                                                              # 다시 반복
#     else:                                                                                                 # 아닐 경우
#         list_participants_todo.append(dict_participate_todo)                                              # list_participants_todo에 dictionary 추가 후, 
#         break                                                                                             # 종료
# if check_finish == "x":                                                                                   # 종료 여부가 x일 경우
#     break                                                                                                 # 입력 완전 종료
# quest_todo.participants_todo.insert_many(list_participants_todo)                                                    # 모든 참여자의 입력이 끝나면, participants_todo collection에 추가 


# for i in user_name:
#     dict_user_name = {}                                                                                       # 참여자의 dictionary 구성
#     dict_user_name["_id"] = i["_id"]                                                                          # 참여자의 아이디 dictionary에 추가
#     dict_user_name["name"] = i["name"]                                                                        # 참여자의 이름 dictionary에 추가
#     list_user_name.append(dict_user_name)                                                                     # 참여자의 dictionary를 list에 추가

# quest_todo.participant_todo_upload(list_user_name)                                                                  # 참여자의 todo list와 진행 여부를 participants_todo에 추가
