utensils={"Fork","spoon","knife"}
dishes={"bowl","plate","cup","knife"}
#utensils.update(dishes)
utensils.add("napkin")
utensils.remove("Fork")

for i in utensils:
    print(i)
print(utensils.difference(dishes))
print(utensils.intersection(dishes))
