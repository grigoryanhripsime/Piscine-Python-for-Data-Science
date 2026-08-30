def give_bmi(
    height: list[int | float], weight: list[int | float]
) -> list[int | float]:
    """
    Calculate the BMI for each pair of height and weight values.
    """
    if not isinstance(height, list) or not isinstance(weight, list):
        print("Error: Both height and weight must be lists")
        return None

    if len(height) != len(weight):
        print("Error: height and weight lists must have the same length")
        return None

    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            print("Error: All elements must be int or float")
            return None
        if h <= 0:
            print("Error: Height must be positive")
            return None

    return [w / (h ** 2) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Return a list of booleans indicating whether each BMI is above the limit.
    """
    if not isinstance(bmi, list):
        print("Error: bmi must be a list")
        return None
    if not isinstance(limit, int):
        print("Error: limit must be an int")
        return None

    for value in bmi:
        if not isinstance(value, (int, float)):
            print("Error: All BMI values must be int or float")
            return None

    return [value > limit for value in bmi]
