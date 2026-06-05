# AI Fact Checker V2 (Prompt-Style Reasoning Simulation)

def fact_check_v2(claim):
    claim = claim.lower()

    response = {
        "claim": claim,
        "analysis": "",
        "result": ""
    }

    if "earth" in claim and "flat" in claim:
        response["analysis"] = "Scientific evidence from astronomy and physics shows Earth is spherical."
        response["result"] = "FALSE"

    elif "2+2" in claim:
        response["analysis"] = "Basic arithmetic rules apply."
        response["result"] = "TRUE"

    elif "kenya" in claim and "capital" in claim:
        response["analysis"] = "Geographical knowledge confirms Nairobi as capital."
        response["result"] = "TRUE"

    else:
        response["analysis"] = "Insufficient data. Requires external verification."
        response["result"] = "UNCERTAIN"

    return response


# Test run
if __name__ == "__main__":
    test = "The Earth is flat"
    result = fact_check_v2(test)

    print("CLAIM:", result["claim"])
    print("ANALYSIS:", result["analysis"])
    print("RESULT:", result["result"])
