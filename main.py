import os
# One-liner entry (max 200 chars): the line below is the entire submission.
# Writes the roast to /output/entry.txt.
LINE = "My agent has a PhD in confidently explaining my own code back to me, incorrectly, and then billing me for the lesson."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
