# AI Fact Checker Pro (Prompt-Engineered Version)

def build_prompt(claim):
    return f"""
You are an AI fact-checking system.

Task:
Analyze the following claim and respond in a structured format.

Claim: {claim}

Return format:
- Verdict: TRUE / FALSE / UNCERTAIN
- Reasoning: short explanation
- Confidence: low / medium / high
"""


def ai_engine(claim):
    prompt = build_prompt(claim)

    claim_lower = claim.lower()

    # Simulated AI reasoning (placeholder for real LLM/API later)
    if "earth" in claim_lower and "flat" in claim_lower:
        return {
            "prompt_used": prompt,
            "verdict": "FALSE",
            "reasoning": "Scientific evidence from astronomy confirms Earth is spherical.",
            "confidence": "high"
        }

    elif "2+2" in claim_lower:
        return {
            "prompt_used": prompt,
            "verdict": "TRUE",
            "reasoning": "Basic arithmetic confirms 2+2 equals 4.",
            "confidence": "high"
        }

    elif "kenya" in claim_lower and "capital" in claim_lower:
        return {
            "prompt_used": prompt,
            "verdict": "TRUE",
            "reasoning": "Nairobi is officially the capital of Kenya.",
            "confidence": "high"
        }

    else:
        return {
            "prompt_used": prompt,
            "verdict": "UNCERTAIN",
            "reasoning": "Insufficient data available. Requires external verification.",
            "confidence": "low"
        }


# Demo run
if __name__ == "__main__":
    test_claim = "The Earth is flat"

    result = ai_engine(test_claim)

    print("\n--- AI FACT CHECK REPORT ---\n")
    print("VERDICT:", result["verdict"])
    print("REASONING:", result["reasoning"])
    print("CONFIDENCE:", result["confidence"])
