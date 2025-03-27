import streamlit as st


# ------------------------- Initialisierung der Session-State-Variablen ------------------------------
if 'gewaehlteLKs' not in st.session_state:
    st.session_state.gewaehlteLKs = []

if 'gewaehlteGKs' not in st.session_state:
    st.session_state.gewaehlteGKs = []

if 'möglicheLKs' not in st.session_state:
    st.session_state.möglicheLKs = [
        "Biologie", "Deutsch", "Geschichte", "Informatik", "Englisch",
        "Geographie", "Mathematik", "Politik", "Physik",
    ]

if 'möglicheGKs' not in st.session_state:
    st.session_state.möglicheGKs = [
        "Deutsch", "Englisch",
        "Geschichte", "Geographie", "Politik", "Religion",
        "Mathematik", "Physik", "Chemie", "Biologie", "Informatik"
    ]

if 'pflicht_LK' not in st.session_state:
    st.session_state.pflicht_LK = [
        "Deutsch",
        "Mathematik",
        "Biologie",
        "Physik",
    ]

if 'pflicht_GK' not in st.session_state:
    st.session_state.pflicht_GK = [
        "Deutsch",
        "Englisch", 
        "Geschichte",
        "Mathematik", 
        "Religion",
        "Sport",
        "Projektarbeit"
        # Künstlerisches Fach, (DSP, Kunst oder Musik)
        # WSL Fach (Physik Chemie oder Biologie)
    ]

if 'gesamtstunden' not in st.session_state:
    st.session_state.gesamtstunden = 0
    
if 'vorherige_faecher_abgeschlossen' not in st.session_state:
    st.session_state.vorherige_faecher_abgeschlossen = False

# Adding a new session state to store subject hours when added
if 'gewaehlteGKs_mit_stunden' not in st.session_state:
    st.session_state.gewaehlteGKs_mit_stunden = {}

if 'gewaehlteLKs_mit_stunden' not in st.session_state:
    st.session_state.gewaehlteLKs_mit_stunden = {}




# --------------------------------------------- Listen -----------------------------------------
# Alle verfügbaren Fächer
alle_faecher = {
    # Sprachfächer (muttersprachlich/Fremdsprachen)
    "Deutsch": 3,
    "Englisch": 3,
    "Französisch": 3,
    "Latein": 3,
    "Spanisch": 3,
    "Spanisch für Neueinsteiger": 4,
    
    # Künstlerische Fächer
    "DSP": 3,
    "Kunst": 3,
    "Musik": 3,
    
    # Gesellschaftswissenschaften
    "Geschichte": 3,
    "Geographie": 3,
    "Politik": 3,
    "Religion": 3,
    
    # MINT-Fächer
    "Mathematik": 3,
    "Physik": 3,
    "Chemie": 3,
    "Biologie": 3,
    "Informatik": 3,
    
    # Praxis/Spezialfächer
    "Sport": 2,
    "Projektarbeit": 2
}


# Pflicht falls LK1 Physik oder Biologie
lk1phybio = [
    "Deutsch",
    "Englisch",
    "Mathematik",
    "Geschichte",
    "Politik",
    "Geographie"
]



# --------------------------------------------- Funktionen -----------------------------------------

# Fächerabfrage
def waehle_vorherige_faecher():
    st.info("Bitte wählen Sie die Fächer aus, die Sie vorher belegt haben. Diese Informationen beeinflussen Ihre möglichen Kurswahlen.")
    
    Fremdsprache = st.selectbox("Welche zweite Fremdsprache hatten Sie von der 6. bis zur 9. Klasse?", ["Französisch", "Latein", "Spanisch", "Keine"])
    
    # Auswahl der Künstlerischen Fächer
    kuenstlerisches_fach = st.selectbox("Welches künstlerische Fach hatten Sie in der 10. Klasse?", ["DSP", "Kunst", "Musik"])
    
    
    if st.button("Weiter zu den Leistungskursen"):
        # Update der möglichen Fremdsprachen
        if Fremdsprache == "Keine":
            st.session_state.gewaehlteGKs.append("Spanisch für Neueinsteiger")
            st.session_state.gewaehlteGKs_mit_stunden["Spanisch für Neueinsteiger"] = "4h"
            st.session_state.gesamtstunden += 4
        if Fremdsprache == "Französisch":
            st.session_state.möglicheLKs.append("Französisch")
            st.session_state.möglicheGKs.append("Französisch")
            st.session_state.pflicht_LK.append("Französisch")
        if Fremdsprache == "Latein":
            st.session_state.möglicheLKs.append("Latein")
            st.session_state.möglicheGKs.append("Latein")
            st.session_state.pflicht_LK.append("Latein")
        if Fremdsprache == "Spanisch":
            st.session_state.möglicheGKs.append("Spanisch")


        # Update der möglichen Künstlerischen Fächer
        if kuenstlerisches_fach == "DSP":        
            st.session_state.pflicht_GK.append("DSP")
        if kuenstlerisches_fach == "Kunst":
            st.session_state.möglicheLKs.append("Kunst")
            st.session_state.möglicheGKs.append("Kunst")
            st.session_state.pflicht_GK.append("Kunst")
        if kuenstlerisches_fach == "Musik":
            st.session_state.möglicheLKs.append("Musik")
            st.session_state.möglicheGKs.append("Musik")
            st.session_state.pflicht_GK.append("Musik")

        
        st.session_state.vorherige_faecher_abgeschlossen = True
        st.rerun()

