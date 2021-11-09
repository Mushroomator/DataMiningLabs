import pandas as pd

# Read top selling articles except article 100013
# facttab = pd.read_csv("facttab.csv", sep=";", usecols=["PSID", "quantity"])
# prodtab = pd.read_csv("product.csv", sep=";", usecols=["PSID", "artid", "name"])
#
# # join fact and product table
# joinFactProd = pd.merge(left=facttab, right=prodtab, on="PSID")
# # only keep the entries that do not have artid == 100013
# artFiltered = joinFactProd[joinFactProd.artid != 100013]
# result = artFiltered.groupby(["PSID", "artid", "name"]).sum().sort_values("quantity", ascending=False)
# print(result[:10])


#
facttab = pd.read_csv("facttab.csv", sep=";", usecols=["PSID", "CSID","quantity"])
prodtab = pd.read_csv("product.csv", sep=";", usecols=["PSID", "artid", "name"])

# join fact and product table
joinFactProd = pd.merge(left=facttab, right=prodtab, on="PSID")
print(joinFactProd.shape)
# get all customers which bought article 100013
custBoughtArt = joinFactProd[joinFactProd.artid == 100013].CSID
merged = pd.merge(left=custBoughtArt, right=joinFactProd, on="CSID")
print(merged)
#custBoughtAnother = joinFactProd[joinFactProd.artid != 100013]
#result = merged.groupby(["PSID", "CSID", "artid", "name"]).sum().sort_values("quantity", ascending=False)
#print(result[:10])