import json

def charger_donnees(fichier_json):
    with open(fichier_json, 'r') as f:
        donnees = json.load(f)
    # Vérification des clés nécessaires
    cles_necessaires = [
        'vitesse_vol', 'corde', 'densite_air', 'masse_avion',
        'surface_alaire', 'finesse', 'rendement_helice', 'cz', 'cx',
        'rendement_moteur', 'pouvoir_calorifique', 'temps_vol',
        'allongement', 'coeff_empennage_h', 'coeff_empennage_v'
    ]
    for cle in cles_necessaires:
        if cle not in donnees:
            raise KeyError(f"La clé '{cle}' est manquante dans le fichier JSON.")
    return donnees

def calculer_reynolds(vitesse, corde, viscosite=15.68e-6):
    return (vitesse * corde) / viscosite

def calculer_forces(densite, surface, cz, cx, vitesse):
    force_portance = 0.5 * densite * surface * cz * vitesse**2
    force_trainee = 0.5 * densite * surface * cx * vitesse**2
    return force_portance, force_trainee

def calculer_puissance_necessaire(force_trainee, vitesse_vol, rendement_moteur, rendement_helice):
    return (force_trainee * vitesse_vol) / (rendement_moteur * rendement_helice)

def calculer_masse_carburant(puissance_necessaire, temps_vol, pouvoir_calorifique):
    return (puissance_necessaire * temps_vol * 3600) / pouvoir_calorifique

def calculer_surface_alaire(masse_totale, densite, cz, vitesse):
    return (2 * masse_totale * 9.81) / (densite * cz * vitesse**2)

def calculer_dimensions_aile(surface_alaire, allongement):
    envergure = (allongement * surface_alaire) ** 0.5
    corde = surface_alaire / envergure
    return envergure, corde

def calculer_surface_empennage(surface_alaire, coefficient):
    return coefficient * surface_alaire

def main(fichier_json):
    donnees = charger_donnees(fichier_json)

    # Masse initiale de carburant (hypothèse)
    masse_carburant = 100  # en kg, à ajuster

    convergence = False
    iteration = 0
    while not convergence and iteration < 10:
        iteration += 1
        masse_totale = donnees['masse_avion'] + masse_carburant

        # Calcul des forces
        force_portance, force_trainee = calculer_forces(
            donnees['densite_air'],
            donnees['surface_alaire'],
            donnees['cz'],
            donnees['cx'],
            donnees['vitesse_vol']
        )

        # Calcul de la puissance nécessaire
        puissance_necessaire = calculer_puissance_necessaire(
            force_trainee,
            donnees['vitesse_vol'],
            donnees['rendement_moteur'],
            donnees['rendement_helice']
        )

        # Calcul de la masse de carburant nécessaire
        masse_carburant_calculee = calculer_masse_carburant(
            puissance_necessaire,
            donnees['temps_vol'],
            donnees['pouvoir_calorifique']
        )

        # Vérification de la convergence
        if abs(masse_carburant - masse_carburant_calculee) < 1e-3:
            convergence = True
        else:
            masse_carburant = masse_carburant_calculee

    print(f"Masse de carburant nécessaire: {masse_carburant:.2f} kg")

    # Calcul du nombre de Reynolds
    reynolds = calculer_reynolds(donnees['vitesse_vol'], donnees['corde'])
    print(f"Nombre de Reynolds: {reynolds:.2e}")

    # Calcul de la surface alaire nécessaire
    surface_alaire_necessaire = calculer_surface_alaire(
        masse_totale,
        donnees['densite_air'],
        donnees['cz'],
        donnees['vitesse_vol']
    )
    print(f"Surface alaire nécessaire: {surface_alaire_necessaire:.2f} m²")

    # Calcul des dimensions de l'aile
    envergure, corde = calculer_dimensions_aile(
        surface_alaire_necessaire,
        donnees['allongement']
    )
    print(f"Envergure: {envergure:.2f} m, Corde moyenne: {corde:.2f} m")

    # Calcul des surfaces d'empennage
    surface_empennage_h = calculer_surface_empennage(
        surface_alaire_necessaire,
        donnees['coeff_empennage_h']
    )
    surface_empennage_v = calculer_surface_empennage(
        surface_alaire_necessaire,
        donnees['coeff_empennage_v']
    )
    print(f"Surface empennage horizontal: {surface_empennage_h:.2f} m²")
    print(f"Surface empennage vertical: {surface_empennage_v:.2f} m²")

if __name__ == "__main__":
    main('donnees_type_DR400.json')
