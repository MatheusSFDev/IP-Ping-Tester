#by MatheusSFDev
program = True

# * Program Functions
def mainMenu():
    print("1. Ping Single IP")
    print("2. Ping Multiple IPs")
    print("0. Exit")
    
    return input("-> ")

def pingIP():
    print("- Ping Single IP -")
    
def pingMultipleIPs():
    print("- Ping Multiple IPs -")

print("-------------------------------------------------------")
print("- IP Ping Tester -")
print(" #by MatheusSFDev")
print("-------------------------------------------------------")

# * Main Program
while program:
    match mainMenu():
        case "1":
            pingIP()
        case "2":
            pingMultipleIPs()
        case "0":
            program = False
        case _:
            print("Unvalid Option, Please choose a correct option")
    
    print("-------------------------------------------------------")

print("Thanks for Using!")
print("-------------------------------------------------------")

input("Press anything to Close...")