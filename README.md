# Prédimensionnement d'un Avion Historique

Ce projet a pour objectif de **prédimensionner un avion historique** en automatisant les calculs nécessaires à l'aide d'un script Python. En se basant sur le célèbre **Hughes H-1 Racer**, le script calcule les caractéristiques principales de l'avion, telles que la puissance nécessaire, la masse de carburant, les dimensions de l'aile et de l'empennage, ainsi que des paramètres aérodynamiques essentiels.

## Table des matières

- [Introduction](#introduction)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Structure du Projet](#structure-du-projet)
- [Exemples de Fichiers JSON](#exemples-de-fichiers-json)
- [Calculs Effectués](#calculs-effectués)
- [Correspondance avec les Étapes de l'Exercice](#correspondance-avec-les-étapes-de-lexercice)
- [Résultats](#résultats)
- [Personnalisation](#personnalisation)
- [Contributions](#contributions)
- [Licence](#licence)

---

## Introduction

Le **Hughes H-1 Racer** est un avion emblématique des années 1930, connu pour ses performances exceptionnelles et ses avancées technologiques. Ce projet vise à recréer le processus de prédimensionnement de cet avion en utilisant des méthodes de calcul modernes et automatisées.

Le script Python fourni permet de :

- Calculer la puissance mécanique et chimique nécessaires en croisière.
- Estimer la masse totale de carburant requise, en incluant des marges pour le décollage et la montée.
- Déterminer les dimensions clés de l'avion : surface alaire, envergure, corde moyenne, surfaces d'empennage, etc.
- Calculer des paramètres aérodynamiques tels que le coefficient de portance et le nombre de Reynolds.
- Générer un rapport détaillé des résultats dans un fichier texte.

---

## Installation

1. **Cloner le dépôt :**

   ```bash
   git clone https://github.com/dylanPerinetti/airplane_calculations/
   cd airplane_calculations
   ```

2. **Vérifier l'environnement Python :**

   Assurez-vous d'avoir **Python 3** installé sur votre système.

3. **Installer les dépendances :**

   Aucune dépendance externe n'est requise. Le script utilise uniquement les bibliothèques standard de Python.

---

## Utilisation

1. **Préparer les fichiers de données :**

   - **`avion_data.json`** : Contient les données spécifiques à l'avion (exemple ci-dessous).
   - **`parametres.json`** : Contient les paramètres environnementaux et les constantes physiques (exemple ci-dessous).

2. **Exécuter le script principal :**

   ```bash
   python calculs_avion.py
   ```

   > **Note :** Le script doit être exécuté dans le même répertoire que les fichiers JSON.

3. **Consulter les résultats :**

   - Les résultats sont affichés dans le terminal.
   - Un fichier texte nommé `predim_<nom_de_l_avion>.txt` est généré, contenant un rapport détaillé des calculs.

---

## Structure du Projet

```
.
├── calculs_avion.py         # Script principal pour exécuter les calculs
├── avion_data.json          # Données spécifiques à l'avion
├── parametres.json          # Paramètres environnementaux et constantes physiques
├── predim_<nom_avion>.txt   # Rapport généré des résultats (après exécution)
├── README.md                # Documentation du projet
└── LICENSE                  # Licence du projet
```

---

## Exemples de Fichiers JSON

### `avion_data.json`

```json
{
    "nom_de_l_avion": "Hughes_H-1_Racer",
    "masse_a_vide": 1800,
    "masse_pilote": 80,
    "masse_charge_utile": 20,
    "puissance_moteur_max": 500000,
    "vitesse_croisiere": 111,
    "allongement": 7,
    "finesse": 8,
    "corde_moyenne": 1.8,
    "surface_alaire_estimee": 17,
    "temps_vol": 10800,
    "coefficient_portance_fournie": 0.55,
    "rendement_helice": 0.8,
    "rendement_moteur": 0.25
}
```

- **`nom_de_l_avion`** : Nom de l'avion.
- **`masse_a_vide`** : Masse à vide de l'avion en kg.
- **`masse_pilote`** : Masse du pilote en kg.
- **`masse_charge_utile`** : Masse des charges utiles en kg.
- **`puissance_moteur_max`** : Puissance maximale du moteur en Watts.
- **`vitesse_croisiere`** : Vitesse de croisière en m/s.
- **`allongement`** : Allongement de l'aile (rapport envergure²/surface alaire).
- **`finesse`** : Finesse totale de l'avion.
- **`corde_moyenne`** : Corde moyenne de l'aile en m.
- **`surface_alaire_estimee`** : Surface alaire estimée en m².
- **`temps_vol`** : Temps de vol en secondes.
- **`coefficient_portance_fournie`** : Coefficient de portance fourni (par exemple, par un logiciel comme PredimRC).
- **`rendement_helice`** : Rendement de l'hélice.
- **`rendement_moteur`** : Rendement du moteur.

### `parametres.json`

```json
{
    "densite_air": 1.2,
    "viscosite_air": 1.56e-5,
    "gravite": 9.81,
    "pouvoir_calorifique": 44000000
}
```

- **`densite_air`** : Densité de l'air en kg/m³.
- **`viscosite_air`** : Viscosité cinématique de l'air en m²/s.
- **`gravite`** : Accélération due à la gravité en m/s².
- **`pouvoir_calorifique`** : Pouvoir calorifique du carburant en J/kg.

---

## Calculs Effectués

Le script suit une série d'étapes pour calculer les caractéristiques de l'avion :

1. **Calcul de la puissance mécanique en croisière (\(P_m\)) :**

   \[
   P_m = \text{pourcentage}_{P_m} \times P_{m0}
   \]

   - \(\text{pourcentage}_{P_m} = 0.72\) (72 % de la puissance maximale).
   - \(P_{m0}\) : Puissance maximale du moteur.

2. **Calcul de la puissance chimique nécessaire (\(P_c\)) :**

   \[
   P_c = \frac{P_m}{\nu_m}
   \]

   - \(\nu_m\) : Rendement du moteur.

3. **Calcul du débit massique de carburant (\(\dot{m}_c\)) :**

   \[
   \dot{m}_c = \frac{P_m}{\nu_h \nu_m \text{PCI}}
   \]

   - \(\nu_h\) : Rendement de l'hélice.
   - \(\text{PCI}\) : Pouvoir calorifique du carburant.

4. **Calcul de la masse totale de carburant (\(M_c\)) :**

   \[
   M_c = \dot{m}_c \times t_{\text{vol}}
   \]

   - \(t_{\text{vol}}\) : Temps de vol en secondes.

5. **Ajout d'une marge pour le décollage et la montée :**

   \[
   M_c^{\text{total}} = M_c \times 1.25
   \]

   - Marge de 25 % ajoutée.

6. **Calcul de la masse minimale de carburant à emporter (\(m_c^{\text{min}}\)) :**

   \[
   m_c^{\text{min}} = \frac{P_{m0}}{K \nu_m \text{PCI}} \left(1 - e^{-K t_{\text{vol}}}\right)
   \]

   - \(K = \frac{g V}{\nu_h \nu_m \text{PCI} f_{\text{tot}}}\)
   - \(f_{\text{tot}}\) : Finesse totale.

7. **Calcul de la masse totale de l'avion (\(m\)) :**

   \[
   m = m_{\text{vide}} + M_c^{\text{total}} + m_{\text{pilote}} + m_{\text{charge\_utile}}
   \]

8. **Calcul du nombre de Reynolds (\(Re\)) :**

   \[
   Re = \frac{V \times l}{\nu_{\text{air}}}
   \]

   - \(l\) : Corde moyenne de l'aile.

9. **Calcul du coefficient de portance (\(C_z\)) :**

   \[
   C_z = \frac{2 m g}{\rho S V^2}
   \]

   - \(\rho\) : Densité de l'air.
   - \(S\) : Surface alaire estimée.

10. **Calcul de la surface alaire requise (\(S_{\text{required}}\)) :**

    \[
    S_{\text{required}} = \frac{2 m g}{\rho C_z V^2}
    \]

11. **Calcul de l'envergure (\(L\)) et de la corde moyenne (\(l\)) :**

    \[
    L = \sqrt{\lambda \times S_{\text{required}}}
    \]

    \[
    l = \frac{S_{\text{required}}}{L}
    \]

    - \(\lambda\) : Allongement de l'aile.

12. **Calcul de la géométrie de l'empennage et des ailerons :**

    - **Surface du stabilisateur horizontal (\(S_{\text{stab}}\)) :**

      \[
      S_{\text{stab}} = 0.15 \times S_{\text{required}}
      \]

    - **Surface de la dérive verticale (\(S_{\text{dériv}}\)) :**

      \[
      S_{\text{dériv}} = 0.6 \times S_{\text{stab}}
      \]

    - **Surface des ailerons (\(S_{\text{ail}}\)) :**

      \[
      S_{\text{ail}} = 0.1 \times S_{\text{required}}
      \]

    - **Surface des volets mobiles (\(S_{\text{volets}}\)) :**

      \[
      S_{\text{volets}} = 0.4 \times S_{\text{stab}}
      \]

    - **Bras de levier du stabilisateur (\(l_{\text{bras}}\)) :**

      \[
      l_{\text{bras}} = 2.5 \times l
      \]

---

## Correspondance avec les Étapes de l'Exercice

Le script couvre les étapes suivantes de l'exercice :

1. **Choix d'un avion historique :**

   - Utilisation du **Hughes H-1 Racer** comme référence.

2. **Détermination des performances :**

   - Vitesse de croisière et temps de vol réalistes basés sur les données historiques.

3. **Hypothèse sur la masse de carburant et calcul de la puissance moteur :**

   - Calculs détaillés de la puissance et de la masse de carburant.

4. **Calcul de la masse minimale de carburant à emporter :**

   - Utilisation de l'équation spécifique pour déterminer \(m_c^{\text{min}}\).

5. **Choix d'un moteur d'époque en fonction de la puissance calculée :**

   - Le moteur **Pratt & Whitney R-1535** correspond aux besoins en puissance.

6. **Calcul du nombre de Reynolds :**

   - Calculé pour caractériser l'écoulement autour de l'aile.

7. **Détermination du coefficient de portance et de l'angle de calage :**

   - Comparaison entre le \(C_z\) fourni et le \(C_z\) calculé.

8. **Calcul de la surface alaire :**

   - Détermination de la surface alaire requise pour soutenir la masse de l'avion.

9. **Modification de l'envergure et de la corde de l'aile :**

   - Ajustement des dimensions de l'aile en fonction de l'allongement.

10. **Calcul de la géométrie de l'empennage et des ailerons :**

    - Calcul des surfaces des stabilisateurs, dérives et ailerons selon des proportions standard.

---

## Résultats

Après exécution du script avec les données fournies, les résultats suivants sont obtenus :

```
Résultats des calculs pour l'avion (Hughes_H-1_Racer):
-----------------------------------------------------
1. Puissance mécanique en croisière (P_m) : 360.00 kW
2. Puissance chimique nécessaire (P_c) : 1440.00 kW
3. Débit massique de carburant (ṁ_c) : 0.0409 kg/s
4. Masse totale de carburant (M_c) : 442.09 kg
5. Masse totale de carburant avec marge (M_c_total) : 552.61 kg
6. Masse minimale de carburant (m_c_min) : 452.10 kg
   Masse minimale de carburant avec marge (m_c_min_total) : 565.12 kg

Total des masses :
 - Masse à vide : 1800 kg
 - Masse du carburant (avec marge) : 552.61 kg
 - Masse du pilote : 80 kg
 - Masse des charges utiles : 20 kg
= Masse totale de l'avion (m) : 2452.61 kg

7. Nombre de Reynolds (Re) : 1.28e+07
8. Coefficient de portance (C_z) :
   - C_z fourni par PredimRC : 0.55
   - C_z calculé pour la croisière : 0.20
9. Surface alaire requise (S) : 17.00 m²
10. Envergure (L) : 10.91 m
    Corde moyenne (l̄) : 1.56 m
11. Géométrie de l'empennage et des ailerons :
    - Surface du stabilisateur horizontal (S_h) : 2.55 m²
    - Surface de la dérive verticale (S_v) : 1.53 m²
    - Surface des ailerons (S_a) : 1.70 m²
    - Surface des volets mobiles (S_f) : 1.02 m²
    - Bras de levier du stabilisateur (l_b) : 3.90 m
```

Ces résultats confirment la cohérence des hypothèses de conception et sont en accord avec les performances historiques du **Hughes H-1 Racer**.

---

## Personnalisation

Pour adapter le script à un autre avion :

1. **Modifier `avion_data.json` :**

   - Remplacez les valeurs par celles correspondant à l'avion souhaité.
   - Assurez-vous que toutes les clés nécessaires sont présentes.

2. **Modifier `parametres.json` :**

   - Ajustez les paramètres environnementaux si nécessaire (par exemple, pour une altitude différente).

3. **Exécuter le script :**

   - Lancez `python calculs_avion.py` pour générer les nouveaux calculs.

---

## Contributions

Les contributions sont les bienvenues ! Si vous souhaitez améliorer le script, corriger des erreurs ou ajouter de nouvelles fonctionnalités, n'hésitez pas à :

- **Forker** le dépôt.
- **Créer une branche** pour vos modifications.
- **Soumettre une pull request** avec une description claire de vos changements.

---

## Licence

Ce projet est sous licence **MIT**. Consultez le fichier [LICENSE](LICENSE) pour plus de détails.

---

**Auteur :** Dylan PERINETTI

**Date :** 28 novembre 2024
