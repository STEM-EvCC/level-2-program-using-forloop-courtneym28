mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]



total_missions = len(mission_names) # len is for length. took me too long to realize the resemblance
print("Total number of missions:", total_missions ) # for total number of missions


successful_missions_total = sum(mission_success) # True counts as 1 and False counts as nothing so this works. again, took me too long to realize
print("Number of successful missions:", successful_missions_total) # for the number of successful missions


success_rate = (successful_missions_total / total_missions) * 100 # calculates success rate percentage
print(f"Success rate: {round(success_rate, 2)}%") # idk what the f does still but this rounds success_rate to two decimal places and adds % straight after it


mission_count = 0 # starting number for following:
for year in mission_years: # for loop - loops through mission_years
    if year < 2000: # if the year is before 2000 ->
        mission_count += 1 # -> it adds 1 to mission_count
print("Number of missions launched before 2000:") # prints string
# following for the mission names:
for name, year in zip(mission_names, mission_years): # name for mission_names, year for mission_years; zip combines lists into pairs so they can be referenced together (I think)
    if year < 2000: # if the year is less than 2000 ->
        print("-", name) # -> it prints the name of the corresponding mission. if not, it just ignores it

