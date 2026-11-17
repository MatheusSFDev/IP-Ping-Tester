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
    
    validIP = False
    while not validIP:
        print("Please Enter the IP you want to check")
        ip = input("-> ")
        validIP = checkIPStr(ip)
    
    with concurrent.futures.ThreadPoolExecutor() as exec:
        future = exec.submit(ping, ip)
        ip, code = future.result()
        
        result = "Connected" if code == 0 else "Disconnected"
        print(F"Result: {result}")
    
def pingIPs():
    print("- Ping Multiple IPs -")
    IPs = []
    
    inserting = True
    while inserting:
        print("Please Enter the IP you want to check (Press Enter when you finish)")
        ip = input("-> ")
        
        if ip != "":
            validIP = False
            while not validIP:
                validIP = checkIPStr(ip)
                
                if not validIP:
                    print("(Or if you want to exit press Enter)")
                    ip = input("-> ")
                    
                    if ip == "":
                        inserting = False
                        break
                    
            if validIP:
                IPs.append(ip)
        elif len(IPs) == 0:
            print("Insert at least 1 IP")
        else:
            inserting = False
    
    results = []
    
    with concurrent.futures.ThreadPoolExecutor() as exec:
        futures = [exec.submit(ping, ip) for ip in IPs]
        for future in concurrent.futures.as_completed(futures):
            ip, code = future.result()
            results.append({"ip": ip, "code": code})
            
    if len(results) != 0:
        connected, disconnected = [], []
        
        for result in results:
            if int(result["code"]) == 0:
                connected.append(result["ip"])
            else:
                disconnected.append(result["ip"])

        print("- Connected IPs -")
        for con in connected:
            print(F"IP: {con}")
        
        print("- Disconnected IPs -")
        for dis in disconnected:
                print(F"IP: {dis}")
    
def ping(ip):
    try:
        if system == 'Windows':
            result = subprocess.run(["ping", "-n", "1", ip], capture_output=True, text=True, encoding="cp850")
        else:
            result = subprocess.run(["ping", "-c", "1", ip], capture_output=True, text=True)
            
        if "TTL" in result.stdout.upper() or result.returncode == 0 and "bytes=" in result.stdout.lower():
            return ip, 0
        else:
            return ip, 1
            
    except Exception as ex:
        print(f"An Error has occurred for {ip}: {ex}")
        return ip, 1
        
    
def checkIPStr(ip):
    numbers = ip.rsplit(".")
    
    if len(numbers) == 4:
        for num in numbers:
            if int(num) < 0 or int(num) > 255:
                return False
        
        return True
    else:
        print("Incorrect Format, Please Insert an Valid IP, Ex: 192.168.1.1")
        return False

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