import requests

# URL du site et informations d'authentification
url = 'http://localhost:65434/hello'

# Création d'une session
with requests.Session() as session:

    # Envoie une requête POST pour se connecter
    response = session.post(url)

    # Vérifie si la connexion a réussi (status code 200)
    if response.ok:
        print("Connexion réussie!")
        page_content = session.get('http://localhost:65434').text
        print(page_content)
    else:
        print(f"Échec de la connexion. Statut de la réponse : {response.status_code}")

