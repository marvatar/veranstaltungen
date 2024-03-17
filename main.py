import streamlit as st

import numpy as np
import pandas as pd

#################################################

@st.cache_data
def get_veranstaltungsliste() -> pd.DataFrame:
    input_df = pd.read_excel("Veranstaltungen_v1.xlsx")
    return input_df

#################################################

def main():
    st.title("Veranstaltungen der STB München")

    st.divider()

    container01 = st.container(border=True)

    st.divider()

    container02 = st.container(border=True)

#################################################

    base_df = get_veranstaltungsliste()

    with container02:
        #slider_input = st.slider('My slider', 0, 10, 5, key='my_slider')
        lst_stbs = base_df['Bibliothek'].unique()
        lst_stbs = np.append("Alle", lst_stbs)

        select_stbs = st.selectbox('Stadtbibliothek auswählen', lst_stbs)

        if select_stbs != "Alle":
            #st.write(f"{select_stbs}")
            df_show = base_df[base_df['Bibliothek'] == select_stbs]
        else:
            st.write("Alle Anderen")
            df_show = base_df.copy()

        anz_vas = df_show.shape[0]
        anz_tns = df_show['Teilnehmer gesamt'].sum()

        st.write(df_show)

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
    page_icon="👋",
    layout="wide",

    )
    main()