# Research protocol

## Project

Constructive Alignment Auditor

## Research questions

1. Where do the cognitive demands of intended outcomes, learning activities, and assessment tasks differ?
2. Can transparent rule-based signals help curriculum reviewers notice cases worth closer inspection?
3. How often do rule-based review flags agree or disagree with expert curriculum judgments?

## Current baseline

The baseline intentionally separates two kinds of evidence:

- **cognitive-level evidence** from explicitly detected Bloom-style action verbs
- **lexical evidence** from stopword-filtered Jaccard overlap between curriculum elements

The system reports detected levels, matched verbs, level gaps, direction of the gap, lexical overlap, and review flags. It does not combine these signals into a single opaque alignment score.

## Interpretation of level gaps

A level difference is a **review signal**, not proof of misalignment. An activity or assessment may legitimately operate above the stated outcome, and disciplinary context can change the meaning and complexity of a verb.

The baseline therefore uses labels such as `above_outcome`, `below_outcome`, and `same_level` rather than automatically declaring an item aligned or misaligned.

## Evidence to collect

For an empirical study, record:

- outcome, activity, and assessment text
- discipline and educational level
- expert cognitive-level labels
- expert constructive-alignment judgments
- reviewer confidence
- whether a flagged difference is intentional
- reasons for disagreement between reviewers and the baseline

## Validation

Use multiple instructional-design or curriculum experts. Report inter-rater agreement before treating expert labels as a reference. Compare the rule baseline with stronger semantic methods under the same labeled examples.

Evaluate separate error types, including:

- missed lower-demand activities or assessments
- unnecessary flags for intentionally higher-demand tasks
- unknown verbs
- lexical false positives caused by shared wording
- lexical false negatives caused by paraphrase

## What counts as a useful result

A useful result is not simply high average agreement. The study should show which kinds of curriculum cases the transparent baseline helps reviewers inspect and where it breaks down.

## Threats to validity

A single outcome may contain several verbs. The same verb can represent different complexity across disciplines. Bloom-style verb lists are heuristics rather than a complete representation of cognitive demand. Lexical overlap measures wording similarity, not conceptual equivalence. Expert reviewers can also disagree about alignment.
