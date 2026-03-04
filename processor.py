from bs4 import BeautifulSoup
import json

class DataProcessor:
    def __init__(self, input_file="raw_data.jsonl", output_file="cleaned_data.jsonl"):
        self.input_file = input_file
        self.output_file = output_file
        self.trash_keywords = ["հաշվառումից հանված է"]

    def parse_html(self, html, cid):
        soup = BeautifulSoup(html, 'html.parser')
        name_div = soup.find("div", {"class": "compname"})
        if not name_div: return None

        details = {}
        table = soup.find("table", {"class": "formtbl"})
        if table:
            for row in table.find_all("tr"):
                k, v = row.find("td", {"class": "fnam"}), row.find("td", {"class": "fval"})
                if k and v:
                    details[k.text.strip().replace(":", "")] = v.text.strip()

        status = details.get('Կարգավիճակ', '').lower()
        if any(word in status for word in self.trash_keywords):
            return None

        return {"id": cid, "name": name_div.text.strip(), "details": details}

    def process_all(self):
        with open(self.input_file, 'r', encoding='utf-8') as fin, \
             open(self.output_file, 'w', encoding='utf-8') as fout:
            for line in fin:
                data = json.loads(line)
                clean_record = self.parse_html(data['html'], data['id'])
                if clean_record:
                    fout.write(json.dumps(clean_record, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    processor = DataProcessor()
    processor.process_all()