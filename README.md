# Facebook-Ads-Attribution
Facebook Ads iOS Attribution Fix for Shopify Stores With Short Funnels

Continuing from here: https://twitter.com/AsimAkhtar0/status/1415043223706292228

TL;DR - add this to ALL your Facebook Ad URL parameters to record ~30% more purchases.

`utm_medium=Facebook&utm_term={{adset.id}}&utm_content={{ad.id}}&utm_campaign={{campaign.name}}`

Should be added on the AD LEVEL.

![image](https://user-images.githubusercontent.com/87388055/125772183-593d4df8-edd0-40db-826d-b55966a3bde7.png)

Looks like this once done if you add the URL parameter column.

![image](https://user-images.githubusercontent.com/87388055/125774851-c0f83f02-5d17-4c6a-86d0-89b310f305cc.png)


## REPORTING:

**To read the data:**


### 1. Export Facebook adsmanager to CSV, sort by Adset ID (You need the adset ID column)

![image](https://user-images.githubusercontent.com/87388055/125773254-eb4c2160-e66e-45d7-aeee-81b77e894a3e.png)


### 2. Export Shopify reporting to CSV, sort by Adset ID (UTM Campaign term = Ad sets and Sessions Converted = Purchases columns needed)
https://YOURSTORE.myshopify.com/admin/reports/sessions_attributed_to_marketing

**In this example I'm only viewing ad sets and looking at purchases.**

![image](https://user-images.githubusercontent.com/87388055/125773442-2768956f-9d18-4bdd-81f9-ac77af73f80f.png)


### 3. Compare/combine into one CSV

Facebook exported file, sorted by Adset ID:
![image](https://user-images.githubusercontent.com/87388055/125775889-c98d86a2-051d-4d7c-ab86-e916646dcc92.png)

Shopify exported file, sorted by UTM Campaign Term = Adset ID:
![image](https://user-images.githubusercontent.com/87388055/125775997-8bcd227d-98a4-4a0a-ab1e-1a444273d9c7.png)


**Copy purchase data over:**

![image](https://user-images.githubusercontent.com/87388055/125776587-074149e4-b4e4-4f3a-b81b-cff0a3156e32.png)

![image](https://user-images.githubusercontent.com/87388055/125776674-bf1bbcfb-4a78-4f0e-9700-e79d963c702d.png)


### 4. Read data as appropriate

![image](https://user-images.githubusercontent.com/87388055/125776956-b39a3912-47b4-42c7-9978-77fda6658d06.png)


Is there an easier way? Ish. 

I could create an app that integrates Shopify + Facebook, but it would only save you a 3-5 minutes of time, and waste weeks of mine.

You could also create a program that does the end bit (combining the CSV files) and making data look pretty, but it would probably only save you a few minutes.

>> I did this with main2.py -- you will have to install python and use pip install pandas csv os


>> You will also have to have your "Facebook.csv" (Facebook adsmanager export on "Ad set" level) and "Shopify.csv" (Shopify reports with "total_orders_placed" = sessions converted and "utm_campaign_term" columns in the same folder as main2.py

Feel free to adjust main2.py if you need a solution for viewing ad sets, should be fairly simple. Instead of sorting by ad set IDs, sort by ad IDs and use an "ad" export instead of "ad set id"

>> Note: I only use 1 creative per ad set. You probably should too. 2-3 creatives doesn't work well these days due to iOS updates.


>> Output file will be called Final Sorted CSV and give you something like this:

![image](https://user-images.githubusercontent.com/87388055/125993589-8cb7f99a-fccd-4ee0-87f6-17943ee1a5dd.png)

You SHOULD NOT be checking your ad sets every single day regardless, so 5 minutes per 3-4 days/week is negligible.


After $30k+/day ad spend you might consider using an easier method. Till then, this is my "quick fix".
