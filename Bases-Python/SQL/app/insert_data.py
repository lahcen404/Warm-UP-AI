from datetime import datetime
from decimal import Decimal

from app.database import SessionLocal
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

# python -m app.insert_data - -- - run this file as a python module


with SessionLocal() as session:

    # =========================
    # 1. CATEGORIES
    # =========================

    categories = [
        Category(id=1, nom="Entrée"),
        Category(id=2, nom="Plat principal"),
        Category(id=3, nom="Dessert"),
        Category(id=4, nom="Boisson"),
        Category(id=5, nom="Végétarien"),
    ]

    session.add_all(categories)


    # =========================
    # 2. FOURNISSEURS
    # =========================

    fournisseurs = [
        Fournisseur(
            id=1,
            nom="AgriFresh",
            contact="contact@agrifresh.com"
        ),
        Fournisseur(
            id=2,
            nom="MeatSupplier",
            contact="info@meatsupplier.com"
        ),
        Fournisseur(
            id=3,
            nom="BevCo",
            contact="sales@bevco.com"
        ),
        Fournisseur(
            id=4,
            nom="DairyFarm",
            contact="dairy@farm.com"
        ),
    ]

    session.add_all(fournisseurs)


    # =========================
    # 3. CLIENTS
    # =========================

    clients = [
        Client(
            id=1,
            nom="Amine Lahmidi",
            email="amine@example.com",
            telephone="+212600123456"
        ),
        Client(
            id=2,
            nom="Sara Benali",
            email="sara.b@example.com",
            telephone="+212600654321"
        ),
        Client(
            id=3,
            nom="Youssef El Khalfi",
            email="youssef.k@example.com",
            telephone=None
        ),
        Client(
            id=4,
            nom="Fatima Zahra",
            email="fatima.z@example.com",
            telephone="+212600987654"
        ),
        Client(
            id=5,
            nom="Omar Alaoui",
            email="omar.a@example.com",
            telephone="+212600112233"
        ),
    ]

    session.add_all(clients)


    # =========================
    # 4. PLATS
    # =========================

    plats = [
        Plat(
            id=1,
            nom="Salade César",
            prix=Decimal("45.00"),
            description="Salade avec poulet grillé",
            categorie_id=1
        ),
        Plat(
            id=2,
            nom="Soupe de légumes",
            prix=Decimal("30.00"),
            description="Soupe chaude de saison",
            categorie_id=1
        ),
        Plat(
            id=3,
            nom="Steak frites",
            prix=Decimal("90.00"),
            description="Viande grillée et frites",
            categorie_id=2
        ),
        Plat(
            id=4,
            nom="Pizza Margherita",
            prix=Decimal("70.00"),
            description="Pizza tomate & mozzarella",
            categorie_id=2
        ),
        Plat(
            id=5,
            nom="Tiramisu",
            prix=Decimal("35.00"),
            description="Dessert italien",
            categorie_id=3
        ),
        Plat(
            id=6,
            nom="Glace 2 boules",
            prix=Decimal("25.00"),
            description="Glace au choix",
            categorie_id=3
        ),
        Plat(
            id=7,
            nom="Coca-Cola",
            prix=Decimal("15.00"),
            description="Boisson gazeuse",
            categorie_id=4
        ),
        Plat(
            id=8,
            nom="Eau minérale",
            prix=Decimal("10.00"),
            description="Eau plate ou gazeuse",
            categorie_id=4
        ),
        Plat(
            id=9,
            nom="Curry de légumes",
            prix=Decimal("65.00"),
            description="Plat végétarien épicé",
            categorie_id=5
        ),
        Plat(
            id=10,
            nom="Falafel wrap",
            prix=Decimal("50.00"),
            description="Wrap avec falafels et légumes",
            categorie_id=5
        ),
    ]

    session.add_all(plats)


    # =========================
    # 5. INGREDIENTS
    # =========================

    ingredients = [
        Ingredient(
            id=1,
            nom="Poulet",
            cout_unitaire=Decimal("15.00"),
            stock=Decimal("50.00"),
            fournisseur_id=2
        ),
        Ingredient(
            id=2,
            nom="Laitue",
            cout_unitaire=Decimal("5.00"),
            stock=Decimal("20.00"),
            fournisseur_id=1
        ),
        Ingredient(
            id=3,
            nom="Tomate",
            cout_unitaire=Decimal("3.00"),
            stock=Decimal("30.00"),
            fournisseur_id=1
        ),
        Ingredient(
            id=4,
            nom="Mozzarella",
            cout_unitaire=Decimal("10.00"),
            stock=Decimal("15.00"),
            fournisseur_id=4
        ),
        Ingredient(
            id=5,
            nom="Pomme de terre",
            cout_unitaire=Decimal("2.00"),
            stock=Decimal("100.00"),
            fournisseur_id=1
        ),
        Ingredient(
            id=6,
            nom="Café",
            cout_unitaire=Decimal("20.00"),
            stock=Decimal("5.00"),
            fournisseur_id=3
        ),
        Ingredient(
            id=7,
            nom="Sucre",
            cout_unitaire=Decimal("1.50"),
            stock=Decimal("25.00"),
            fournisseur_id=3
        ),
        Ingredient(
            id=8,
            nom="Pois chiches",
            cout_unitaire=Decimal("4.00"),
            stock=Decimal("40.00"),
            fournisseur_id=1
        ),
    ]

    session.add_all(ingredients)


    # =========================
    # 6. COMMANDES
    # =========================

    commandes = [
        Commande(
            id=1,
            client_id=1,
            date_commande=datetime(2025, 7, 7, 12, 30),
            total=Decimal("120.00")
        ),
        Commande(
            id=2,
            client_id=2,
            date_commande=datetime(2025, 7, 7, 13, 0),
            total=Decimal("85.00")
        ),
        Commande(
            id=3,
            client_id=1,
            date_commande=datetime(2025, 7, 8, 19, 45),
            total=Decimal("150.00")
        ),
        Commande(
            id=4,
            client_id=3,
            date_commande=datetime(2025, 8, 15, 18, 30),
            total=Decimal("200.00")
        ),
        Commande(
            id=5,
            client_id=4,
            date_commande=datetime(2025, 9, 1, 20, 0),
            total=Decimal("95.00")
        ),
        Commande(
            id=6,
            client_id=5,
            date_commande=datetime(2025, 9, 10, 12, 15),
            total=Decimal("75.00")
        ),
    ]

    session.add_all(commandes)


    # =========================
    # 7. COMMANDE_PLATS
    # =========================

    commande_plats = [
        CommandePlat(commande_id=1, plat_id=1, quantite=1),
        CommandePlat(commande_id=1, plat_id=3, quantite=1),
        CommandePlat(commande_id=1, plat_id=7, quantite=2),

        CommandePlat(commande_id=2, plat_id=2, quantite=1),
        CommandePlat(commande_id=2, plat_id=4, quantite=1),
        CommandePlat(commande_id=2, plat_id=8, quantite=1),

        CommandePlat(commande_id=3, plat_id=3, quantite=1),
        CommandePlat(commande_id=3, plat_id=5, quantite=1),
        CommandePlat(commande_id=3, plat_id=7, quantite=1),

        CommandePlat(commande_id=4, plat_id=4, quantite=2),
        CommandePlat(commande_id=4, plat_id=9, quantite=1),

        CommandePlat(commande_id=5, plat_id=10, quantite=1),
        CommandePlat(commande_id=5, plat_id=8, quantite=2),

        CommandePlat(commande_id=6, plat_id=7, quantite=3),
        CommandePlat(commande_id=6, plat_id=6, quantite=1),
    ]

    session.add_all(commande_plats)


    # =========================
    # 8. PLAT_INGREDIENTS
    # =========================

    plat_ingredients = [
        PlatIngredient(
            plat_id=1,
            ingredient_id=1,
            quantite_necessaire=Decimal("0.2")
        ),
        PlatIngredient(
            plat_id=1,
            ingredient_id=2,
            quantite_necessaire=Decimal("0.1")
        ),

        PlatIngredient(
            plat_id=2,
            ingredient_id=2,
            quantite_necessaire=Decimal("0.05")
        ),
        PlatIngredient(
            plat_id=2,
            ingredient_id=5,
            quantite_necessaire=Decimal("0.1")
        ),

        PlatIngredient(
            plat_id=3,
            ingredient_id=1,
            quantite_necessaire=Decimal("0.3")
        ),
        PlatIngredient(
            plat_id=3,
            ingredient_id=5,
            quantite_necessaire=Decimal("0.2")
        ),

        PlatIngredient(
            plat_id=4,
            ingredient_id=3,
            quantite_necessaire=Decimal("0.1")
        ),
        PlatIngredient(
            plat_id=4,
            ingredient_id=4,
            quantite_necessaire=Decimal("0.15")
        ),

        PlatIngredient(
            plat_id=5,
            ingredient_id=6,
            quantite_necessaire=Decimal("0.05")
        ),
        PlatIngredient(
            plat_id=5,
            ingredient_id=7,
            quantite_necessaire=Decimal("0.02")
        ),

        PlatIngredient(
            plat_id=9,
            ingredient_id=8,
            quantite_necessaire=Decimal("0.1")
        ),

        PlatIngredient(
            plat_id=10,
            ingredient_id=8,
            quantite_necessaire=Decimal("0.15")
        ),
    ]

    session.add_all(plat_ingredients)


    # =========================
    # 9. AVIS
    # =========================

    avis = [
        Avis(
            id=1,
            client_id=1,
            plat_id=1,
            note=4,
            commentaire="Très frais, poulet bien cuit",
            date_avis=datetime(2025, 7, 7, 13, 0)
        ),
        Avis(
            id=2,
            client_id=2,
            plat_id=4,
            note=5,
            commentaire="Meilleure pizza du coin !",
            date_avis=datetime(2025, 7, 7, 14, 0)
        ),
        Avis(
            id=3,
            client_id=3,
            plat_id=9,
            note=3,
            commentaire="Un peu trop épicé",
            date_avis=datetime(2025, 8, 15, 19, 0)
        ),
        Avis(
            id=4,
            client_id=4,
            plat_id=10,
            note=4,
            commentaire="Bon, mais manque de sauce",
            date_avis=datetime(2025, 9, 1, 21, 0)
        ),
        Avis(
            id=5,
            client_id=5,
            plat_id=6,
            note=5,
            commentaire="Glace délicieuse",
            date_avis=datetime(2025, 9, 10, 13, 0)
        ),
    ]

    session.add_all(avis)


    # =========================
    # COMMIT
    # =========================

    session.commit()

    print("Data inserted successfully!")