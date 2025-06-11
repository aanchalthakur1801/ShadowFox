PI = 3.14
radius = 84  
water_per_sq_meter = 1.4  

pond_area = PI * (radius ** 2)

total_water = int(pond_area * water_per_sq_meter)  

print("The area of the pond is:", round(pond_area, 2), "square meters")
print("The total amount of water in the pond is:", total_water, "liters")
