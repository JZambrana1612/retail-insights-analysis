"""
clean_retail_data.py
====================

This script reads the raw retail sales CSV file, standardises column names
and computes additional metrics used throughout the Retail Sales Insights
project.  The raw dataset contains columns with spaces such as ``Date``
and ``Price per Unit``; these are renamed to match the naming convention
used in the analysis (e.g. ``SaleDate`` and ``PricePerUnit``).  The script
also derives the following fields:

* **Revenue** – calculated as ``Quantity × PricePerUnit``.
* **Basket Size** – synonymous with ``Quantity`` to emphasise the number
  of items in each transaction.
* **Month** – a ``YYYY-MM`` string extracted from the sale date.
* **Quarter** – a ``Qx-YYYY`` string derived from the sale date.

Usage
-----

Run this script from the command line, specifying the input and output
CSV paths.  For example:

```
python clean_retail_data.py --input retail_sales_full_dataset.csv --output retail_sales_clean.csv
```

If no output path is provided, the script writes ``retail_sales_clean.csv``
in the current directory.  The input CSV must contain the columns
``Transaction ID``, ``Date``, ``Customer ID``, ``Gender``, ``Age``,
``Product Category``, ``Quantity``, ``Price per Unit`` and ``Total Amount``.
"""

import argparse
import pandas as pd


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Rename columns, parse dates and compute derived fields.

    Parameters
    ----------
    df : pd.DataFrame
        Raw retail sales data with original column names.

    Returns
    -------
    pd.DataFrame
        Cleaned retail sales data with new columns and consistent naming.
    """
    # Standardise column names
    rename_map = {
        'Transaction ID': 'TransactionID',
        'Date': 'SaleDate',
        'Customer ID': 'CustomerID',
        'Product Category': 'ProductCategory',
        'Price per Unit': 'PricePerUnit',
        'Total Amount': 'TotalAmount'
    }
    df = df.rename(columns=rename_map)

    # Parse dates and drop time component
    df['SaleDate'] = pd.to_datetime(df['SaleDate']).dt.date.astype(str)

    # Compute revenue and basket size
    df['Revenue'] = df['Quantity'] * df['PricePerUnit']
    df['Basket Size'] = df['Quantity']

    # Derive month and quarter
    sale_dates = pd.to_datetime(df['SaleDate'])
    df['Month'] = sale_dates.dt.strftime('%Y-%m')
    df['Quarter'] = 'Q' + sale_dates.dt.quarter.astype(str) + '-' + sale_dates.dt.year.astype(str)

    # Reorder columns for readability
    ordered_cols = [
        'TransactionID', 'SaleDate', 'CustomerID', 'Gender', 'Age',
        'ProductCategory', 'Quantity', 'PricePerUnit', 'TotalAmount',
        'Month', 'Quarter', 'Basket Size', 'Revenue'
    ]
    return df[ordered_cols]


def clean_file(input_path: str, output_path: str) -> None:
    """Load a raw CSV, clean it and write the result to a new file.

    Parameters
    ----------
    input_path : str
        Path to the raw retail sales CSV file.
    output_path : str
        Destination path for the cleaned CSV file.
    """
    raw_df = pd.read_csv(input_path)
    cleaned_df = clean_dataset(raw_df)
    cleaned_df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}. Rows: {len(cleaned_df)}; Columns: {len(cleaned_df.columns)}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Clean the raw retail sales data")
    parser.add_argument('-i', '--input', dest='input_path', required=True,
                        help='Path to the raw CSV file')
    parser.add_argument('-o', '--output', dest='output_path', default='retail_sales_clean.csv',
                        help='Path for the cleaned CSV file (default: retail_sales_clean.csv)')
    args = parser.parse_args()
    clean_file(args.input_path, args.output_path)


if __name__ == '__main__':
    main()