# AI Fact Checker API Version (Real-world structure)

import json

def build_messages(claim):
    return [
        {
            "role": "system",
            "content": "You are a strict fact-checking AI. Respond only in JSON format."
        },
        {
            "role": "user",
            "content": f"""
Check this claim:

{claim}

Return format:
{{
  "verdict": "TRUE / FALSE / UNCERTAIN",
  "reasoning": "short explanation",
  "confidence": "low / medium / high"
}}
"""
        }
    ]


# Simulated API response (this is where a real API would connect)
def fake_ai_response(claim):
    claim_lower = claim.lower()

    if "earth" in claim_lower and "flat" in claim_lower:
        return {
            "verdict": "FALSE",
            "reasoning": "Scientific evidence confirms Earth is spherical.",
            "confidence": "high"
        }

    elif "2+2" in claim_lower:
        return {
            "verdict": "TRUE",
            "reasoning": "Basic arithmetic confirms 2+2 = 4.",
            "confidence": "high"
        }

    else:
        return {
            "verdict": "UNCERTAIN",
            "reasoning": "No reliable data available for verification.",
            "confidence": "low"
        }


def run_fact_checker(claim):
    messages = build_messages(claim)

    # In real life: this is where OpenAI API call would happen
    response = fake_ai_response(claim)

    return {
        "messages_sent": messages,
        "ai_response": response
    }


# Demo
if __name__ == "__main__":
    claim = "The Earth is flat"

    result = run_fact_checker(claim)

    print("\n--- AI FACT CHECK API OUTPUT ---\n")
    print(json.dumps(result, indent=2))
