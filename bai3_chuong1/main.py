import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("./GDPlist.csv", encoding="windows-1252")
colunms = df.info()
print(colunms)

print("số dòng và cột là:",df.shape)
# mỗi châu lục có bao nhiêu quốc gia nằm trong bảng 
data_continent = df.groupby('Continent')[['Country']].count()
print("châu lục có số lượng quốc gia:\n", data_continent)
# tổng số gdp của các châu lục
gdp_continent = df.groupby("Continent")[['GDP (millions of US$)']].sum()
print("tổng số gdp của từng châu lục:\n", gdp_continent)
#top 10 quốc gia cso gdp cao nhất :
gdp_country_max = df.groupby("Country")[['GDP (millions of US$)']].sum().sort_values('GDP (millions of US$)', ascending= False)
print("top 10 quốc gia có GDP cao nhất :\n ", gdp_country_max.head(10))
# phân tích sự đồng đều gdp
print("=========================================================================")
gdp_country = df.groupby("Country")[['GDP (millions of US$)']].sum()
print(gdp_country)

plt.hist(gdp_country['GDP (millions of US$)'], bins=10)
plt.title("Phân bố GDP của các quốc gia")

plt.show()