ice_cream: dict[str, int] = {"chocolate": 12,"vanilla": 8, "strawberry": 5}
print("Made my dictionary.")
ice_cream["mint"] = 3
ice_cream.pop("mint")
print(ice_cream["chocolate"])
ice_cream["vanilla"] = 10
print(ice_cream)

print(len(ice_cream))

print("chocolate" in ice_cream)
print("mint" in ice_cream)

if "mint" in ice_cream:
    print (f"There are {ice_cream['mint']} orders of mint ice cream")
else:
    print("There are no orders of mint.")

for key in ice_cream:
    print(f"{key} has {ice_cream[key]} orders")

