import re

BLOOM = {
    "remember": {"define", "list", "recall", "identify"},
    "understand": {"explain", "summarize", "classify"},
    "apply": {"apply", "calculate", "demonstrate", "use"},
    "analyze": {"analyze", "compare", "differentiate"},
    "evaluate": {"evaluate", "justify", "critique"},
    "create": {"design", "create", "develop", "construct"},
}
BLOOM_ORDER = tuple(BLOOM)


def _tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-z]+", text.lower()))


def bloom_level(text: str) -> str:
    """Return the highest Bloom level indicated by an explicit action verb."""
    words = _tokens(text)
    for level in reversed(BLOOM_ORDER):
        if words & BLOOM[level]:
            return level
    return "unknown"


def token_overlap(left: str, right: str) -> float:
    """Return Jaccard overlap between lowercased word sets."""
    left_tokens = _tokens(left)
    right_tokens = _tokens(right)
    union = left_tokens | right_tokens
    return len(left_tokens & right_tokens) / len(union) if union else 0.0


def audit(outcome: str, activity: str, assessment: str) -> dict:
    """Summarize cognitive levels and lexical overlap for a design review."""
    return {
        "outcome_level": bloom_level(outcome),
        "activity_level": bloom_level(activity),
        "assessment_level": bloom_level(assessment),
        "activity_overlap": token_overlap(outcome, activity),
        "assessment_overlap": token_overlap(outcome, assessment),
    }
