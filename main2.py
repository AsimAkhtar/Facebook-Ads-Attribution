import os
import csv
import pandas as pd

FILE_PATH = os.path.dirname(__file__)
FACEBOOK_ADSETS_FILE = os.path.join(FILE_PATH, "Facebook.csv")
SHOPIFY_FILE = os.path.join(FILE_PATH, "Shopify.csv")
SORTED_CSV = os.path.join(FILE_PATH, "Sorted.csv")
FINAL_SORTED_CSV = os.path.join(FILE_PATH, "Final Sorted.csv")


# FACEBOOK LIST CREATING THING

with open(FACEBOOK_ADSETS_FILE, newline='') as f:
    reader = csv.reader(f)
    facebook_data = list(reader)

facebook_first_col = facebook_data[0]

for z in range(len(facebook_first_col)):
    if "spent" in facebook_first_col[z]:
        spent_val = z
    if "Ad set ID" in facebook_first_col[z]:
        adsetid_val = z
    if "Ad Set Name" in facebook_first_col[z]:
        adsetname_val = z

spent_list = []
adsetid_list = []
adsetname_list = []

for y in range(len(facebook_data)):
    if "spent" not in facebook_data[y][spent_val]:
        spent_list.append(str(facebook_data[y][spent_val]))

for y in range(len(facebook_data)):
    if "Ad set ID" not in facebook_data[y][adsetid_val]:
        adsetid_list.append(str(facebook_data[y][adsetid_val]))

for y in range(len(facebook_data)):
    if "Ad Set Name" not in facebook_data[y][adsetname_val]:
        adsetname_list.append(str(facebook_data[y][adsetname_val]))

# SHOPIFY LIST CREATING THING

with open(SHOPIFY_FILE, newline='') as f:
    reader = csv.reader(f)
    shopify_data = list(reader)

shopify_first_col = shopify_data[0]

for z in range(len(shopify_first_col)):
    if "campaign_term" in shopify_first_col[z]:
        campaign_val = z
    if "orders_placed" in shopify_first_col[z]:
        ordersplaced_val = z

campaign_list = []
ordersplaced_list = []

for y in range(len(shopify_data)):
    if "campaign_term" not in shopify_data[y][campaign_val]:
        campaign_list.append(str(shopify_data[y][campaign_val]))

for y in range(len(shopify_data)):
    if "orders_placed" not in shopify_data[y][ordersplaced_val]:
        ordersplaced_list.append(str(shopify_data[y][ordersplaced_val]))

# COMPARING SHOPIFY DATA TO FACEBOOK DATA

new_campaign_list = []
new_ordersplaced_list = []

if len(campaign_list) == len(ordersplaced_list):

    for a in range(len(campaign_list)):
        if str(campaign_list[a]) in adsetid_list:
            new_campaign_list.append(campaign_list[a])
            new_ordersplaced_list.append(ordersplaced_list[a])

campaign_list = new_campaign_list
ordersplaced_list = new_ordersplaced_list

new_spent_list = ["ASDF"] * len(campaign_list)

for adsetid in campaign_list: # Shopify
    if adsetid in adsetid_list: # Facebook
        index1 = adsetid_list.index(adsetid)
        index2 = campaign_list.index(adsetid)
        new_spent_list[index2] = spent_list[index1]

cpp_list = []

for x in range(len(new_spent_list)):
    cost = float(new_spent_list[x])
    purchase = float(ordersplaced_list[x])
    if purchase != 0:
        cpp = cost / purchase
    else:
        cpp = 0
    cpp = round(cpp, 2)
    cpp_list.append(str(cpp))



new_adsetname_list = ["ASDF"] * len(campaign_list)

ss = -1

""" for adsetid in adsetid_list:
    index3 = campaign_list.index(adsetid)
    ss += 1
    new_adsetname_list[index3] = adsetname_list[ss]

for adsetid in campaign_list: # Shopify
    if adsetid in adsetid_list: # Facebook
        index1 = adsetid_list.index(adsetid)
        index2 = adsetname_list.index(adsetid)
        new_adsetname_list[index2] = adsetname_list[index1] """


rows = zip(new_adsetname_list,campaign_list,new_spent_list,ordersplaced_list,cpp_list)

with open(SORTED_CSV, "w") as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)

df = pd.read_csv(SORTED_CSV)
df.to_csv(FINAL_SORTED_CSV, index=False)

df = pd.read_csv(FINAL_SORTED_CSV, 
                  sep=',', 
                  names=["Ad set name", "Ad set ID", "Amount spent","Purchases", "Cost Per Purchase"])

df.to_csv(FINAL_SORTED_CSV, index=False)

os.remove(SORTED_CSV)

# print(campaign_list)
# print(ordersplaced_list)
# print(new_spent_list)
# print(cpp_list)

# df = pd.DataFrame(campaign_list, columns=["Ad set ID"])
# df.to_csv(SORTED_CSV, index=False)

# print(campaign_list)
# print(ordersplaced_list)
# print(shopify_dict)


# print("hi")

# for a in range(len(campaign_list)):
#     if str(campaign_list[a]) in adsetid_list:
#         print(campaign_list[a])

# print(spent_list)
# print(adsetid_list)
# print(campaign_list)
# print(ordersplaced_list)
