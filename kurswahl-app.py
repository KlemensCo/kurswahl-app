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
    ]

if 'gesamtstunden' not in st.session_state:
    st.session_state.gesamtstunden = 0
    
if 'vorherige_faecher_abgeschlossen' not in st.session_state:
    st.session_state.vorherige_faecher_abgeschlossen = False

if 'gewaehlteGKs_mit_stunden' not in st.session_state:
    st.session_state.gewaehlteGKs_mit_stunden = {}

if 'gewaehlteLKs_mit_stunden' not in st.session_state:
    st.session_state.gewaehlteLKs_mit_stunden = {}

# Neu: Verlauf für Zurück-Button
if 'verlauf' not in st.session_state:
    st.session_state.verlauf = []

# --------------------------------------------- Listen -----------------------------------------
alle_faecher = {
    "Deutsch": 3, "Englisch": 3, "Französisch": 3, "Latein": 3, "Spanisch": 3, "Spanisch für Neueinsteiger": 4,
    "DSP": 3, "Kunst": 3, "Musik": 3, "Geschichte": 3, "Geographie": 3, "Politik": 3, "Religion": 3,
    "Mathematik": 3, "Physik": 3, "Chemie": 3, "Biologie": 3, "Informatik": 3, "Sport": 2, "Projektarbeit": 2
}

lk1phybio = ["Deutsch", "Englisch", "Mathematik", "Geschichte", "Politik", "Geographie"]

# --------------------------------------------- Funktionen -----------------------------------------
def speichere_zustand():
    """Speichert den aktuellen Zustand für den Zurück-Button"""
    aktueller_zustand = {
        'gewaehlteLKs': list(st.session_state.gewaehlteLKs),
        'gewaehlteGKs': list(st.session_state.gewaehlteGKs),
        'gesamtstunden': st.session_state.gesamtstunden,
        'möglicheLKs': list(st.session_state.möglicheLKs),
        'möglicheGKs': list(st.session_state.möglicheGKs),
        'vorherige_faecher_abgeschlossen': st.session_state.vorherige_faecher_abgeschlossen,
        'gewaehlteLKs_mit_stunden': dict(st.session_state.gewaehlteLKs_mit_stunden),
        'gewaehlteGKs_mit_stunden': dict(st.session_state.gewaehlteGKs_mit_stunden)
    }
    st.session_state.verlauf.append(aktueller_zustand)
    # Verlauf auf 10 Schritte begrenzen
    if len(st.session_state.verlauf) > 10:
        st.session_state.verlauf.pop(0)

def gehe_zurueck():
    """Setzt den vorherigen Zustand wieder her"""
    if st.session_state.verlauf:
        letzter_zustand = st.session_state.verlauf.pop()
        
        st.session_state.gewaehlteLKs = letzter_zustand['gewaehlteLKs']
        st.session_state.gewaehlteGKs = letzter_zustand['gewaehlteGKs']
        st.session_state.gesamtstunden = letzter_zustand['gesamtstunden']
        st.session_state.möglicheLKs = letzter_zustand['möglicheLKs']
        st.session_state.möglicheGKs = letzter_zustand['möglicheGKs']
        st.session_state.vorherige_faecher_abgeschlossen = letzter_zustand['vorherige_faecher_abgeschlossen']
        st.session_state.gewaehlteLKs_mit_stunden = letzter_zustand['gewaehlteLKs_mit_stunden']
        st.session_state.gewaehlteGKs_mit_stunden = letzter_zustand['gewaehlteGKs_mit_stunden']
        
        st.rerun()

def waehle_vorherige_faecher():
    st.info("Bitte wählen Sie die Fächer aus, die Sie vorher belegt haben.")
    
    Fremdsprache = st.selectbox("Welche zweite Fremdsprache hatten Sie von der 6. bis zur 9. Klasse?", 
                              ["Französisch", "Latein", "Spanisch", "Keine"])
    
    kuenstlerisches_fach = st.selectbox("Welches künstlerische Fach hatten Sie in der 10. Klasse?", 
                                      ["DSP", "Kunst", "Musik"])
    
    if st.button("Weiter zu den Leistungskursen"):
        speichere_zustand()  # Zustand vor Änderungen speichern
        
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

