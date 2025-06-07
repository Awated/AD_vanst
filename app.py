import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_authenticator import Authenticate


st.set_page_config(
    layout="centered", initial_sidebar_state="expanded"
)

# Nos données utilisateurs doivent respecter ce format
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'administrateur'
        }
    }
}

authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "cookie name",         # Le nom du cookie, un str quelconque
    "cookie key",          # La clé du cookie, un str quelconque
    30,                    # Le nombre de jours avant que le cookie expire
)


user_name = lesDonneesDesComptes['usernames']['root']['name']
authenticator.login()


def accueil():

    if st.session_state["authentication_status"]:
        st.subheader("Bienvenue sur le contenu réservé aux utilisateurs connectés")
        # On affiche un menu DANS la barre latérale (sidebar)
        with st.sidebar:
            # Creation du bouton deconnexion
            authenticator.logout("Déconnexion")

            st.write(f"Bienvenue ***{user_name}***")

            selected = option_menu(
                menu_title=None,
                options=["Accueil", "Photos"],
                icons=["house", "image"],  # facultatif
                menu_icon="cast",          # facultatif
                default_index=0
                )

        if selected == "Accueil":
            st.header("***Bienvenue sur ma page citronnée!***")
            st.image("https://www.bioceno.be/wp-content/uploads/2019/11/citrons-3.jpg")
        elif selected == "Photos":
            st.header("***Bienvenue sur mon album photo***")
            # Création de 3 colonnes
            col1, col2, col3 = st.columns(3)

            # Contenu de la première colonne :
            with col1:
                st.subheader("Le chat ")
                st.image("https://static.streamlit.io/examples/cat.jpg")

            # Contenu de la deuxième colonne :
            with col2:
                st.subheader("Ce chien")
                st.image("https://static.streamlit.io/examples/dog.jpg")

            # Contenu de la troisième colonne :
            with col3:
                st.subheader("Chouette!")
                st.image("https://static.streamlit.io/examples/owl.jpg")
                # Le bouton de déconnexion

    elif st.session_state["authentication_status"] is False:
        st.error("L'username ou le password est/sont incorrect")
    elif st.session_state["authentication_status"] is None:
        st.warning('Les champs username et mot de passe doivent être remplie')


accueil()

# FIN
