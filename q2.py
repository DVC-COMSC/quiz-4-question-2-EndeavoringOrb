largest_string = ""
smallest_string = ""
while True:
    new_string = input("Enter a string: ")
    if new_string == "STOP" or new_string == "stop":
        break
    if len(new_string) > len(largest_string):
        largest_string = new_string
    if len(new_string) < len(smallest_string):
        smallest_string = new_string
print(f"{largest_string} {smallest_string}")