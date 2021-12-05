responces={}

act_flag=True

while act_flag:
    name=input("what is your name?:")
    responce=input("mountain?")

    responces[name]=responce

    repeat=input("agein?yes/no")

    if repeat == "no":
        act_flag=False
    
print("---result---")

for name,res in responces.items():
    print(f"{name} ga {res}")
