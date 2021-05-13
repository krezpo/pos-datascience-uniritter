import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_excel("data.xlsx", engine='openpyxl')

x = df[["Unidades", "Leitos por Unidade", "Custo Médio - RS"]]
y = df["Pedido Ideal"]

linear_regression = LinearRegression()

linear_regression.fit(x, y)

new_sample = np.array([[130, 100, 2.63]])
y_pred = linear_regression.predict(new_sample)

print("O pedido ideal para esse new_sample é: {}".format(y_pred))