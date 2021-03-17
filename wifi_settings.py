#Stephen Bowen 2021
import os
import time

#Write data to .conf file
def writeToFile(conf):
    with open ("/etc/wpa_supplicant/TigerWiFi.conf", "w") as file:
        file.write("ctrl_interface=DIR=/var/wpa_supplicant\n")
        file.write(conf)
        file.write("\n")

#Easy setup for TigerWiFi network at Mizzou
def TigerWiFi(identity, password):
    conf = "network={\n  ssid=\"TigerWiFi\"\n  key_mgmt=WPA-EAP\n  eap=PEAP\n  phase2=\"MSCHAPV2\"\n  identity="+f"\"{identity}\"\n  "+f"password=\"{password}\"\n"+"}"
    writeToFile(conf)
    print("\n\nSuccess!\n\n")
    time.sleep(5)
    os.system('clear')
    print("\n\nRebooting Pi...\n\n")
    time.sleep(3)
    os.system('reboot')

#Setup for generic wifi network 
#MIGHT REQUIRE MANUAL CONFIGURATION
def GenericWiFi(securityType, ssid, password):
    conf = "network={\n  ssid="+f"\"{ssid}\"\n  key_mgmt=\"{securityType}\"\n  psk=\"{password}\"\n"+"}"
    writeToFile(conf)
    print("\n\nSuccess!\n\n")
    time.sleep(5)
    os.system('clear')
    print("\n\nRebooting Pi...\n\n")
    time.sleep(3)
    os.system('reboot')

def main():
    os.system('clear')
    print("="*os.get_terminal_size().columns)
    print("This program sets the default wifi network that this Pi will connect to on boot.".center(os.get_terminal_size().columns))
    print("If you want to connect to a network temporarily, use the GUI found in settings.".center(os.get_terminal_size().columns))
    print("="*os.get_terminal_size().columns)
    print("\n")
    print("To what network would you like to connect?\n")
    print("\t1. TigerWifi")
    print("\t2. Other\n")
    networkChoice = input("Enter your choice as a number: ")

    if networkChoice == "1":
        os.system('clear')
        print("Please enter your credentials for TigerWifi (pawprint).\n")
        identity = input("Username: ")
        password = input("Password: ")
        TigerWiFi(identity,password)
    elif networkChoice == "2":
        os.system('clear')
        print("Please enter your credentials the wifi network.\n")
        securityType = input("Type of Security: ")
        ssid = input("SSID: ")
        password = input("Password: ")
        GenericWiFi(securityType, ssid, password)
    else:
        os.system('clear')
        print("Please enter only 1 or 2.")
        time.sleep(3)
        main()

if __name__ == "__main__":
    main()