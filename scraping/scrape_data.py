import requests
from bs4 import BeautifulSoup
import pandas as pd

# Fonction pour scraper les données générales (coût de la vie)
def scrape_numbeo_data(url="https://www.numbeo.com/cost-of-living/rankings.jsp"):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Erreur: statut {response.status_code}")
        return None
    soup = BeautifulSoup(response.text, 'lxml')

    # Trouver la table principale
    table = soup.find('table', {'id': 't2'})
    if not table:
        print("Table de coût de la vie non trouvée.")
        return None

    # Extraction des en-têtes
    headers = [th.get_text(strip=True) for th in table.find('thead').find_all('th')]

    # Extraction des lignes
    rows_data = []
    for tr in table.find('tbody').find_all('tr'):
        cols = tr.find_all('td')
        row = [col.get_text(strip=True) for col in cols]
        rows_data.append(row)

    # Création du DataFrame
    df = pd.DataFrame(rows_data, columns=headers)
    return df

# Fonction pour scraper le crime index
def scrape_crime_data(url="https://www.numbeo.com/crime/rankings.jsp"):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Erreur: statut {response.status_code}")
        return None
    soup = BeautifulSoup(response.text, 'lxml')

    # Trouver la table principale
    table = soup.find('table', {'id': 't2'})
    if not table:
        print("Table du crime index non trouvée.")
        return None

    # Extraction des en-têtes
    headers = [th.get_text(strip=True) for th in table.find('thead').find_all('th')]

    # Extraction des lignes
    rows_data = []
    for tr in table.find('tbody').find_all('tr'):
        cols = tr.find_all('td')
        row = [col.get_text(strip=True) for col in cols]
        rows_data.append(row)

    # Création du DataFrame
    df = pd.DataFrame(rows_data, columns=headers)

    # Renommer les colonnes utiles
    df = df[['City', 'Crime Index', 'Safety Index']]
    return df

# Fonction principale pour exécuter tout le scraping et fusionner les données
def main():
    print("Scraping des données du coût de la vie...")
    df_cost = scrape_numbeo_data()

    print("Scraping des données du crime index...")
    df_crime = scrape_crime_data()

    if df_cost is None or df_crime is None:
        print("Erreur lors du scraping. Vérifiez les sites sources.")
        return

    # Fusionner les données sur la colonne "City"
    df_merged = pd.merge(df_cost, df_crime, on="City", how="left")

    # Sauvegarde en CSV
    output_file = "../data/raw_data.csv"
    df_merged.to_csv(output_file, index=False)
    print(f"Données fusionnées enregistrées dans {output_file}")

if __name__ == "__main__":
    main()
