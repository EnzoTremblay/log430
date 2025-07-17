
# Architecture multi-magasins, centre logistique, maison mère
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
import os

Base = declarative_base()

class Produit(Base):
    __tablename__ = 'produits'
    id = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False, index=True)
    categorie = Column(String, nullable=False, index=True)
    prix = Column(Float, nullable=False)

class Magasin(Base):
    __tablename__ = 'magasins'
    id = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False)
    quartier = Column(String, nullable=False)
    stock = relationship('StockMagasin', back_populates='magasin')

class StockMagasin(Base):
    __tablename__ = 'stock_magasins'
    id = Column(Integer, primary_key=True)
    magasin_id = Column(Integer, ForeignKey('magasins.id'))
    produit_id = Column(Integer, ForeignKey('produits.id'))
    quantite = Column(Integer, nullable=False)
    magasin = relationship('Magasin', back_populates='stock')
    produit = relationship('Produit')

class CentreLogistique(Base):
    __tablename__ = 'centre_logistique'
    id = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False)

class StockLogistique(Base):
    __tablename__ = 'stock_logistique'
    id = Column(Integer, primary_key=True)
    centre_id = Column(Integer, ForeignKey('centre_logistique.id'))
    produit_id = Column(Integer, ForeignKey('produits.id'))
    quantite = Column(Integer, nullable=False)
    produit = relationship('Produit')

class MaisonMere(Base):
    __tablename__ = 'maison_mere'
    id = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False)

class Vente(Base):
    __tablename__ = 'ventes'
    id = Column(Integer, primary_key=True)
    magasin_id = Column(Integer, ForeignKey('magasins.id'))
    total = Column(Float, nullable=False)
    date = Column(DateTime, nullable=False, index=True)

DB_FILE = "sqlite:///magasin.db"
engine = create_engine(DB_FILE)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

# Initialisation des entités pour le prototype
def initialiser_donnees():
    session = Session()
    session.query(StockMagasin).delete()
    session.query(Magasin).delete()
    session.query(Produit).delete()
    session.query(CentreLogistique).delete()
    session.query(StockLogistique).delete()
    session.query(MaisonMere).delete()

    produits = [
        Produit(id=1, nom='Outil', categorie='Bricolage', prix=10.0),
        Produit(id=2, nom='Stylo', categorie='Papeterie', prix=1.5),
        Produit(id=3, nom='Chaise', categorie='Mobilier', prix=50.0)
    ]
    session.add_all(produits)

    magasins = [
        Magasin(id=1, nom='Magasin A', quartier='Nord'),
        Magasin(id=2, nom='Magasin B', quartier='Sud'),
        Magasin(id=3, nom='Magasin C', quartier='Est'),
        Magasin(id=4, nom='Magasin D', quartier='Ouest'),
        Magasin(id=5, nom='Magasin E', quartier='Centre')
    ]
    session.add_all(magasins)

    for magasin in magasins:
        for produit in produits:
            session.add(StockMagasin(magasin_id=magasin.id, produit_id=produit.id, quantite=100))

    centre = CentreLogistique(id=1, nom='Centre Logistique Principal')
    session.add(centre)
    for produit in produits:
        session.add(StockLogistique(centre_id=centre.id, produit_id=produit.id, quantite=500))

    maison_mere = MaisonMere(id=1, nom='Maison Mère')
    session.add(maison_mere)

    session.commit()
    session.close()

def synchroniser_stock(magasin_id, produit_id, quantite):
    session = Session()
    stock = session.query(StockMagasin).filter_by(magasin_id=magasin_id, produit_id=produit_id).first()
    if stock:
        stock.quantite = quantite
        session.commit()
    session.close()

def consulter_stock_central():
    session = Session()
    stocks = session.query(StockLogistique).all()
    result = {s.produit.nom: s.quantite for s in stocks}
    session.close()
    return result

def generer_rapport_consolide():
    session = Session()
    rapport = {}
    magasins = session.query(Magasin).all()
    for magasin in magasins:
        ventes = session.query(Vente).filter_by(magasin_id=magasin.id).all()
        total_ventes = sum(v.total for v in ventes)
        rapport[magasin.nom] = {
            'total_ventes': total_ventes,
            'ventes': len(ventes)
        }
    session.close()
    return rapport

def main():
    print("Bienvenue dans le système multi-magasins !")
    initialiser_donnees()
    print("Données initialisées.")
    print("1. Consulter le stock central")
    print("2. Générer un rapport consolidé des ventes")
    print("3. Synchroniser le stock d'un magasin")
    print("4. Quitter")
    choix = input("Choisissez une option : ")
    if choix == "1":
        print("Stock central :", consulter_stock_central())
    elif choix == "2":
        print("Rapport consolidé :", generer_rapport_consolide())
    elif choix == "3":
        magasin_id = int(input("ID du magasin : "))
        produit_id = int(input("ID du produit : "))
        quantite = int(input("Nouvelle quantité : "))
        synchroniser_stock(magasin_id, produit_id, quantite)
        print("Stock synchronisé.")
    else:
        print("Au revoir !")

if __name__ == "__main__":
    main()
