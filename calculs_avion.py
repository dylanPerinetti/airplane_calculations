import json
import math


# Chargement des données depuis les fichiers JSON
with open('avion_data.json', 'r') as fichier_avion:
    avion_data = json.load(fichier_avion)

with open('parametres.json', 'r') as fichier_parametres:
    parametres = json.load(fichier_parametres)


# Extraction des données de l'avion
nom_avion = avion_data['nom_de_l_avion']
masse_a_vide = avion_data['masse_a_vide']
masse_pilote = avion_data.get('masse_pilote', 0)
masse_charge_utile = avion_data.get('masse_charge_utile', 0)
P_m0 = avion_data['puissance_moteur_max']
V = avion_data['vitesse_croisiere']
lambda_aspect_ratio = avion_data['allongement']
f_tot = avion_data['finesse']
l_corde = avion_data['corde_moyenne']
S_alaire_estimee = avion_data['surface_alaire_estimee']
t_vol = avion_data['temps_vol']
C_z_fournie = avion_data['coefficient_portance_fournie']  # C_z fourni par PredimRC
nu_h = avion_data['rendement_helice']
nu_m = avion_data['rendement_moteur']


# Extraction des paramètres environnementaux
rho = parametres['densite_air']
nu_air = parametres['viscosite_air']
g = parametres['gravite']
PCI = parametres['pouvoir_calorifique']


# 1. Calcul de la puissance mécanique nécessaire en croisière (P_m)
pourcentage_P_m = 0.72  # 72% de la puissance maximale
P_m = pourcentage_P_m * P_m0  # en Watts

# 2. Calcul de la puissance chimique nécessaire (P_c)
P_c = P_m / nu_m

# 3. Calcul du débit massique de carburant (mpoint_c)
mpoint_c = P_m / (nu_h * nu_m * PCI)

# 4. Calcul de la masse totale de carburant (M_c) sur le temps de vol
M_c = mpoint_c * t_vol

# 5. Ajout d'une marge de 25% pour le décollage et la montée
M_c_total = M_c * 1.25

# 6. Calcul de la masse minimale de carburant à emporter (m_c_min)
K = g * V / (nu_h * nu_m * PCI * f_tot)
m_c_min = P_m0 / (K * nu_m * PCI) * (1 - math.exp(-K * t_vol))
m_c_min_total = m_c_min * 1.25  # Avec marge de 25%

# Calcul de la masse totale de l'avion
m = masse_a_vide + M_c_total + masse_pilote + masse_charge_utile

# 7. Calcul du nombre de Reynolds (Re)
Re = V * l_corde / nu_air

# 8. Calcul du coefficient de portance (C_z) en croisière
C_z_calculé = (2 * m * g) / (rho * S_alaire_estimee * V**2)

# 9. Calcul de la surface alaire requise (S_required) en utilisant le C_z calculé
S_required = (2 * m * g) / (rho * C_z_calculé * V**2)

# 10. Calcul de l'envergure (L) et de la corde moyenne (l)
L = math.sqrt(lambda_aspect_ratio * S_required)
l = S_required / L

# 11. Calcul de la géométrie de l'empennage et des ailerons
S_stab = 0.15 * S_required       # Surface du stabilisateur horizontal
S_deriv = 0.6 * S_stab           # Surface de la dérive verticale
S_ail = 0.1 * S_required         # Surface des ailerons
S_volets = 0.4 * S_stab          # Surface des volets mobiles
l_bras = 2.5 * l                 # Bras de levier du stabilisateur



