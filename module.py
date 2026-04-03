def get_zodiac_sign(month, day):
    """Logic to determine sign based on month and day."""
    # Example logic:
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "aries"
    # Zon: Add the rest of the 11 signs here...
    return "unknown"

def calculate_compatibility(sign1, sign2, data):
    """Uses the 2D matrix from JSON to find a match score."""
    signs = data["signs_list"]
    idx1 = signs.index(sign1.lower())
    idx2 = signs.index(sign2.lower())
    return data["compatibility_matrix"][idx1][idx2]