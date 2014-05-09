import subprocess

GETWANIP_SERVER = "myexternalip.com/raw"
REMOTE_SERVER = "SERVERNAME"
REMOTE_USER = "USERNAME"
REMOTE_PASSWORD ="PASSWORD"
rpi_wan_ip = ""
rpi_user = "pi"
FILE_NAME = "ip.txt"
LOCAL_PATH = ""
REMOTE_PATH = "REMOTE_PATH"

#GET_WAN_IP
curl = subprocess.Popen(
    ["curl", GETWANIP_SERVER],
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE
)
rpi_wan_ip, error = curl.communicate()
rpi_wan_ip = (rpi_wan_ip.decode('utf-8'))
print ("Vehicle Control System - WAN-IP Address: ")
print (rpi_wan_ip)

#PRINT TO FILE
f = open('FILE_NAME', 'w')
s = str(rpi_wan_ip)
f.write(s)
f.close()

#UPLOAD TO SERVER
from ftplib import FTP
ftp = FTP(REMOTE_SERVER,REMOTE_USER,REMOTE_PASSWORD)
#ftp.login()
ftp.cwd(REMOTE_PATH)
file = open('ip.txt','rb')                  # file to send
ftp.storbinary('STOR ip.txt', file)     # send the file


file.close()                                    # close file and FTP
ftp.quit()
