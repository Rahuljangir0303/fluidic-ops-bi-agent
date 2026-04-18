def answer_query(query, summary):
    query = query.lower()

    # Best department
    if "best" in query:
        best = summary['profit'].idxmax()
        return f"{best} is the best performing department."

    # Worst department
    elif "worst" in query or "weak" in query:
        worst = summary['profit'].idxmin()
        return f"{worst} is the weakest department."

    # Profit info
    elif "profit" in query:
        response = ""
        for dept, row in summary.iterrows():
            response += f"{dept} profit is {row['profit']}\n"
        return response

    # Recommendation
    elif "recommend" in query:
        return "Focus on reducing expenses and increasing sales."

    else:
        return "Sorry, I didn't understand. Try asking about best, worst, profit, or recommendations."