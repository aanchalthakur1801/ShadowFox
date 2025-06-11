# Step 1: Define the Justice League list
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("The justice league members are:",justice_league)

# Step 2: Add Batgirl and Nightwing to the list
justice_league.extend(["Batgirl", "Nightwing"])
print("Adding batgirl and nightwing:",justice_league)

# Step 3: Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("Moving the wonder woman to the beginning:",justice_league)

# Step 4: Separate Aquaman and Flash by inserting Green Lantern between them
justice_league.remove("Green Lantern")  
aquaman_index = justice_league.index("Aquaman")
justice_league.insert(aquaman_index + 1, "Green Lantern")
print("separating aquaman and flash and inserting green lantern between them:",justice_league)

# Step 5: Replace the existing list with new members
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("the justice league new members are:",justice_league)

# Step 6: Sort the list alphabetically and make the 0th index the new leader
justice_league.sort()
new_leader = justice_league[0]
print("sorting the list alphabetically and making the 0th index the new leader:",justice_league)

# Print the final results
print("Final Justice League members:", justice_league)
print("The new leader is:", new_leader)
