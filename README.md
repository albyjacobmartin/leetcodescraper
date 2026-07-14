# LeetCode Progress

A lightweight Python tool that generates a cumulative progress report from your LeetCode submission history.

## Features

- Fetches all submissions using LeetCode GraphQL
- Counts each problem using the latest Accepted submission
- Groups solved problems by date
- Calculates cumulative progress
- Generates a clean Markdown report

## Example

| Day | Date | Solved Today | Cumulative |
|---:|:-----------|------------:|-----------:|
| 1 | 2026-06-15 | 2 | 2 |
| 2 | 2026-06-16 | 2 | 4 |
| 3 | 2026-06-17 | 2 | 6 |

## Requirements

```bash
pip install -r requirements.txt
```

## Setup

Create a `.env` file:

```env
LEETCODE_SESSION=your_session_cookie
```

## Run

```bash
python main.py
```

A `summary.md` file will be generated.

## Project Structure

```text
api.py
config.py
main.py
progress.py
report.py
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.