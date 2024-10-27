# Projet de Calcul des Caractéristiques d'un Avion Historique

Ce projet vise à calculer diverses caractéristiques aérodynamiques et de performance d'un avion historique, similaire au **Spirit of St. Louis**. Il suit une série d'étapes pour estimer des paramètres clés tels que la masse de carburant nécessaire, la puissance moteur requise, les dimensions de l'aile, etc.

## Table des matières

- [Introduction](#introduction)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Structure du Projet](#structure-du-projet)
- [Exemple de Fichier JSON](#exemple-de-fichier-json)
- [Calculs Effectués](#calculs-effectués)
- [Correspondance avec les Étapes de l'Exercice](#correspondance-avec-les-étapes-de-lexercice)
- [Licence](#licence)

## Introduction

Ce projet a pour objectif de répondre à une série de questions visant à dimensionner un avion de l'époque du **Spirit of St. Louis**. Il intègre des calculs pour estimer la masse de carburant, la puissance moteur, les dimensions de l'aile, les surfaces d'empennage, etc., en suivant les équations et méthodes présentées dans un cours spécifique (référencé par des équations telles que Eq. 9.1, Eq. 9.6, etc.).

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
   python main.py donnees_avion.json
   ```

3. **Consulter les résultats** :

   Le script affichera dans le terminal les résultats calculés, tels que la masse de carburant nécessaire, la puissance moteur requise, le nombre de Reynolds, la surface alaire nécessaire, les dimensions de l'aile, et les surfaces d'empennage.

## Structure du Projet

```
.
├── main.py                # Script principal pour exécuter les calculs
├── README.md              # Documentation du projet
└── donnees_avion.json     # Exemple de données JSON pour l'avion historique
```

## Exemple de Fichier JSON

Un fichier JSON doit être structuré comme suit :

```json
{
  "vitesse_vol": 70,               // Vitesse de vol en m/s
  "corde": 1.5,                    // Corde initiale de l'aile en m
  "densite_air": 1.225,            // Densité de l'air en kg/m³
  "masse_avion": 1200,             // Masse à vide de l'avion en kg
  "surface_alaire": 16,            // Surface alaire initiale en m²
  "finesse": 15,                   // Finesse de l'avion
  "rendement_helice": 0.85,        // Rendement de l'hélice (entre 0 et 1)
  "cz": 0.6,                       // Coefficient de portance
  "cx": 0.007,                     // Coefficient de traînée
  "rendement_moteur": 0.85,        // Rendement du moteur (entre 0 et 1)
  "pouvoir_calorifique": 43e6,     // Pouvoir calorifique du carburant en J/kg
  "temps_vol": 2.0,                // Temps de vol en heures
  "allongement": 6.0,              // Allongement de l'aile (rapport envergure²/surface)
  "coeff_empennage_h": 0.25,       // Coefficient pour l'empennage horizontal
  "coeff_empennage_v": 0.15        // Coefficient pour l'empennage vertical
}
```

### Champs requis :

- **`vitesse_vol`** : Vitesse de vol en **mètres par seconde (m/s)**.
- **`corde`** : Corde initiale de l'aile en **mètres (m)**.
- **`densite_air`** : Densité de l'air en **kilogrammes par mètre cube (kg/m³)**.
- **`masse_avion`** : Masse à vide de l'avion en **kilogrammes (kg)**.
- **`surface_alaire`** : Surface alaire initiale en **mètres carrés (m²)**.
- **`finesse`** : Finesse de l'avion (rapport portance/traînée).
- **`rendement_helice`** : Rendement de l’hélice (valeur entre 0 et 1).
- **`cz`** : Coefficient de portance.
- **`cx`** : Coefficient de traînée.
- **`rendement_moteur`** : Rendement du moteur (valeur entre 0 et 1).
- **`pouvoir_calorifique`** : Pouvoir calorifique du carburant en **joules par kilogramme (J/kg)**.
- **`temps_vol`** : Temps de vol en **heures (h)**.
- **`allongement`** : Allongement de l'aile (valeur positive).
- **`coeff_empennage_h`** : Coefficient pour l'empennage horizontal.
- **`coeff_empennage_v`** : Coefficient pour l'empennage vertical.

## Calculs Effectués

Le script suit une série d'étapes pour calculer les caractéristiques de l'avion :

### 1. **Hypothèse initiale sur la masse de carburant**

Une estimation initiale de la masse de carburant est faite (par exemple, 100 kg). Cette valeur sera ajustée lors des itérations pour converger vers une masse cohérente.

### 2. **Calcul des forces de portance et de traînée**

Utilise les coefficients de portance (`cz`) et de traînée (`cx`) pour calculer les forces correspondantes :

\[
F_{\text{portance}} = \frac{1}{2} \times \rho \times S \times C_z \times V^2
\]

\[
F_{\text{traînée}} = \frac{1}{2} \times \rho \times S \times C_x \times V^2
\]

### 3. **Calcul de la puissance moteur nécessaire**

La puissance nécessaire est calculée en utilisant la force de traînée et la vitesse de vol, en tenant compte du rendement du moteur :

\[
P_{\text{nécessaire}} = \frac{F_{\text{traînée}} \times V}{\eta_{\text{moteur}}}
\]

### 4. **Calcul de la masse de carburant nécessaire**

Utilise le pouvoir calorifique du carburant pour estimer la masse de carburant nécessaire pour le temps de vol spécifié :

\[
m_{\text{carburant}} = \frac{P_{\text{nécessaire}} \times t_{\text{vol}} \times 3600}{q_{\text{carburant}}}
\]

Où :

- \( P_{\text{nécessaire}} \) : Puissance en watts (W)
- \( t_{\text{vol}} \) : Temps de vol en heures (h)
- \( q_{\text{carburant}} \) : Pouvoir calorifique du carburant en J/kg

### 5. **Itération jusqu'à convergence de la masse de carburant**

Le calcul de la masse de carburant est itéré jusqu'à ce que la différence entre l'hypothèse précédente et la nouvelle valeur soit négligeable.

### 6. **Calcul du nombre de Reynolds**

Calculé à partir de la vitesse de vol, de la corde de l'aile et de la viscosité cinématique de l'air :

\[
\text{Re} = \frac{V \times C}{\nu}
\]

- \( \nu \) : Viscosité cinématique de l'air (15.68 × 10⁻⁶ m²/s à 15°C)

### 7. **Calcul de la surface alaire nécessaire**

Calcule la surface alaire minimale nécessaire pour générer la portance suffisante pour le poids total (masse de l'avion + masse de carburant) :

\[
S_{\text{nécessaire}} = \frac{2 \times m_{\text{total}} \times g}{\rho \times C_z \times V^2}
\]

- \( m_{\text{total}} \) : Masse totale de l'avion (masse à vide + masse de carburant)
- \( g \) : Accélération gravitationnelle (9.81 m/s²)

### 8. **Calcul des dimensions de l'aile**

Utilise l'allongement pour calculer l'envergure et la corde moyenne :

\[
b = \sqrt{A \times S}
\]

\[
C = \frac{S}{b}
\]

- \( A \) : Allongement de l'aile

### 9. **Calcul des surfaces d'empennage**

Calcule les surfaces de l'empennage horizontal et vertical en utilisant des coefficients proportionnels à la surface alaire :

\[
S_{\text{empennage\_h}} = k_h \times S
\]

\[
S_{\text{empennage\_v}} = k_v \times S
\]

- \( k_h \), \( k_v \) : Coefficients pour les empennages horizontal et vertical

## Correspondance avec les Étapes de l'Exercice

Le script correspond aux étapes suivantes :

1. **Choix d’un avion historique** : Les données du fichier JSON doivent refléter un avion de l'époque du **Spirit of St. Louis**.

2. **Choix d’une vitesse et d’un temps de trajet réaliste** : Les valeurs `vitesse_vol` et `temps_vol` sont définies en fonction des performances de l'avion et des capacités des pilotes.

3. **Hypothèse sur la masse de carburant et calcul de la puissance moteur** : Le script fait une hypothèse initiale sur la masse de carburant et calcule la puissance moteur nécessaire.

4. **Calcul de la masse minimale de carburant et convergence** : La masse de carburant est recalculée jusqu'à convergence.

5. **Choix d’un moteur d’époque** : Une fois la puissance moteur nécessaire calculée, vous pouvez choisir un moteur historique approprié.

6. **Calcul du nombre de Reynolds** : Calculé avec l'équation appropriée.

7. **Détermination du coefficient de portance** : Le coefficient de portance `cz` doit être déterminé selon la méthode proposée en Section 9.2 (à adapter si nécessaire).

8. **Calcul de la surface alaire** : Utilise l'équation (9.6) pour calculer la surface alaire nécessaire.

9. **Modification de l’envergure et de la corde** : Les dimensions de l'aile sont ajustées pour respecter la surface alaire nécessaire.

10. **Calcul de la géométrie de l’empennage et des ailerons** : Les surfaces d'empennage sont calculées à partir des ordres de grandeur donnés en Section 9.3.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
