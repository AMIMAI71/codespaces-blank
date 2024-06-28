import pandas as pd
import streamlit as st

from constantes import ROUTE_TYPE, DEPARTMENTS
st.set_page_config(page_title="Carte Interactive", page_icon="🌍")

dataUsagers = pd.read_csv("datas/usagers.csv", sep=";")
dataVehicules = pd.read_csv("datas/vehicules.csv", sep=";")
dataLieux = pd.read_csv("datas/lieux.csv", sep=";")
dataCaracteristiques = pd.read_csv("datas/carcteristiques.csv", sep=";", decimal=',')

def get_day_of_week(date):
    days = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    return days[date.weekday()]

def add_all_option(options):
    options = ["Tous"] + options
    return options

st.header("Carte interactive de réparition des accidents corporels de la circulation routière")
col1, col2= st.columns(2)
with st.sidebar:
    on = st.sidebar.toggle("filter")
    #map interactive
    departments = sorted(DEPARTMENTS.values())
    departments = add_all_option(departments)
    selectedDep = st.selectbox(label="Département", options=departments)
    if selectedDep != "Tous":
        inversedDico = dict(map(reversed, DEPARTMENTS.items()))
        selectedDep = inversedDico[selectedDep]
        filteredCaracteristiques = dataCaracteristiques[dataCaracteristiques['dep'] == selectedDep]
    else:
        filteredCaracteristiques = dataCaracteristiques

    conditionsAtomospheriques = sorted(dataCaracteristiques["atm"].unique())
    conditionsAtomospheriques = add_all_option(conditionsAtomospheriques)
    conditionAtmospheriqueSelected = st.sidebar.selectbox(label="Condition athmosphérique", options = conditionsAtomospheriques)
    if conditionAtmospheriqueSelected != "Tous":
        filteredCaracteristiques = filteredCaracteristiques[filteredCaracteristiques["atm"] == conditionAtmospheriqueSelected]
        
    conditionsEclairages = sorted(dataCaracteristiques["lum"].unique())
    conditionsEclairages = add_all_option(conditionsEclairages)
    conditionEclairageSelected = st.sidebar.selectbox(label="Luminosité", options = conditionsEclairages)
    if conditionEclairageSelected != "Tous":
        filteredCaracteristiques = filteredCaracteristiques[filteredCaracteristiques["lum"] == conditionEclairageSelected]

    localisation = sorted(dataCaracteristiques["agg"].unique())
    localisation = add_all_option(localisation)
    localisationSelected = st.sidebar.selectbox(label="Localisation", options = localisation)
    if localisationSelected != "Tous":
        filteredCaracteristiques = filteredCaracteristiques[filteredCaracteristiques["lum"] == localisationSelected]

    colisions = sorted(dataCaracteristiques["col"].unique())
    colisions = add_all_option(colisions)
    typeColision = st.selectbox(label="Colision", options = colisions)
    if typeColision != "Tous":
        filteredCaracteristiques = filteredCaracteristiques[filteredCaracteristiques["col"] == typeColision]

    categories = sorted(ROUTE_TYPE.values())
    categories = add_all_option(categories)
    selectedCategorieRoute = st.selectbox(label="Catégorie de route", options=categories)
    if selectedCategorieRoute != "Tous":
        inversedDico = dict(map(reversed, ROUTE_TYPE.items()))
        selectedCategorieRoute = inversedDico[selectedCategorieRoute]
        filteredLieuxByCatr = dataLieux[dataLieux['catr'] == selectedCategorieRoute]
    else:
        filteredLieuxByCatr = dataLieux

    dataJoinedAndFiltered = filteredCaracteristiques.join(filteredLieuxByCatr, how="inner")
        
#Le nombre d'accidents.
nombreaccidentvehicule = filteredCaracteristiques['Accident_Id'].nunique()

#Le nombre de véhicules impliqués.
joined_df = filteredCaracteristiques.join(dataVehicules.set_index('Num_Acc'), on='Accident_Id')
nombrevehiculeimpliquedyna = joined_df['id_vehicule'].nunique()

#Le nombre d'usagers impliqués.
joined_df = filteredCaracteristiques.join(dataUsagers.set_index('Num_Acc'), on='Accident_Id')
nombreusagerimplique = joined_df['id_usager'].nunique()

#Le nombre de décès.
joined_df = filteredCaracteristiques.join(dataUsagers.set_index('Num_Acc'), on= 'Accident_Id')
nombredecesjoin= len(joined_df[joined_df['grav'] == 2])

#Le taux de létalité.
letalite = (nombredecesjoin/nombreaccidentvehicule)*100
letalite_formate = f"{letalite:.2f}%"
dataPosition = filteredCaracteristiques[['lat','long']]

col1, col2, col3, col4, col5= st.columns([2,3,3,2,3])
col1.metric(label="🚧Nombre accident", value= nombreaccidentvehicule)
col2.metric(label="🚗Nombre de vehicule implique", value= nombrevehiculeimpliquedyna)
col3.metric(label="🧍Nombre d'usager impliqué", value= nombreusagerimplique)
col4.metric(label="💀Nombre de décès", value= nombredecesjoin)
col5.metric(label="⚰️Taux de létalité", value= letalite_formate)


df = pd.DataFrame({
    "col1": dataPosition['lat'],
    "col2": dataPosition['long']
})
st.map(df, latitude="col1", longitude="col2")