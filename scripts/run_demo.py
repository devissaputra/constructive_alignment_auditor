import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from constructive_alignment_auditor.core import audit


result = audit(
    "Analyze system tradeoffs",
    "Compare system architectures and tradeoffs",
    "Justify the selected system architecture",
)

for key, value in result.items():
    print(f"{key.replace('_', ' ').title()}: {value}")
