import pandas as pd

def clean_data(input_csv="../data/raw_data.csv", output_csv="clean_data.csv"):
    """
    Nettoie les données fusionnées de Numbeo en effectuant :
      - Chargement et renommage des colonnes
      - Conversion des indices en types numériques
      - Suppression des valeurs manquantes
      - Filtrage des valeurs aberrantes (ex. Crime Index > 100)
      - Suppression de la colonne Rank si elle est vide
      - Tri des villes (City) par ordre alphabétique
      - Sauvegarde des données nettoyées dans un fichier CSV
    """

    # 1. Charger le CSV brut
    df = pd.read_csv(input_csv)

    # 2. Vérifier et sélectionner les colonnes attendues
    expected_columns = [
        "Rank", "City",
        "Cost of Living Index", "Rent Index", "Cost of Living Plus Rent Index",
        "Groceries Index", "Restaurant Price Index", "Local Purchasing Power Index",
        "Crime Index", "Safety Index"
    ]

    available_columns = [col for col in expected_columns if col in df.columns]
    df = df[available_columns]  # Sélectionner uniquement les colonnes présentes

    # 3. Supprimer les lignes avec des valeurs manquantes sur des colonnes clés
    df.dropna(subset=["City", "Cost of Living Index", "Crime Index", "Safety Index"], inplace=True)

    # 4. Conversion des colonnes en types numériques
    numeric_cols = [
        "Cost of Living Index", "Rent Index", "Cost of Living Plus Rent Index",
        "Groceries Index", "Restaurant Price Index", "Local Purchasing Power Index",
        "Crime Index", "Safety Index"
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # 5. Gestion de la colonne Rank
    if "Rank" in df.columns:
        df["Rank"] = pd.to_numeric(df["Rank"], errors="coerce")
        if df["Rank"].isnull().all():  # Vérifie si Rank est complètement vide (NaN)
            df.drop(columns=["Rank"], inplace=True)
        else:
            df.sort_values(by="Rank", inplace=True, ignore_index=True)  # Trier par Rank si dispo

    # 6. Filtrage des valeurs aberrantes
    df = df[(df["Cost of Living Index"] <= 200) & (df["Crime Index"] <= 100) & (df["Safety Index"] <= 100)]

    # 7. Renommer les colonnes pour plus de lisibilité
    df.rename(columns={
        "City": "city",
        "Cost of Living Index": "cost_of_living_index",
        "Rent Index": "rent_index",
        "Cost of Living Plus Rent Index": "cost_of_living_plus_rent_index",
        "Groceries Index": "groceries_index",
        "Restaurant Price Index": "restaurant_price_index",
        "Local Purchasing Power Index": "local_purchasing_power_index",
        "Crime Index": "crime_index",
        "Safety Index": "safety_index"
    }, inplace=True)

    # 8. Trier par ordre alphabétique des villes si Rank a été supprimé
    if "Rank" not in df.columns:
        df.sort_values(by="city", inplace=True, ignore_index=True)

    # 9. Sauvegarder le CSV nettoyé
    df.to_csv(output_csv, index=False)
    print(f"✅ Données nettoyées enregistrées dans {output_csv}")

def main():
    clean_data(input_csv="../data/raw_data.csv", output_csv="clean_data.csv")

if __name__ == "__main__":
    main()