from data_loader import load_data
from analyzer import calculate_profit, department_summary
from insights import generate_insights, generate_recommendations
from decision_engine import rank_departments
from charts import generate_chart
import data_loader
print(dir(data_loader))

def run_agent():
    data = load_data("data/business_data.csv")

    if data is None:
        return None

    data = calculate_profit(data)
    summary = department_summary(data)

    insights = generate_insights(summary)
    recommendations = generate_recommendations(summary)
    ranking = rank_departments(summary)

    generate_chart(summary)

    return {
        "summary": summary.to_dict(),
        "insights": insights,
        "recommendations": recommendations,
        "ranking": ranking
    }