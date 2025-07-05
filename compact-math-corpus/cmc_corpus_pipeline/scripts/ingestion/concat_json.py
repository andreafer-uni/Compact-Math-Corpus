import json

file_paths = [
    'aajudson-processed.json',
    'dmlevin-processed.json',
    'lahefferon-processed.json'
]

combined_data = {"sentences": []}
for path in file_paths:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        combined_data["sentences"].extend(data.get("sentences", []))

with open("cmcorpus-concat.json", 'w', encoding='utf-8') as f:
    json.dump(combined_data, f, ensure_ascii=False, indent=2)
