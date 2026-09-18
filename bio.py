import streamlit as st

# 1. Configuración de la página
st.set_page_config(
    page_title="Johanna Fuchs | Journalistin & Politikwissenschaftlerin",
    page_icon="🌍",
    layout="centered",
)

# 2. Estilos CSS con textura de papel real de fondo
st.markdown(
    """
    <style>
    /* Fondo con textura real de papel / pergamino sutil */
    .stApp {
        background-color: #f4f1ea;
        background-image: url("https://www.transparenttextures.com/patterns/textured-paper.png");
        color: #262626;
    }
    
    /* Contenedor central de la imagen de perfil */
    .centered-image {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 1.5rem;
    }
    .centered-image img {
        border-radius: 50%;
        width: 130px;
        height: 130px;
        object-fit: cover;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.12);
        border: 3px solid #ffffff;
    }

    /* Estilo de botones minimalistas tipo píldora */
    .stLinkButton > a {
        display: block;
        text-align: center !important;
        background-color: #ffffff;
        color: #222222 !important;
        padding: 1rem 1.25rem;
        border-radius: 9999px; /* Bordes totalmente redondeados tipo píldora */
        font-weight: 500;
        border: 1px solid #e0d7cc;
        text-decoration: none;
        box-shadow: 0 4px 12px 0 rgba(0, 0, 0, 0.04);
        transition: all 0.2s ease;
        margin-bottom: 0.75rem;
    }
    .stLinkButton > a:hover {
        background-color: #1a1a1a;
        color: #ffffff !important;
        border-color: #1a1a1a;
        transform: translateY(-2px);
        box-shadow: 0 6px 16px -2px rgba(0, 0, 0, 0.15);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 3. Cabecera con Imagen Centrada
avatar_url = "https://ugc.production.linktr.ee/7fef9bf1-1b6a-4ffb-967c-9f89e90ae0cb_images.jpeg?io=true&size=avatar-v3_0"

st.markdown(
    f"""
    <div class="centered-image">
        <img src="{avatar_url}" alt="Johanna Fuchs">
    </div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    "<h1 style='text-align: center; color: #1a1a1a; font-size: 1.8rem; font-weight: 700; margin-bottom: 0.2rem;'>Johanna Fuchs</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; color: #595959; font-size: 1rem; margin-bottom: 2rem;'>Journalistin und Politikwissenschaftlerin in Berlin, die Deutschland & Lateinamerika verbindet 🌍✍️</p>",
    unsafe_allow_html=True,
)

# 4. Enlaces y Artículos
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
    "<p style='text-align: center; color: #8c8c8c; font-size: 0.85rem;'>Erstellt mit Python & Streamlit ⚡</p>",
    unsafe_allow_html=True,
)
