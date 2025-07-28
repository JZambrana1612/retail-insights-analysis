"""
q2_monthly_revenue.py
=====================

This script answers Question 2 from the Retail Sales Insights project:
**How does the timing or frequency of purchases affect revenue?**

It loads the cleaned retail sales CSV, aggregates total revenue by month
and displays the results.  Optionally, the monthly revenue can be
exported to a CSV file for further analysis or visualisation.

Usage
-----

```
python q2_monthly_revenue.py --input retail_sales_clean.csv
```

Specify ``--output`` to save the monthly revenue table to disk.
"""

import argparse
import pandas as pd


def summarise_by_month(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate revenue by month.

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned retail sales data.

    Returns
    -------
    pd.DataFrame
        Monthly revenue totals sorted chronologically.
    """
    monthly = (
        df.groupby('Month')
          .agg(TotalRevenue=('Revenue', 'sum'))
          .reset_index()
          .sort_values('Month')
    )
    return monthly


def main(input_path: str, output_path: str | None) -> None:
    df = pd.read_csv(input_path)
    monthly = summarise_by_month(df)
    print("Monthly revenue:\n", monthly.to_string(index=False))
    if output_path:
        monthly.to_csv(output_path, index=False)
        print(f"\nMonthly revenue saved to {output_path}.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Aggregate revenue by month")
    parser.add_argument('-i', '--input', dest='input_path', default='retail_sales_clean.csv',
                        help='Path to the cleaned retail sales CSV file')
    parser.add_argument('-o', '--output', dest='output_path', default=None,
                        help='Optional path to save the monthly revenue CSV')
    args = parser.parse_args()
    main(args.input_path, args.output_path)