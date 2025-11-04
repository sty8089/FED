# GDP Analysis Project

## Overview
Analysis of GDP trends for UK, USA, Brazil, Japan, China, Germany, and Switzerland from 2002-2022 using World Bank data.

## Project Structure
- `data.py`: Functions for loading and cleaning GDP data
- `plot_utils.py`: Functions for visualizing GDP data
- `gdp_analysis.ipynb`: Main analysis notebook with visualizations and insights
- `world bank data.csv`: GDP data from World Bank (2002-2022)
- `environment.yml`: Conda environment specification
- `pyproject.toml`: Project configuration and dependencies
- `.pre-commit-config.yaml`: Pre-commit hooks configuration

## Installation

### Using conda:
```bash
conda env create -f environment.yml
conda activate gdp-analysis
```

### Using pip:
```bash
pip install pandas matplotlib jupyter
```

## Usage
1. Open `gdp_analysis.ipynb` in Jupyter Notebook or VS Code
2. Run all cells to see the analysis and visualizations

## Key Findings
- **China**: Most dramatic growth, expanding from ~$1.5T to over $18T
- **United States**: Maintained largest economy, growing from ~$11T to $26T
- **Japan**: Relatively stagnant, fluctuating between $4-6T
- **Brazil**: Most volatile, with significant peaks and declines

## Data Source
World Bank GDP data (current US$): https://data.worldbank.org/

---

## Problem Set 2 - Exercise 1 Answers

### Question 1: Was the CSV file ignored after adding .gitignore?

**Answer:** No, the CSV file (`world bank data.csv`) was not ignored because it was already committed to Git before the `.gitignore` was created. `.gitignore` only prevents new and untracked files from being added to Git. Files that were already committed remain tracked.

**Evidence:** Running `git status` after creating `.gitignore` still showed `world bank data.csv` as "modified" rather than being ignored.

**To truly ignore it:** We would need to run `git rm --cached "world bank data.csv"` to remove it from Git's tracking while keeping the file locally.

### Question 2: Why add additional_dependencies to mypy in .pre-commit-config.yaml?

**Answer:** Mypy needs type stubs (type information) for third-party libraries to properly check type hints. Without `additional_dependencies`, mypy wouldn't know about the types in libraries like pandas, matplotlib, and seaborn, and would report errors or fail to validate type hints correctly.

The `additional_dependencies` line installs necessary type stub packages:
- `pandas-stubs`: Type information for pandas
- `types-seaborn`: Type information for seaborn
- `matplotlib`: Type information for matplotlib
- `polars`: Type information for polars

This allows mypy to understand and validate the type hints we use with these libraries.
