def predict_risk(amount: int) -> float:
    """
    Mock ML risk scoring (0.0 - 1.0)
    """
    if amount > 100000:
        return 0.92
    elif amount > 50000:
        return 0.65
    return 0.10
