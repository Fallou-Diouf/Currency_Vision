# CurrencyVision
Est un projet académique de détection de pièces de monnaie et d’évaluation des performances d’un algorithme de vision par ordinateur, réalisé dans le cadre du module Traitement d'Image(IF06X070) à l’Université Paris Cité.
# Contexte
On considère une image couleur acquise par un smartphone, représentant un ensemble de pièces en euro disposées sur une surface plane à fond homogène.
# Objectif
Développer un algorithme de vision par ordinateur permettant de détecter les pièces présentes dans l’image, d’en déterminer le nombre et d’estimer la somme totale correspondante.
# Solution 
La solution repose sur une pipeline de traitement d’images combinant prétraitement, segmentation et extraction de caractéristiques, avec une première exploration de la classification par filtres de Gabor–Granger.
# Méthodes Classiques Utilisées
La solution proposée pour la détection et le comptage des pièces de monnaie repose sur plusieurs méthodes classiques de traitement d’images, organisées par étape :
# Prétraitement
Flou Gaussien : réduction du bruit et lissage de l’image.
Flou Médian : suppression du bruit impulsionnel tout en préservant les contours.
Correction Gamma : ajustement de la luminosité.
Conversion en niveaux de gris : simplification de l’image pour le traitement.
Égalisation de l’histogramme adaptatif (CLAHE) : amélioration du contraste local.
# Segmentation
Seuillage d’Otsu : seuil global automatique pour séparer les pièces du fond.
Seuillage Multi-Otsu : segmentation en plusieurs classes (fond, pièces, reflets).
Seuillage adaptatif : seuil local pour gérer les variations d’éclairage.
Segmentation basée sur les couleurs : séparation des pièces selon leur couleur (cuivre, doré, bicolore).
# Détection de formes
Détection de contours avec Canny : extraction des bords des pièces.
Transformée de Hough (cercles) : identification des cercles correspondant aux pièces, récupération du centre et du rayon.
# Extraction de caractéristiques
Filtres de Gabor–Granger : analyse de texture et des motifs de surface.
Local Binary Patterns (LBP) : descripteur de texture robuste aux variations d’éclairage.
# 
Cette chaîne de méthodes classiques permet d’identifier, de compter et de caractériser les pièces de monnaie dans une image en vue de leur classification et estimation de valeur.
# 📂 Structure du projet
CurrencyVision/
│
├── dataset/
│         ├── images 
│         └── labels
├── src/ 
│ ├── 
│ ├── 
│ └── 
│
├── requirements.txt
├── README.md
└── .gitignore


# 🛠️ Technologies utilisées

Python 3.x
OpenCV
NumPy
Matplotlib

# ▶️ Installation
pip install -r requirements.txt

# 🏁 Commencer

Pour démarrer avec le projet, suivez ces étapes :

Clonez le dépôt:
git clone https://github.com/Fallou-Diouf/CurrencyVision.git
cd Currency_Vision


# 👤 Auteur
Fallou Diouf
