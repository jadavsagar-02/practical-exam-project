
import pandas as pd

def validate_data(df):

    required_columns = [
        "Transaction ID",
        "Date",
        "User ID",
        "Book Title",
        "Genre",
        "Borrowing Duration (Days)"
    ]

    # Check columns
    for col in required_columns:
        if col not in df.columns:
            raise ValueError("Missing column: " + col)

    # Remove missing values
    df = df.dropna(subset=required_columns)

    # Convert date
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # Convert borrowing duration
    df["Borrowing Duration (Days)"] = pd.to_numeric(
        df["Borrowing Duration (Days)"],
        errors="coerce"
    )

    df = df.dropna(subset=["Date", "Borrowing Duration (Days)"])

    # Remove negative duration
    df = df[df["Borrowing Duration (Days)"] >= 0]

    # Remove duplicate transactions
    df = df.drop_duplicates(subset=["Transaction ID"])

    if len(df) == 0:
        raise ValueError("No valid data found!")

    return df.reset_index(drop=True)
