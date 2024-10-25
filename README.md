
# Projet de Calcul des Caractéristiques d'un Avion

Ce projet utilise Python pour calculer différentes caractéristiques aérodynamiques d’un avion en se basant sur des valeurs fournies dans un fichier JSON. Il permet, entre autres, de calculer le nombre de Reynolds, la portance, la traînée, la surface alaire nécessaire et la puissance moteur.

## Table des matières
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Structure du Projet](#structure-du-projet)
- [Exemple d'Entrée JSON](#exemple-dentrée-json)
- [Calculs Effectués](#calculs-effectués)
- [Licence](#licence)

## Installation

1. **Cloner le dépôt**:
   ```bash
   git clone https://github.com/dyanPerinetti/airplane_calculations.git
   cd airplane_calculations
   ```

2. **Installer les dépendances** (si applicable) :
   ```bash
   pip install -r requirements.txt
   ```

> Note : Le script utilise uniquement des bibliothèques standard de Python et ne nécessite donc aucune dépendance externe.

## Utilisation

1. Créez un fichier JSON avec les données de l’avion à analyser. Voir la section [Exemple d'Entrée JSON](#exemple-dentrée-json) pour un exemple.

2. Exécutez le script principal en passant le fichier JSON comme argument :
   ```bash
   python main.py donnees_h1_racer.json
   ```

3. Le script affichera dans le terminal les résultats calculés, tels que le nombre de Reynolds, les forces de portance et de traînée, la surface alaire nécessaire et la puissance moteur requise.

## Structure du Projet

```
.
├── main.py                # Script principal pour exécuter les calculs
├── README.md              # Documentation du projet
└── donnees_h1_racer.json  # Exemple de données JSON pour le H-1 Racer
```

## Exemple d'Entrée JSON

Un fichier JSON doit être structuré comme suit :

```json
{
  "vitesse_vol": 560,
  "distance_parcourue": 4800,
  "temps_vol": 6.5,
  "corde": 1.9,
  "densite_air": 1.225,
  "masse_avion": 2500,
  "surface_alaire": 14.6,
  "finesse": 10,
  "rendement_helice": 0.85
}
```

### Champs requis :
- `vitesse_vol` : Vitesse de vol en km/h.
- `distance_parcourue` : Distance totale parcourue en km.
- `temps_vol` : Temps total de vol en heures.
- `corde` : Longueur de la corde de l'aile en mètres.
- `densite_air` : Densité de l'air en kg/m³.
- `masse_avion` : Masse de l'avion en kg.
- `surface_alaire` : Surface de l'aile en m².
- `finesse` : Ratio de finesse de l'aile.
- `rendement_helice` : Rendement de l’hélice.

## Calculs Effectués

1. **Nombre de Reynolds** : Calculé à partir de la vitesse, la corde de l’aile et la viscosité de l’air.
2. **Portance et Traînée** : Forces calculées pour un profil d'aile donné.
3. **Surface Alaire** : Surface nécessaire pour obtenir la portance suffisante en vol.
4. **Puissance Moteur** : Estimation de la puissance moteur requise pour maintenir un vol constant.

Les résultats sont affichés dans le terminal et permettent d'évaluer les paramètres de prédimensionnement de l'avion choisi.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.