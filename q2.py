string_list = []
while True:
    string_list.append(input("Enter a string: "))
    if string_list[len(string_list)-1]=="STOP" or string_list[len(string_list)-1]=="stop":
        break
    for i in range(len(string_list)-1,0,-1):
        if len(string_list[i]) > len(string_list[i-1]):
            string_list[i],string_list[i-1] = string_list[i-1],string_list[i]
print(f"{string_list[0]} {string_list[len(string_list)-2]}")