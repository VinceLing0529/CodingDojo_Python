def sac():
    number_of_student=input("How many students do you have: ")
    if isinstance(int(number_of_student),int):
        dic=[]
        for i in range(int(number_of_student)):
            dic.append({"name":None,"grade":None,"course":None})
        for i in range(int(number_of_student)):
            name=input("Student Name: ")
            if name!=None:
                dic[i]["name"]=name
                grade = input("Student Grade: ")
                if isinstance(int(grade),int):
                    dic[i]["grade"]=grade
                    course = input("1.Math,2.Science,3.History: ")
                    if int(course)>=1 and int(course) <= 3:
                        dic[i]["course"]=int(course)
                else:
                    print("Invalid grade ,try again")
                    return
            else:
                print("Invalid name ,try again")
                return
        course_name=["Math","Science","History"]
        for i in dic:
            print(f"Name:{i['name']}, Grade:{i['grade']},Course: {course_name[i['course']-1]}")
        
sac()