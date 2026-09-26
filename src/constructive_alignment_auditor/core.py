# Calculation reading guide: ../CALCULATIONS.md (repository root).
# Content overlap = shared content tokens / union of content tokens.
# Lexical overlap is not semantic alignment. A Bloom verb can mean different things in context, and unknown levels should prompt review. The tool supports expert judgment rather than certifying curriculum quality.

import re

BLOOM = {
    "remember": {
        "define", "duplicate", "identify", "label", "list", "memorize",
        "name", "recognize", "recall", "repeat", "reproduce", "state",
    },
    "understand": {
        "classify", "describe", "discuss", "exemplify", "explain", "express",
        "infer", "interpret", "paraphrase", "report", "restate", "summarize",
        "translate",
    },
    "apply": {
        "apply", "calculate", "compute", "demonstrate", "employ", "execute",
        "illustrate", "implement", "operate", "practice", "prepare", "solve",
        "use",
    },
    "analyze": {
        "analyze", "categorize", "compare", "contrast", "deconstruct",
        "differentiate", "discriminate", "distinguish", "examine", "inspect",
        "investigate", "organize", "question", "relate", "separate", "structure",
        "test",
    },
    "evaluate": {
        "appraise", "argue", "assess", "critique", "defend", "estimate",
        "evaluate", "judge", "justify", "prioritize", "rate", "recommend",
        "support", "validate", "verify",
    },
    "create": {
        "assemble", "build", "combine", "compose", "construct", "create",
        "design", "develop", "devise", "formulate", "generate", "invent",
        "plan", "propose", "synthesize",
    },
}

BLOOM_ORDER = tuple(BLOOM)
BLOOM_INDEX = {level: index for index, level in enumerate(BLOOM_ORDER)}

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "in",
    "into", "is", "it", "of", "on", "or", "that", "the", "their", "this",
    "to", "with",
}


def _raw_tokens(text: str) -> list[str]:
    if not isinstance(text, str):
        raise TypeError("text inputs must be strings")
    return re.findall(r"[a-z]+", text.lower())


def _verb_candidates(token: str) -> set[str]:
    candidates = {token}

    if len(token) > 4 and token.endswith("ies"):
        candidates.add(token[:-3] + "y")

    if len(token) > 4 and token.endswith("ied"):
        candidates.add(token[:-3] + "y")

    if len(token) > 5 and token.endswith("ing"):
        stem = token[:-3]
        candidates.update({stem, stem + "e"})
        if len(stem) > 2 and stem[-1] == stem[-2]:
            candidates.add(stem[:-1])

    if len(token) > 4 and token.endswith("ed"):
        stem = token[:-2]
        candidates.update({stem, stem + "e"})
        if len(stem) > 2 and stem[-1] == stem[-2]:
            candidates.add(stem[:-1])

    if len(token) > 3 and token.endswith("es"):
        candidates.update({token[:-2], token[:-1]})

    if len(token) > 3 and token.endswith("s") and not token.endswith(
        ("ss", "us", "is")
    ):
        candidates.add(token[:-1])

    return candidates


def _canonical_bloom_verbs(text: str) -> dict[str, list[str]]:
    matches = {level: set() for level in BLOOM_ORDER}

    for token in _raw_tokens(text):
        candidates = _verb_candidates(token)
        for level, verbs in BLOOM.items():
            matched = candidates & verbs
            if matched:
                matches[level].update(matched)

    return {
        level: sorted(words)
        for level, words in matches.items()
        if words
    }


def bloom_evidence(text: str) -> dict[str, list[str]]:
    """Return the Bloom levels and action verbs explicitly detected in text."""
    return _canonical_bloom_verbs(text)


def bloom_level(text: str) -> str:
    """Return the highest Bloom level indicated by an explicit action verb."""
    evidence = bloom_evidence(text)
    for level in reversed(BLOOM_ORDER):
        if level in evidence:
            return level
    return "unknown"


def _normalize_content_token(token: str) -> str:
    if len(token) > 4 and token.endswith("ies"):
        return token[:-3] + "y"
    if len(token) > 4 and token.endswith("s") and not token.endswith(
        ("ss", "us", "is")
    ):
        return token[:-1]
    return token


