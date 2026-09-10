import restaurant_json as rj
import json


# print(rj.restaurant["name"])

json_data = json.dumps(rj.restaurant, indent=4, ensure_ascii=True ,sort_keys=False) # python to JSON string
#print(json_data)
# print(type(json_data))

with open("restaurant.json", "w", encoding="utf-8") as file:
        json.dump(
        rj.restaurant,
        file,
        indent=4,
        ensure_ascii=False
    )
        
with open("restaurant.json" , "r" , encoding="utf-8") as file:
   data =  json.load(file)

print(data)


# convert Plat object to JSON serializable format
class Plat:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix


def convert_plat(obj):
    if isinstance(obj, Plat):
        return {
            "nom": obj.nom,
            "prix": obj.prix
        }

    raise TypeError("Object not serializable")


plat = Plat("Tajine", 60)

json_data = json.dumps(
    plat,
    default=convert_plat,
    indent=4
)

print(json_data)