# Funktion zur Auswahl der Leistungskurse
def waehle_leistungskurse():

    # Auswahl des ersten LKs (Pflicht LK)
    if len(st.session_state.gewaehlteLKs) == 0:
        st.info("Wählen Sie Ihre Leistungskurse aus. Sie müssen drei Leistungskurse belegen, die jeweils 5 Wochenstunden umfassen.")
        lk1 = st.selectbox("Leistungskurs 1", st.session_state.pflicht_LK)

        if st.button("Bestätigen", key="button_lk1"):
            st.session_state.gewaehlteLKs.append(lk1)
            st.session_state.gewaehlteLKs_mit_stunden[lk1] = "5h"
            st.session_state.gesamtstunden += 5
            if lk1 in ["Französisch", "Latein", "Musik"]:
                if "Französisch" in st.session_state.möglicheLKs:
                    st.session_state.möglicheLKs.remove("Französisch")
                if "Latein" in st.session_state.möglicheLKs:
                    st.session_state.möglicheLKs.remove("Latein")
                if "Musik" in st.session_state.möglicheLKs:
                    st.session_state.möglicheLKs.remove("Musik")
            else: 
                st.session_state.möglicheLKs.remove(lk1)
            st.rerun()
    
    # Auswahl des zweiten LKs
    elif len(st.session_state.gewaehlteLKs) == 1:
        
        if st.session_state.gewaehlteLKs[0] in ["Biologie", "Physik"]:
            st.info("Da Sie Biologie oder Physik als ersten Leistungskurs gewählt haben, müssen Sie einen der folgenden Leistungskurse wählen:")
            lk2 = st.selectbox("Leistungskurs 2", lk1phybio)
        else:
            lk2 = st.selectbox("Leistungskurs 2", st.session_state.möglicheLKs)

        if st.button("Bestätigen", key="button_lk2"):
            st.session_state.gewaehlteLKs.append(lk2)
            st.session_state.gewaehlteLKs_mit_stunden[lk2] = "5h"
            st.session_state.gesamtstunden += 5
            if lk2 in ["Französisch", "Latein", "Musik"]:
                if "Französisch" in st.session_state.möglicheLKs:
                    st.session_state.möglicheLKs.remove("Französisch")
                if "Latein" in st.session_state.möglicheLKs:
                    st.session_state.möglicheLKs.remove("Latein")
                if "Musik" in st.session_state.möglicheLKs:
                    st.session_state.möglicheLKs.remove("Musik")
            else:
                st.session_state.möglicheLKs.remove(lk2)
            st.rerun()

    # Auswahl des dritten LKs
    elif len(st.session_state.gewaehlteLKs) == 2:
        st.info("Wählen Sie Ihren dritten Leistungskurs aus den verbleibenden Fächern.")
        
        lk3 = st.selectbox("Leistungskurs 3", st.session_state.möglicheLKs)

        if st.button("Bestätigen", key="button_lk3"):
            st.session_state.gewaehlteLKs.append(lk3)
            st.session_state.gewaehlteLKs_mit_stunden[lk3] = "5h"
            st.session_state.gesamtstunden += 5
            if lk3 in ["Französisch", "Latein", "Musik"]:
                if "Französisch" in st.session_state.möglicheLKs:
                    st.session_state.möglicheLKs.remove("Französisch")
                if "Latein" in st.session_state.möglicheLKs:
                    st.session_state.möglicheLKs.remove("Latein")
                if "Musik" in st.session_state.möglicheLKs:
                    st.session_state.möglicheLKs.remove("Musik")
            else:
                st.session_state.möglicheLKs.remove(lk3)
            st.rerun()


