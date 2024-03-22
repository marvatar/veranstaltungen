import streamlit as st

import numpy as np
import pandas as pd

import os
from pathlib import Path

#################################################

@st.cache_data
def get_veranstaltungsliste() -> pd.DataFrame:
#    input_df = pd.read_excel("Veranstaltungen_v1.xlsx")
    input_df = pd.read_excel(Path.cwd() / "dash.xlsx")
    return input_df

#################################################

def main():
    b1, b2 = st.columns([1,3])
    with b1:
        st.image(str(Path.cwd() / "MSB_Logo_kurz.jpg"), width=100)
    with b2:    
        st.title("Veranstaltungen der STB München")

    st.divider()

    container01 = st.container(border=True)

    st.divider()

    container02 = st.container(border=True)

    st.divider()

    container03 = st.container(border=True, height=500)
    
#################################################

    try:
        base_df = get_veranstaltungsliste()
    except ImportError:
        data = {
            'Bibliothek' : ['Sendling', 'Bogenhausen', 'Giesing', 'Pasing'],
            'Veranstaltungsmerkmal' : ['offen', 'geschlossen', 'geschlossen', 'geschlossen'],
            'Teilnehmer gesamt' : [115,120,125,4],
        }
        base_df = pd.DataFrame(data)

    lst_stbs = base_df['Bibliothek'].unique()
    lst_stbs = np.append("Alle", lst_stbs)

    lst_vmss = base_df['Veranstaltungsmerkmal'].unique()
    lst_vmss = np.append("Alle", lst_vmss)

    lst_vmrh = base_df['Veranstaltungsreihe'].unique()
    lst_vmrh = np.append("Alle", lst_vmrh)

    
#################################################
    
    with container02:
        #slider_input = st.slider('My slider', 0, 10, 5, key='my_slider')

        #st.write(Path.cwd())
        
        #uploaded_file = st.file_uploader(
        #    label = "Datei auswählen",
        #    type = ['xlsx'],
        #)
        #if uploaded_file is not None:
        #    base_df = pd.read_excel(uploaded_file)
        #else:
                
        scol1, scol2, scol3 = st.columns(3)
        with scol1:
            select_stbs = st.selectbox('Stadtbibliothek auswählen', lst_stbs)

        with scol3:
            select_vmss = st.selectbox('Veranstaltungsmerkmal auswählen', lst_vmss)
            select_vmrh = st.selectbox('Veranstaltungsreihe auswählen', lst_vmrh)

        if select_stbs != "Alle":
            #st.write(f"{select_stbs}")
            df_show = base_df[base_df['Bibliothek'] == select_stbs]
        else:
            #st.write("Alle Anderen")
            df_show = base_df.copy()

        if select_vmss != "Alle":
            df_show = df_show[df_show['Veranstaltungsmerkmal'] == select_vmss]
        else:
            df_show = df_show.copy()

        if select_vmrh != "Alle":
            df_show = df_show[df_show['Veranstaltungsreihe'] == select_vmrh]
        else:
            df_show = df_show.copy()


        anz_vas = df_show.shape[0]
        anz_tns = df_show['Teilnehmer gesamt'].sum()
    
    with container03:
        st.dataframe(df_show)

    with container01:
        c1, c2, c3, c4, c5 = st.columns(5)
        with c2:
            st.metric(":ticket: **Anzahl Veranstaltungen** :ticket:", anz_vas)
        with c4:
            st.metric(":couple: :couple: **Anzahl Teilnehmer**", f"{anz_tns:.0f}")


#################################################

if __name__ == "__main__":
    st.set_page_config(
    page_title="Veranstaltungen der STB München",
    page_icon=":books:",
    layout="wide",

    )
    main()
