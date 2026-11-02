
import pandas as pd
from control_structure import validate_data


class PandasHandler:

    def __init__(self):
        self.data = None

    def load_data(self, file_path):

        self.data = pd.read_csv(file_path)

        self.data = validate_data(self.data)

        # Create Month column
        self.data["Month"] = self.data["Date"].dt.to_period("M").astype(str)

        # Create Day column
        self.data["Day"] = self.data["Date"].dt.day_name()

        # Frequent borrowers
        user_count = self.data["User ID"].value_counts()

        self.data["User Borrowing Count"] = (
            self.data["User ID"].map(user_count)
        )

        self.data["Frequent Borrower"] = (
            self.data["User Borrowing Count"] >= 5
        )

        # Late return calculation
        if "Due Date" in self.data.columns and "Return Date" in self.data.columns:

            self.data["Due Date"] = pd.to_datetime(
                self.data["Due Date"], errors="coerce"
            )

            self.data["Return Date"] = pd.to_datetime(
                self.data["Return Date"], errors="coerce"
            )

            self.data["Late Return"] = (
                self.data["Return Date"] > self.data["Due Date"]
            )

        else:
            self.data["Late Return"] = False

        print("Data loaded successfully!")

        return self.data

    def filter_transactions(self, genre="all"):

        if genre.lower() == "all":
            return self.data

        return self.data[
            self.data["Genre"].str.lower() == genre.lower()
        ]

    def genre_summary(self):

        return self.data.groupby("Genre").agg(
            Total_Borrowings=("Transaction ID", "count"),
            Average_Duration=("Borrowing Duration (Days)", "mean")
        ).round(2)
