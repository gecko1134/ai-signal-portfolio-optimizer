def normalize_scores(score_list):
    total = sum(score_list)
    return [round(x / total, 4) for x in score_list] if total else [0] * len(score_list)
