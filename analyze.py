from pathlib import Path
import csv
import numpy as np

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "student_performance.csv"
OUTPUT_DIR = BASE_DIR / "output"
REPORT_FILE = OUTPUT_DIR / "analysis_report.txt"


def load_dataset(file_path):
    """Load a CSV whose first column is an identifier and remaining columns are numeric."""
    with file_path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        if not reader.fieldnames or len(reader.fieldnames) < 2:
            raise ValueError("CSV must contain an identifier column and at least one numeric column.")

        identifier_column = reader.fieldnames[0]
        numeric_columns = reader.fieldnames[1:]
        rows = list(reader)

    if not rows:
        raise ValueError("The CSV dataset is empty.")

    data = {}
    for column in numeric_columns:
        try:
            values = np.array([float(row[column]) for row in rows], dtype=float)
        except (TypeError, ValueError) as error:
            raise ValueError(f"Column '{column}' must contain only numeric values.") from error

        if not np.all(np.isfinite(values)):
            raise ValueError(f"Column '{column}' contains missing or non-finite values.")
        data[column] = values

    identifiers = [row[identifier_column] for row in rows]
    return identifiers, data


def analyze_column(values):
    """Return descriptive statistics and IQR-based potential outliers."""
    q1 = np.percentile(values, 25)
    q3 = np.percentile(values, 75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = values[(values < lower_bound) | (values > upper_bound)]

    return {
        "count": len(values),
        "mean": np.mean(values),
        "median": np.median(values),
        "std": np.std(values),  # Population standard deviation
        "min": np.min(values),
        "max": np.max(values),
        "q1": q1,
        "q3": q3,
        "lower_bound": lower_bound,
        "upper_bound": upper_bound,
        "outliers": outliers,
    }


def format_report(data):
    lines = [
        "NUMPY STATISTICAL ANALYSIS",
        "=" * 30,
        "Dataset: Student Performance",
        "Standard deviation: population (ddof=0)",
        "Potential outliers: 1.5 × IQR rule",
        "",
    ]

    for column, values in data.items():
        stats = analyze_column(values)
        lines.extend([
            f"Subject: {column.replace('_', ' ')}",
            "-" * (9 + len(column)),
            f"Observations: {stats['count']}",
            f"Mean: {stats['mean']:.2f}",
            f"Median: {stats['median']:.2f}",
            f"Standard deviation: {stats['std']:.2f}",
            f"Minimum: {stats['min']:.2f}",
            f"Maximum: {stats['max']:.2f}",
            f"Q1: {stats['q1']:.2f}",
            f"Q3: {stats['q3']:.2f}",
            f"IQR bounds: {stats['lower_bound']:.2f} to {stats['upper_bound']:.2f}",
        ])

        if stats["outliers"].size:
            lines.append("Potential unusually high/low values: " +
                         ", ".join(f"{value:g}" for value in stats["outliers"]))
        else:
            lines.append("Potential unusually high/low values: None detected")

        difference = abs(stats["mean"] - stats["median"])
        if np.isclose(stats["mean"], stats["median"]):
            comparison = "Mean and median are approximately equal."
        elif stats["mean"] > stats["median"]:
            comparison = "Mean is greater than median; high values may be pulling the average upward."
        else:
            comparison = "Mean is less than median; low values may be pulling the average downward."
        lines.append(comparison)
        lines.append("")

    lines.append("Note: IQR flags are only indicators for review, not proof of incorrect data.")
    return "\n".join(lines)


def main():
    try:
        _, dataset = load_dataset(DATA_FILE)
        report = format_report(dataset)
        print(report)

        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        REPORT_FILE.write_text(report + "\n", encoding="utf-8")
        print(f"\nReport saved to: {REPORT_FILE}")
    except (OSError, ValueError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
