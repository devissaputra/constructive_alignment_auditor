import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from constructive_alignment_auditor import core


class CoreTests(unittest.TestCase):
    def test_bloom_level_detects_create(self):
        self.assertEqual(core.bloom_level("Design a prototype"), "create")

    def test_bloom_level_handles_inflected_verbs(self):
        self.assertEqual(core.bloom_level("Analyzing competing explanations"), "analyze")
        self.assertEqual(core.bloom_level("Evaluated the alternatives"), "evaluate")

    def test_highest_detected_level_wins(self):
        text = "Analyze the evidence and design a new intervention"
        self.assertEqual(core.bloom_level(text), "create")

    def test_unknown_level_is_explicit(self):
        self.assertEqual(core.bloom_level("Read chapter three"), "unknown")
        self.assertEqual(core.bloom_evidence("Read chapter three"), {})

    def test_bloom_evidence_is_transparent(self):
        evidence = core.bloom_evidence("Compare options and justify a recommendation")
        self.assertEqual(evidence["analyze"], ["compare"])
        self.assertEqual(evidence["evaluate"], ["justify", "recommend"])

    def test_content_tokens_remove_stopwords_and_normalize_plural(self):
        tokens = core.content_tokens("Compare the architectures in two systems")
        self.assertIn("architecture", tokens)
        self.assertIn("system", tokens)
        self.assertNotIn("the", tokens)

    def test_token_overlap_uses_content_words(self):
        overlap = core.token_overlap(
            "Analyze system tradeoffs",
            "Compare system architectures and tradeoffs",
        )
        self.assertGreater(overlap, 0)

    def test_empty_overlap_is_zero(self):
        self.assertEqual(core.token_overlap("", ""), 0.0)

    def test_compare_levels_same_level(self):
        result = core.compare_levels("analyze", "analyze")
        self.assertEqual(result, {"gap": 0, "relation": "same_level"})

    def test_compare_levels_above_and_below(self):
        self.assertEqual(
            core.compare_levels("analyze", "evaluate"),
            {"gap": 1, "relation": "above_outcome"},
        )
        self.assertEqual(
            core.compare_levels("analyze", "apply"),
            {"gap": -1, "relation": "below_outcome"},
        )

    def test_compare_levels_handles_unknown(self):
        self.assertEqual(
            core.compare_levels("unknown", "analyze"),
            {"gap": None, "relation": "unknown"},
        )

    def test_audit_reports_all_components(self):
        result = core.audit(
            "Analyze system tradeoffs",
            "Compare system architectures and tradeoffs",
            "Justify the selected system architecture",
        )
        self.assertEqual(result["outcome_level"], "analyze")
        self.assertEqual(result["activity_level"], "analyze")
        self.assertEqual(result["assessment_level"], "evaluate")
        self.assertEqual(result["activity_level_gap"], 0)
        self.assertEqual(result["assessment_level_gap"], 1)
        self.assertEqual(result["assessment_relation"], "above_outcome")
        self.assertIn("assessment_above_outcome", result["review_flags"])

    def test_assessment_below_outcome_is_flagged(self):
        result = core.audit(
            "Design a prototype",
            "Develop a prototype",
            "Explain the prototype",
        )
        self.assertIn("assessment_below_outcome", result["review_flags"])
        self.assertEqual(result["assessment_level_gap"], -4)

    def test_unknown_components_are_flagged(self):
        result = core.audit(
            "Read the documentation",
            "Discuss the documentation",
            "Write notes",
        )
        self.assertIn("outcome_level_unknown", result["review_flags"])
        self.assertIn("assessment_level_unknown", result["review_flags"])

    def test_non_string_text_is_rejected(self):
        with self.assertRaises(TypeError):
            core.bloom_level(None)
        with self.assertRaises(TypeError):
            core.token_overlap("text", 10)


if __name__ == "__main__":
    unittest.main()
