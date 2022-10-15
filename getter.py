from urllib.request import urlopen
# importing necessary modules
import requests, os, json, zipfile
from io import BytesIO
import shutil
from tqdm.auto import tqdm
import os
from colorama import init,Fore
init()
os.system("cls" or "clear")


url = requests.get("https://changelogs-live.fivem.net/api/changelog/versions/win32/server")
data = json.loads(url.text)

choice = input(Fore.CYAN +"Choose Windows Fivem artifacts version ["+Fore.GREEN+"R = Recommended, "+Fore.MAGENTA+"O = Optional, "+Fore.BLUE+"L = Latest, "+Fore.RED+"C = Critical"+Fore.CYAN +"]: "+Fore.WHITE+" \n")
if choice == 'R':
    print('Version: '+ Fore.BLUE + data['recommended']+ Fore.WHITE)
    print('Download URL: '+ Fore.BLUE + data['recommended_download']+ Fore.WHITE +'\n')
    download_url = data['recommended_download']
elif choice == 'O':
    print('Version: '+ Fore.BLUE + data['optional'] + Fore.WHITE)
    print('Download URL: '+ Fore.BLUE +data['optional_download']+ Fore.WHITE +'\n')
    download_url = data['optional_download']
elif choice == 'L':
    print('Version: '+ Fore.BLUE + data['latest']+ Fore.WHITE)
    print('Download URL: '+ Fore.BLUE +data['latest_download']+ Fore.WHITE +'\n')
    download_url = data['latest_download']
elif choice == 'C':
    print('Version: '+ Fore.BLUE + data['critical']+ Fore.WHITE)
    print('Download URL: '+ Fore.BLUE +data['critical_download']+ Fore.WHITE +'\n')
    download_url = data['critical_download']
else:
    print("Wrong Choice, terminating the program.")


cwd = os.getcwd() # Get the current working directory
print(Fore.WHITE+"Downloading and extracting on directory:"+Fore.BLUE+" {0}".format(cwd+ "\\tmp\\"))
print(Fore.BLUE)
# make an HTTP request within a context manager
with requests.get(download_url, stream=True) as r:
    
    # check header to get content length, in bytes
    total_length = int(r.headers.get("Content-Length"))
    
    # implement progress bar via tqdm
    with tqdm.wrapattr(r.raw, "read", total=total_length, desc="")as raw:
    
        # save the output to a file
        with open(f"{os.path.basename(r.url)}", 'wb')as output:
            shutil.copyfileobj(raw, output)

print(Fore.WHITE)
print('Downloading Completed')

# # extracting the zip file contents
with zipfile.ZipFile('server.zip', 'r') as z:
   z.extractall(cwd + "/tmp/")
print('Extract Completed')

   
