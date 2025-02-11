import math

def allocate_stacks(categories, stack_height=4, max_bays=5, max_rows=5):
    """
    Allocates stacks for container categories within a block.
    
    Parameters:
        categories (dict): Dictionary mapping category names to number of containers.
                           e.g., {'Cat1': 23, 'Cat2': 30, ...}
        stack_height (int): Maximum number of containers per stack.
        max_bays (int): Maximum number of bays in the block.
        max_rows (int): Maximum number of rows per bay.
    
    Returns:
        allocation (dict): Dictionary mapping each category to a list of stack positions.
                           Each position is a tuple (bay, row).
    """
    allocation = {}
    current_bay = 1
    current_row = 1
    
    # Iterate through each category in the order provided (order matters)
    for category, num_containers in categories.items():
        stacks_needed = math.ceil(num_containers / stack_height)
        allocation[category] = []  # Initialize the list for this category
        
        for i in range(stacks_needed):
            # Check if we have exceeded the block dimensions
            if current_bay > max_bays:
                raise Exception("Not enough bays in the block to allocate all stacks.")
            
            # Append the current position for the new stack
            allocation[category].append((current_bay, current_row))
            
            # Move to the next row in the current bay
            current_row += 1
            
            # If current row exceeds max_rows, reset to first row and increment bay
            if current_row > max_rows:
                current_row = 1
                current_bay += 1
    
    return allocation

# Example usage:
if __name__ == "__main__":
    # Define container categories and number of containers in each category
    # For example, these categories might represent different weight classes for 40ft containers
    categories = {
        'V1': 23,   # Heaviest containers
        'V2': 24,   # Next heaviest
        'V3': 22,   # Lighter containers
        'V4': 18    # Lightest containers
    }
    
    # Allocate stacks in the block
    try:
        allocation = allocate_stacks(categories, stack_height=4, max_bays=5, max_rows=5)
        print("Stack Allocation:")
        for category, stacks in allocation.items():
            print(f"Category {category}: {stacks}")
    except Exception as e:
        print("Error during allocation:", e)
