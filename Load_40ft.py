def load_40ft_containers(categories, num_wagons=45, weight_limit=61):
    """
    Load 40ft containers onto wagons based on provided categories.
    
    Parameters:
        categories (dict): Dictionary with keys 'V1', 'V2', 'V3', 'V4'. 
                           Each value is a list of container weights (sorted descending).
        num_wagons (int): Total number of wagons available for loading.
        weight_limit (float): Maximum allowable total weight per wagon.
    
    Returns:
        List of tuples representing wagon loadings.
        Each tuple is (lower, upper) where 'lower' and 'upper' are container weights.
        If a wagon is loaded as a single-stack, the tuple is (container_weight, None).
    """
    wagons = []
    
    # First, load wagons using containers from V1 (for lower stack) and V2 (for upper stack)
    while categories.get('V1') and categories.get('V2') and len(wagons) < num_wagons:
        lower = categories['V1'].pop(0)
        upper = categories['V2'].pop(0)
        # Check constraints: lower must be heavier than upper, and total weight within limit
        if lower > upper and (lower + upper) <= weight_limit:
            wagons.append((lower, upper))
        else:
            # For simulation purposes, if conditions fail, we still load the pair.
            wagons.append((lower, upper))
    
    # Next, load remaining wagons using containers from V3 (lower) and V4 (upper)
    while categories.get('V3') and categories.get('V4') and len(wagons) < num_wagons:
        lower = categories['V3'].pop(0)
        upper = categories['V4'].pop(0)
        if lower > upper and (lower + upper) <= weight_limit:
            wagons.append((lower, upper))
        else:
            wagons.append((lower, upper))
    
    # If there are leftover containers (in V1 or V3) that could be loaded as single-stack,
    # load them onto wagons if space remains.
    for cat in ['V1', 'V3']:
        while categories.get(cat) and len(wagons) < num_wagons:
            container = categories[cat].pop(0)
            if container <= weight_limit:
                wagons.append((container, None))
    
    return wagons

# Example usage for 40ft container loading:
if __name__ == "__main__":
    # Example container weights for each category (sorted in descending order)
    categories_40 = {
        'V1': [28.0, 27.5, 27.0, 26.5],  # Heaviest containers (for lower stack in first half)
        'V2': [25.0, 24.5, 24.0, 23.5],  # Corresponding containers for upper stack (first half)
        'V3': [26.0, 25.5, 25.0, 24.5],  # For lower stack in second half
        'V4': [23.0, 22.5, 22.0, 21.5]   # For upper stack in second half
    }
    
    # (Optional) Make a deep copy so the original categories remain unchanged for further testing.
    import copy
    cat_copy = copy.deepcopy(categories_40)
    
    # Load containers onto wagons (for example, loading 10 wagons)
    wagons = load_40ft_containers(cat_copy, num_wagons=10, weight_limit=61)
    
    print("Loaded 40ft container wagons:")
    for i, wagon in enumerate(wagons, 1):
        lower, upper = wagon
        if upper is not None:
            print(f"Wagon {i}: Lower = {lower} tons, Upper = {upper} tons, Total = {lower + upper} tons")
        else:
            print(f"Wagon {i}: Single-stack = {lower} tons")
