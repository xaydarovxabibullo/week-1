reservoir_level = float(input("Enter opening reservoir level (L) "))
is_premium = reservoir_level >= 10.0
print(f"Welcome! Opening level: {reservoir_level} L")
if is_premium == True:
    print("Setup tier: Premium")
else:
    print("Setup tier: Basic")

while True:
    print("")
    print("[1] Refill reservoir  [2] Water plants  [3] Check level  [4] Exit")

    choice = int(input("Your choice: "))

    # 1-tanlov kodi
    if choice == 1:
        add = float(input("Litres to add: "))
        if add >= 0:
            
            reservoir_level = reservoir_level + add
            print(f"Reservoir refilled. New level: {reservoir_level} L")
        if add < 0:
            print("Invalid amount. Please enter a positive value.")
    # 1-tanlov ishi yakunlandi


    # 2-tanlov
    if choice == 2 :
        use = float(input("Litres to use: "))
        if use > reservoir_level and use > 0:
            print(f"Not enough water. Current level: {reservoir_level} L")
        if use <= reservoir_level and use >= 0:
            reservoir_level = reservoir_level - use
            print(f"Plants watered. Reservoir level: {reservoir_level} L")
       
        if use < 0:
            print("Invalid amount. Please enter a positive value.")
    # 2-tanlov tugadi

    # 3-tanlov 

    if choice == 3:
            print(f"Current reservoir level: {reservoir_level} L")
    # 3-tanlov tugadi


    # 4-tanlov
    if choice == 4:
        print(f"Session ended. Final reservoir level: {reservoir_level} L")
        break
  
        
    if choice != 1 and choice != 2 and choice != 3 and choice != 4:
            print("System stopped")
            break
