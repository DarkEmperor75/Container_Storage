def load_mixed_containers(c20, d_containers, num_wagons=45, weight_limit=61):
    """
    Load a mix of 20ft and 40ft containers onto wagons.

    Parameters:
        c20 (list): List of available 20ft container weights (sorted in descending order).
                    These are intended for pairing (lower stack).
        d_containers (dict): Dictionary with keys 'D1', 'D2', 'D3', 'D4' where:
                             - 'D1': List of 40ft container weights for single-stack (sorted descending)
                             - 'D2': List of 40ft container weights for lower stack of double-stack wagons (sorted descending)
                             - 'D3': List of 40ft container weights for upper stack of double-stack wagons (sorted descending)
                             - 'D4': List of 40ft container weights intended to be paired with 20ft containers (sorted descending;
                                      the lightest container is at the end, so pop from the end)
        num_wagons (int): Maximum number of wagons available for loading.
        weight_limit (float): Maximum allowable weight per wagon.

    Returns:
        list: A list of loaded wagon configurations. Each element is:
              - For a 20ft pair with D4: ((twenty1, twenty2), d4_container)
              - For a D2-D3 pair: (d2_container, d3_container)
              - For a single D1 load: (d1_container, None)
    """
    wagons = []
    
    # Phase 1: Pair 20ft containers with D4 containers.
    # We require at least 2 twenty-foot containers and at least 1 container in D4.
    while d_containers.get('D4') and len(c20) >= 2 and len(wagons) < num_wagons:
        # Select the two heaviest available 20ft containers
        twenty1 = c20.pop(0)
        twenty2 = c20.pop(0)
        # For D4, use the lightest available (pop from end)
        candidate_d4 = d_containers['D4'][-1]
        
        # Check: Lower stack must be heavier than the candidate and total weight within limit.
        if (twenty1 + twenty2 > candidate_d4) and (twenty1 + twenty2 + candidate_d4 <= weight_limit):
            # Load the wagon with this combination.
            wagons.append(((twenty1, twenty2), candidate_d4))
            d_containers['D4'].pop()  # Remove the candidate from D4.
        else:
            # If the pairing is not feasible, push back the 20ft containers and break out.
            # (Alternative strategies could be implemented here.)
            c20.insert(0, twenty2)
            c20.insert(0, twenty1)
            break  # Exit the pairing loop.
    
    # Phase 2: Pair D2 and D3 containers for double-stack loading.
    while d_containers.get('D2') and d_containers.get('D3') and len(wagons) < num_wagons:
        d2 = d_containers['D2'].pop(0)  # Heaviest available from D2.
        d3 = d_containers['D3'].pop(0)  # Heaviest available from D3.
        if (d2 + d3) <= weight_limit:
            wagons.append((d2, d3))
        else:
            # If the pairing exceeds the weight limit, one could try alternative strategies.
            # For now, we simply skip this pairing.
            continue
    
    # Phase 3: Load remaining D1 containers as single-stack loads.
    while d_containers.get('D1') and len(wagons) < num_wagons:
        d1 = d_containers['D1'].pop(0)
        if d1 <= weight_limit:
            wagons.append((d1, None))
        else:
            continue  # Skip if it doesn't meet the weight constraint.
    
    return wagons

# Example usage for mixed container loading:
if __name__ == "__main__":
    # Sample 20ft container weights (sorted in descending order)
    # (These could be the heavy half of the 20ft container block.)
    twenty_ft = [24.0, 23.5, 23.0, 22.5, 22.0, 21.5]
    
    # Sample 40ft container categories:
    d_containers = {
        'D1': [28.5, 27.8, 27.0],      # For single-stack loads (sorted descending)
        'D2': [26.0, 25.5, 25.0],      # For lower stack of double-stack loads (sorted descending)
        'D3': [23.5, 23.0, 22.5],      # For upper stack of double-stack loads (sorted descending)
        # For D4, we want the lightest container available for pairing, so sorted descending;
        # the lightest will be at the end.
        'D4': [21.5, 21.0, 20.5, 20.0]  # For pairing with 20ft containers.
    }
    
    # Make copies if you plan to run multiple tests.
    import copy
    twenty_ft_copy = copy.deepcopy(twenty_ft)
    d_containers_copy = copy.deepcopy(d_containers)
    
    # Load mixed containers onto, say, 10 wagons.
    mixed_wagons = load_mixed_containers(twenty_ft_copy, d_containers_copy, num_wagons=10, weight_limit=61)
    
    print("Loaded mixed container wagons:")
    for i, wagon in enumerate(mixed_wagons, 1):
        # Determine type of load based on tuple structure.
        if isinstance(wagon[0], tuple):
            # This is a 20ft pair with a D4 container.
            (twenty1, twenty2), d4_container = wagon
            total = twenty1 + twenty2 + d4_container
            print(f"Wagon {i}: 20ft pair = ({twenty1}, {twenty2}) tons, D4 = {d4_container} tons, Total = {total} tons")
        else:
            # Either a D2-D3 pair or a single D1 load.
            lower, upper = wagon
            if upper is not None:
                print(f"Wagon {i}: D2-D3 load: Lower = {lower} tons, Upper = {upper} tons, Total = {lower + upper} tons")
            else:
                print(f"Wagon {i}: Single-stack D1 load = {lower} tons")
