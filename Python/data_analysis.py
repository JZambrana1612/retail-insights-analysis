"""
data_analysis.py
=================

This script demonstrates how to load, clean and analyse the sample retail
sales dataset used in the Retail Sales Insights project.  It uses pandas
for data manipulation and seaborn/matplotlib for basic visualisations.

Functions are provided for:

* Loading the CSV file and computing derived columns (Revenue, Basket Size,
  Month, Quarter) if they are missing.
* Summarising revenue and basket size by gender.
* Summarising revenue and ticket metrics by product category.
* Summarising revenue by month and quarter.
* Plotting simple bar and line charts and saving them to PNG files.

Run this script as a stand‑alone programme to generate summary tables and
charts.  Modify the `CSV_PATH` variable in the ``if __name__ == '__main__'``
section to point to your local CSV file.
"""

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")


def load_data(csv_path: str) -> pd.DataFrame:
    """Load the retail sales CSV file and ensure required fields exist.

    Parameters
    ----------
    csv_path : str
        Path to the CSV file.

    Returns
    -------
    pd.DataFrame
        DataFrame with parsed dates and computed fields.
    """
    df = pd.read_csv(csv_path)

    # Parse SaleDate as datetime if present
    if 'SaleDate' in df.columns:
        df['SaleDate'] = pd.to_datetime(df['SaleDate'])

    # Compute Revenue if missing
    if 'Revenue' not in df.columns and {'Quantity', 'PricePerUnit'}.issubset(df.columns):
        df['Revenue'] = df['Quantity'] * df['PricePerUnit']

    # Compute Basket Size if missing
    if 'Basket Size' not in df.columns and 'Quantity' in df.columns:
        df['Basket Size'] = df['Quantity']

    # Derive Month and Quarter if missing and SaleDate exists
    if 'SaleDate' in df.columns:
        if 'Month' not in df.columns:
            df['Month'] = df['SaleDate'].dt.strftime('%Y-%m')
        if 'Quarter' not in df.columns:
            df['Quarter'] = df['SaleDate'].dt.to_period('Q').astype(str)

    return df


def summarise_by_gender(df: pd.DataFrame) -> pd.DataFrame:
    """Compute total revenue, average revenue, transaction count and average
    basket size by gender.

    Parameters
    ----------
    df : pd.DataFrame
        The retail sales data.

    Returns
    -------
    pd.DataFrame
        Summary table indexed by gender.
    """
    summary = (
        df.groupby('Gender')
        .agg(Transactions=('Revenue', 'count'),
             Total_Revenue=('Revenue', 'sum'),
             Avg_Revenue=('Revenue', 'mean'),
             Avg_Basket_Size=('Basket Size', 'mean'))
        .reset_index()
    )
    return summary


def summarise_by_category(df: pd.DataFrame) -> pd.DataFrame:
    """Compute total and average revenue per transaction by product category.

    Parameters
    ----------
    df : pd.DataFrame
        The retail sales data.

    Returns
    -------
    pd.DataFrame
        Summary table indexed by product category.
    """
    summary = (
        df.groupby('ProductCategory')
        .agg(Transactions=('Revenue', 'count'),
             Total_Revenue=('Revenue', 'sum'),
             Avg_Revenue=('Revenue', 'mean'),
             Avg_Unit_Price=('PricePerUnit', 'mean'))
        .reset_index()
        .sort_values('Total_Revenue', ascending=False)
    )
    return summary


