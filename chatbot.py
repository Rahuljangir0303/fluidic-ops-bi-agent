import pandas as pd
import os

# ✅ pehle path banao
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, "business_data.csv")

# ✅ fir print karo
print("PATH CHECK:", file_path)
print("FILE EXISTS:", os.path.exists(file_path))

# ✅ fir read karo
df = pd.read_csv(file_path)

def answer_query(query):
    query = query.lower()

    # ✅ TOTAL PROFIT
    if "profit" in query and "electronics" not in query and "clothing" not in query:
        total_profit = (df["sales"] - df["expenses"]).sum()
        return f"Total Profit is ₹{total_profit}"

    # ✅ ELECTRONICS PROFIT
    elif "electronics" in query and "profit" in query:
        data = df[df["department"].str.lower() == "electronics"]
        profit = (data["sales"] - data["expenses"]).sum()
        return f"Electronics Profit is ₹{profit}"

    # ✅ CLOTHING PROFIT
    elif "clothing" in query and "profit" in query:
        data = df[df["department"].str.lower() == "clothing"]
        profit = (data["sales"] - data["expenses"]).sum()
        return f"Clothing Profit is ₹{profit}"

    return "I didn't understand your question 🤖"