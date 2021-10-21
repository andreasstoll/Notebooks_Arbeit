import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def create_quantity_series(table: pd.DataFrame, col: str) -> pd.Series:
    """Erstellt eine pd.Series die jedes Ausprägung in der Spalte col die Anzahl Vorkommnisse zuordnet"""
    quantity_dict = {}
    for element in table[col].unique():
        quantity_dict[element] = len(table[col].loc[table[col] == element])
    quantity_series = pd.Series(quantity_dict)
    quantity_series.name = col
    return quantity_series


def pie_chart(table: pd.DataFrame, col: str) -> None:
    """Erstellt ein Kuchendiagramm der Spalte col des Datensatzes table"""
    pie_chart_series = create_quantity_series(table, col)
    pie_chart_series.sort_index(inplace=True)
    ax = pie_chart_series.plot(kind="pie", autopct='%1.1f%%', labels=None)
    ax.legend(loc="upper right", bbox_to_anchor=(
        1.5, 1), labels=pie_chart_series.index)


def bar_chart(table: pd.DataFrame, col: str) -> None:
    """Erstellt ein Balkendiagramm der Spalte col des Datensatzes table"""
    pie_chart_series = create_quantity_series(table, col)
    ax = pie_chart_series.plot(kind="bar", rot=60)


def histogram(table: pd.DataFrame, col: str, bin: int) -> None:
    """Erstellt ein Histogramm der Spalte col des Datensatzes table, dabei gibt bin die Anzahl Kategorien an"""
    column = table[col]
    ax = column.plot.hist(bins=bin)


def box_plot(table: pd.DataFrame, col: str) -> None:
    """Erstellt einen Boxplot der Spalte col des Datensatzes table"""
    column = table[col]
    ax = column.plot.box()


def scatter_plot(table: pd.DataFrame, col1: str, col2: str) -> None:
    """Erstellt ein Streudiagramm der Spalte col des Datensatzes table"""
    ax = table.plot.scatter(x=col1, y=col2)


def r_value(table: pd.DataFrame, col1: str, col2: str) -> float:
    """Berechnet den Pearson-Korrelationskoeffizienten für x-Werte: col1 und y-Werte: col2"""
    new_db = pd.DataFrame(table, columns=[col1, col2])
    r = new_db.corr(method="pearson")
    return float(r.iloc[0][1])


def lr_plot(table: pd.DataFrame, col1: str, col2: str) -> None:
    """Erstellt ein Lineare-Regression-Diagramm für x-Werte: col1 und y-Werte: col2.
    Dieses Diagramm enthält ein Streudiagramm, eine Regressionsgerade, 
    die Funktionsgleichung der Regressionsgerade und den Korrelationskoeffizienten"""
    x = table[[col1]]
    y = table[[col2]]
    regressor = LinearRegression()
    linear_model = regressor.fit(x, y)
    m = round(float(linear_model.coef_), 3)
    q = round(float(linear_model.intercept_), 3)
    r = round(r_value(table, col1, col2), 3)
    y_prediction = regressor.predict(x)
    plt.scatter(x, y, color='red')
    plt.plot(x, y_prediction, color='blue')
    if q >= 0:
        plt.suptitle(f"Lineare Regression: y = {m}x+{q}, Korrelation: {r}")
    else:
        plt.suptitle(f"Lineare Regression: y = {m}x{q}, Korrelation: {r}")
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.show()
