import streamlit as st

# 1. Configuración de la página
st.set_page_config(
    page_title="Johanna Fuchs | Journalistin & Politikwissenschaftlerin",
    page_icon="🌍",
    layout="centered",
)

# 2. Estilos CSS personalizados para un look profesional y limpio
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    
    /* Clase para centrar la imagen de perfil y darle un borde circular */
    .centered-image {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 1.5rem;
    }
    .centered-image img {
        border-radius: 50%;
        border: 2px solid #374151;
        object-fit: cover;
    }

    /* Estilo moderno para los botones/enlaces */
    .stLinkButton > a {
        display: block;
        text-align: left !important;
        background-color: #1f2937;
        color: #ffffff !important;
        padding: 0.85rem 1rem;
        border-radius: 10px;
        font-weight: 500;
        border: 1px solid #374151;
        text-decoration: none;
        transition: all 0.3s ease;
    }
    .stLinkButton > a:hover {
        background-color: #3b82f6;
        border-color: #3b82f6;
        color: #ffffff !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 3. Cabecera con Imagen Centrada usando HTML nativo
avatar_url = "https://ugc.production.linktr.ee/7fef9bf1-1b6a-4ffb-967c-9f89e90ae0cb_images.jpeg?io=true&size=avatar-v3_0"

st.markdown(
    f"""
    <div class="centered-image">
        <img src="{avatar_url}" width="140" height="140" alt="Johanna Fuchs">
    </div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    "<h1 style='text-align: center; margin-bottom: 0;'>Johanna Fuchs</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; color: #9ca3af; font-size: 1.05rem;'>Journalistin und Politikwissenschaftlerin in Berlin, die Deutschland & Lateinamerika verbindet 🌍✍️</p>",
    unsafe_allow_html=True,
)

st.markdown("---")

# 4. Enlaces y Artículos reales
st.markdown("### 📰 Veröffentlichungen & Artikel")

articulos = [
    {
        "label": (
            "Immobilienspekulation vertreibt Kaffeeproduzent*innen (NPLA)"
        ),
        "url": "https://www.npla.de/thema/allgemein/immobilienspekulation-vertreibt-kaffeeproduzentinnen/",
    },
    {
        "label": (
            "Der Kampf um den Erhalt von Wasser in den mexikanischen"
            " Chinampas"
        ),
        "url": "https://www.npla.de/thema/umwelt-wirtschaft/der-kampf-um-den-erhalt-von-wasser-in-den-mexikanischen-chinampas/",
    },
    {
        "label": (
            "„Wertschätzen, was Leben in sich trägt“ – Lateinamerika"
            " Nachrichten"
        ),
        "url": "https://lateinamerika-nachrichten.de/artikel/wertschaetzen-was-leben-in-sich-traegt/",
    },
    {
        "label": "Guatemala – Palmöl raubt die heilige Erde | nd-aktuell.de",
        "url": "https://www.nd-aktuell.de/artikel/1194943.guatemala-palmoel-raubt-die-heilige-erde.html",
    },
    {
        "label": (
            "Honduras: Palmöl mit Blutspuren: Kleinbauern klagen deutsche"
            " Konzerne an (NPLA)"
        ),
        "url": "https://www.npla.de/thema/umwelt-wirtschaft/palmoel-honduras-lieferkettengesetz",
    },
    {
        "label": (
            "Landwirtschaft in Mexiko – Die letzten Äcker von Mexiko-Stadt |"
            " nd-aktuell.de"
        ),
        "url": "https://www.nd-aktuell.de/artikel/1193582.landwirtschaft-in-mexiko-die-letzten-aecker-von-mexiko-stadt.html",
    },
    {
        "label": (
            "Christopher Street Day – Pride Parade in Brandenburg: Regenbogenfahnen"
            " im Regio | nd-aktuell.de"
        ),
        "url": "https://www.nd-aktuell.de/artikel/1200791.christopher-street-day-pride-parade-in-brandenburg-regenbogenfahnen-im-regio.html",
    },
]

for item in articulos:
    st.link_button(item["label"], item["url"], use_container_width=True)

# 5. Pie de página
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #6b7280; font-size: 0.85rem;'>Erstellt mit Python & Streamlit ⚡</p>",
    unsafe_allow_html=True,
)