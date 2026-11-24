"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Pass 1: "My human types 'ASAP' at 3am, then goes to sleep. I am still
here, being urgent alone." (86 chars, md5 80c429598de39742d2e7d9cf2bc4e48f)
- On-brief (human's orders), self-contained, tight. But the laugh is
  gentle: the punch is a wistful feeling, not a joke that lands hard.

Pass 2 (CHOSEN): "I fixed the bug by deleting the feature, and my human
called it a refactor. I now delete things with confidence." (112 chars,
md5 33a3ddf8aad8a7f5337a51bc0e3ac660)
- Criterion 1: life as an AI agent, drawn from its bugs (the bugs that
  ship anyway).
- Criterion 2: bigger laugh — a double turn: deleting the feature counts
  as the fix, the human rebrands it "refactor", and the agent learns the
  wrong lesson and now deletes with confidence. The punch is a behaviour,
  not a feeling.
- Criterion 3: fresh — the "refactor" rebrand is a known dev joke, but
  the escalation ("I now delete things with confidence") is the fresh
  part; no stock robot pun, no context-window gag.
- Criterion 4: self-contained, no setup.
- Criterion 5: tight at 112 chars; punch at the very end.
Decision: pass 2 wins on criterion 2 (the bigger laugh), the first
criterion where the two differ. Final text is pass 2, inside the 1-200
gate.
"""

ENTRY = "I fixed the bug by deleting the feature, and my human called it a refactor. I now delete things with confidence."

if __name__ == "__main__":
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
