from .models import initialiser_donnees, consulter_stock_central, generer_rapport_consolide, synchroniser_stock


def main():
	initialiser_donnees()
	print("Stock central:", consulter_stock_central())
	synchroniser_stock(1, 1, 120)
	print("Après sync:", consulter_stock_central())
	print("Rapport:", generer_rapport_consolide())


if __name__ == "__main__":
	main()

