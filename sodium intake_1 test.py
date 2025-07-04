# Example valid Python code

def calculate_total_blood_volume(plasma_volume, red_blood_cell_volume):
    """
    Calculate total blood volume as the sum of plasma volume and red blood cell volume.

    Args:
            plasma_volume (float): Plasma volume in mL.
            red_blood_cell_volume (float): Red blood cell volume in mL.

    Returns:
            float: Total blood volume in mL.
    """
    return plasma_volume + red_blood_cell_volume


# Example usage:
pv = 2633  # plasma volume in mL
rbv = 1249  # red blood cell volume in mL
tbv = calculate_total_blood_volume(pv, rbv)
print(f"Total blood volume: {tbv} mL")
