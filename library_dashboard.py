
from pandas_handler import PandasHandler
from numpy_analysis import calculate_duration
from visualization import create_charts
from report_generation import generate_report


class LibraryDashboard:

    def __init__(self):

        self.handler = PandasHandler()

        self.data = None

    # Load CSV
    def load_data(self, file_path):

        self.data = self.handler.load_data(file_path)

        return self.data

    # Calculate Statistics
    def calculate_statistics(self):

        if self.data is None:
            print("Please load data first!")
            return {}

        stats = calculate_duration(self.data)

        print("\nLIBRARY STATISTICS")

        print("Total Transactions:", len(self.data))

        print("Unique Books:", self.data["Book Title"].nunique())

        print("Unique Users:", self.data["User ID"].nunique())

        print(
            "Most Borrowed Book:",
            self.data["Book Title"].value_counts().idxmax()
        )

        print(
            "Busiest Day:",
            self.data["Day"].value_counts().idxmax()
        )

        print("\nTOP 5 BOOKS")

        print(self.data["Book Title"].value_counts().head(5))

        print("\nGENRE SUMMARY")

        print(self.handler.genre_summary())

        return stats

    # Filter Transactions
    def filter_transactions(self, genre="all"):

        result = self.handler.filter_transactions(genre)

        print("\nFILTERED DATA")

        print(result.to_string(index=False))

        return result

    # Generate Report
    def generate_report(self):

        if self.data is None:
            print("Please load data first!")
            return

        stats = calculate_duration(self.data)

        generate_report(self.data, stats)

    # Generate Charts
    def generate_visualizations(self):

        if self.data is None:
            print("Please load data first!")
            return

        create_charts(self.data)
