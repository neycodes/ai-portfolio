# AI Fact Checker (Simple Portfolio Version)

def fact_check(claim):
    """
    Simple reasoning-based fact checker.
    In real AI systems, this would connect to APIs or models.
    """

    claim = claim.lower()

    # Basic heuristic logic (portfolio demo version)
    if "earth" in claim and "flat" in claim:
        return "FALSE - Scientific consensus confirms Earth is spherical."

    elif "2+2" in claim or "2 + 2" in claim:
        return "TRUE - Basic arithmetic confirms 2+2 = 4."

    elif "kenya" in claim and "capital" in claim:
        return "TRUE - Nairobi is the capital of Kenya."

    else:
        return "UNCERTAIN - Needs external verification or more data."


# Example usage
if __name__ == "__main__":
    test_claims = [
        "The Earth is flat",
        "2+2 equals 4",
        "The capital of Kenya is Nairobi",
        "AI will replace all jobs tomorrow"
    ]

    for claim in test_claims:
        print(f"Claim: {claim}")
        print(f"Result: {fact_check(claim)}")
        print("-" * 50)
