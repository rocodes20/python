import json

data = {
    "name":"rohit",
    "skills":["py","flask","sql"],
    "age":20
}

# with open("data.json","w") as f:
#     json.dump(data,f,indent=4)


with open("data.json","r") as f:
    cnt = json.load(f)
    print(cnt)
    print(cnt["name"])