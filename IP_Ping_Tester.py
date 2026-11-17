#by MatheusSFDev
import platform, subprocess, concurrent.futures

system = platform.system()
program = True

# * Program Functions
def mainMenu():
    print("1. Ping Single IP")
    print("2. Ping Multiple IPs")
    print("0. Exit")
    
    return input("-> ")

def pingIP():
    print("- Ping Single IP -")
    
    print("Please Enter the IP you want to check")
    ip = input("-> ")
    
    with concurrent.futures.ThreadPoolExecutor() as exec:
        future = exec.submit(ping, ip)
        result = "Connected" if future.result() == 0 else "Disconnected"
        
    print(F"Result: {result}")
    
def pingIPs():
    print("- Ping Multiple IPs -")
    
def ping(ip):
    try:
        if (system == 'Windows'):
            result = subprocess.run(["ping", ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            result = subprocess.run(["ping", "-c", "4", ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as ex:
        print("An Error has ocurred while executing the Ping Command, More Info:")
        print(ex)
    else:
        return result.returncode

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
            pingIPs()
        case "0":
            program = False
        case _:
            print("Unvalid Option, Please choose a correct option")
    
    print("-------------------------------------------------------")

print("Thanks for Using!")
print("-------------------------------------------------------")

input("Press Enter to Close...")