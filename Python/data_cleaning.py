"""
data_cleaning.py
=================

This utility script prepares the raw retail sales dataset for analysis by
computing derived fields and standardising the column names.  It takes as
input a raw CSV file and produces a cleaned version with the following
additional columns:

* **Revenue** – the total amount spent per transaction (Quantity × PricePerUnit).
* **Basket Size** – an alias for the Quantity field to emphasise the number of
  items purchased.
* **Month** – a ``YYYY-MM`` string derived from the ``SaleDate``.
* **Quarter** – a ``YYYY-QX`` string indicating the fiscal quarter.

Usage
-----

Run this script from the project root, specifying the input and output
paths:

```bash
python python/data_cleaning.py --input data/retail_sales_raw.csv --output data/retail_sales_clean.csv
```

If the input dataset already contains some of these fields, they will be
recomputed to ensure consistency.  The output CSV overwrites any existing
file at the given path.
"""

import argparse
import pandas as pd


def clean_data(input_path: str, output_path: str) -> None:
    """Load the raw retail sales CSV, compute derived fields and save to a new file.

    Parameters
    ----------
    input_path : str
        Path to the raw CSV file.
    output_path : str
        Path where the cleaned CSV will be written.
    """
    df = pd.read_csv(input_path)

    # Ensure SaleDate is a datetime
    if 'SaleDate' in df.columns:
        df['SaleDate'] = pd.to_datetime(df['SaleDate'])

    # Compute Revenue (Quantity × PricePerUnit)
    if {'Quantity', 'PricePerUnit'}.issubset(df.columns):
        df['Revenue'] = df['Quantity'] * df['PricePerUnit']
    else:
        raise KeyError("Input data must contain 'Quantity' and 'PricePerUnit' columns to compute Revenue.")

    # Create Basket Size as a copy of Quantity
    if 'Basket Size' not in df.columns:
        df['Basket Size'] = df['Quantity']

    # Derive Month and Quarter
    if 'SaleDate' in df.columns:
        df['Month'] = df['SaleDate'].dt.strftime('%Y-%m')
        df['Quarter'] = df['SaleDate'].dt.to_period('Q').astype(str)
    else:
        raise KeyError("Input data must contain 'SaleDate' to derive Month and Quarter.")

    # Save cleaned dataset
    df.to_csv(output_path, index=False)

    print(f"Cleaned data saved to {output_path}.  Rows: {len(df)}. Columns: {len(df.columns)}.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Clean the raw retail sales data")
    parser.add_argument('-i', '--input', dest='input_path', required=True,
                        help='Path to the raw CSV file')
    parser.add_argument('-o', '--output', dest='output_path', default='retail_sales_clean.csv',
                        help='Path for the cleaned CSV file (default: retail_sales_clean.csv)')
    args = parser.parse_args()
    clean_data(args.input_path, args.output_path)


if __name__ == '__main__':
    main()