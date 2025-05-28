import sqlite3

# Initialisation de la base de données
DB_FILE = "magasin.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produits (
        id INTEGER PRIMARY KEY,
        nom TEXT NOT NULL,
        categorie TEXT NOT NULL,
        prix REAL NOT NULL,
        stock INTEGER NOT NULL
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ventes (
        id INTEGER PRIMARY KEY,
        total REAL NOT NULL,
        date TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def rechercher_produit(critere, valeur):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Validation du critère
    colonnes_valides = ['id', 'nom', 'categorie']
    if critere not in colonnes_valides:
        raise ValueError(f"Critère invalide : {critere}. Les critères valides sont {colonnes_valides}.")

    query = f"SELECT * FROM produits WHERE {critere} = ?"
    cursor.execute(query, (valeur,))
    resultats = cursor.fetchall()
    conn.close()
    return resultats

def enregistrer_vente(produits):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    total = sum(p['prix'] * p['quantite'] for p in produits)
    cursor.execute("INSERT INTO ventes (total, date) VALUES (?, datetime('now'))", (total,))
    vente_id = cursor.lastrowid
    for produit in produits:
        cursor.execute("UPDATE produits SET stock = stock - ? WHERE id = ?", (produit['quantite'], produit['id']))
    conn.commit()
    conn.close()
    return vente_id

def consulter_stock():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produits")
    stock = cursor.fetchall()
    conn.close()
    return stock

def main():
    init_db()
    print("Bienvenue dans le système de caisse du magasin !")
    while True:
        print("1. Rechercher un produit")
        print("2. Enregistrer une vente")
        print("3. Consulter le stock")
        print("4. Quitter")
        choix = input("Choisissez une option : ")
        if choix == "1":
            critere = input("Rechercher par (id, nom, categorie) : ")
            valeur = input("Valeur : ")
            resultats = rechercher_produit(critere, valeur)
            print("Résultats :", resultats)
        elif choix == "2":
            produits = []
            while True:
                id_produit = int(input("ID du produit : "))
                quantite = int(input("Quantité : "))
                produits.append({"id": id_produit, "quantite": quantite})
                continuer = input("Ajouter un autre produit ? (o/n) : ")
                if continuer.lower() != "o":
                    break
            vente_id = enregistrer_vente(produits)
            print(f"Vente enregistrée avec l'ID {vente_id}")
        elif choix == "3":
            stock = consulter_stock()
            print("Stock actuel :", stock)
        elif choix == "4":
            print("Merci d'avoir utilisé le système de caisse. Au revoir !")
            break
        else:
            print("Option invalide.")

if __name__ == "__main__":
    main()