# Funktion zur Auswahl der Grundkurse
def waehle_grundkurse():
    st.info("Wählen Sie Ihre Grundkurse aus. Beachten Sie, dass Sie mindestens 34 Wochenstunden erreichen müssen.")
    
    for sub in st.session_state.pflicht_GK:
        if sub not in st.session_state.gewaehlteLKs and sub not in st.session_state.gewaehlteGKs:
            st.session_state.gewaehlteGKs.append(sub)
            st.session_state.gewaehlteGKs_mit_stunden[sub] = f"{alle_faecher[sub]}h"
            st.session_state.gesamtstunden += alle_faecher[sub]
            if sub in st.session_state.möglicheGKs:
                st.session_state.möglicheGKs.remove(sub)
    
    # Update der möglichen Grundkurse
    for sub in st.session_state.möglicheGKs:
        if sub in st.session_state.gewaehlteGKs or sub in st.session_state.gewaehlteLKs:
            st.session_state.möglicheGKs.remove(sub)
    


    # Auswahl der Grundkurse
    gk = st.selectbox("Grundkurse", st.session_state.möglicheGKs)
    if st.button("Bestätigen", key="button_gk"):
        if st.session_state.gesamtstunden + alle_faecher[gk] <= 38:
            st.session_state.gewaehlteGKs.append(gk)
            st.session_state.gewaehlteGKs_mit_stunden[gk] = f"{alle_faecher[gk]}h"
            st.session_state.gesamtstunden += alle_faecher[gk]
            st.session_state.möglicheGKs.remove(gk)
            st.rerun()
        else:
            if gk == "Spanisch für Neueinsteiger" and st.session_state.gesamtstunden + 4 == 39:
                st.session_state.möglicheGKs.remove(gk)
                st.error("Die maximale Stundenzahl von 38 Stunden wurde überschritten. Bitte wählen Sie ein anderes Fach.")
                st.rerun()
            st.error("Die maximale Anzahl an Grundkursen wurde erreicht.")
    



# ------------------------------------------ Streamlit Layout ---------------------------------------

st.title("Kurswahl für die Oberstufe")
st.divider()






# --------------------------------------- Hauptfunktionen aufrufen ----------------------------------

if not st.session_state.vorherige_faecher_abgeschlossen:
    st.subheader("Vorherige Fächer auswählen")
    waehle_vorherige_faecher()
else:
    if not len(st.session_state.gewaehlteLKs) == 3:
        st.subheader("Leistungskurse auswählen")
        waehle_leistungskurse()

    if len(st.session_state.gewaehlteLKs) == 3:
        st.subheader("Grundkurse auswählen")
        waehle_grundkurse()





# --------- Übersicht ---------

st.divider()  # Trennlinie
st.subheader("Kurswahl-Übersicht")

# Drei gleich breite Spalten
col_lk, col_gk, col_h = st.columns(3)

with col_lk:
        st.write("**🎯 Leistungskurse**")
        if 'gewaehlteLKs_mit_stunden' in st.session_state and st.session_state.gewaehlteLKs_mit_stunden:
            for lk, stunden in st.session_state.gewaehlteLKs_mit_stunden.items():
                st.write(f"- {lk} ({stunden})")
        else:
            st.write("- Noch nicht gewählt")  # Platzhalter

with col_gk:
    st.write("**📚 Grundkurse**")
    if 'gewaehlteGKs_mit_stunden' in st.session_state and st.session_state.gewaehlteGKs_mit_stunden:
        for gk, stunden in st.session_state.gewaehlteGKs_mit_stunden.items():
            st.write(f"- {gk} ({stunden})")
    else:
        st.write("- Noch nicht gewählt")  # Platzhalter

with col_h:
    st.write("**⏱ Wochenstunden**")
    # Container für perfekte vertikale Ausrichtung
    with st.container():
        st.metric(
            label="", 
            value=f"{st.session_state.get('gesamtstunden', 0)}",
        )