x=0
try:
    with open("sample.txt", "r") as file:
        for line in file:
            x+=1
            print("Line",x,":", line.strip())
except FileNotFoundError:
    print("The file was not found.")