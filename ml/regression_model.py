import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


def regression_example(input_csv="../data_cleaning/clean_data.csv"):
    df = pd.read_csv(input_csv)

    # Sélection des variables explicatives
    features = ["rent_index", "groceries_index", "crime_index", "safety_index"]
    target = "cost_of_living_index"

    df.dropna(subset=features + [target], inplace=True)

    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    print("\n📌 Évaluation du modèle de régression linéaire :")
    print(f"✅ RMSE : {rmse:.2f}")
    print(f"✅ R² : {r2:.2f}")

    # Visualisation
    plt.figure(figsize=(8, 5))
    plt.scatter(y_test, y_pred, alpha=0.7)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color="red", linestyle="--")
    plt.xlabel("Valeurs réelles")
    plt.ylabel("Valeurs prédites")
    plt.title("Régression : Prédictions vs Réalités")
    plt.show()

    # Coefficients du modèle
    coeffs = dict(zip(features, model.coef_))
    print("📌 Coefficients du modèle :", coeffs)
    print("📌 Intercept :", model.intercept_)


if __name__ == "__main__":
    regression_example()
