def calculate_fuel():
    cargo_weight = 0
    
    while True:
        cargo = input("Cargo (or type 'launch' to finish): ").strip().lower()
        
        if cargo == "launch":
            break
        elif cargo == "satellite":
            cargo_weight += 10000
        elif cargo == "rover":
            cargo_weight += 2500
        elif cargo == "supplies":
            cargo_weight += 500
        else:
            print("Invalid cargo type. Please try again.")
            continue  
        if cargo_weight > 10000:
            print("The cargo weight is too heavy for the mission!")
            return

    rocket_weight = 50000
    total_fuel = (cargo_weight + rocket_weight) * 3
    
    print(f"\nMission Approved!")
    print(f"Total Cargo Weight: {cargo_weight} kg")
    print(f"Total Fuel Needed: {total_fuel} liters")
calculate_fuel(1)