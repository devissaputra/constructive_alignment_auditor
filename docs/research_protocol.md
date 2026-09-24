# Research protocol

## Project

Constructive Alignment Auditor

## Questions

1. Where do outcome verbs, learning activities, and assessment demands diverge?
2. Can transparent text features support expert review without replacing instructional judgment?
3. Which alignment gaps should be prioritized for redesign?

## Baseline methods

- Bloom verb classification
- Jaccard token overlap
- outcome activity comparison
- outcome assessment comparison
- human review summary

## Evidence to collect

Start from the current transparent baseline and record every transformation needed to produce Bloom level labels and two transparent lexical overlap scores. Keep a clear boundary between synthetic demonstration data and any future empirical dataset.

## Validation

Use multiple expert reviewers to label alignment examples, calculate agreement, and compare the rule baseline with a stronger semantic method. Analyze false alarms and missed mismatches separately.

## What counts as a useful result

I would next build a labeled set of curriculum examples reviewed by instructional design experts. The baseline can then be compared with a semantic model and evaluated on disagreement cases rather than only average agreement.

## Threats to validity

Learning outcomes can contain several verbs, the same verb can imply different complexity by context, and lexical overlap can reward wording similarity without genuine alignment.
