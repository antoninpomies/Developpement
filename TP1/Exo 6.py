import sys
import subprocess
resultat = subprocess.run("curl ipinfo.io", shell=True,stdout=subprocess.PIPE)
listinfo = resultat.stdout.splitlines()
print(listinfo)