from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Produit:
	id: int
	nom: str
	categorie: str
	prix: float


@dataclass
class Magasin:
	id: int
	nom: str
	quartier: str


@dataclass
class Vente:
	magasin_id: int
	total: float


class DepotMemoire:
	def __init__(self):
		self.produits: Dict[int, Produit] = {}
		self.magasins: Dict[int, Magasin] = {}
		# stock[(magasin_id, produit_id)] = quantite
		self.stock: Dict[tuple, int] = {}
		self.ventes: List[Vente] = []

	def reset(self):
		self.produits.clear()
		self.magasins.clear()
		self.stock.clear()
		self.ventes.clear()


db = DepotMemoire()


def initialiser_donnees():
	db.reset()
	produits = [
		Produit(1, "Outil", "Bricolage", 10.0),
		Produit(2, "Stylo", "Papeterie", 1.5),
		Produit(3, "Chaise", "Mobilier", 50.0),
	]
	for p in produits:
		db.produits[p.id] = p

	magasins = [
		Magasin(1, "Magasin A", "Nord"),
		Magasin(2, "Magasin B", "Sud"),
	]
	for m in magasins:
		db.magasins[m.id] = m

	for m in magasins:
		for p in produits:
			db.stock[(m.id, p.id)] = 100


def synchroniser_stock(magasin_id: int, produit_id: int, quantite: int) -> None:
	if (magasin_id, produit_id) not in db.stock:
		# initialise si absent
		db.stock[(magasin_id, produit_id)] = 0
	db.stock[(magasin_id, produit_id)] = int(quantite)


def consulter_stock_central() -> Dict[str, int]:
	# Somme des quantités par produit (tous magasins)
	agr: Dict[int, int] = {}
	for (magasin_id, produit_id), q in db.stock.items():
		agr[produit_id] = agr.get(produit_id, 0) + q
	# retourne par nom de produit
	return {db.produits[pid].nom: qty for pid, qty in agr.items() if pid in db.produits}


def generer_rapport_consolide() -> Dict[str, dict]:
	rapport: Dict[str, dict] = {}
	for m in db.magasins.values():
		ventes = [v for v in db.ventes if v.magasin_id == m.id]
		total = round(sum(v.total for v in ventes), 2)
		rapport[m.nom] = {"total_ventes": total, "ventes": len(ventes)}
	return rapport

