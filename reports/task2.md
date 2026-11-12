# Task 2 report: App deployment

| Field | Value |
| --- | --- |
| Student | Makrem Riahi |
| Dataset | Adult Census Income (`datasets/census_income.csv`), 1994 US Census. Becker, B. & Kohavi, R. (1996). *Adult* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5XW20. License CC BY 4.0. |
| Task | 2 |
| Tag / commit | `task2` |
| How to run | `git lfs pull`, then from the repo root `docker compose -f task2/compose.yaml up --build` and open http://localhost:8501. Stop with `docker compose -f task2/compose.yaml down` |
| Timebox | About 2 h (12:40 to 14:45); finished |

## 1. Summary

I built a Streamlit app to explore the census data and I run it in a Docker container with Docker Compose. The app uses the same cleaning as the Task 1 notebook, so it shows the same numbers: 48,790 people and 23.9% earning more than 50K. The user can filter by sex and age and see the share earning more than 50K for each category, like education or marital status. The image is slim, pinned to an exact version and runs as a non-root user, while the data is not inside the image but mounted read-only, with its path set in the DATA_PATH variable. The main limit is the image size (805 MB), mostly because of Streamlit, and the app runs in a single container instead of separate services.

**Evidence:** `task2/`, screenshot `task2/figures/app_in_container.png`.

## 2. Goal and success criteria

**Goal.** Build an app to explore the data interactively, containerise it with my own Dockerfile and deploy it with Docker Compose.

| Criterion | How it is measured | Target | Result |
| --- | --- | --- | --- |
| Same data as Task 1 | `python task2/app/cleaning.py` checks the shape | (48790, 16) | Done: `OK (48790, 16)` |
| Interactive exploration | Filters and chart react to user input | Filters + chart by category | Done: sex and age filters, group-by chart |
| Deployment works end to end | `docker compose up`, app opened in the browser | Same numbers as the notebook | Done: 48,790 and 23.9% |
| Image quality | Base image, tag, user | Slim, pinned, non-root | Done: `python:3.12.16-slim`, `whoami` returns `appuser` |
| Configuration | Data path not hard-coded | Env var | Done: `DATA_PATH` |

**Evidence:** commits `d019b7a`, `3fed6d7`, `4ccfce6`.

## 3. Approach and key decisions

| # | Decision | Why | Alternative considered | Where in the code |
| --- | --- | --- | --- | --- |
| D1 | Moved the notebook cleaning into a function `load_clean()` | The app must use the same clean data as Task 1; one function avoids copying code | Load the cleaned CSV from Task 1 (it is git-ignored, so not in a fresh clone) | `task2/app/cleaning.py` |
| D2 | Streamlit as framework | Pure Python, reuses pandas directly, easy to run in a container | Dash, Gradio, Flask + HTML | `task2/app/app.py` |
| D3 | `@st.cache_data` on the data loading | Streamlit reruns the script on every click; the cache reads and cleans the CSV only once | No cache (slow on every interaction) | `task2/app/app.py` |
| D4 | Base image `python:3.12.16-slim`, exact tag | Small base, same Python as the project, reproducible builds | `python:3.12` (much bigger), `latest` (not reproducible), Alpine (pandas wheels harder to install) | `task2/Dockerfile` |
| D5 | Copy `requirements.txt` and install before copying the code | Docker layer cache: changing the code does not reinstall the libraries (second build 1.1 s) | Copy everything at once | `task2/Dockerfile` |
| D6 | Non-root user `appuser` | If the app is compromised, the attacker is not root in the container | Run as root (default) | `task2/Dockerfile` |
| D7 | Data mounted as a read-only volume, path in `DATA_PATH` | The image stays independent of the data; the app cannot change the dataset | Copy the CSV into the image | `task2/compose.yaml` |
| D8 | Docker Compose, one service | One command to build and run; ports, env var and volume written in a file instead of a long `docker run` | Kubernetes on minikube (more setup, not needed for one service) | `task2/compose.yaml` |