# Affichage des résultats
print(f"Résultats des calculs pour l'avion ({nom_avion}):")
print("-----------------------------------------------------")
print(f"1. Puissance mécanique en croisière (P_m) : {P_m / 1000:.2f} kW")
print(f"2. Puissance chimique nécessaire (P_c) : {P_c / 1000:.2f} kW")
print(f"3. Débit massique de carburant (mpoint_c) : {mpoint_c:.4f} kg/s")
print(f"4. Masse totale de carburant (M_c) : {M_c:.2f} kg")
print(f"5. Masse totale de carburant avec marge (M_c_total) : {M_c_total:.2f} kg")
print(f"6. Masse minimale de carburant (m_c_min) : {m_c_min:.2f} kg")
print(f"   Masse minimale de carburant avec marge (m_c_min_total) : {m_c_min_total:.2f} kg")
print()
print("Total des masses :")
print(f" - Masse à vide : {masse_a_vide} kg")
print(f" - Masse du carburant (avec marge) : {M_c_total:.2f} kg")
print(f" - Masse du pilote : {masse_pilote} kg")
print(f" - Masse des charges utiles : {masse_charge_utile} kg")
print(f"= Masse totale de l'avion (m) : {m:.2f} kg")
print()
print(f"7. Nombre de Reynolds (Re) : {Re:.2e}")
print(f"8. Coefficient de portance (C_z) :")
print(f"   - C_z fourni par PredimRC : {C_z_fournie}")
print(f"   - C_z calculé pour la croisière : {C_z_calculé:.2f}")
print(f"9. Surface alaire requise (S_required) : {S_required:.2f} m^2")
print(f"10. Envergure (L) : {L:.2f} m")
print(f"    Corde moyenne (l) : {l:.2f} m")
print(f"11. Surface du stabilisateur horizontal (S_stab) : {S_stab:.2f} m^2")
print(f"    Surface de la dérive verticale (S_deriv) : {S_deriv:.2f} m^2")
print(f"    Surface des ailerons (S_ail) : {S_ail:.2f} m^2")
print(f"    Surface des volets mobiles (S_volets) : {S_volets:.2f} m^2")
print(f"    Bras de levier du stabilisateur (l_bras) : {l_bras:.2f} m")


# Écriture des résultats dans le fichier 'predim_Hughes_H-1_Racer.txt'
with open('predim_'+ nom_avion +'.txt', 'w', encoding='utf-8') as fichier_sortie:
    fichier_sortie.write("Résultats des calculs pour l'avion :\n")
    fichier_sortie.write("-------------------------------------\n")
    fichier_sortie.write(f"1. Puissance mécanique en croisière (Pₘ) : {P_m / 1000:.2f} kW\n")
    fichier_sortie.write(f"2. Puissance chimique nécessaire (P_c) : {P_c / 1000:.2f} kW\n")
    # Utilisation de ṁ_c avec le point au-dessus
    fichier_sortie.write(f"3. Débit massique de carburant (\u0307m_c) : {mpoint_c:.4f} kg/s\n")
    fichier_sortie.write(f"4. Masse totale de carburant (M_c) : {M_c:.2f} kg\n")
    fichier_sortie.write(f"5. Masse totale de carburant avec marge (M_c_total) : {M_c_total:.2f} kg\n")
    fichier_sortie.write(f"6. Masse minimale de carburant (m_c_min) : {m_c_min:.2f} kg\n")
    fichier_sortie.write(f"   Masse minimale de carburant avec marge (m_c_min_total) : {m_c_min_total:.2f} kg\n")
    fichier_sortie.write("\n")
    fichier_sortie.write("Total des masses :\n")
    fichier_sortie.write(f" - Masse à vide : {masse_a_vide} kg\n")
    fichier_sortie.write(f" - Masse du carburant (avec marge) : {M_c_total:.2f} kg\n")
    fichier_sortie.write(f" - Masse du pilote : {masse_pilote} kg\n")
    fichier_sortie.write(f" - Masse des charges utiles : {masse_charge_utile} kg\n")
    fichier_sortie.write(f"= Masse totale de l'avion (m) : {m:.2f} kg\n")
    fichier_sortie.write("\n")
    fichier_sortie.write(f"7. Nombre de Reynolds (Re) : {Re:.2e}\n")
    fichier_sortie.write(f"8. Coefficient de portance (C_z) :\n")
    fichier_sortie.write(f"   - C_z fourni par PredimRC : {C_z_fournie}\n")
    fichier_sortie.write(f"   - C_z calculé pour la croisière : {C_z_calculé:.2f}\n")
    fichier_sortie.write(f"9. Surface alaire requise (S) : {S_required:.2f} m²\n")
    fichier_sortie.write(f"10. Envergure (L) : {L:.2f} m\n")
    fichier_sortie.write(f"    Corde moyenne (l̄) : {l:.2f} m\n")
    fichier_sortie.write(f"11. Géométrie de l'empennage et des ailerons :\n")
    fichier_sortie.write(f"    - Surface du stabilisateur horizontal (S_h) : {S_stab:.2f} m²\n")
    fichier_sortie.write(f"    - Surface de la dérive verticale (S_v) : {S_deriv:.2f} m²\n")
    fichier_sortie.write(f"    - Surface des ailerons (S_a) : {S_ail:.2f} m²\n")
    fichier_sortie.write(f"    - Surface des volets mobiles (S_f) : {S_volets:.2f} m²\n")
    fichier_sortie.write(f"    - Bras de levier du stabilisateur (l_b) : {l_bras:.2f} m\n")