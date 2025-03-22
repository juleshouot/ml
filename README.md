# cost_of_living_project

Ce projet illustre un pipeline complet pour récupérer, nettoyer et analyser les données du coût de la vie
(à titre d'exemple, depuis Numbeo).

## Structure du projet

- **scraping/** : contient le script `scrape_data.py` et `requirements.txt`.
- **data_cleaning/** : contient `clean_data.py` pour le nettoyage.
- **ml/** : contient plusieurs scripts ML (clustering, régression, classification).
- **data/** : stockage des CSV (données brutes `raw_data.csv`, données nettoyées `clean_data.csv`, etc.).

## Étapes de base

1. **Installer** les dépendances depuis `scraping/requirements.txt` (et `pip install scikit-learn matplotlib` pour la partie ML).
2. **Scraper** : `cd scraping && python scrape_data.py` pour générer `data/raw_data.csv`.
3. **Nettoyer** : `cd ../data_cleaning && python clean_data.py` pour générer `data/clean_data.csv`.
4. **Analyser** : 
   - `cd ../ml && python cluster_analysis.py`
   - `python regression_model.py`
   - `python classification_model.py`
"# MonProjet" 
