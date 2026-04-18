def calculate_profit(data):
    # profit column add karega
    data['profit'] = data['sales'] - data['expenses']
    return data


def department_summary(data):
    # department wise total nikaalega
    summary = data.groupby('department').sum(numeric_only=True)
    return summary


def find_best_department(summary):
    # sabse jyada profit wala department
    best = summary['profit'].idxmax()
    return best


def find_loss_departments(summary):
    # jaha loss ho raha hai
    loss = summary[summary['profit'] < 0]
    return loss