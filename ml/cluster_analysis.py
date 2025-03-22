import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def cluster_analysis(input_csv="../data_cleaning/clean_data.csv"):
    df = pd.read_csv(input_csv)

    # Sélection des features utiles pour le clustering
    features = ["cost_of_living_index", "crime_index", "safety_index"]

    # Standardisation
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df[features])

    # K-Means avec 3 clusters
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    df["cluster"] = kmeans.fit_predict(X_scaled)

    # Affichage des clusters en scatter plot
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x=df["cost_of_living_index"], y=df["crime_index"], hue=df["cluster"], palette="Set1")
    plt.xlabel("Cost of Living Index")
    plt.ylabel("Crime Index")
    plt.title("Clustering des villes")
    plt.legend(title="Cluster")
    plt.show()

    # Moyenne par cluster
    print("\n📌 Moyenne des indices par cluster:")
    print(df.groupby("cluster")[features].mean())

    # Sauvegarde
    df.to_csv("../data/clustered_data.csv", index=False)
    print("✅ Clustering terminé. Fichier enregistré dans ../data/clustered_data.csv.")


if __name__ == "__main__":
    cluster_analysis()
