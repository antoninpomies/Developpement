import re, subprocess

re_adress_ip = re.compile(rb'"ip": "([0-9\.]+)"')

resultat = subprocess.run('curl ipinfo.io 2> /dev/null', shell=True, stdout=subprocess.PIPE)
sortie = resultat.stdout
#print(sortie)

resultat = re_adress_ip.search(sortie)
if resultat:
    print(resultat.group(1))

