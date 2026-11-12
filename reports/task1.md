# Task 1 report: Exploratory data analysis

| Field | Value |
| --- | --- |
| Student | Makrem Riahi |
| Dataset | Adult Census Income (`datasets/census_income.csv`), 1994 US Census. Becker, B. & Kohavi, R. (1996). *Adult* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5XW20. License CC BY 4.0. |
| Task | 1 |
| Tag / commit | `task1` |
| How to run | `git lfs pull`, `uv sync`, then open `task1/notebooks/01_eda.ipynb` in VS Code, select the `.venv` kernel and run all cells |
| Timebox | About 3 h (09:06 to 12:15); finished |

## 1. Summary

I explored the Adult Census Income dataset in a Jupyter notebook, resolved its data quality issues, and analyzed the key factors linked to earning over $50K a year. After data cleaning, 48,790 out of 48,842 rows remain. Only 23.9% of individuals earn more than $50K, making the target variable imbalanced. The strongest predictors are marital status—with around 45% of married people earning >$50K compared to 5–8% of others—and education, ranging from 1.2% for Preschool to over 70% for Doctorate holders. Interestingly, the income gap between men (30.4%) and women (10.9%) nearly disappears among married individuals. The main limitation is that all findings represent correlations within a 1994 sample, rather than causal relationships.

**Evidence:** `task1/notebooks/01_eda.ipynb`, section 7 (Summary).

## 2. Goal and success criteria

**Goal.** Load the dataset in a reproducible way, find and fix data quality problems, analyse distributions, correlations, target behaviour and anomalies, and present the findings with labelled charts.

| Criterion | How it is measured | Target | Result |
| --- | --- | --- | --- |
| Reproducible loading | Notebook runs from top to bottom after a kernel restart | No errors | Done: 28 code cells, 0 errors |
| Data issues found and fixed | Each issue documented with a number and a decision | Labels, missing values, duplicates, outliers, leakage | Done: 5 issues documented |
| Statistical analysis | Distributions, correlations, target behaviour, anomalies | All four covered | Done: 5 figures |
| Charts back a claim | Title, axis labels and a sentence with a number | Every chart | 5 of 5 |

**Evidence:** notebook sections 1-6; commit `7c09ea4` (full re-run).

## 3. Approach and key decisions

| # | Finding | Decision | Alternative considered | Where in the code |
| --- | --- | --- | --- | --- |
| D1 | `income` has 4 labels instead of 2: the trailing dot comes from the original test file | Removed the dot and created a binary target `income_gt50k` | Keep 4 classes | Notebook section 2 |
| D2 | `isna()` shows 0 missing values, but `?` hides 3,620 rows (7.4%); these rows earn >50K only 13.2% of the time vs 24.8% | Replaced `?` with NaN and kept the rows | Drop the rows; replace with "Unknown" | Notebook section 3 |
| D3 | 52 duplicate rows after fixing the labels | Removed them (0.1% of the data) | Keep them | Notebook section 4 |
| D4 | `fnlwgt` is a census sampling weight, not a property of the person | Dropped the column | Keep it as a feature | Notebook section 4 |
| D5 | `capital_gain` = 99999 for 244 people, all earning >50K: it is a top-code ("at least 99,999") | Kept the rows and added the flag `capital_gain_topcoded` | Drop or cap the values | Notebook section 5 |
| D6 | `education` and `education_num` carry the same information | Kept both, noted that a model should use only one | Drop one now | Notebook section 4 |

**Evidence:** commits `e7391a4`, `2e06519`, `c54c5f7`, `264c815`, `d9c4b17`.

## 4. Results

