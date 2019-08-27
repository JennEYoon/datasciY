import pandas as pd

mydata = 
manhattanBedrmsPrice = pd.DataFrame(data=xmydata, dtype=int64)

0      859
5     1055
9      615
11     663
13    1317
Name: Price Value, dtype: int64


bins = [400,600,800,1000,1200, 1400,1600,1800,2000,2200,2400,2600,2800,3000]

manPriceCategories = pd.cut(manhattanBedrmsPrice, bins)