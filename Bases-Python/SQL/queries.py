from sqlalchemy import (
    select,
    func,
    desc,
    asc,
    and_,
    or_,
    
)

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


# 3  Plats prix order decroissant

with SessionLocal() as session:
    
    stmt = select(Plat).order_by(desc(Plat.prix))
    
    plats = session.scalars(stmt).all()
    
    for plat in plats:
        print(plat.nom, plat.prix)
        
        
# 4 Plats between 30 and 80

with SessionLocal() as session:
    
    stmt = select(Plat).where(Plat.prix.between(30, 80))
    
    plats = session.scalars(stmt).all()
    
    for plat in plats:
            print(plat.nom, plat.prix)
            
            
#5 Clients names start with S or F

with SessionLocal() as session:
    
    stmt = select(Client).where(or_(Client.nom.like("S%"),
                                    Client.nom.like("F%")))
    
    clients = session.scalars(stmt).all()
    
    for client in clients:
        print(client.nom)
        

# 6 --- Afficher les plats avec leur nom de catégorie et le nom du fournisseur principal (via l'ingrédient le plus utilisé).

with SessionLocal() as session:
    stmt = (
    select(
        Plat.nom,
        Category.nom,
        Fournisseur.nom
    )
    .join(Category, Category.id == Plat.categorie_id)
    .join(PlatIngredient, PlatIngredient.plat_id == Plat.id)
    .join(Ingredient, Ingredient.id == PlatIngredient.ingredient_id)
    .join(Fournisseur, Fournisseur.id == Ingredient.fournisseur_id)
)

result = session.execute(stmt).all()

for row in result:
    print(row)
        
        
#7 - comnds + client + nmbr de plats

with SessionLocal() as session:
    
    stmt = (
    select(
        Commande.id ,
        Client.nom ,
        Commande.date_commande ,
        func.sum(CommandePlat.quantite).label(
            "number_plats"
        )
        )
        .join(
            Client,
            Client.id == Commande.client_id
        )
        .join(
            CommandePlat,
            CommandePlat.commande_id == Commande.id
        )
        .group_by(
            Commande.id,
            Client.nom,
            Commande.date_commande
        )
    )

results = session.execute(stmt).all()

for row in results:
        print(
            row.id,
            row.nom,
            row.date_commande,
            row.number_plats
        )
        
        
        
# 8  -  Commandes + plats + quantity + cout  ingredients




# 9 Nombre de plats par catgory

with SessionLocal() as session:
    
    stmt = (
    select(
        Category.nom,
        func.count(Plat.id).label("nombre_plats")
    )
    .join(
        Plat,
        Plat.categorie_id == Category.id
    )
    .group_by(
        Category.id,
        Category.nom
    )
)

result = session.execute(stmt).all()

for row in result:
    print(row)
    
    
# 11 nuumber of orders per client

with SessionLocal() as session:
    
    stmt = (
    select(
        Client.nom,
        func.count(Commande.id).label("nombre_commandes")
    )
    .join(
        Commande,
        Commande.client_id == Client.id
    )
    .group_by(
        Client.id,
        Client.nom
    )
    .order_by(
        func.count(Commande.id).desc()
    )
)

result = session.execute(stmt).all()

for row in result:
    print(row)
    

#12 Clients with more than 2 orders

with SessionLocal() as session:
    
    stmt = (
    select(
        Client.nom,
        func.count(Commande.id).label("nombre_commandes")
    )
    .join(
        Commande,
        Commande.client_id == Client.id
    )
    .group_by(
        Client.id,
        Client.nom
    )
    .having(
        func.count(Commande.id) > 2
    )
)

result = session.execute(stmt).all()

for row in result:
    print(row)
    
    
#13 Plats ordered more than 3 times + average rating

with SessionLocal() as session:
    
    rating = (
    select(
        Avis.plat_id,
        func.avg(Avis.note).label("note_moyenne")
    )
    .group_by(Avis.plat_id)
    .subquery()
)

stmt = (
    select(
        Plat.nom,
        func.sum(
            CommandePlat.quantite
        ).label("quantite_totale"),
        rating.c.note_moyenne
    )
    .join(
        CommandePlat,
        CommandePlat.plat_id == Plat.id
    )
    .join(
        rating,
        rating.c.plat_id == Plat.id
    )
    .group_by(
        Plat.id,
        Plat.nom,
        rating.c.note_moyenne
    )
    .having(
        func.sum(CommandePlat.quantite) > 3
    )
)

result = session.execute(stmt).all()

for row in result:
    print(row)
    
    
#14 Orders in Q3(jullly august september) 2025

with SessionLocal() as session:
    
    from datetime import datetime

start = datetime(2025, 7, 1)
end = datetime(2025, 10, 1)

stmt = (
    select(Commande)
    .where(
        Commande.date_commande >= start,
        Commande.date_commande < end
    )
)

commandes = session.scalars(stmt).all()

for commande in commandes:
    print(
        commande.id,
        commande.date_commande
    )
    
    
    
