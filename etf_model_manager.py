
ETF_MODELS = {
    'Growth': {'VUG': 0.4, 'QQQ': 0.3, 'IWF': 0.3},
    'Income': {'VYM': 0.4, 'SCHD': 0.3, 'HDV': 0.3},
    'Balanced': {'VTI': 0.5, 'BND': 0.3, 'VNQ': 0.2}
}

ETF_SIGNAL_SCORES = {
    'VUG': 82, 'QQQ': 75, 'IWF': 65,
    'VYM': 58, 'SCHD': 62, 'HDV': 55,
    'VTI': 70, 'BND': 50, 'VNQ': 48
}

def evaluate_etf_model(model_name):
    portfolio = ETF_MODELS.get(model_name, {})
    score = sum(weight * ETF_SIGNAL_SCORES.get(etf, 50) for etf, weight in portfolio.items())
    return round(score, 2)

def suggest_replacements(model_name):
    portfolio = ETF_MODELS.get(model_name, {})
    suggestions = {}
    for etf in portfolio:
        score = ETF_SIGNAL_SCORES.get(etf, 50)
        if score < 60:
            best = max((e for e in ETF_SIGNAL_SCORES.items() if e[1] > score and e[0] not in portfolio), key=lambda x: x[1], default=None)
            if best: suggestions[etf] = best[0]
    return suggestions
