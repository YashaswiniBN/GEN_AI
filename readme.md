# Day 3 — Prompt Engineering

Five prompting techniques applied to the same sentiment classification task.
Tested manually via Google AI Studio (Gemini 1.5 Flash) — API integration pending.

## Techniques
| # | Technique | Best for |
|---|-----------|----------|
| 1 | Zero-shot | Quick, simple tasks |
| 2 | Few-shot | Format-sensitive tasks |
| 3 | Chain-of-thought | Reasoning, edge cases |
| 4 | Structured output | Downstream code parsing |
| 5 | Negative prompting | Suppressing model habits |

## Key finding
CoT produced the most reliable output on ambiguous inputs.
Structured output required explicit schema + low temperature to avoid formatting errors.

## Tools used
- Google AI Studio (Gemini 1.5 Flash) — free, no API key needed
- Claude.ai — for comparison testing