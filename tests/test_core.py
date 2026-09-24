import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from constructive_alignment_auditor import core


class CoreTests(unittest.TestCase):
    def test_bloom_level_and_overlap(self):
        self.assertEqual(core.bloom_level("Design a prototype"), "create")
        self.assertGreater(core.token_overlap("analyze data", "analyze data patterns"), 0)

    def test_audit_reports_each_component(self):
        result = core.audit("Analyze evidence", "Compare evidence", "Justify a decision")
        self.assertEqual(result["outcome_level"], "analyze")
        self.assertEqual(result["assessment_level"], "evaluate")


if __name__ == "__main__":
    unittest.main()
