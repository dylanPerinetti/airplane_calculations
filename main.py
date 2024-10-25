import json
import math

# Charger les données depuis un fichier JSON
def charger_donnees(fichier_json):
    with open(fichier_json, 'r') as f:
        donnees = json.load(f)
    return donnees

# Calculer le nombre de Reynolds
def calculer_reynolds(vitesse, corde, viscosite=15.6e-6):
    return (vitesse * corde) / viscosite

# Calculer la force de portance et de traînée
def calculer_forces(densite, surface, cz, cx, vitesse):
    force_portance = 0.5 * densite * surface * cz * vitesse**2
    force_trainee = 0.5 * densite * surface * cx * vitesse**2
    return force_portance, force_trainee

# Calculer la surface alaire nécessaire
def calculer_surface_alaire(masse, densite, cz, vitesse):
    return (2 * masse * 9.81) / (densite * cz * vitesse**2)

# Calculer la puissance moteur
def calculer_puissance_moteur(masse, vitesse, finesse, rendement_helice):
    return (masse * 9.81 * vitesse) / (finesse * rendement_helice)

# Exécution du programme principal
def main(fichier_json):
    # Charger les données
    donnees = charger_donnees(fichier_json)
    
    # Calcul du nombre de Reynolds
    reynolds = calculer_reynolds(donnees['vitesse_vol'], donnees['corde'])
    print(f"Nombre de Reynolds: {reynolds}")
    
    # Calcul de la portance et de la traînée (utiliser des coefficients Cz et Cx exemples)
    cz, cx = 0.6, 0.007  # Valeurs de coefficient de portance et de traînée pour un profil donné
    force_portance, force_trainee = calculer_forces(donnees['densite_air'], donnees['surface_alaire'], cz, cx, donnees['vitesse_vol'])
    print(f"Force de portance: {force_portance} N, Force de traînée: {force_trainee} N")
    
    # Calcul de la surface alaire
    surface_alaire = calculer_surface_alaire(donnees['masse_avion'], donnees['densite_air'], cz, donnees['vitesse_vol'])
    print(f"Surface alaire nécessaire: {surface_alaire} m²")
    
    # Calcul de la puissance moteur
    puissance_moteur = calculer_puissance_moteur(donnees['masse_avion'], donnees['vitesse_vol'], donnees['finesse'], donnees['rendement_helice'])
    print(f"Puissance moteur nécessaire: {puissance_moteur} W")

# Appel de la fonction principale avec le fichier JSON contenant les données
main('donnees_h1_racer.json')
