from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
import os

Base = declarative_base()

class Produit(Base):
    __tablename__ = 'produits'
    id = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False, index=True)  # Added index for faster queries
    categorie = Column(String, nullable=False, index=True)  # Added index for faster queries
    prix = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)

class Vente(Base):
    __tablename__ = 'ventes'
    id = Column(Integer, primary_key=True)
    total = Column(Float, nullable=False)
    date = Column(DateTime, nullable=False, index=True)  # Added index for faster queries

DB_FILE = "sqlite:///magasin.db"
engine = create_engine(DB_FILE)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

# Remplacer la logique SQLite par SQLAlchemy ORM
session = Session()

# Exemple : Ajout de données de test
session.query(Produit).delete()  # Nettoyer les données existantes
produits_test = [
    Produit(id=1, nom='Outil', categorie='Bricolage', prix=10.0, stock=100),
    Produit(id=2, nom='Stylo', categorie='Papeterie', prix=1.5, stock=200),
    Produit(id=3, nom='Chaise', categorie='Mobilier', prix=50.0, stock=50)
]
session.add_all(produits_test)
session.commit()
session.close()

def rechercher_produit(critere, valeur):
    session = Session()

    # Validation du critère
    colonnes_valides = ['id', 'nom', 'categorie']
    if critere not in colonnes_valides:
        raise ValueError(f"Critère invalide : {critere}. Les critères valides sont {colonnes_valides}.")

    resultats = session.query(Produit).filter(getattr(Produit, critere) == valeur).all()
    session.close()
    return resultats

def enregistrer_vente(produits):
    session = Session()
    total = 0
    for produit in produits:
        p = session.query(Produit).filter(Produit.id == produit['id']).first()
        if p:
            total += p.prix * produit['quantite']
        else:
            raise ValueError(f"Produit avec ID {produit['id']} introuvable.")
    nouvelle_vente = Vente(total=total)
    session.add(nouvelle_vente)
    session.commit()
    vente_id = nouvelle_vente.id
    for produit in produits:
        p = session.query(Produit).filter(Produit.id == produit['id']).first()
        if p:
            p.stock -= produit['quantite']
    session.commit()
    session.close()
    return vente_id

def consulter_stock(filter_nom=None):
    session = Session()
    if filter_nom:
        stock = session.query(Produit).filter(Produit.nom == filter_nom).all()
    else:
        stock = session.query(Produit).all()
    session.close()
    return stock

def main():
    print("Bienvenue dans le système de caisse du magasin !")
    docker_env = os.getenv("DOCKER_CONTAINER")
    print(f"DOCKER_CONTAINER environment variable: {docker_env}")

    if docker_env:
        print("Mode non interactif détecté. Passage par défaut à l'option 4 (Quitter).")
        choix = "4"
    else:
        print("1. Rechercher un produit")
        print("2. Enregistrer une vente")
        print("3. Consulter le stock")
        print("4. Quitter")
        try:
            choix = input("Choisissez une option : ")
        except EOFError:
            print("EOFError détecté. Passage par défaut à l'option 4 (Quitter).")
            choix = "4"

    print(f"Option choisie: {choix}")

if __name__ == "__main__":
    main()
