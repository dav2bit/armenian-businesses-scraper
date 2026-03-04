import json

def sort_by_date(filename="cleaned_data.jsonl"):
    records = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            records.append(json.loads(line))
    
    # Sort by registration date [cite: 18]
    records.sort(key=lambda x: x.get('details', {}).get('Գրանցման ամսաթիվ', '0000-00-00'), reverse=True)
    
    with open("final_businesses.jsonl", "w", encoding="utf-8") as f:
        for item in records:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
    print(f"Successfully sorted {len(records)} records.")

if __name__ == "__main__":
    sort_by_date()