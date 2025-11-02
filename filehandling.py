with open("notes.txt","w") as f:
    f.write("""1. Learn a  lot 
2. work well as a full stack ai Dev
3. Be fitter""")
    
with open("notes.txt","r") as f:
    cnt = f.read()
    print(cnt)

with open("notes.txt","a") as f:
    f.write("4.Earn something")

with open("notes.txt","r") as f:
    cnt = f.read()
    print(cnt)