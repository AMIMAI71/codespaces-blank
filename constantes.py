SEXE = {1: 'Homme', 2: 'Femme'}
TRAJET = {0: 'Non renseigné', 1: 'Domicile travail', 2: 'Domicile école', 3: 'Courses Achat', 4: 'Utilisation professionnelle', 5: 'Promenade loisirs', 9: 'Autre'}
MOIS = {1: 'Janvier', 2: 'Fevrier', 3: 'Mars', 4: 'Avril', 5: 'Mai', 6: 'Juin', 7: 'Juillet', 8: 'Aout', 9: 'Septembre', 10: 'Octobre', 11: 'Novembre', 12: 'Decembre'}
CATEGORIES_VEHICULES = {
    '00': 'Indéterminable',
    '01': 'Bicyclette',
    '02': 'Cyclomoteur <50cm3',
    '03': 'Voiturette (Quadricycle à moteur carrossé) (anciennement "voiturette ou tricycle à moteur")',
    '04': 'Référence inutilisée depuis 2006 (scooter immatriculé)',
    '05': 'Référence inutilisée depuis 2006 (motocyclette)',
    '06': 'Référence inutilisée depuis 2006 (side-car)',
    '07': 'VL seul',
    '08': 'Référence inutilisée depuis 2006 (VL + caravane)',
    '09': 'Référence inutilisée depuis 2006 (VL + remorque)',
    '10': 'VU seul 1,5T <= PTAC <= 3,5T avec ou sans remorque (anciennement VU seul 1,5T <= PTAC <= 3,5T)',
    '11': 'Référence inutilisée depuis 2006 (VU (10) + caravane)',
    '12': 'Référence inutilisée depuis 2006 (VU (10) + remorque)',
    '13': 'PL seul 3,5T <PTCA <= 7,5T',
    '14': 'PL seul > 7,5T',
    '15': 'PL > 3,5T + remorque',
    '16': 'Tracteur routier seul',
    '17': 'Tracteur routier + semi-remorque',
    '18': 'Référence inutilisée depuis 2006 (transport en commun)',
    '19': 'Référence inutilisée depuis 2006 (tramway)',
    '20': 'Engin spécial',
    '21': 'Tracteur agricole',
    '30': 'Scooter < 50 cm3',
    '31': 'Motocyclette > 50 cm3 et <= 125 cm3',
    '32': 'Scooter > 50 cm3 et <= 125 cm3',
    '33': 'Motocyclette > 125 cm3',
    '34': 'Scooter > 125 cm3',
    '35': 'Quad léger <= 50 cm3 (Quadricycle à moteur non carrossé)',
    '36': 'Quad lourd > 50 cm3 (Quadricycle à moteur non carrossé)',
    '37': 'Autobus',
    '38': 'Autocar',
    '39': 'Train',
    '40': 'Tramway',
    '41': '3RM <= 50 cm3',
    '42': '3RM > 50 cm3 <= 125 cm3',
    '43': '3RM > 125 cm3',
    '50': 'EDP à moteur',
    '60': 'EDP sans moteur',
    '80': 'VAE',
    '99': 'Autre véhicule'
}

CATEGORIES_VEHICULES_GROUPE = {0: 'Indéterminable',
        1: 'Bicyclette',
        2: 'Cyclomoteur', 
        4: 'Cyclomoteur', 
        5: 'Cyclomoteur', 
        6: 'Cyclomoteur', 
        30: 'Cyclomoteur', 
        32: 'Cyclomoteur', 
        34: 'Cyclomoteur', 
        35: 'Cyclomoteur',
        31: 'Cyclomoteur', 
        33: 'Cyclomoteur', 
        3: 'Voiturette', 
        7: 'Véhicule Léger', 
        8: 'Véhicule Léger', 
        9: 'Véhicule Léger', 
        10: 'VU', 
        11: 'VU', 
        12: 'VU',
        13: 'PL',
        14: 'PL',
        15: 'PL',
        16: 'PL',
        17: 'PL',
        21: 'PL',
        15: 'PL',
        16: 'Tracteur',
        17: 'Tracteur',
        21: 'Tracteur',
        18: 'Transport en commun',
        37: 'Car',
        38: 'Car',
        35: 'Quad',
        36: 'Quad',
        19: 'Tramway',
        40: 'Tramway',
        20: 'Engin spécial',
        41: '3RM',
        42: '3RM',
        43: '3RM',
        50: 'EDP',
        60: 'EDP',
        80: 'VAE',
        99: 'Autre véhicule'
        }

ROUTE_TYPE = {
    1: 'Autoroute',
    2: 'Route nationale',
    3: 'Route Départementale',
    4: 'Voie Communales',
    5: 'Hors réseau public',
    6: 'Parc de stationnement ouvert à la circulation publique',
    7: 'Routes de métropole urbaine',
    9: 'autre'
}

