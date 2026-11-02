
import numpy as np


def calculate_duration(data):

    duration = np.array(
        data["Borrowing Duration (Days)"]
    )

    average = np.mean(duration)

    standard_deviation = np.std(duration)

    minimum = np.min(duration)

    maximum = np.max(duration)

    print("\nNUMPY ANALYSIS")

    print("Average Duration:", round(average, 2))

    print("Standard Deviation:", round(standard_deviation, 2))

    print("Minimum Duration:", minimum)

    print("Maximum Duration:", maximum)

    return {
        "average": round(float(average), 2),
        "standard_deviation": round(float(standard_deviation), 2),
        "minimum": float(minimum),
        "maximum": float(maximum)
    }
