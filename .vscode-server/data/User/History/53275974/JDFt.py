import sqlite3
import os

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

    # Insertion de données de test
    cursor.execute("DELETE FROM produits")  # Nettoyer les données existantes
    produits_test = [
        (1, 'Outil', 'Bricolage', 10.0, 100),
        (2, 'Stylo', 'Papeterie', 1.5, 200),
        (3, 'Chaise', 'Mobilier', 50.0, 50)
    ]
    cursor.executemany("INSERT INTO produits (id, nom, categorie, prix, stock) VALUES (?, ?, ?, ?, ?)", produits_test)

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
    total = 0
    for produit in produits:
        cursor.execute("SELECT prix FROM produits WHERE id = ?", (produit['id'],))
        prix = cursor.fetchone()
        if prix:
            total += prix[0] * produit['quantite']
        else:
            raise ValueError(f"Produit avec ID {produit['id']} introuvable.")
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
    docker_env = os.environ.get("DOCKER_CONTAINER")
    print(f"DOCKER_CONTAINER environment variable: {docker_env}")
    if docker_env:
        print("Exécution en mode conteneur. Interaction utilisateur désactivée.")
        print("DOCKER_CONTAINER variable detected.")
        print("Veuillez utiliser une interface externe pour interagir avec l'application.")
        return
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
