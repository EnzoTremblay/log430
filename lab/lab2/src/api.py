from flask import Flask, jsonify, request
from flask_cors import CORS
from .models import (
	initialiser_donnees,
	consulter_stock_central,
	generer_rapport_consolide,
	synchroniser_stock,
)


def create_app() -> Flask:
	app = Flask(__name__)
	CORS(app)
	initialiser_donnees()

	@app.route("/api/v1/stores/<int:magasin_id>/stock", methods=["GET"])
	def get_stock_magasin(magasin_id: int):
		stock = consulter_stock_central()
		return jsonify({"stock": stock}), 200

	@app.route("/api/v1/report", methods=["GET"])
	def get_rapport():
		rapport = generer_rapport_consolide()
		return jsonify({"rapport": rapport}), 200

	@app.route("/api/v1/products/<int:produit_id>", methods=["PUT"])
	def update_produit(produit_id: int):
		data = request.get_json(force=True) or {}
		# pour le scope du lab: on synchronise juste un stock si fourni
		quantite = data.get("quantite")
		magasin_id = data.get("magasin_id", 1)
		if quantite is not None:
			synchroniser_stock(int(magasin_id), int(produit_id), int(quantite))
		return jsonify({"produit": {"id": produit_id, **data}}), 200

	@app.route("/api/v1/dashboard", methods=["GET"])
	def get_dashboard():
		# Exemple d’indicateurs simples
		rapport = generer_rapport_consolide()
		nb_magasins = len(rapport)
		ventes_total = sum(v["total_ventes"] for v in rapport.values())
		indicateurs = {
			"nb_magasins": nb_magasins,
			"ventes_total": ventes_total,
		}
		return jsonify({"indicateurs": indicateurs}), 200

	return app


if __name__ == "__main__":
	app = create_app()
	app.run(host="0.0.0.0", port=5000)

