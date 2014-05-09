import subprocess

host = "myexternalip.com/raw"

curl = subprocess.Popen(
    ["curl", host],
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE
)

out, error = curl.communicate()
out = (out.decode('utf-8'))
print (out)
