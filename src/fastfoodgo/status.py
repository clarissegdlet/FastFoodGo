def is_valid_status_transition(current_status, next_status):
    """
    Vérifie si la transition de statut est autorisée.
    """
    if current_status == "CREATED" and next_status in ["PAID", "CANCELLED"]:
        return True
    if current_status == "PAID" and next_status == "PREPARING":
        return True
    if current_status == "PREPARING" and next_status == "DELIVERED":
        return True

    return False
