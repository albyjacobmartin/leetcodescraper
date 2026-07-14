# 📘 LeetCode Progress

A lightweight Python tool that fetches your complete LeetCode submission history using the GraphQL API and generates both a Markdown progress report and a progress curve image.

## Features

- Fetches all submissions from LeetCode using GraphQL
- Counts each problem using its **latest Accepted** submission
- Groups solved problems by date
- Calculates cumulative progress
- Generates a clean Markdown report
- Automatically exports structured progress data (`progress.json`)
- Generates a smooth progress curve image

---

## Example Report

| Day | Date | Solved Today | Cumulative |
|---:|:-----------|------------:|-----------:|
| 1 | 2026-06-15 | 2 | 2 |
| 2 | 2026-06-16 | 2 | 4 |
| 3 | 2026-06-17 | 2 | 6 |

---

## Requirements

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Setup

Create a `.env` file in the project root.

```env
LEETCODE_SESSION=your_session_cookie
```

---

## Generate Progress Report

Run:

```bash
python main.py
```

This generates:

- `summary.md`
- `progress.json`

---

## Generate Progress Plot

After generating the report:

```bash
python plot.py
```

This generates:

- `leetcode_progress.png`

---

## Project Structure

```text
.
├── api.py
├── config.py
├── main.py
├── plot.py
├── progress.py
├── report.py
├── requirements.txt
├── README.md
├── LICENSE
└── .env
```

---

## Generated Files

These files are generated automatically and are ignored by Git.

```text
summary.md
progress.json
leetcode_progress.png
```

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.