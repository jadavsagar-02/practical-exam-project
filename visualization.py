
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os


def create_charts(data):

    os.makedirs("library_output", exist_ok=True)

    sns.set_theme(style="whitegrid")


    top_books = data["Book Title"].value_counts().head(5)

    plt.figure(figsize=(9, 5))

    plt.barh(top_books.index, top_books.values)

    plt.title("Top 5 Most Borrowed Books")
    plt.xlabel("Total Borrowings")
    plt.ylabel("Book Title")

    plt.tight_layout()
    plt.savefig("library_output/bar_chart.png")
    plt.show()
    plt.close()



    monthly = data.groupby("Month").size()

    plt.figure(figsize=(9, 5))

    plt.plot(monthly.index, monthly.values, marker="o")

    plt.title("Monthly Borrowing Trends")
    plt.xlabel("Month")
    plt.ylabel("Total Borrowings")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig("library_output/line_chart.png")
    plt.show()
    plt.close()


    genre = data["Genre"].value_counts()

    plt.figure(figsize=(7, 7))

    plt.pie(
        genre.values,
        labels=genre.index,
        autopct="%1.1f%%"
    )

    plt.title("Books Borrowed by Genre")

    plt.tight_layout()
    plt.savefig("library_output/pie_chart.png")
    plt.show()
    plt.close()

    if "Borrowing Time" in data.columns:

        hours = pd.to_datetime(
            data["Borrowing Time"],
            format="%H:%M",
            errors="coerce"
        ).dt.hour

        heat_data = pd.crosstab(data["Day"], hours)

        heat_data = heat_data.reindex(
            ["Monday", "Tuesday", "Wednesday",
             "Thursday", "Friday", "Saturday", "Sunday"],
            fill_value=0
        )

        plt.figure(figsize=(10, 5))

        sns.heatmap(heat_data, cmap="YlGnBu")

        plt.title("Borrowing Activity by Day and Time")
        plt.xlabel("Hour")
        plt.ylabel("Day")

    else:

        heat_data = pd.crosstab(data["Day"], data["Month"])

        plt.figure(figsize=(10, 5))

        sns.heatmap(heat_data, annot=True, cmap="YlGnBu")

        plt.title("Borrowing Activity by Day and Month")
        plt.xlabel("Month")
        plt.ylabel("Day")

    plt.tight_layout()
    plt.savefig("library_output/heatmap.png")
    plt.show()
    plt.close()

    print("All charts generated successfully!")
