import json

try:
    with open("data.json","r") as f:
        cnt = json.load(f)
        print(cnt)
except FileNotFoundError:
    with open("data.json","w") as f:
        json.dump([],f,indent=4)

except json.JSONDecodeError:
    with open("data.json","w") as f:
        json.dump([],f)

except Exception as e:
    print(e)

finally:
    print("task done")