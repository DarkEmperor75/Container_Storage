def load_20ft_containers(categories, num_wagons=45, weight_limit=61, pairing_limit=20):
    """
    Load 20ft containers onto wagons according to specified conditions.

    Parameters:
        categories (dict): Dictionary with keys 'Cat1', 'Cat2', 'Cat3'.
                           Each value is a list of container weights (sorted descending).
        num_wagons (int): Total number of wagons available for loading.
        weight_limit (float): Maximum allowable total weight per wagon.
        pairing_limit (float): Maximum allowable weight difference between two containers loaded as a pair.

    Returns:
        wagons (list): List of loaded wagons. Each entry is a tuple:
                       (weight_from_first_container, weight_from_second_container) 
                       or (container_weight, None) for single-stack loads.
    """
    wagons = []
    
    # Iterate until we fill all wagons or no more loading options remain.
    while len(wagons) < num_wagons:
        loaded = False

        # Condition 1: At least two containers in Cat1
        if len(categories.get('Cat1', [])) >= 2:
            cont1 = categories['Cat1'][0]
            cont2 = categories['Cat1'][1]
            if abs(cont1 - cont2) < pairing_limit and (cont1 + cont2) <= weight_limit:
                categories['Cat1'].pop(0)
                categories['Cat1'].pop(0)
                wagons.append((cont1, cont2))
                loaded = True
                continue

        # Condition 2: At least one container in Cat1 and one in Cat2
        if len(categories.get('Cat1', [])) >= 1 and len(categories.get('Cat2', [])) >= 1:
            cont1 = categories['Cat1'][0]
            cont2 = categories['Cat2'][0]
            if (cont1 + cont2) <= weight_limit:
                categories['Cat1'].pop(0)
                categories['Cat2'].pop(0)
                wagons.append((cont1, cont2))
                loaded = True
                continue

        # Condition 3: At least two containers in Cat2
        if len(categories.get('Cat2', [])) >= 2:
            cont1 = categories['Cat2'][0]
            cont2 = categories['Cat2'][1]
            if abs(cont1 - cont2) < pairing_limit and (cont1 + cont2) <= weight_limit:
                categories['Cat2'].pop(0)
                categories['Cat2'].pop(0)
                wagons.append((cont1, cont2))
                loaded = True
                continue

        # Condition 4: At least one container in Cat2 and one in Cat3
        if len(categories.get('Cat2', [])) >= 1 and len(categories.get('Cat3', [])) >= 1:
            cont1 = categories['Cat2'][0]
            cont2 = categories['Cat3'][0]
            if (cont1 + cont2) <= weight_limit:
                categories['Cat2'].pop(0)
                categories['Cat3'].pop(0)
                wagons.append((cont1, cont2))
                loaded = True
                continue

        # Fallback: Load a single container from Cat3
        if len(categories.get('Cat3', [])) >= 1:
            cont = categories['Cat3'].pop(0)
            if cont <= weight_limit:
                wagons.append((cont, None))
                loaded = True
                continue
        
        # If no container was loaded in this iteration, break out of the loop.
        if not loaded:
            break

    return wagons


# Example usage for 20ft container loading:
if __name__ == "__main__":
    # Example container weights for each category (sorted descending)
    categories_20 = {
        'Cat1': [24.0, 23.5, 23.0, 22.5],  # Containers in weight range [20, 24] tons
        'Cat2': [19.0, 18.5, 18.0, 17.5],    # Containers in weight range (4, 20) tons
        'Cat3': [4.0, 3.8, 3.5, 3.2]         # Containers with weight <= 4 tons
    }
    
    # (Optional) Make a deep copy if you plan to run multiple tests.
    import copy
    cat_copy = copy.deepcopy(categories_20)
    
    # Load containers onto wagons (for example, load 10 wagons)
    loaded_wagons = load_20ft_containers(cat_copy, num_wagons=10, weight_limit=61, pairing_limit=20)
    
    print("Loaded 20ft container wagons:")
    for i, wagon in enumerate(loaded_wagons, 1):
        cont_a, cont_b = wagon
        if cont_b is not None:
            print(f"Wagon {i}: Container A = {cont_a} tons, Container B = {cont_b} tons, Total = {cont_a + cont_b} tons")
        else:
            print(f"Wagon {i}: Single-stack container = {cont_a} tons")
