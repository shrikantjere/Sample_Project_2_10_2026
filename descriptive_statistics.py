import csv
from pathlib import Path
from statistics import mean, median, multimode, pstdev, pvariance, quantiles, stdev, variance


def main():
    csv_path = Path(__file__).with_name("sample_data.csv")
    with csv_path.open(newline="", encoding="utf-8") as csv_file:
        rows = csv.DictReader(csv_file)
        values = [float(row["daily_orders"]) for row in rows if row["daily_orders"]]

    if len(values) < 2:
        raise ValueError("The CSV must contain at least two numeric values.")

    first_quartile, _, third_quartile = quantiles(values, n=4, method="inclusive")
    modes = ", ".join(f"{value:g}" for value in multimode(values))

    print("Descriptive statistics for daily orders")
    print(f"Count: {len(values)}")
    print(f"Mean: {mean(values):.2f}")
    print(f"Median: {median(values):.2f}")
    print(f"Mode(s): {modes}")
    print(f"Minimum: {min(values):.2f}")
    print(f"Maximum: {max(values):.2f}")
    print(f"Range: {max(values) - min(values):.2f}")
    print(f"Q1 (inclusive): {first_quartile:.2f}")
    print(f"Q3 (inclusive): {third_quartile:.2f}")
    print(f"Interquartile range: {third_quartile - first_quartile:.2f}")
    print(f"Population variance: {pvariance(values):.2f}")
    print(f"Population standard deviation: {pstdev(values):.2f}")
    print(f"Sample variance: {variance(values):.2f}")
    print(f"Sample standard deviation: {stdev(values):.2f}")


if __name__ == "__main__":
    main()