def content_tokens(text: str) -> set[str]:
    """Return stopword-filtered, lightly normalized tokens for lexical comparison."""
    return {
        _normalize_content_token(token)
        for token in _raw_tokens(text)
        if token not in STOPWORDS
    }


def token_overlap(left: str, right: str) -> float:
    """Return Jaccard overlap between normalized content-word sets."""
    left_tokens = content_tokens(left)
    right_tokens = content_tokens(right)
    union = left_tokens | right_tokens
    return len(left_tokens & right_tokens) / len(union) if union else 0.0


def compare_levels(outcome_level: str, other_level: str) -> dict[str, object]:
    """Compare a detected activity or assessment level with the outcome level."""
    if outcome_level == "unknown" or other_level == "unknown":
        return {"gap": None, "relation": "unknown"}

    gap = BLOOM_INDEX[other_level] - BLOOM_INDEX[outcome_level]

    if gap == 0:
        relation = "same_level"
    elif gap < 0:
        relation = "below_outcome"
    else:
        relation = "above_outcome"

    return {"gap": gap, "relation": relation}


def _review_flags(
    outcome_level: str,
    activity_level: str,
    assessment_level: str,
) -> list[str]:
    flags = []

    if outcome_level == "unknown":
        flags.append("outcome_level_unknown")
    if activity_level == "unknown":
        flags.append("activity_level_unknown")
    if assessment_level == "unknown":
        flags.append("assessment_level_unknown")

    activity = compare_levels(outcome_level, activity_level)
    assessment = compare_levels(outcome_level, assessment_level)

    if activity["relation"] == "below_outcome":
        flags.append("activity_below_outcome")
    elif activity["relation"] == "above_outcome":
        flags.append("activity_above_outcome")

    if assessment["relation"] == "below_outcome":
        flags.append("assessment_below_outcome")
    elif assessment["relation"] == "above_outcome":
        flags.append("assessment_above_outcome")

    return flags


def _review_summary(flags: list[str]) -> str:
    if not flags:
        return (
            "No rule-based cognitive-level review flags were triggered. "
            "Expert review is still required."
        )

    messages = {
        "outcome_level_unknown": "No recognized Bloom action verb was found in the outcome.",
        "activity_level_unknown": "No recognized Bloom action verb was found in the activity.",
        "assessment_level_unknown": "No recognized Bloom action verb was found in the assessment.",
        "activity_below_outcome": (
            "The activity is classified below the outcome level; review whether it "
            "gives learners enough practice for the intended demand."
        ),
        "activity_above_outcome": (
            "The activity is classified above the outcome level; review whether the "
            "extra cognitive demand is intentional."
        ),
        "assessment_below_outcome": (
            "The assessment is classified below the outcome level; review whether it "
            "can demonstrate achievement of the intended outcome."
        ),
        "assessment_above_outcome": (
            "The assessment is classified above the outcome level; review whether the "
            "assessment demand exceeds what the stated outcome requires."
        ),
    }
    return " ".join(messages[flag] for flag in flags)


def audit(outcome: str, activity: str, assessment: str) -> dict[str, object]:
    """Produce transparent rule-based signals for constructive-alignment review."""
    outcome_level = bloom_level(outcome)
    activity_level = bloom_level(activity)
    assessment_level = bloom_level(assessment)

    activity_comparison = compare_levels(outcome_level, activity_level)
    assessment_comparison = compare_levels(outcome_level, assessment_level)
    flags = _review_flags(outcome_level, activity_level, assessment_level)

    return {
        "outcome_level": outcome_level,
        "activity_level": activity_level,
        "assessment_level": assessment_level,
        "outcome_evidence": bloom_evidence(outcome),
        "activity_evidence": bloom_evidence(activity),
        "assessment_evidence": bloom_evidence(assessment),
        "activity_level_gap": activity_comparison["gap"],
        "assessment_level_gap": assessment_comparison["gap"],
        "activity_relation": activity_comparison["relation"],
        "assessment_relation": assessment_comparison["relation"],
        "activity_overlap": token_overlap(outcome, activity),
        "assessment_overlap": token_overlap(outcome, assessment),
        "review_flags": flags,
        "review_summary": _review_summary(flags),
    }
