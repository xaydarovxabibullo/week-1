def noise_report(site_name, hourly_db, limit_db = 70.0):
    count = 0
    for i in hourly_db:
        
        if i > limit_db:
            count += 1
    total = 0
    for el in hourly_db:
        total += el
    avarage = total / len(hourly_db)
    hourly_change = []
    for j in range(len(hourly_db)):
        if hourly_db[j-1] in hourly_db:
            dif = hourly_db[j] - hourly_db[j-1]
            hourly_change.append(dif)
    difference = (hourly_change[1:])
    
    
        
    print(f"Site         : {site_name}")

    print(f"Hours        : {len(hourly_db)} dB")
    print(f"Average      : {round(avarage, 1)}")
    print(f"Peak level   : {max(hourly_db)} dB")
    print(f"Lowest level : {min(hourly_db)} dB")
    print(f"Breaches     : {count}")
    return(f"Hourly change: {difference}")


# Breaches     : 4
# Hourly change: [7, 8, -12, 7, 10, -15]
print(noise_report("Construction Zone 3", [65, 72, 80, 68, 75, 85, 70]))
print(noise_report("Road Intersection B", [55, 60, 73, 58, 62], limit_db=65.0))
