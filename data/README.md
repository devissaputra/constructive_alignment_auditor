# Data Documentation

## Included data

`sample.csv` contains one synthetic curriculum-design example used for smoke tests and demonstrations. It contains no learner records or personal data.

## Current schema

- `course_id`: synthetic course identifier
- `module_id`: synthetic module or unit identifier
- `outcome`: intended learning outcome text
- `activity`: teaching or learning activity text
- `assessment`: assessment task text

A future research dataset may also include rubric criteria, discipline, programme level, reviewer IDs, expert alignment judgments, and reviewer notes.

## What the baseline needs

The current code operates on three text fields: outcome, activity, and assessment. Production adapters should validate that these fields are present, non-empty, and mapped to the correct curriculum unit before analysis.

## Expert-labelled evaluation data

For empirical evaluation, keep the automated signals separate from expert judgments. Recommended labels include:

- detected or assigned cognitive level for each curriculum element
- whether an activity gives adequate practice for the stated outcome
- whether an assessment can demonstrate achievement of the outcome
- whether a flagged level difference is pedagogically intentional
- reviewer confidence and notes

Use multiple reviewers when possible and report inter-rater agreement.

## Do not commit

Do not commit confidential curriculum documents, restricted institutional materials, private student work, accreditation evidence that cannot be redistributed, or licensed content that prohibits publication.

## Dataset card requirement

For any real study, document source, permission or license, educational level, discipline, inclusion criteria, preprocessing, annotation procedure, reviewer expertise, disagreement handling, known limitations, and permitted uses.
