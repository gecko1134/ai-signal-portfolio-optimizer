
def analyze_uploaded_portfolio(uploaded_df, available_models):
    portfolio = uploaded_df.set_index("Ticker")["Weight (%)"].to_dict()
    summary = {
        "Total Holdings": len(portfolio),
        "Total Weight": sum(portfolio.values()),
        "Overweight Assets": [],
        "Underweight Assets": [],
        "Missing from Model": [],
        "Suggested Allocation": {}
    }
    for model_name, model in available_models.items():
        for ticker, model_weight in model.items():
            current_weight = portfolio.get(ticker, 0)
            delta = round(current_weight - (model_weight * 100), 2)
            if delta > 10:
                summary["Overweight Assets"].append((ticker, delta))
            elif delta < -10:
                summary["Underweight Assets"].append((ticker, delta))
        summary["Missing from Model"] = list(set(model.keys()) - set(portfolio.keys()))
        summary["Suggested Allocation"] = {k: round(v * 100, 1) for k, v in model.items()}
        break
    return summary
