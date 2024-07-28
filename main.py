import pandas as pd

df=pd.read_csv("food delivery costs.csv")
df.head()
df.info()
df["Order Date and Time"]=pd.to_datetime(df["Order Date and Time"])
df["Delivery Date and Time"]=pd.to_datetime(df["Delivery Date and Time"])

def extract(value):
    a=str(value).split(" ")
    return a[0]

df["Discounts and Offers"]=df["Discounts and Offers"].apply(extract)

def removep(value):
    if "%" in value:
        a=value.replace("%"," ")
        return float(a)
    else:
        return float(value)
    
df["Discounts and Offers"]=df["Discounts and Offers"].apply(removep)

df.loc[(df["Discounts and Offers"]<=15),"Discounts and Offers"] = (df["Discounts and Offers"]/100)*df["Order Value"]
df["Discounts and Offers"]=df["Discounts and Offers"].fillna(0)

df["Costs"]=df["Delivery Fee"]+df["Discounts and Offers"]+df["Payment Processing Fee"]

df["Profit"]=df["Commission Fee"]-df["Costs"]
print(df["Profit"].sum())

cost_d=df[["Delivery Fee","Payment Processing Fee","Discounts and Offers"]].sum()
cost_d

import matplotlib.pyplot as plt

plt.figure(figsize=(3,3))
plt.pie(cost_d, labels=cost_d.index, autopct="%1.1f%%")
plt.show()

