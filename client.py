class EcommerceSmartProductComparisonDecisionEngineClient:
    def compare_products(self, product_ids: list, user_preferences: dict = None) -> dict:
        matrix = {
            "Product_A": {"battery": "12h", "price": "$199", "sentiment": "Positive (88%)"},
            "Product_B": {"battery": "18h", "price": "$249", "sentiment": "Highly Positive (94%)"}
        }
        return {
            "top_recommendation": "Product_B (Best battery & user satisfaction match)",
            "comparison_matrix": matrix,
            "value_for_money_score": 9.2
        }
