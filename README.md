# Laptop Sales Distribution in Flipkart
## Problem Statement
The objective of this project is to analyze the sales data of different laptop products in Flipkart. So first I scraped [this](https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_df6b6d84-2193-4f7e-9610-33baa9b5d33c_1_372UD5BXDFYS_MC.34WHNYFH5V2Y&otracker=hp_rich_navigation_8_1.navigationCard.RICH_NAVIGATION_Electronics~Laptop%2Band%2BDesktop_34WHNYFH5V2Y&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_8_L1_view-all&cid=34WHNYFH5V2Y&page=1) website for creating the dataset. Later I used it to create a Tableau Public Dashboard. For creating I used different tool components like Filters, Marks, Dimensions, Measure Names, Calculated Values, Custom Functions, Built-in functions and lot more.
1. Find out each brand of laptop's market share by their collective revenue in different products.
2. Divide the total market into 3 segments:- High-end Market, Middle-end Market, Low-end Market according to price range, show a comparison.
3. Show the distribution of operating system across brands and their concentration.
4. Show top 15 trending products that has more number of interactions, compare with price and discount.
   
You can visit the public dashboard [here](https://public.tableau.com/app/profile/md.sajjad.hossain6563/viz/LaptopSalesDistributioninFlipkart/LaptopSalesDistributioninFlipkart?publish=yes).

# Findings and Observations from the Dashboard
1. Overall Microsoft has the highest cut of market share considering their product's monetary value. In the high-end market also Microsoft has the highest cut. But in middle-end market and low-end market the leaders are Asus and HP respectively.
2. Microsoft has the highest number of products in the market.
3. The number Windows OS laptops are higher than any other OS, where 2nd positioned chrome OS is too far from the number of Windows OS laptops.
4. Among the top 15 trending products those have the highest number of reviews, also has very good portion of discounts. So dicounted products are more active in comparison to those static priced products.

# Build from sources
1. Clone the repo
   ```git
   git clone https://github.com/SajjadHossain43/Project--Web-scraping---Visualization-.git
   ```
2. Create and activate virtual environment
   ```git
   virtualenv --no-site-packages venv
   ```
3. Install dependencies
   ```git
   pip install -r requirements.txt
   ```
4. Run the scraper
   
