import json
data = [{
    "name" : "Rohit","mark" : 90
},{"name" : "rahul","mark" : 80},{"name" : "vinayak","mark" : 99}]
# with open("stu.json","w") as f:
#     json.dump(data,f,indent=4)


data.append({"name":"puli","marks":35})

with open("stu.json","w") as f:
    json.dump(data,f,indent=4)

with open("stu.json","r") as f:
    info = json.load(f)
    print(info)
