# Analytic system card

## System

Constructive Alignment Auditor

## Purpose

Rule based baseline for checking cognitive level and lexical overlap across outcomes, activities, and assessments.

## Current maturity

Working research prototype. The bundled example checks the software path with synthetic inputs. It does not establish validity for real learners, instructors, courses, or workplaces.

## Inputs

See `../data/README.md` for the current synthetic schema and the documentation expected before real data are connected.

## Outputs

The current code produces Bloom level labels and two transparent lexical overlap scores. These outputs are research signals and should be interpreted with the educational context that produced them.

## Evidence needed before real use

Use multiple expert reviewers to label alignment examples, calculate agreement, and compare the rule baseline with a stronger semantic method. Analyze false alarms and missed mismatches separately.

## Main limitation

Bloom verbs and token overlap are crude proxies for constructive alignment. Context, task complexity, rubric quality, and disciplinary conventions still require expert judgment.

## Human oversight

A person must review any output before it can affect a learner, instructor, applicant, or employee.
