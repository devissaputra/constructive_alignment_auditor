# Analytic system card

## System

Constructive Alignment Auditor

## Purpose

Transparent decision-support for reviewing relationships among intended learning outcomes, learning activities, and assessment tasks.

## Current maturity

Working research prototype. The bundled example is synthetic and checks the software path only. It does not establish validity for accreditation, programme approval, instructor evaluation, or other consequential decisions.

## Inputs

The current baseline accepts three text fields:

- intended learning outcome
- learning activity
- assessment task

See `../data/README.md` for the synthetic schema and recommended fields for future expert-labelled studies.

## Outputs

The code reports:

- highest detected Bloom-style level for each curriculum element
- matched action verbs by level
- activity and assessment level gaps relative to the outcome
- relation labels: `same_level`, `below_outcome`, `above_outcome`, or `unknown`
- stopword-filtered lexical overlap
- transparent review flags
- a plain-language review summary

## Interpretation

A review flag is not a verdict. A higher or lower detected level can be pedagogically appropriate, and verb-based taxonomies cannot capture task complexity on their own.

The tool deliberately avoids a single overall alignment score.

## Evidence needed before real use

Evaluate against curriculum examples reviewed by multiple experts. Report inter-rater agreement, disagreement cases, unknown-verb rates, and error patterns. Compare the rule baseline with at least one semantic method before making claims about practical utility.

## Main limitations

The Bloom lexicon is incomplete and context-insensitive. Morphological normalization is lightweight. Jaccard overlap measures lexical similarity rather than conceptual alignment. Rubric quality, disciplinary conventions, scaffolding, authenticity, and assessment conditions are outside the current model.

## Human oversight

A qualified curriculum or instructional-design reviewer should interpret every flag in context. The prototype must not be used as an automatic accreditation, compliance, instructor-performance, or programme-quality judge.
