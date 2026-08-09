from client import EcommerceSmartProductComparisonDecisionEngineClient

def main():
    client = EcommerceSmartProductComparisonDecisionEngineClient()
    res = client.compare_products(["PROD_001", "PROD_002"], {"priority": "battery_life"})
    print(f"Top Recommendation: {res['top_recommendation']}")
    print(f"Value Score: {res['value_for_money_score']}/10")

if __name__ == "__main__":
    main()
