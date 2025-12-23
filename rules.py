def check_rules(amount: int) -> bool:
    """
    Simple rule engine
    Returns True if suspicious
    """
    if amount > 50000:
        return True
    return False
