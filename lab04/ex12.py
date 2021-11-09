import pandas as pd
import numpy as np

facttab = pd.read_csv("facttab.csv", sep=";", usecols=["PSID", "CSID"])
prodtab = pd.read_csv("product.csv", sep=";", usecols=["PSID", "artid", "name"])
custtab = pd.read_csv("customer.csv", sep=";", usecols=["CSID", "custid", "name"])

# Get all bought products
join1 = pd.merge(left=facttab, right=prodtab, on="PSID")
# Column which can be aggregates; each product is bought once
join1["times_bought"] = 1
# get customer infomation
join2 = pd.merge(left=join1, right=custtab, on="CSID")
# Sum up all the products per customer and product
prodsByCust = join2.groupby(["CSID", "custid", "PSID", "artid"]).agg({"times_bought": np.sum}).nlargest(3, columns=["times_bought"])
print("Products by customer")
print(prodsByCust)
#mostProdsByCust = prodsByCust.groupby("CSID")
#print(prodsByCust)
#print(prodsByCust.shape)
    #.sum().sort_values("times_bought", ascending=False)
#result = pd.DataFrame(columns=["CSID", "PSID", "artid", "custid", "times_bought"])

#groups = prodsByCust.groups.keys()
#print(len(groups), groups)

#for name, group in groups:
#    sorted = pd.DataFrame(columns=["CSID", "custid", "PSID", "artid", "time_bought"], data=group).sort_values("time_bought", ascending=False, inplace=True)
#    print(name, sorted[:3])
#prodsByCust.apply(lambda x: result.append(x[0], ignore_index=True))