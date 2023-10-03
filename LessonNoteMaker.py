import os
from datetime import date
import json

PATH = os.getcwd()


def createFile(Title, body) -> None:        
    try:
        with open(f"{title}.md", "x") as f:
            f.writelines(body)

    except FileExistsError:
        print(f"File: {Title}.md , Already Exists, File not created")
        input()


current_date = date.today()

title = date.isoformat(current_date).replace("-",".")

with open("Week time table.JSON", "r") as f:
    table = json.load(f)

WEEK_TIMETABLE = [table[i] for i in table]

metadata = f"""
---
aliases : []
tags : ["Lesson_Notes", "{WEEK_TIMETABLE[date.isoweekday(current_date)-1]["teacher"]}", "{WEEK_TIMETABLE[date.isoweekday(current_date)-1]["lesson"]}"]
---
"""

createFile(title, [metadata, "\n", "---\n"])