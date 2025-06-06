Voici mon petit projet SUR IA

# Classificateur de Type de Pokémon

si EAU FEU ECLAIR TERRE FYING

Ce projet est un outil de classification d'images de Pokémon par type élémentaire à l'aide de **TensorFlow**

Bibliothèques utilisées

- [TensorFlow] : pour le chargement et l’utilisation du modèle de classification.
- [NumPy]: pour les opérations sur les tableaux de données.
- [Pillow (PIL)]: pour le traitement des images.
- [Tkinter] : pour créer l’interface graphique utilisateur.

> Assurez-vous que ces bibliothèques sont installées :

pip install tensorflow numpy pillow

#Utilisation

1. lancer le model.py pour l'entrainement si pokemon_type_classifier.h5 n est pas encore crée sinon voir 2)
2. lancer predit.py :apres lancement il faut coller le chemin complet vers l'image de votre pokémon et ajouter apres son nom avec extension(png)
   exemple : C:\Users\user\pokémon\data\eau\blastoise.png
3. lancer gui_predict.py : apres lancement il faut naviguée jusqu'a votre image et le selectionnée.
