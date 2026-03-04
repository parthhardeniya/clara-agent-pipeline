import json
from pathlib import Path

def read_text(path):
    return Path(path).read_text(encoding="utf-8")

def read_json(path):
    return json.loads(Path(path).read_text())

def write_json(path, data):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path,"w") as f:
        json.dump(data,f,indent=2)

def write_text(path, text):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path,"w") as f:
        f.write(text)