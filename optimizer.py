def score_candidate(c, weights):
    # cost normalized; higher comfort is better
    cost_score = (c['cost'] / 1000.0)
    return weights['cost'] * cost_score - weights['comfort'] * c['comfort']

def optimize_candidates(candidates, weights=None, top_k=3):
    weights = weights or {'cost': 0.5, 'comfort': 0.5}
    ranked = sorted(candidates, key=lambda c: score_candidate(c, weights))
    return ranked[:top_k]