**Evidence:** commits `d019b7a`, `3e557bf`, `3fed6d7`, `4ccfce6`.

## 4. Results

| Result | Value | Baseline or reference |
| --- | --- | --- |
| Rows shown in the app | 48,790 | Same as the Task 1 notebook |
| Share earning >50K (no filters) | 23.9% | Same as Task 1 |
| Women only | 16,176 people, 10.9% | Task 1: 10.9% |
| Image size | 805 MB | Base `python:3.12-slim` is about 150 MB |
| Rebuild after no change | 1.1 s (all layers cached) | First build 62 s |
| User inside the container | `appuser` | Default is `root` |

Architecture:

```
datasets/census_income.csv  --(read-only volume)-->  /data/census_income.csv
                                                         |
                                       DATA_PATH env var |
                                                         v
container "app" (python:3.12.16-slim, user appuser)
  app.py  --> cleaning.load_clean() --> cached DataFrame --> filters, metrics, chart
  streamlit on 0.0.0.0:8501  --(port 8501:8501)-->  browser on http://localhost:8501
```

**Evidence:** screenshot `task2/figures/app_in_container.png`; `docker run --rm census-app whoami`.

## 5. Problems and how you handled them

| Problem | Cause | What you did | Status |
| --- | --- | --- | --- |
| `requirements.txt` created in the wrong folder | VS Code shows nested folders compactly | Moved it to `task2/` | Solved |
| `compose.yaml` did not parse | Wrong indentation (spaces on empty lines, `ports:` too indented) | Fixed to 4 spaces, checked with `docker compose config --quiet` | Solved |
| Port 8501 possibly busy | The local Streamlit test was still running | Stopped it before starting the container | Solved |

**Evidence:** commit `4ccfce6`.

## 6. Limitations and trade-offs

| Area | Limitation or trade-off | Impact | Mitigation or next step |
| --- | --- | --- | --- |
| Image | 805 MB, mostly Streamlit and its dependencies | Slower to pull and push | Multi-stage build or a lighter framework |
| Architecture | One container does everything (no microservices) | Not the advanced objective | Split into a data API and a UI service |
| Configuration | No secrets needed (public data, no login) | Nothing to protect yet | If added, pass them with env vars or Docker secrets, never in the image or git |
| App | The cleaning runs at startup on the raw CSV | Startup takes a few seconds | Fine for 48k rows; precompute if the data grows |
| App | Charts show correlations only | Same limits as Task 1 | Said explicitly in the presentation |
| Security | No authentication on the app | Anyone on the network can open it | Only run locally |

**Evidence:** `task2/Dockerfile`, `task2/compose.yaml`.

## 7. Next steps

| Priority | Next step | Why | Effort |
| --- | --- | --- | --- |
| 1 | Add a health check in Compose | Docker knows if the app is really up | S |
| 2 | Split into API + UI services | Advanced objective (microservices) | L |
| 3 | Reduce image size | Faster deploys | M |

## 8. Use of AI assistants

| Tool | What you used it for | Where (files or sections) | How you checked the output |
| --- | --- | --- | --- |
| Claude | Code for the cleaning module and the Streamlit app | `task2/app/` | Ran the shape check and compared the numbers with the notebook |
| Claude | Explanation of Dockerfile instructions and Compose fields | `task2/Dockerfile`, `task2/compose.yaml` | Wrote them myself, built the image, checked the user and the app in the browser |

The full list is in `AI_LOG.md`. The choices of framework, base image, non-root user and read-only data volume are mine.

## Checklist

- [x] Task tag pushed and named in the table at the top
- [x] Runs from a fresh clone with the commands above
- [x] No secrets, API keys or large data files committed
- [x] Every section has an Evidence line
- [x] Every figure has a caption with a number
- [x] Guidance blocks and placeholders removed
- [x] `AI_LOG.md` up to date
