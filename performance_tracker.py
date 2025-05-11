
BASE_EXPECTED_RETURNS = {
    "Growth": 0.08,
    "Income": 0.05,
    "Balanced": 0.065
}

UPSIDE_CAPTURE = {"Growth": 1.15, "Income": 0.7, "Balanced": 0.9}
DOWNSIDE_CAPTURE = {"Growth": 1.1, "Income": 0.4, "Balanced": 0.6}

def get_performance_tracking(portfolio_type, current_ytd_return, market_ytd_return):
    base = BASE_EXPECTED_RETURNS.get(portfolio_type, 0.06)
    proj_return = current_ytd_return * (1 / 0.33)
    delta = proj_return - base
    flag = "Stable"
    if delta < -0.03: flag = "High Anxiety Risk"
    elif delta < -0.01: flag = "Medium Concern"
    return {
        "Base Target Return": round(base * 100, 2),
        "Current YTD Return": round(current_ytd_return * 100, 2),
        "Projected Annual Return": round(proj_return * 100, 2),
        "Return Delta vs Target": round(delta * 100, 2),
        "Behavioral Risk Alert": flag,
        "Upside Capture (%)": round(UPSIDE_CAPTURE.get(portfolio_type, 1.0) * 100, 1),
        "Downside Capture (%)": round(DOWNSIDE_CAPTURE.get(portfolio_type, 1.0) * 100, 1)
    }
