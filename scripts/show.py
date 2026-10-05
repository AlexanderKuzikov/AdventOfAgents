import json
import sys
from pathlib import Path

day = sys.argv[1] if len(sys.argv) > 1 else "day02"
path = Path("data") / day / ("translation.json" if len(sys.argv) > 2 else "draft.json")
data = json.loads(path.read_text(encoding="utf-8"))
segs = data["segments"] if isinstance(data, dict) else data

for i, s in enumerate(segs):
    print("[{}] ({}s) {}".format(i, s["t"], s["en"]))