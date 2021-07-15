# Facebook-Ads-Attribution
Facebook Ads iOS Attribution Fix for Shopify Stores With Short Funnels

Continuing from here: https://twitter.com/AsimAkhtar0/status/1415043223706292228

TL;DR - add this to ALL your Facebook Ad URL parameters to record ~30% more purchases.

`utm_medium=Facebook&utm_term={{adset.id}}&utm_content={{ad.id}}&utm_campaign={{campaign.name}}`

Should be added on the AD LEVEL.

![image](https://user-images.githubusercontent.com/87388055/125772183-593d4df8-edd0-40db-826d-b55966a3bde7.png)

Looks like this once done if you add the URL parameter column.

![image](https://user-images.githubusercontent.com/87388055/125774851-c0f83f02-5d17-4c6a-86d0-89b310f305cc.png)


### REPORTING:

To read the data:


1. Export Facebook adsmanager to CSV, sort by Adset ID (You need the adset ID column)
![image](https://user-images.githubusercontent.com/87388055/125773254-eb4c2160-e66e-45d7-aeee-81b77e894a3e.png)


2. Export Shopify reporting to CSV, sort by Adset ID (UTM Campaign term = Ad sets and Sessions Converted = Purchases columns needed)
https://YOURSTORE.myshopify.com/admin/reports/sessions_attributed_to_marketing

In this example I'm only viewing ad sets and looking at purchases.
![image](https://user-images.githubusercontent.com/87388055/125773442-2768956f-9d18-4bdd-81f9-ac77af73f80f.png)

3. Compare/combine into one CSV

4. Read data as appropriate
