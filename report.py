import json
from config import OUTPUT_FILE

def generate_markdown(daily):
    running_total = 0
    total_problems = sum(daily.values())
    json_data = {
        "total_problems": total_problems,
        "activity_days": len(daily),
        "days": []
    }
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write("# LeetCode Progress\n\n")
        file.write("| Statistics | Value |\n")
        file.write("|------------|------:|\n")
        file.write(f"| Total Problems | {total_problems} |\n")
        file.write(f"| Active Days | {len(daily)} |\n\n")
        file.write("---\n\n")
        file.write("## Daily Progress\n\n")
        file.write("| Day | Date | Solved | Total |\n")
        file.write("|---:|------------|------:|------:|\n")
        for day, (date, solved_today) in enumerate(daily.items(), start=1):
            running_total += solved_today
            file.write(f"| {day} | {date} | {solved_today} | {running_total} |\n")
            json_data["days"].append({
                "day": day,
                "date": date,
                "completed_today": solved_today,
                "cumulative": running_total
            })
    with open("progress.json", "w", encoding="utf-8") as file:
        json.dump(json_data, file, indent=4)