def waehle_leistungskurse():
    if len(st.session_state.gewaehlteLKs) == 0:
        st.info("Wählen Sie Ihre Leistungskurse aus. Sie müssen drei Leistungskurse belegen.")
        lk1 = st.selectbox("Leistungskurs 1", st.session_state.pflicht_LK)

        if st.button("Bestätigen", key="button_lk1"):
            speichere_zustand()
            st.session_state.gewaehlteLKs.append(lk1)
            st.session_state.gewaehlteLKs_mit_stunden[lk1] = "5h"
            st.session_state.gesamtstunden += 5
            if lk1 in ["Französisch", "Latein", "Musik"]:
                for fach in ["Französisch", "Latein", "Musik"]:
                    if fach in st.session_state.möglicheLKs:
                        st.session_state.möglicheLKs.remove(fach)
            else: 
                st.session_state.möglicheLKs.remove(lk1)
            st.rerun()
    
    elif len(st.session_state.gewaehlteLKs) == 1:
        if st.session_state.gewaehlteLKs[0] in ["Biologie", "Physik"]:
            st.info("Da Sie Biologie oder Physik als ersten Leistungskurs gewählt haben:")
            lk2 = st.selectbox("Leistungskurs 2", lk1phybio)
        else:
            lk2 = st.selectbox("Leistungskurs 2", st.session_state.möglicheLKs)

        if st.button("Bestätigen", key="button_lk2"):
            speichere_zustand()
            st.session_state.gewaehlteLKs.append(lk2)
            st.session_state.gewaehlteLKs_mit_stunden[lk2] = "5h"
            st.session_state.gesamtstunden += 5
            if lk2 in ["Französisch", "Latein", "Musik"]:
                for fach in ["Französisch", "Latein", "Musik"]:
                    if fach in st.session_state.möglicheLKs:
                        st.session_state.möglicheLKs.remove(fach)
            else:
                st.session_state.möglicheLKs.remove(lk2)
            st.rerun()

    elif len(st.session_state.gewaehlteLKs) == 2:
        st.info("Wählen Sie Ihren dritten Leistungskurs aus.")
        lk3 = st.selectbox("Leistungskurs 3", st.session_state.möglicheLKs)

        if st.button("Bestätigen", key="button_lk3"):
            speichere_zustand()
            st.session_state.gewaehlteLKs.append(lk3)
            st.session_state.gewaehlteLKs_mit_stunden[lk3] = "5h"
            st.session_state.gesamtstunden += 5
            if lk3 in ["Französisch", "Latein", "Musik"]:
                for fach in ["Französisch", "Latein", "Musik"]:
                    if fach in st.session_state.möglicheLKs:
                        st.session_state.möglicheLKs.remove(fach)
            else:
                st.session_state.möglicheLKs.remove(lk3)
            st.rerun()

def waehle_grundkurse():
    st.info("Wählen Sie Ihre Grundkurse aus. Mindestens 34 Wochenstunden benötigt.")
    
    for sub in st.session_state.pflicht_GK:
        if sub not in st.session_state.gewaehlteLKs and sub not in st.session_state.gewaehlteGKs:
            st.session_state.gewaehlteGKs.append(sub)
            st.session_state.gewaehlteGKs_mit_stunden[sub] = f"{alle_faecher[sub]}h"
            st.session_state.gesamtstunden += alle_faecher[sub]
            if sub in st.session_state.möglicheGKs:
                st.session_state.möglicheGKs.remove(sub)
    
    for sub in st.session_state.möglicheGKs:
        if sub in st.session_state.gewaehlteGKs or sub in st.session_state.gewaehlteLKs:
            st.session_state.möglicheGKs.remove(sub)

    gk = st.selectbox("Grundkurse", st.session_state.möglicheGKs)
    if st.button("Bestätigen", key="button_gk"):
        if st.session_state.gesamtstunden + alle_faecher[gk] <= 38:
            speichere_zustand()
            st.session_state.gewaehlteGKs.append(gk)
            st.session_state.gewaehlteGKs_mit_stunden[gk] = f"{alle_faecher[gk]}h"
            st.session_state.gesamtstunden += alle_faecher[gk]
            st.session_state.möglicheGKs.remove(gk)
            st.rerun()
        else:
            if gk == "Spanisch für Neueinsteiger" and st.session_state.gesamtstunden + 4 == 39:
                st.session_state.möglicheGKs.remove(gk)
                st.error("Maximale Stundenzahl (38h) überschritten.")
                st.rerun()
            st.error("Maximale Anzahl an Grundkursen erreicht.")

def uebersicht():
    col_lk, col_gk, col_h = st.columns(3)
    with col_lk:
        st.write("**🎯 Leistungskurse**")
        if st.session_state.gewaehlteLKs_mit_stunden:
            for lk, stunden in st.session_state.gewaehlteLKs_mit_stunden.items():
                st.write(f"- {lk} ({stunden})")
        else:
            st.write("- Noch nicht gewählt")

    with col_gk:
        st.write("**📚 Grundkurse**")
        if st.session_state.gewaehlteGKs_mit_stunden:
            for gk, stunden in st.session_state.gewaehlteGKs_mit_stunden.items():
                st.write(f"- {gk} ({stunden})")
        else:
            st.write("- Noch nicht gewählt")

    with col_h:
        st.write("**⏱ Wochenstunden**")
        st.metric(label="", value=f"{st.session_state.get('gesamtstunden', 0)}")

# ------------------------------------------ Streamlit Layout ---------------------------------------

st.title("Kurswahl für die Oberstufe")
st.divider()

# Zurück-Button (wenn Verlauf vorhanden)
if st.session_state.verlauf:
    if st.button("↩️ Letzte Auswahl rückgängig machen", help="Klicken Sie hier, um den letzten Schritt rückgängig zu machen"):
        gehe_zurueck()



# ------------------------------------------ Hauptfunktionen -----------------------------------------

# Vorherige Fächer auswählen
if not st.session_state.vorherige_faecher_abgeschlossen:
    st.subheader("Vorherige Fächer auswählen")
    waehle_vorherige_faecher()
else:
    # Leistungskurse auswählen
    if not len(st.session_state.gewaehlteLKs) == 3:
        st.subheader("Leistungskurse auswählen")
        waehle_leistungskurse()

    # Grundkurse auswählen
    if len(st.session_state.gewaehlteLKs) == 3:
        st.subheader("Grundkurse auswählen")
        waehle_grundkurse()



# ------------------------------------------ Übersicht -----------------------------------------

st.divider()
st.subheader("Kurswahl-Übersicht")

uebersicht()
