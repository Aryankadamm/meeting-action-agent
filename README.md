# Meeting Action Agent

A small meeting-notes assistant that identifies likely action items, captures simple `Name: task` ownership, and saves results as JSON for a person to review.

## Run it

Requires Python 3.10+; no packages or API key required.

```bash
python agent.py sample-notes.txt
```

By default it writes `actions.json`. You can choose another path with `--output reviewed-actions.json`.

## Design notes

The prototype uses explicit action-language patterns rather than an LLM, so its limits are visible and its output is predictable. It labels results `needs review` because pattern matching can miss tasks or select the wrong sentence. A next step is to add an LLM extraction adapter with a strict JSON schema and compare precision/recall against manually labeled notes.

## Skills demonstrated

Python, text processing, lightweight agent workflow, structured output, human review, and clear limitations.

