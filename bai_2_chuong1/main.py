import pandas as pd
df = pd.read_csv("./OnlineRetail.csv", encoding='ISO-8859-1')
print(df.head(5))
print(df.info())
print("colunm:", df.columns)
print("row and colunms: ", df.shape)
# tổng số đơn hàng bán ra và doanh thu
df['total'] = df['Quantity']* df['UnitPrice']
doanh_thu = df['total'].sum()
print("tổng doanh thu:", str(doanh_thu))
print("tổng số đơn hàng: ", str(df['Quantity'].sum()))
code = df.StockCode.unique()
code_max = df.groupby("StockCode")[['Quantity']].sum().sort_values('Quantity', ascending= False)
print("số lượng mặt hàng: ", len(code))
print("top 10 mặt hàng bán chạy nhất: \n", code_max.head(10))
# top 10 mặt hàng có doanh thu cao nhất
doanh_thu_code_max = df.groupby("StockCode")[['total']].sum().sort_values('total', ascending= False)
print("top 10 mặt hàng có doanh thu cao nhất: ", doanh_thu_code_max.head(10))