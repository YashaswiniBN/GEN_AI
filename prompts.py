# day3-prompt-engineering/prompts.py
# NOTE: API calls commented out until API key available
# Prompts tested manually via Google AI Studio / Claude.ai
# Results documented in README.md

REVIEW = "The product arrived on time but quality was much worse than pictures suggested. Stitching was coming apart already."

# ── 1. Zero-shot ──────────────────────────────────────────────
ZERO_SHOT_SYSTEM = "You are a helpful assistant."

ZERO_SHOT_USER = f"""Classify the sentiment of this review as Positive, Negative, or Neutral.

Review: {REVIEW}"""

# ── 2. Few-shot ───────────────────────────────────────────────
FEW_SHOT_SYSTEM = "You are a sentiment classifier."

FEW_SHOT_USER = f"""Classify sentiment as Positive, Negative, or Neutral.

Review: "Absolutely love this, works perfectly!" → Positive
Review: "Stopped working after two days. Disappointed." → Negative
Review: "It's okay, nothing special." → Neutral

Review: "{REVIEW}" →"""

# ── 3. Chain-of-thought ───────────────────────────────────────
COT_SYSTEM = "You are a reasoning assistant. Always think step by step before giving your final answer."

COT_USER = f"""Classify the sentiment of this review.
Think through it carefully step by step before answering.

Review: {REVIEW}"""

# ── 4. Structured output ──────────────────────────────────────
STRUCTURED_SYSTEM = """You are a data extraction API.
Return ONLY valid JSON. No explanation. No markdown backticks.

Schema:
{{
  "sentiment": "positive" | "negative" | "neutral",
  "issues": ["list of specific problems mentioned"],
  "rating_estimate": 1-5
}}"""

STRUCTURED_USER = f"Extract from this review: {REVIEW}"

# ── 5. Negative prompting ─────────────────────────────────────
NEGATIVE_SYSTEM = """Summarise customer reviews in one sentence.
Rules:
- Do NOT start with 'The customer'
- Do NOT use 'Overall', 'In summary', or 'The review states'
- Do NOT add suggestions or recommendations
- Maximum 20 words"""

NEGATIVE_USER = f"Review: {REVIEW}"


# ── Results from manual testing (Google AI Studio) ────────────
RESULTS = {
    "zero_shot": {
        "output": "Negative",
        "observation": "Correct label but no reasoning, format varies"
    },
    "few_shot": {
        "output": "Negative",
        "observation": "More consistent, exactly matched example format"
    },
    "chain_of_thought": {
        "output": "Step 1: Product arrived on time — positive signal. Step 2: Quality worse than shown — negative. Step 3: Stitching failing — negative. Final: Negative",
        "observation": "Showed reasoning trace, most reliable on edge cases"
    },
    "structured": {
        "output": '{"sentiment": "negative", "issues": ["quality worse than images", "stitching coming apart"], "rating_estimate": 2}',
        "observation": "Valid JSON, parseable, required temp=0 to be reliable"
    },
    "negative": {
        "output": "Product quality fell far short of advertised images with stitching defects noted on arrival.",
        "observation": "Clean output, no filler phrases, under 20 words"
    }
}

# ── Key learnings ─────────────────────────────────────────────
LEARNINGS = """
1. Few-shot beats zero-shot when output format matters
2. CoT is most reliable for ambiguous or edge-case inputs
3. Structured output needs explicit schema + low temperature
4. Negative prompting eliminates default model habits
5. Same task, 5 prompts = measurably different quality outputs
"""