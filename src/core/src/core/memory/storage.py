import json
from pathlib import Path
class JSONStorage:
    def __init__(self,path="data/memory/memory.json"):
        self.path=Path(path)
        self.path.parent.mkdir(parents=True,exist_ok=True)
        if not self.path.exists():
            self.save({})
    def load(self):
        return json.loads(self.path.read_text())
    def save(self,data):
        self.path.write_text(json.dumps(data,indent=2))