| Result | Value | Baseline or reference |
| --- | --- | --- |
| Rows after cleaning | 48,790 | 48,842 raw |
| Share earning >50K | 23.9% | About 3 to 1 imbalance |
| Rows with missing values | 3,620 (7.4%), 13.2% earn >50K | 24.8% for complete rows |
| Median age | 43 for >50K | 34 for <=50K |
| Married people earning >50K | about 45% (men and women) | 5-8% for non-married |
| Men vs women earning >50K | 30.4% vs 10.9% | 61.0% of men married vs 15.3% of women |
| Strongest numeric correlation with the target | `education_num` 0.33 | `age` and `hours_per_week` 0.23 |
| People with capital gain | 8.3% | 91.7% have 0 |

Figures (in `task1/figures/`):

- `fig01_age_by_income.png`: people earning >50K are older, median age 43 vs 34.
- `fig02_rate_by_education.png`: the share earning >50K grows from 1.2% (Preschool) to over 70% (Doctorate).
- `fig03_rate_by_marital_and_sex.png`: about 45% of married people earn >50K, for both men and women.
- `fig04_correlation.png`: `education_num` is the numeric column most linked to the target (0.33).
- `fig05_capital_gain.png`: an isolated bar at 99999 shows 244 top-coded values.

**Evidence:** notebook section 5; figures in `task1/figures/`.

## 5. Problems and how you handled them

| Problem | Cause | What you did | Status |
| --- | --- | --- | --- |
| Values started with a space | The CSV has a space after each comma | Used `skipinitialspace=True` in `read_csv` | Solved |
| Missing values not detected | They are written as `?` | Counted `?` and converted them to NaN | Solved |
| Two dataset files always shown as modified by git | They are declared as Git LFS in `.gitattributes` but stored as normal files | Marked them as `assume-unchanged` locally, not committed | Workaround |

**Evidence:** notebook sections 1 and 3.

## 6. Limitations and trade-offs

| Area | Limitation or trade-off | Impact | Mitigation or next step |
| --- | --- | --- | --- |
| Data | The data is a sample from 1994, not the full population | Current rates may differ | Treat findings as purely descriptive |
| Data | `income` is binary (>50K or ≤50K); exact figures are unknown | Income regression is not possible | Frame the task as a classification problem |
| Analysis | Findings only show correlations | Gender and marital status effects cannot be interpreted as causal | Clarify this explicitly when presenting results |
| Data | `sex`, `race`, and `relationship` are sensitive attributes | Models risk introducing bias or discrimination | Run fairness checks in later modeling stages |
| Data | Missing values are left as NaN | Downstream tasks will need to handle them | Impute missing values inside the modeling pipeline |

**Evidence:** notebook sections 3 and 5.

## 7. Next steps

| Priority | Next step | Why | Effort |
| --- | --- | --- | --- |
| 1 | Reuse the cleaning steps in the Task 2 app | The app needs the same clean data | S |
| 2 | Add interactive charts | Advanced objective of Task 1 | M |
| 3 | Check the rate by occupation and hours per week | Other possible drivers not plotted yet | S |

## 8. Use of AI assistants

| Tool | What you used it for | Where (files or sections) | How you checked the output |
| --- | --- | --- | --- |
| Claude | Explaining the task rules and the dataset columns | Start of the task | Compared with the md files of the repo |
| Claude | uv setup commands | `pyproject.toml`, `uv.lock` | Ran them myself |
| Claude | Pandas, matplotlib and seaborn code for the notebook cells, and meaning of new concepts (correlation, top-coding) | `task1/notebooks/01_eda.ipynb` | Ran every cell, checked the counts, wrote and decided the observations myself |

The full list is in `AI_LOG.md`. The analysis decisions (keep the missing rows, drop `fnlwgt`, flag the 99999 values) and the interpretation of the charts are mine.

## Checklist

- [x] Task tag pushed and named in the table at the top
- [x] Runs from a fresh clone with the commands above
- [x] No secrets, API keys or large data files committed
- [x] Every section has an Evidence line
- [x] Every figure has a caption with a number
- [x] Guidance blocks and placeholders removed
- [x] `AI_LOG.md` up to date
