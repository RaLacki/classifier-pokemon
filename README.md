# 🧠 Classificateur de Type de Pokémon

Ce projet est un outil de classification d'images de Pokémon par **type élémentaire** à l'aide de **TensorFlow** et d'un modèle de réseau de neurones convolutifs (**CNN**).  
Il permet de détecter 5 types de Pokémon :

> **Eau**, **Feu**, **Éclair**, **Terre**, **Flying**

---

## 📦 Bibliothèques utilisées

- [TensorFlow](https://www.tensorflow.org/) : pour le chargement et l’utilisation du modèle de classification.
- [NumPy](https://numpy.org/) : pour les opérations sur les tableaux de données.
- [Pillow (PIL)](https://python-pillow.org/) : pour le traitement des images.
- [Tkinter] : pour créer l’interface graphique utilisateur (optionnelle).

✅ **Installation :**

```bash
pip install tensorflow numpy pillow
```

---

## 🚀 Fonctionnalités

- 📁 Chargement d'images de Pokémon depuis un dossier organisé (`data/<type>/`)
- 🔁 Entraînement d'un modèle CNN avec **data augmentation**
- 🔍 Prédiction du type de Pokémon à partir d'une image
- 🖼️ Interface graphique simple pour sélectionner une image et afficher la prédiction
- 💾 Modèle sauvegardé automatiquement au format `.h5`

---

## 📂 Structure du projet

```
pokemon-classifier/
│
├── data/
│   ├── eau/
│   ├── feu/
│   ├── eclair/
│   ├── terre/
│   └── flying/
│
├── model.py                     # Script d'entraînement du modèle
├── predict.py                   # Script de prédiction en ligne de commande
├── gui_predict.py               # Interface graphique Tkinter
├── pokemon_type_classifier.h5   # Modèle sauvegardé
└── README.md
```

---

## 📈 Performances du modèle

- **Images utilisées** : ~30 images par classe
- **Accuracy entraînement** : entre 20% et 90%
- **Accuracy validation** : entre 60% et 80% (selon la qualité et diversité des images)
- **Architecture** :
  - 2 couches `Conv2D + MaxPooling2D`
  - 1 couche `Dense` de 64 neurones

---

## 🧠 Utilisation

### 1. Entraîner le modèle (si `pokemon_type_classifier.h5` n'existe pas encore) :

```bash
python model.py
```

---

### 2. Lancer la prédiction en ligne de commande :

```bash
python predict.py
```

Ensuite, entrez le **chemin complet** vers l’image, par exemple :

```bash
C:\Users\user\pokémon\data\eclair\pikachu.png
```

---

### 3. Utiliser l’interface graphique (facultatif) :

```bash
python gui_predict.py
```

Une fenêtre s’ouvrira. Naviguez jusqu’à l’image de votre choix.
