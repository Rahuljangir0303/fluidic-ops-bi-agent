def evaluate_department(row):
    score = 0

    # Profit weight
    if row['profit'] > 20000:
        score += 3
    elif row['profit'] > 10000:
        score += 2
    else:
        score += 1

    # Expense efficiency
    if row['expenses'] < row['sales'] * 0.5:
        score += 2
    else:
        score += 1

    return score


def rank_departments(summary):
    ranking = {}

    for dept, row in summary.iterrows():
        ranking[dept] = evaluate_department(row)

    sorted_rank = sorted(ranking.items(), key=lambda x: x[1], reverse=True)
    return sorted_rank