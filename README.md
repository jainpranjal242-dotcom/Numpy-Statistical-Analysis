# NumPy Statistical Analysis

**Internship Track:** AI & ML  
**Organization:** Veda Technology  
**Project:** NumPy Statistical Analysis  
**Author:** Pranjal jain

## Project Overview
This project analyzes a small numerical dataset using Python and NumPy. It calculates common descriptive statistics and highlights unusually high or low observations using the interquartile range (IQR) method.

The included sample dataset represents student marks in five subjects. You can replace it with another numeric CSV dataset.

## Objectives
- Practice NumPy statistical functions on numerical data.
- Calculate mean, median, standard deviation, minimum, and maximum.
- Compare mean and median.
- Identify possible unusually high or low values.
- Save a concise analysis report.

## Project Structure
```text
NumPy_Statistical_Analysis/
├── data/
│   └── student_performance.csv
├── output/
│   └── .gitkeep
├── analyze.py
├── requirements.txt
└── README.md
```

## Requirements
- Python 3.9+
- NumPy

Install the dependency:
```bash
pip install -r requirements.txt
```

## Run the Project
From the project directory, run:
```bash
python analyze.py
```

The script reads `data/student_performance.csv`, prints the statistics in the terminal, and writes the results to `output/analysis_report.txt`.

## Dataset
The sample CSV contains a `student` column and numerical marks columns:
- Mathematics
- Physics
- Computer_Science

Each row represents one student. The analysis is performed separately for each subject.

## Statistical Methods
- **Mean:** Average of the observations.
- **Median:** Middle value after sorting the observations.
- **Standard deviation:** Measures how spread out values are around the mean. This project uses population standard deviation (`numpy.std`, `ddof=0`).
- **Minimum / Maximum:** Smallest and largest values.
- **IQR outlier check:** Values below `Q1 - 1.5 × IQR` or above `Q3 + 1.5 × IQR` are flagged as potential outliers. These are indicators for review, not proof of an error.

## Example Output
The exact values are calculated from the included CSV when you run the script. The report includes the number of observations and all requested statistics for each subject, along with a brief mean-versus-median comparison and any IQR flags.

## Customizing the Dataset
Keep a header row and at least one numeric column. The first column is treated as an identifier; all remaining columns must contain numeric values. To use your own dataset, replace `data/student_performance.csv` while keeping the same format.

## Tools Used
- Python
- NumPy
- CSV dataset
- Jupyter Notebook (optional; the analysis can also be run directly as a Python script)

## Author
Ayush Rajput  
B.Tech CSE (AI & ML)
