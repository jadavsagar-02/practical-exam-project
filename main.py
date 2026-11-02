
from library_dashboard import LibraryDashboard


def main():

    print("======================================")
    print(" E-LIBRARY DATA INSIGHTS DASHBOARD")
    print("======================================")

    dashboard = LibraryDashboard()

    file_path = input(
        "Enter CSV file name: "
    ).strip()

    if file_path == "":
        file_path = "library_transactions.csv"

    try:

        dashboard.load_data(file_path)

    except Exception as error:

        print("Error:", error)

        return

    while True:

        print("\n========== MAIN MENU ==========")

        print("1. Calculate Statistics")

        print("2. Filter Transactions")

        print("3. Generate Report")

        print("4. Generate Visualizations")

        print("5. Show Dataset")

        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            dashboard.calculate_statistics()

        elif choice == "2":

            genre = input(
                "Enter Genre (or all): "
            ).strip()

            if genre == "":
                genre = "all"

            dashboard.filter_transactions(genre)

        elif choice == "3":

            dashboard.generate_report()

        elif choice == "4":

            dashboard.generate_visualizations()

        elif choice == "5":

            print(dashboard.data.head(10))

        elif choice == "6":

            print("Thank you for using the dashboard!")

            break

        else:

            print("Invalid choice! Try again.")


if __name__ == "__main__":

    main()
