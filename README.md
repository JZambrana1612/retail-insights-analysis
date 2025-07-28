# Retail Sales Insights

### Uncovering customer trends, product performance, and seasonal patterns using Python and data visualisation

This project analyses a sample retail sales dataset to answer key business questions about who buys what, when they buy it and how to prioritise inventory. Rather than treating the GitHub repository as the data source, this updated README references the original dataset provider. The sample retail data is hosted by **Gigasheet**, a spreadsheet‑like platform that offers open datasets for practice. Their page notes that the retail sales dataset contains **1,000 rows and 10 columns**, including transaction IDs, dates, customer information, product category, quantity and price. These fields allow analysts to explore sales trends, customer behaviour and total revenue without requiring database access.

---

## Executive Summary

This analysis answers three high‑impact questions that matter to retail decision‑makers:

1. **Which customer segments contribute most to revenue?** By analysing revenue and basket size by gender, we identify the customer groups that drive sales.
2. **How does purchase timing affect revenue?** Aggregating sales by month reveals seasonal peaks and troughs; these patterns guide inventory planning and marketing calendars.
3. **Which products should be prioritised?** Ranking product categories by total and average revenue highlights where merchandising and promotional budgets should be focused.

### Dashboard Overview

The planned dashboard (to be built after finalising the analysis) will include:

- **Segment‑based revenue breakdown:** charts summarising revenue and average basket size by gender.
- **Monthly revenue trend:** a line graph showing seasonal fluctuations across the year.
- **Product category comparison:** a bar chart ranking Beauty, Clothing and Electronics by total revenue and average revenue per transaction.

> A live dashboard will be created after the analytical work is finalised, using Python visualisations as a foundation.

---

## Actionable Recommendations

- **Target high‑value customer segments.** Female customers generated slightly higher total revenue and purchased marginally more items per transaction than males. Tailored promotions (e.g., bundle offers or loyalty perks) could increase their lifetime value.
- **Prioritise beauty products.** Beauty products delivered the highest total revenue and the highest average ticket value. Ensure adequate stock levels, highlight premium SKUs and consider bundling related items to maximise profitability.
- **Align marketing with seasonal peaks.** May 2023 produced the largest revenue spike, while March and September were slower months. Plan promotional campaigns and staffing schedules around these peaks and troughs to optimise resources.
- **Nurture high‑value transactions.** Several customers made large purchases (US $2,000). Identifying and rewarding these customers through VIP programmes or personalised outreach could enhance retention and encourage repeat purchases.

---

## Deep Dive: Analytical Approach

### Dataset Overview

The dataset analysed in this project originates from Gigasheet’s sample data gallery. According to the provider, the table contains **1,000 rows and 10 columns** with fields such as transaction ID, date, customer information, product category, quantity and price. These columns allow computation of revenue (quantity × price), basket size (number of items) and derived temporal dimensions (month, quarter). The data spans transactions between January 2023 and January 2024.

### Analytical Steps

1. **Data import & cleaning:** The CSV file was downloaded and loaded into pandas. Because the sample data was already clean, minimal preprocessing was needed. Sale dates were parsed as dates and revenue was computed where necessary.
2. **Aggregation:** Revenue and basket size were aggregated by gender and product category to understand customer and product performance. Monthly revenues were summed to identify seasonal patterns.
3. **Visualisation:** Bar charts and line charts were created using seaborn/matplotlib to communicate the findings clearly. These visuals will form the basis of an interactive dashboard.

---

## Python Scripts

To help others replicate the analysis or adapt it to their own datasets, this repository includes standalone Python scripts in the `python/` directory:

- **`data_cleaning.py`** – loads the raw retail sales CSV, computes new fields (`Revenue`, `Basket Size`, `Month`, `Quarter`), and writes the cleaned version.
- **`data_analysis.py`** – summarises the data by gender, product category, and month, and generates bar/line charts shown in the README.

---

## Tools Used

- **Python (pandas, seaborn, matplotlib):** for data import, aggregation and visualisation.
- **SQL (MySQL):** used to reproduce core insights with joins, groupings, and date filters.
- **Jupyter Notebook / Tableau:** for exploration and dashboard prototyping.

---

## Data Source

- **Provider:** Gigasheet sample data gallery
- **Description:** A retail sales dataset with transaction details, dates, customer demographics, product categories, quantities and prices.
- **Size:** 1,000 rows × 10 columns
- **Link:** [Gigasheet Retail Dataset](https://www.gigasheet.com/sample-data/retail-sales-dataset)

---

## About the Analyst

Jeremy Gutierrez – Data Analyst focused on turning raw data into actionable insights and communicating findings clearly. Connect via LinkedIn or GitHub.