def generate_insights(summary):
    insights = []

    for dept, row in summary.iterrows():
        profit = row['profit']
        sales = row['sales']
        expenses = row['expenses']

        if profit > 20000:
            insights.append(f"{dept} is performing very well with high profit.")
        elif profit > 10000:
            insights.append(f"{dept} is stable but can improve further.")
        else:
            insights.append(f"{dept} needs improvement due to low profit.")

    return insights


def generate_recommendations(summary):
    recommendations = []

    for dept, row in summary.iterrows():
        sales = row['sales']
        expenses = row['expenses']

        if expenses > sales * 0.7:
            recommendations.append(f"Reduce expenses in {dept}.")

        if sales < 30000:
            recommendations.append(f"Increase marketing efforts in {dept}.")

    return recommendations