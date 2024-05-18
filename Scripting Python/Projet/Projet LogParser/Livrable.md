# Livrable du projet LogParser

## Structure générale :
<details>
<summary>Détails</summary>
La structure générale du script commence par l'importation des modules nécessaires, suivi de la définition des fonctions. Ensuite, il y a l'initialisation du parser argparse, la vérification des arguments en ligne de commande, l'ouverture du fichier initial, la recherche des logs et enfin, l'affichage des logs dans une interface Tkinter.
Fonction afficherLogs :
</details>

## Fonction afficherLogs :
<details>
<summary>Détails</summary>
La fonction afficherLogs crée une fenêtre Tkinter avec un champ d'entrée, un bouton de changement de fichier, et un Treeview pour afficher les logs. Elle utilise des tags pour colorer les lignes en fonction du code de statut et ajoute un bouton "Ouverture IP" à chaque ligne. Le Treeview est configuré avec des colonnes et des en-têtes pour afficher différentes informations.
</details>

## Fonction ouvrirIp :
<details>
<summary>Détails</summary>
La fonction ouvrirIp est appelée lorsqu'un utilisateur clique sur le bouton "Ouverture IP". Elle récupère l'adresse IP de la ligne cliquée dans le Treeview et ouvre le navigateur avec cette adresse IP en utilisant le module webbrowser.
</details>

## Fonction chargerFichier :
<details>
<summary>Détails</summary>
La fonction chargerFichier est appelée lorsque l'utilisateur souhaite changer de fichier. Elle utilise filedialog pour ouvrir une boîte de dialogue permettant de sélectionner un nouveau fichier. Elle lit ensuite le contenu de ce fichier, extrait les logs avec une expression régulière, et met à jour l'affichage dans le Treeview.
</details>

## Fonction trierLogsParTaille :
<details>
<summary>Détails</summary>
La fonction trierLogsParTaille est appelée lorsqu'un utilisateur clique sur la colonne 'Taille' pour trier les logs par taille. Elle utilise sort pour trier les logs en fonction de la taille des trames et met à jour l'affichage dans le Treeview.
</details>

## Utilisation de modules externes :
<details>
<summary>Détails</summary>
argparse est utilisé pour gérer les arguments en ligne de commande, permettant à l'utilisateur de spécifier le fichier de logs au moment de l'exécution. filedialog est utilisé pour permettre à l'utilisateur de choisir un fichier via une boîte de dialogue.
</details>

## Gestion des logs :
<details>
<summary>Détails</summary>
Les logs sont extraits du fichier avec une expression régulière (motifLogGenerique) qui correspond à un format spécifique. Les logs extraits sont affichés dans le Treeview avec une coloration en fonction du code de statut.
</details>

## Utilisation de la programmation fonctionnelle :
<details>
<summary>Détails</summary>
Les fonctions anonymes (lambda) sont utilisées pour créer des fonctions ad hoc, par exemple, pour lier des événements à des actions spécifiques dans l'interface utilisateur.
</details>

## Gestion des exceptions et erreurs :
<details>
<summary>Détails</summary>
Le script utilise une structure try-except pour gérer les erreurs potentielles lors de l'ouverture et de la lecture des fichiers. Il affiche également un message si aucun log web n'est trouvé dans le fichier.
</details>

## Extensions possibles :
<details>
<summary>Détails</summary>
Le script pourrait être étendu pour permettre des fonctionnalités telles que le filtrage des logs, la recherche, ou l'affichage de statistiques. L'interface utilisateur pourrait également être améliorée avec plus de fonctionnalités interactives.
</details>
