# src/fastfoodgo/main.py

def calcul_total(articles):
    """
    articles : liste de dict { 'nom': str, 'prix': float, 'quantité': int }
    Retourne le total TTC
    """
    return sum(a['prix'] * a['quantité'] for a in articles)

def valider_transition_statut(old_statut, new_statut):
    """
    Vérifie si une transition de statut est valide
    """
    transitions_valides = {
        "créé": ["en_cours", "annulé"],
        "en_cours": ["préparé", "annulé"],
        "préparé": ["livré"],
        "livré": []
    }
    return new_statut in transitions_valides.get(old_statut, [])