from geopy.distance import distance

def calculate_distance(point1, point2):
    # Example: Calculate distance between two GPS points
    return distance(point1, point2).miles

def calculate_toll(vehicle_type, distance):
    # Example: Simplified toll calculation based on vehicle type and distance
    toll_rate = 0.05  # Example rate per mile
    if vehicle_type == 'car':
        toll = toll_rate * distance
    elif vehicle_type == 'truck':
        toll = toll_rate * distance * 1.5  # Higher rate for trucks
    elif vehicle_type =='bike':
        toll = toll_rate*distance
    else:
        toll = 0  # Default, could handle other vehicle types
    return toll
