# Projet de Calcul des Caractéristiques d'un Avion

Ce projet utilise Python pour calculer différentes caractéristiques aérodynamiques d’un avion en se basant sur des valeurs fournies dans un fichier JSON. Il permet, entre autres, de calculer le nombre de Reynolds, la portance, la traînée, la surface alaire nécessaire et la puissance moteur.

## Table des matières
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Structure du Projet](#structure-du-projet)
- [Exemple de Fichier JSON](#exemple-de-fichier-json)
- [Calculs Effectués](#calculs-effectués)
- [Licence](#licence)

## Installation

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/dyanPerinetti/airplane_calculations.git
   cd airplane_calculations
   ```

2. **Installer les dépendances** (si applicable) :
   ```bash
   pip install -r requirements.txt
   ```

> **Note** : Le script utilise uniquement des bibliothèques standard de Python et ne nécessite donc aucune dépendance externe.

## Utilisation

1. **Préparer le fichier JSON** :

   Créez un fichier JSON avec les données de l’avion à analyser. Voir la section [Exemple de Fichier JSON](#exemple-de-fichier-json) pour un exemple.

2. **Exécuter le script principal** :

   ```bash
   python main.py donnees_h1_racer.json
   ```

3. **Consulter les résultats** :

   Le script affichera dans le terminal les résultats calculés, tels que le nombre de Reynolds, les forces de portance et de traînée, la surface alaire nécessaire et la puissance moteur requise.

## Structure du Projet

```
.
├── main.py                # Script principal pour exécuter les calculs
├── README.md              # Documentation du projet
└── donnees_h1_racer.json  # Exemple de données JSON pour le H-1 Racer
```

## Exemple de Fichier JSON

Un fichier JSON doit être structuré comme suit :

```json
{
  "vitesse_vol": 70,
  "corde": 1.5,
  "densite_air": 1.225,
  "masse_avion": 1200,
  "surface_alaire": 16,
  "finesse": 15,
  "rendement_helice": 0.85,
  "cz": 0.6,
  "cx": 0.007
}
```

### Champs requis :

- `vitesse_vol` : Vitesse de vol en **mètres par seconde (m/s)**.
- `corde` : Longueur de la corde de l'aile en **mètres (m)**.
- `densite_air` : Densité de l'air en **kilogrammes par mètre cube (kg/m³)**.
- `masse_avion` : Masse de l'avion en **kilogrammes (kg)**.
- `surface_alaire` : Surface de l'aile en **mètres carrés (m²)**.
- `finesse` : Finesse de l'aile (rapport portance/traînée).
- `rendement_helice` : Rendement de l’hélice (valeur entre 0 et 1).
- `cz` : Coefficient de portance.
- `cx` : Coefficient de traînée.

## Calculs Effectués

1. **Nombre de Reynolds** : Calculé à partir de la vitesse de vol, de la corde de l’aile et de la viscosité cinématique de l’air.
   \[
   \text{Re} = \frac{V \times C}{\nu}
   \]
   - \( V \) : Vitesse de vol (m/s)
   - \( C \) : Corde de l'aile (m)
   - \( \nu \) : Viscosité cinématique de l'air (m²/s)

2. **Portance et Traînée** : Forces calculées à partir des coefficients aérodynamiques.
   \[
   F_{\text{portance}} = \frac{1}{2} \times \rho \times S \times C_z \times V^2
   \]
   \[
   F_{\text{traînée}} = \frac{1}{2} \times \rho \times S \times C_x \times V^2
   \]
   - \( \rho \) : Densité de l'air (kg/m³)
   - \( S \) : Surface alaire (m²)
   - \( C_z \), \( C_x \) : Coefficients de portance et de traînée
   - \( V \) : Vitesse de vol (m/s)

3. **Surface Alaire Nécessaire** : Surface requise pour obtenir la portance suffisante en vol.
   \[
   S = \frac{2 \times m \times g}{\rho \times C_z \times V^2}
   \]
   - \( m \) : Masse de l'avion (kg)
   - \( g \) : Accélération due à la gravité (9.81 m/s²)

4. **Puissance Moteur** : Estimation de la puissance moteur requise pour maintenir un vol constant.
   \[
   P = \frac{m \times g \times V}{\text{finesse} \times \text{rendement hélice}}
   \]

Les résultats sont affichés dans le terminal et permettent d'évaluer les paramètres de prédimensionnement de l'avion choisi.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
