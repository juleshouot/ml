import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


def classification_example(input_csv="../data_cleaning/clean_data.csv"):
    df = pd.read_csv(input_csv)

    # Création d'une catégorie selon l'indice de coût de la vie
    def categorize_cost_of_living(x):
        if x < 50:
            return 0  # Bas
        elif x < 100:
            return 1  # Moyen
        else:
            return 2  # Élevé

    df["cost_category"] = df["cost_of_living_index"].apply(categorize_cost_of_living)

    # Sélection des features améliorées
    features = ["rent_index", "groceries_index", "crime_index", "safety_index"]
    target = "cost_category"

    df.dropna(subset=features + [target], inplace=True)

    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    clf = RandomForestClassifier(n_estimators=200, max_depth=10, min_samples_split=5, random_state=42)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    print(f"✅ Accuracy: {acc:.2f}")
    print("\n📌 Classification Report:")
    print(classification_report(y_test, y_pred))

    # Matrice de confusion
    plt.figure(figsize=(6, 4))
    sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt="d", cmap="Blues",
                xticklabels=["Bas", "Moyen", "Élevé"], yticklabels=["Bas", "Moyen", "Élevé"])
    plt.xlabel("Prédit")
    plt.ylabel("Réel")
    plt.title("Matrice de Confusion")
    plt.show()


if __name__ == "__main__":
    classification_example()
