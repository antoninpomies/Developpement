# Livrable du projet LogParser
## Structure générale :

La structure générale du script commence par l'importation des modules nécessaires, suivi de la définition des fonctions. Ensuite, il y a l'initialisation du parser argparse, la vérification des arguments en ligne de commande, l'ouverture du fichier initial, la recherche des logs et enfin, l'affichage des logs dans une interface Tkinter.
Fonction afficherLogs :

La fonction afficherLogs crée une fenêtre Tkinter avec un champ d'entrée, un bouton de changement de fichier, et un Treeview pour afficher les logs. Elle utilise des tags pour colorer les lignes en fonction du code de statut et ajoute un bouton "Ouverture IP" à chaque ligne. Le Treeview est configuré avec des colonnes et des en-têtes pour afficher différentes informations.
## Fonction ouvrirIp :

La fonction ouvrirIp est appelée lorsqu'un utilisateur clique sur le bouton "Ouverture IP". Elle récupère l'adresse IP de la ligne cliquée dans le Treeview et ouvre le navigateur avec cette adresse IP en utilisant le module webbrowser.
## Fonction chargerFichier :

La fonction chargerFichier est appelée lorsque l'utilisateur souhaite changer de fichier. Elle utilise filedialog pour ouvrir une boîte de dialogue permettant de sélectionner un nouveau fichier. Elle lit ensuite le contenu de ce fichier, extrait les logs avec une expression régulière, et met à jour l'affichage dans le Treeview.
## Fonction trierLogsParTaille :

La fonction trierLogsParTaille est appelée lorsqu'un utilisateur clique sur la colonne 'Taille' pour trier les logs par taille. Elle utilise sort pour trier les logs en fonction de la taille des trames et met à jour l'affichage dans le Treeview.
## Utilisation de modules externes :

argparse est utilisé pour gérer les arguments en ligne de commande, permettant à l'utilisateur de spécifier le fichier de logs au moment de l'exécution. filedialog est utilisé pour permettre à l'utilisateur de choisir un fichier via une boîte de dialogue.
## Gestion des logs :

Les logs sont extraits du fichier avec une expression régulière (motifLogGenerique) qui correspond à un format spécifique. Les logs extraits sont affichés dans le Treeview avec une coloration en fonction du code de statut.
## Utilisation de la programmation fonctionnelle :

Les fonctions anonymes (lambda) sont utilisées pour créer des fonctions ad hoc, par exemple, pour lier des événements à des actions spécifiques dans l'interface utilisateur.
## Gestion des exceptions et erreurs :

Le script utilise une structure try-except pour gérer les erreurs potentielles lors de l'ouverture et de la lecture des fichiers. Il affiche également un message si aucun log web n'est trouvé dans le fichier.
## Extensions possibles :

Le script pourrait être étendu pour permettre des fonctionnalités telles que le filtrage des logs, la recherche, ou l'affichage de statistiques. L'interface utilisateur pourrait également être améliorée avec plus de fonctionnalités interactives.
