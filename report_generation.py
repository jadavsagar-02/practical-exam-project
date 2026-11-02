
def generate_report(data, stats):

    report = f"""
====================================
 E-LIBRARY DATA INSIGHTS REPORT
====================================

Total Transactions: {len(data)}

Total Books: {data['Book Title'].nunique()}

Total Users: {data['User ID'].nunique()}

Most Borrowed Book:
{data['Book Title'].value_counts().idxmax()}

Busiest Day:
{data['Day'].value_counts().idxmax()}

Average Borrowing Duration:
{stats['average']} Days

Standard Deviation:
{stats['standard_deviation']}

Minimum Duration:
{stats['minimum']}

Maximum Duration:
{stats['maximum']}

Frequent Borrowers:
{int(data['Frequent Borrower'].sum())}

Late Returns:
{int(data['Late Return'].sum())}

GENRE SUMMARY:

{data['Genre'].value_counts().to_string()}

TOP 5 BOOKS:

{data['Book Title'].value_counts().head(5).to_string()}

====================================
 END OF REPORT
====================================
"""

    file = open(
        "library_report.txt",
        "w",
        encoding="utf-8"
    )

    file.write(report)

    file.close()

    print("Report Generated Successfully!")

    print("File Saved: library_report.txt")
