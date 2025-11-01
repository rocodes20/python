def health_index(weight, age, temp):
    index = (weight / age) + (temp / 100)
    return index

analysis = health_index(60,20,98)

if analysis >= 5:
    print("excellent")
elif analysis >= 3 and analysis < 5:
    print("moderate")
else:
    print("attention")

print(analysis)