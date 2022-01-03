import pandas as pd
import matplotlib.pyplot as plt

df_small = pd.read_csv("https://raw.githubusercontent.com/hainmit09/DataAnalysis/main/OnlineRetail_small_fixed.csv")
print(df_small.info())
# công ty bán hàng của bao nhiêu quốc gia
countrys = df_small.Country.unique()
print("số lượng công ty của quốc gia bán hàng:", str(countrys.size))
# số lượng đơn hàng bán ra và tổng doanh thu
df_small["total"] = df_small["Quantity"]* df_small["UnitPrice"]
print("sô lượng doanh thu:",df_small["Quantity"].sum())
print("tổng giá trị của các đơn hàng: ", df_small["total"].sum())
# top 10 mặt hàng bán ra nhiều nhất
quantity_product = df_small.groupby(['Description'])[["Quantity"]].sum()
a = quantity_product.sort_values("Quantity", ascending= False)
print(a.head(10))
# top 10 mặt hàng có doanh thu lớn nhất
total_product = df_small.groupby(['Description'])[["total"]].sum()
b = total_product.sort_values("total", ascending= False)
print("top 10 mặt hàng có danh thu lớn nhất:\n ", b.head(10))



