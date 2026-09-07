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
    
    stmt = select(Client).where(or_(Client.nom.like("S%"), Client.nom.like("F%")))
    
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
