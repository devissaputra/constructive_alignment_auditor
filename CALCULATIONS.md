# Calculation guide

## Question and evidence

Where might objectives, activities and assessments be misaligned?

Supplied instructional statements and a transparent Bloom-verb lexicon.

**Status:** SYNTHETIC / RULE-BASED PROTOTYPE | no educational validity claim.

## Design

Extract candidate verbs and content overlap; compare cognitive levels; expose unknowns and review flags.

## Calculation and interpretation

`Content overlap = shared content tokens / union of content tokens.`

Lexical overlap is not semantic alignment. A Bloom verb can mean different things in context, and unknown levels should prompt review. The tool supports expert judgment rather than certifying curriculum quality.

## Evidence table

Worked example — illustrative, not a measured research result. Full precision below is for traceability, not a claim of measurement precision.

| Quantity | Value | Unit / meaning | JSON path |
|---|---:|---|---|
| token Jaccard: 2 shared / 4 union | 0.5 | unitless | `outputs.token Jaccard: 2 shared / 4 union` |

Source: [results/review_examples.json](results/review_examples.json). Values resolve directly from this file when figures are regenerated.

This auditor compares learning objectives, activities, and assessments using an explicit Bloom-verb lexicon and content-token overlap. It reports the evidence behind each inferred level and flags uncertain or mismatched components for review. Its strength is inspectability: the lexical rules are easy to challenge, and the output is framed as a prompt for instructional-design judgment rather than a validated alignment score.

## Verification performed in this review

15 existing unittest checks passed. The bundled demonstration executed successfully in this review.

The figure-generation check verifies agreement between the selected source values and SVGs. It does not validate the raw dataset, fitted model, identification assumptions, or external generalization.

```bash
python scripts/build_review_figures.py
python scripts/build_review_figures.py --check
```

For the explicitly illustrative example:

```bash
python scripts/review_examples.py
```

## Implementation map

Follow these functions to inspect each transformation. Validation helpers and private functions remain visible in the linked modules.

| Function | Purpose / documented behavior |
|---|---|
| [`bloom_evidence`](src/constructive_alignment_auditor/core.py#L105) | Return the Bloom levels and action verbs explicitly detected in text. |
| [`bloom_level`](src/constructive_alignment_auditor/core.py#L110) | Return the highest Bloom level indicated by an explicit action verb. |
| [`content_tokens`](src/constructive_alignment_auditor/core.py#L129) | Return stopword-filtered, lightly normalized tokens for lexical comparison. |
| [`token_overlap`](src/constructive_alignment_auditor/core.py#L138) | Return Jaccard overlap between normalized content-word sets. |
| [`compare_levels`](src/constructive_alignment_auditor/core.py#L146) | Compare a detected activity or assessment level with the outcome level. |
| [`audit`](src/constructive_alignment_auditor/core.py#L224) | Produce transparent rule-based signals for constructive-alignment review. |

## What remains before a stronger research claim

Lexical overlap is not semantic alignment. A Bloom verb can mean different things in context, and unknown levels should prompt review. The tool supports expert judgment rather than certifying curriculum quality. A successful software test is not validation of a scientific construct. New experiments should state their split unit, comparator, outcome, uncertainty procedure and failure criteria before examining final test results.
