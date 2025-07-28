"""
q1_revenue_by_gender.py
=======================

This script answers Question 1 from the Retail Sales Insights project:
**Which customer segments contribute most to revenue?**

It loads the cleaned retail sales CSV, groups transactions by gender and
computes summary metrics: transaction count, total revenue, average
revenue and average basket size.  The results are printed to the
console and can optionally be saved to a CSV file.

Usage
-----

```
python q1_revenue_by_gender.py --input retail_sales_clean.csv
```

You can specify ``--output`` to write the summary table to a file.
"""

import argparse
import pandas as pd


def summarise_by_gender(df: pd.DataFrame) -> pd.DataFrame:
    """Summarise revenue and basket size statistics by gender.

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned retail sales data.

    Returns
    -------
    pd.DataFrame
        Summary table indexed by gender.
    """
    summary = (
        df.groupby('Gender')
          .agg(Transactions=('Revenue', 'count'),
               TotalRevenue=('Revenue', 'sum'),
               AvgRevenue=('Revenue', 'mean'),
               AvgBasketSize=('Basket Size', 'mean'))
          .reset_index()
          .sort_values('TotalRevenue', ascending=False)
    )
    return summary


def main(input_path: str, output_path: str | None) -> None:
    df = pd.read_csv(input_path)
    summary = summarise_by_gender(df)
    print("Revenue by gender:\n", summary.to_string(index=False))
    if output_path:
        summary.to_csv(output_path, index=False)
        print(f"\nSummary saved to {output_path}.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Summarise revenue by gender")
    parser.add_argument('-i', '--input', dest='input_path', default='retail_sales_clean.csv',
                        help='Path to the cleaned retail sales CSV file')
    parser.add_argument('-o', '--output', dest='output_path', default=None,
                        help='Optional path to save the summary CSV')
    args = parser.parse_args()
    main(args.input_path, args.output_path)