DEPARTMENTS = {
    '01': 'Ain', 
    '02': 'Aisne', 
    '03': 'Allier', 
    '04': 'Alpes-de-Haute-Provence', 
    '05': 'Hautes-Alpes',
    '06': 'Alpes-Maritimes', 
    '07': 'Ardèche', 
    '08': 'Ardennes', 
    '09': 'Ariège', 
    '10': 'Aube', 
    '11': 'Aude',
    '12': 'Aveyron', 
    '13': 'Bouches-du-Rhône', 
    '14': 'Calvados', 
    '15': 'Cantal', 
    '16': 'Charente',
    '17': 'Charente-Maritime', 
    '18': 'Cher', 
    '19': 'Corrèze', 
    '2A': 'Corse-du-Sud', 
    '2B': 'Haute-Corse',
    '21': 'Côte-d\'Or', 
    '22': 'Côtes-d\'Armor', 
    '23': 'Creuse', 
    '24': 'Dordogne', 
    '25': 'Doubs', 
    '26': 'Drôme',
    '27': 'Eure', 
    '28': 'Eure-et-Loir', 
    '29': 'Finistère', 
    '30': 'Gard', 
    '31': 'Haute-Garonne', 
    '32': 'Gers',
    '33': 'Gironde', 
    '34': 'Hérault', 
    '35': 'Ille-et-Vilaine', 
    '36': 'Indre', 
    '37': 'Indre-et-Loire',
    '38': 'Isère', 
    '39': 'Jura', 
    '40': 'Landes', 
    '41': 'Loir-et-Cher', 
    '42': 'Loire', 
    '43': 'Haute-Loire',
    '44': 'Loire-Atlantique', 
    '45': 'Loiret', 
    '46': 'Lot', 
    '47': 'Lot-et-Garonne', 
    '48': 'Lozère',
    '49': 'Maine-et-Loire', 
    '50': 'Manche', 
    '51': 'Marne', 
    '52': 'Haute-Marne', 
    '53': 'Mayenne',
    '54': 'Meurthe-et-Moselle', 
    '55': 'Meuse', 
    '56': 'Morbihan', 
    '57': 'Moselle', 
    '58': 'Nièvre', 
    '59': 'Nord',
    '60': 'Oise', 
    '61': 'Orne', 
    '62': 'Pas-de-Calais', 
    '63': 'Puy-de-Dôme', 
    '64': 'Pyrénées-Atlantiques',
    '65': 'Hautes-Pyrénées', 
    '66': 'Pyrénées-Orientales', 
    '67': 'Bas-Rhin', 
    '68': 'Haut-Rhin', 
    '69': 'Rhône',
    '70': 'Haute-Saône', 
    '71': 'Saône-et-Loire', 
    '72': 'Sarthe', 
    '73': 'Savoie', 
    '74': 'Haute-Savoie',
    '75': 'Paris', 
    '76': 'Seine-Maritime', 
    '77': 'Seine-et-Marne', 
    '78': 'Yvelines', 
    '79': 'Deux-Sèvres',
    '80': 'Somme', 
    '81': 'Tarn', 
    '82': 'Tarn-et-Garonne', 
    '83': 'Var', 
    '84': 'Vaucluse', 
    '85': 'Vendée',
    '86': 'Vienne', 
    '87': 'Haute-Vienne', 
    '88': 'Vosges', 
    '89': 'Yonne', 
    '90': 'Territoire de Belfort',
    '91': 'Essonne', 
    '92': 'Hauts-de-Seine', 
    '93': 'Seine-Saint-Denis', 
    '94': 'Val-de-Marne', 
    '95': 'Val-d\'Oise',
    '971': 'Guadeloupe', 
    '972': 'Martinique', 
    '973': 'Guyane', 
    '974': 'La Réunion', 
    '976': 'Mayotte',
    '2A': 'Corse 2A',
    '2B': 'Corse 2B'
}
GRAVITE = { 1: 'Indemne',
2: 'Tué' ,
3: 'Blessé hospitalisé' ,
4: 'Blessé léger',
   
}
 
ATM = {
    -1:  'Non renseigné',
1: 'Normale ',
2: 'Pluie légère',
3: 'Pluie forte',
4: 'Neige - grêle',
5: 'Brouillard - fumée',
6: 'Vent fort - tempête',
7: 'Temps éblouissant',
8: 'Temps couvert',
9: 'Autre',
}
 
OBSM = {
-1: 'Non renseigné',
0: 'Aucun',
1: 'Piéton',
2: 'Véhicule',
4: 'Véhicule sur rail',
5: 'Animal domestique',
6: 'Animal sauvage',
9: 'Autre'
}

AGG = {
1: 'Hors agglomération ', 
2: 'En agglomération'
}

LUM = {
1: 'Plein jour',
2: 'Crépuscule ou aube',
3: 'Nuit sans éclairage public',
4: 'Nuit avec éclairage public non allumé',
5: 'Nuit avec éclairage public allumé'
}