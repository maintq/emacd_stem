import json

# Read definitions from enrich_all_stem_practice_and_quiz.py and run_master_curriculum_enrichment.py
with open("enrich_all_stem_practice_and_quiz.py", "r", encoding="utf-8") as f:
    text1 = f.read()

with open("run_master_curriculum_enrichment.py", "r", encoding="utf-8") as f:
    text2 = f.read()

print("Ready to assemble.")
