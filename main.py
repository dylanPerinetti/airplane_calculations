import json

def charger_donnees(fichier_json):
    with open(fichier_json, 'r') as f:
        donnees = json.load(f)
    # Vérification des clés nécessaires
    cles_necessaires = ['vitesse_vol', 'corde', 'densite_air', 'surface_alaire', 'masse_avion', 'finesse', 'rendement_helice', 'cz', 'cx']
    for cle in cles_necessaires:
        if cle not in donnees:
            raise KeyError(f"La clé '{cle}' est manquante dans le fichier JSON.")
    return donnees

def calculer_reynolds(vitesse, corde, viscosite=15.6e-6):
    return (vitesse * corde) / viscosite

def calculer_forces(densite, surface, cz, cx, vitesse):
    force_portance = 0.5 * densite * surface * cz * vitesse**2
    force_trainee = 0.5 * densite * surface * cx * vitesse**2
    return force_portance, force_trainee

def calculer_surface_alaire(masse, densite, cz, vitesse):
    return (2 * masse * 9.81) / (densite * cz * vitesse**2)

def calculer_puissance_moteur(masse, vitesse, finesse, rendement_helice):
    return (masse * 9.81 * vitesse) / (finesse * rendement_helice)

def main(fichier_json):
    donnees = charger_donnees(fichier_json)
    
    reynolds = calculer_reynolds(donnees['vitesse_vol'], donnees['corde'])
    print(f"Nombre de Reynolds: {reynolds:.2e}")
    
    force_portance, force_trainee = calculer_forces(
        donnees['densite_air'],
        donnees['surface_alaire'],
        donnees['cz'],
        donnees['cx'],
        donnees['vitesse_vol']
    )
    print(f"Force de portance: {force_portance:.2f} N")
    print(f"Force de traînée: {force_trainee:.2f} N")
    
    surface_alaire = calculer_surface_alaire(
        donnees['masse_avion'],
        donnees['densite_air'],
        donnees['cz'],
        donnees['vitesse_vol']
    )
    print(f"Surface alaire nécessaire: {surface_alaire:.2f} m²")
    
    puissance_moteur = calculer_puissance_moteur(
        donnees['masse_avion'],
        donnees['vitesse_vol'],
        donnees['finesse'],
        donnees['rendement_helice']
    )
    print(f"Puissance moteur nécessaire: {puissance_moteur:.2f} W")

if __name__ == "__main__":
    main('donnees_h1_racer.json')