def summarise_by_month(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate revenue by month.

    Parameters
    ----------
    df : pd.DataFrame
        The retail sales data.

    Returns
    -------
    pd.DataFrame
        Total revenue per month.
    """
    monthly = (
        df.groupby('Month')
        .agg(Revenue=('Revenue', 'sum'))
        .reset_index()
        .sort_values('Month')
    )
    return monthly


def plot_revenue_by_gender(summary: pd.DataFrame, out_path: str) -> None:
    """Plot a bar chart of total revenue by gender.

    Parameters
    ----------
    summary : pd.DataFrame
        Output of ``summarise_by_gender``.
    out_path : str
        File path to save the PNG image.
    """
    plt.figure(figsize=(4, 4))
    ax = sns.barplot(x='Gender', y='Total_Revenue', data=summary, palette='pastel')
    plt.title('Total Revenue by Gender')
    plt.ylabel('Total Revenue')
    # Annotate bars with values
    for idx, row in summary.iterrows():
        ax.text(idx, row['Total_Revenue'] * 1.01, f"{row['Total_Revenue']:.0f}",
                ha='center', va='bottom')
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


def plot_revenue_by_category(summary: pd.DataFrame, out_path: str) -> None:
    """Plot a bar chart of total revenue by product category.

    Parameters
    ----------
    summary : pd.DataFrame
        Output of ``summarise_by_category``.
    out_path : str
        File path to save the PNG image.
    """
    plt.figure(figsize=(6, 4))
    ax = sns.barplot(x='ProductCategory', y='Total_Revenue', data=summary, palette='muted')
    plt.title('Total Revenue by Product Category')
    plt.xlabel('Product Category')
    plt.ylabel('Total Revenue')
    for idx, row in summary.iterrows():
        ax.text(idx, row['Total_Revenue'] * 1.01, f"{row['Total_Revenue']:.0f}",
                ha='center', va='bottom')
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


def plot_monthly_revenue(monthly: pd.DataFrame, out_path: str) -> None:
    """Plot a line chart of revenue by month.

    Parameters
    ----------
    monthly : pd.DataFrame
        Output of ``summarise_by_month``.
    out_path : str
        File path to save the PNG image.
    """
    plt.figure(figsize=(8, 4))
    ax = sns.lineplot(x='Month', y='Revenue', data=monthly, marker='o')
    plt.title('Monthly Revenue Trend')
    plt.xlabel('Month')
    plt.ylabel('Revenue')
    plt.xticks(rotation=45)
    for idx, row in monthly.iterrows():
        plt.text(row['Month'], row['Revenue'] * 1.02, f"{row['Revenue']:.0f}",
                 ha='center', va='bottom', fontsize=8)
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


def main(csv_path: str) -> None:
    """Run the full analysis on the provided CSV path.

    This will print summary tables to the console and save charts in the
    current working directory.

    Parameters
    ----------
    csv_path : str
        Path to the retail sales CSV file.
    """
    df = load_data(csv_path)

    # Summaries
    gender_summary = summarise_by_gender(df)
    category_summary = summarise_by_category(df)
    monthly_summary = summarise_by_month(df)

    print("Revenue by gender:\n", gender_summary.to_string(index=False))
    print("\nRevenue by category:\n", category_summary.to_string(index=False))
    print("\nMonthly revenue:\n", monthly_summary.to_string(index=False))

    # Plot charts
    plot_revenue_by_gender(gender_summary, 'rev_by_gender.png')
    plot_revenue_by_category(category_summary, 'rev_by_category.png')
    plot_monthly_revenue(monthly_summary, 'monthly_revenue_trend.png')
    print("\nCharts saved to current directory.")


if __name__ == '__main__':
    """
    When executed as a script, this module accepts an optional input CSV path
    via the ``--input`` argument.  If omitted, it falls back to the
    ``CSV_PATH`` environment variable or ``retail_sales_clean.csv`` in the
    current directory.

    Examples
    --------
    Run analysis on a specific file:

    ```bash
    python python/data_analysis.py --input data/retail_sales_clean.csv
    ```

    Or using an environment variable:

    ```bash
    CSV_PATH=data/retail_sales_clean.csv python python/data_analysis.py
    ```
    """
    import argparse
    parser = argparse.ArgumentParser(description="Analyse the cleaned retail sales data")
    parser.add_argument('-i', '--input', dest='input_path', default=None,
                        help='Path to the cleaned CSV file')
    args = parser.parse_args()

    # Determine CSV path: command-line > environment variable > default
    csv_env = os.getenv('CSV_PATH')
    csv_path = args.input_path or csv_env or 'retail_sales_clean.csv'

    main(csv_path)