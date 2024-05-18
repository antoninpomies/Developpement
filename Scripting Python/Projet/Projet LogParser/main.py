import argparse
import re

# Création de l'objet ArgumentParser
parser = argparse.ArgumentParser()

# Ajout de l'argument -f pour spécifier le chemin du fichier
parser.add_argument('-f', '--file', help='Chemin du fichier à ouvrir et lire')

# Parsing des arguments de la ligne de commande
args = parser.parse_args()

# Vérification si l'argument -f est présent
if args.file:
    # Ouverture du fichier en mode lecture
    with open(args.file, 'r') as file:
        # Lecture du contenu du fichier
        content = file.read()

        # Expression régulière pour rechercher des trames de logs web
        web_log_pattern = re.compile(r'(\S+) - - \[(.*?)\] "(.*?)" (\d+) (\d+) "(.*?)" "(.*?)"')

        # Recherche des trames de logs web dans le contenu du fichier
        web_logs = web_log_pattern.findall(content)

        # Affichage des trames de logs web décomposées
        if web_logs:
            print('Trames de logs web trouvées :')
            for log in web_logs:
                ip, timestamp, request, status_code, size, referrer, user_agent = log

                # Affichage des blocs décomposés
                print(f'IP: {ip}')
                print(f'Timestamp: {timestamp}')
                print(f'Requête: {request}')
                print(f'Statut: {status_code}')
                print(f'Taille: {size}')
                print(f'Référent: {referrer}')
                print(f'User Agent: {user_agent}')

                # Séparation visuelle entre les blocs
                print('-' * 50)
        else:
            print('Aucune trame de logs web trouvée dans le fichier.')

else:
    print('Veuillez spécifier le chemin du fichier avec l\'argument -f')
