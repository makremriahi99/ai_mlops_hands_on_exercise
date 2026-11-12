# AI Log

| Time  | Purpose                                                              | Kept                                                         |
|-------|----------------------------------------------------------------------|--------------------------------------------------------------|
| 09:06 | Summary of Task 1 requirements, commit/tag rules and AI usage rules  | Used as a checklist                                          |
| 09:25 | uv commands to create the project and add pandas, matplotlib, seaborn, ipykernel | Ran the commands myself as suggested                         |
| 09:44 | Description of census_income.csv: size, columns, target, data issues | Used as a reference for column meanings and issues to check  |
| 09:50 | Code to load census_income.csv in the notebook                       | Ran and checked shape and head                               |
| 10:00 | Code for column types and summary statistics                         | Used to write my own observations on outliers and fnlwgt     |
| 10:10 | Code to clean the income labels and build a 0/1 target               | Used after checking the 4 labels; verified the counts        |
| 10:20 | Code to detect "?" values and compare target rate by missingness     | Used; decided myself to keep rows as NaN                     |
| 10:35 | Code to remove duplicates, rename columns and drop fnlwgt            | Used; chose myself which column to drop and why              |
| 10:45 | Code for the age distribution plot by income                          | Read the plot myself: high earners older (median 43 vs 34)   |
| 11:00 | Code for the income rate by education bar chart                       | Used; wrote my own conclusion on the HS-grad to Bachelors jump |
| 11:15 | Code for the income rate by marital status and sex chart              | Used; found myself that the sex gap comes from marital composition |
| 11:30 | Code for the correlation heatmap and how to read correlation values | Interpreted it myself: education_num strongest (0.33); no column decides income alone; marital status not visible because it is not numeric |
| 11:40 | Code for the capital gain plot and meaning of top-coding | Reasoned myself that 99999 means "at least 99,999", that it alone pushes income above 50K (leakage risk), and decided to keep and flag the 244 rows |
