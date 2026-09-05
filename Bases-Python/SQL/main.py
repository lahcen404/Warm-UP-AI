from app.database import Base, engine

from app.models import (
    Category,
    Plat,
    Client,
    Commande,
    CommandePlat,
    Fournisseur,
    Ingredient,
    PlatIngredient,
    Avis,
)


Base.metadata.create_all(engine)

print("Tables created successfully!")