# 15 Afficher la commande la plus récente avec le nom du client et les plats commandés.

with SessionLocal() as session:
    
    stmt = select(Commande.date_commande,
                Client.nom,
                Plat.nom.label("nom_plat")
            ).join(
                Client,
                Client.id == Commande.client_id
            ).join(
                CommandePlat,
                CommandePlat.commande_id == Commande.id
            ).join(
                Plat,
                CommandePlat.plat_id == Plat.id
            ).order_by(
                Commande.date_commande.desc()
            )
        
    results = session.execute(stmt).all()
    
    for row in results:
        print(
            row.date_commande,
            row.nom,
            row.nom_plat
              )


# 16 --- Afficher les clients ayant passé une commande d’un montant supérieur à 150, avec leur numéro de téléphone.

with SessionLocal() as session:
    
    stmt = select(Client.nom,
                  Commande.total,
                  Client.telephone
                  ).join(
                      Commande,
                      Commande.client_id == Client.id
                      ).where(
                      Commande.total > 150
                  )
                  
    results_clients = session.execute(stmt).all()
    
    for cl in results_clients:
        print(
            cl.nom,
            cl.total,
            cl.telephone
        )
        
        
# 17 --- Plat Cout Total ingredients superireur 50% price Plat

with SessionLocal() as session:
    
    stmt = select(Plat.nom,
                  Plat.prix,
                  func.sum(Ingredient.cout_unitaire * PlatIngredient.quantite_necessaire)
                       .label("cout_total_ingredients"),
                  ).join(
                      PlatIngredient,
                      Plat.id == PlatIngredient.plat_id
                  ).join(
                      Ingredient,
                      Ingredient.id == PlatIngredient.ingredient_id
                  ).group_by(
                      Plat.nom,
                      Plat.prix
                  ).having(
                      func.sum(Ingredient.cout_unitaire * PlatIngredient.quantite_necessaire) > Plat.prix / 2
                  )
                  
    results1 = session.execute(stmt).all()
    for pl in results1:
        print(pl.nom,
              pl.prix,
              pl.cout_total_ingredients)
        
        
# 18 - add new dish with two ingredients 

with SessionLocal() as session:
    plat = Plat(
        id=11,
        nom="Salade Veg",
        prix=20.00,
        description="Salade Végétarien",
        categorie_id=5
    )
    
    #session.add(plat)
    #session.commit()
    print("plaaat added successs !!")
    
    
#19 delete client
from sqlalchemy import delete

with SessionLocal() as session:
    
    client = session.scalar(
        select(Client).where(
            Client.nom == "Youssef El Khalfi")
    )
    
    #session.delete(client)
    session.commit()
    print("Youssef Khalfiii  deleted successs !!")
    
    
# 20 --- Afficher pour chaque client (nom - nombre total de plats commandés - montant total dépensé - note moyenne de leurs avis )

with SessionLocal() as session:
    
    
    total_plats = (
        select(
            Commande.client_id,
            func.sum(CommandePlat.quantite).label("total_plats_commande")
        ).join(
            CommandePlat,
            CommandePlat.commande_id == Commande.id
        ).group_by(
            Commande.client_id
        ).subquery()
    )
    
    total_depense = (
        select(
            Commande.client_id,
            func.sum(Commande.total).label("total_depenses")
        ).group_by(
            Commande.client_id
        ).subquery()
    )
    
    avg_avis =(
        select(
            Avis.client_id,
            func.avg(Avis.note).label("avvg_avis")
        ).group_by(
            Avis.client_id
        ).subquery()
    )
    
    stmt = (
        select(Client.nom,
                    total_plats.c.total_plats_commande,
                    total_depense.c.total_depenses,
                    avg_avis.c.avvg_avis
                ).outerjoin(
                    total_plats,
                    Client.id == total_plats.c.client_id
                ).outerjoin(
                    total_depense,
                    Client.id == total_depense.c.client_id
                ).outerjoin(
                    avg_avis,
                    Client.id == avg_avis.c.client_id
                )
            )
                
    results = session.execute(stmt).all()
    for row in results:
        print(
            row.nom,
            row.total_plats_commande,
            row.total_depenses,
            row.avvg_avis
        )
        
        
# 21 --- Lister les 3 plats les plus commandés (par quantité totale) avec leur catégorie

with SessionLocal() as session:
    
    stmt = (
        select(
            Plat.nom,
            func.sum(CommandePlat.quantite).label("total_quantity"),
            Category.nom.label("category_name")
        ).join(
            CommandePlat,
            CommandePlat.plat_id == Plat.id
        ).join(
            Category,
            Category.id == Plat.categorie_id
        ).group_by(
            Plat.id,
            Plat.nom,
            Category.nom
        ).order_by(
            func.sum(CommandePlat.quantite).desc()
        ).limit(3)
    )
    
    resultss = session.execute(stmt).all()
    
    for row in resultss:
        print(
            row.nom,
            row.total_quantity,
            row.category_name
            )