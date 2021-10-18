import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def create_quantity_series(table: pd.DataFrame, col: str)->pd.Series:
    quantity_dict={}
    for element in table[col].unique():
        quantity_dict[element]= len(table[col].loc[table[col]==element]) 
    quantity_series = pd.Series(quantity_dict)
    quantity_series.name = col
    return quantity_series

def pie_chart(table: pd.DataFrame, col: str)->None:
    pie_chart_series = create_quantity_series(table, col)
    pie_chart_series.sort_index(inplace=True)
    ax=pie_chart_series.plot(kind="pie", autopct='%1.1f%%', labels=None)
    ax.legend(loc="upper right", bbox_to_anchor=(1.5, 1), labels=pie_chart_series.index)

def bar_chart(table: pd.DataFrame, col: str)->None:
    pie_chart_series = create_quantity_series(table, col)
    ax=pie_chart_series.plot(kind="bar", rot=60)

def histogram(table: pd.DataFrame, col: str, bin: int)-> None:
    column = table[col]
    ax = column.plot.hist(bins=bin)

def box_plot(table: pd.DataFrame, col: str)-> None:
    column = table[col]
    ax = column.plot.box()

def scatter_plot(table: pd.DataFrame, col1: str, col2: str)-> None:
    ax = table.plot.scatter(x=col1,y=col2)

def r_value(table: pd.DataFrame, col1: str, col2: str)->float:
    new_db = pd.DataFrame(table, columns= [col1, col2])
    r = new_db.corr(method="pearson")
    return float(r.iloc[0][1])
    
def lr_plot(table: pd.DataFrame, col1: str, col2:str)->None:
    x = table[[col1]]
    y = table[[col2]]
    regressor = LinearRegression()
    linear_model = regressor.fit(x, y)
    m = round(float(linear_model.coef_),3)
    q = round(float(linear_model.intercept_),3)
    r = round(r_value(table, col1, col2),3)
    y_prediction = regressor.predict(x)
    plt.scatter(x, y, color = 'red')
    plt.plot(x, y_prediction, color = 'blue')
    plt.suptitle(f"Lineare Regression: y = {m}x+{q}, Korrelation: {r}")
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.show()