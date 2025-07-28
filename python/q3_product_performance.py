"""
q3_product_performance.py
=========================

This script answers Question 3 from the Retail Sales Insights project:
**If we could only stock or promote a limited range of products, which ones should be prioritised?**

It loads the cleaned retail sales CSV, summarises performance metrics by
product category (transaction count, total revenue, average revenue
and average unit price) and sorts the categories by total revenue in
descending order.  The results can be printed to the console and
optionally saved to a CSV file.

Usage
-----

```
python q3_product_performance.py --input retail_sales_clean.csv
```

Add ``--output`` to save the summary.
"""

import argparse
import pandas as pd


def summarise_by_category(df: pd.DataFrame) -> pd.DataFrame:
    """Compute performance metrics for each product category.

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned retail sales data.

    Returns
    -------
    pd.DataFrame
        Summary table indexed by product category, sorted by total revenue.
    """
    summary = (
        df.groupby('ProductCategory')
          .agg(Transactions=('Revenue', 'count'),
               TotalRevenue=('Revenue', 'sum'),
               AvgRevenue=('Revenue', 'mean'),
               AvgUnitPrice=('PricePerUnit', 'mean'))
          .reset_index()
          .sort_values('TotalRevenue', ascending=False)
    )
    return summary


def main(input_path: str, output_path: str | None) -> None:
    df = pd.read_csv(input_path)
    summary = summarise_by_category(df)
    print("Revenue by product category:\n", summary.to_string(index=False))
    if output_path:
        summary.to_csv(output_path, index=False)
        print(f"\nProduct category summary saved to {output_path}.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Summarise revenue by product category")
    parser.add_argument('-i', '--input', dest='input_path', default='retail_sales_clean.csv',
                        help='Path to the cleaned retail sales CSV file')
    parser.add_argument('-o', '--output', dest='output_path', default=None,
                        help='Optional path to save the product category summary CSV')
    args = parser.parse_args()
    main(args.input_path, args.output_path)