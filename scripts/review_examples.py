"""Reproduce the labeled worked example; this is not an empirical study."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from constructive_alignment_auditor import core
outputs={'token Jaccard: 2 shared / 4 union': 2/4}
result={'kind':'illustrative_calculation','note':'Illustrative overlap arithmetic, not semantic validation.','outputs':outputs}
(ROOT/'results/review_examples.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
