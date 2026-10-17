"""Extract likely action items from meeting notes and save a reviewable task list."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ACTION = re.compile(r"\b(?:will|need to|needs to|should|must|action item:?|TODO:?|follow up:?|send|prepare|create|review|schedule)\b", re.I)


def extract_actions(notes: str) -> list[dict]:
    results = []
    for line in notes.splitlines():
        cleaned = re.sub(r"^\s*(?:[-*•]|\d+[.)])\s*", "", line).strip()
        if not cleaned or not ACTION.search(cleaned):
            continue
        owner_match = re.match(r"([A-Z][a-z]+)\s*:\s*(.*)", cleaned)
        owner, task = (owner_match.group(1), owner_match.group(2)) if owner_match else ("Unassigned", cleaned)
        results.append({"task": task, "owner": owner, "status": "needs review"})
    return results


def process(notes: str) -> list[dict]:
    print("Agent trace: 1) Split notes into lines  2) Found action-like language  3) Flagged items for human review")
    return extract_actions(notes)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract action items from a plain-text meeting note file.")
    parser.add_argument("notes_file", type=Path)
    parser.add_argument("--output", type=Path, default=Path("actions.json"))
    args = parser.parse_args()
    actions = process(args.notes_file.read_text(encoding="utf-8"))
    args.output.write_text(json.dumps(actions, indent=2), encoding="utf-8")
    print(f"Saved {len(actions)} reviewable action(s) to {args.output}")

