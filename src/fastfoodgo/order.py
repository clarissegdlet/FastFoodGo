def calculate_order_total(items):
    """
    Calcule le total d'une commande.
    items : liste de dictionnaires avec 'price' et 'quantity'
    """
    total = 0

    for item in items:
        total += item["price"] * item["quantity"]

    return total
