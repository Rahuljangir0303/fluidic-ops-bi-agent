import matplotlib
matplotlib.use('Agg')   # ✅ no GUI backend
import matplotlib.pyplot as plt

def generate_chart(summary):
    # Bar Chart
    summary['profit'].plot(kind='bar')
    plt.title("Profit by Department")
    plt.savefig("static/bar_chart.png")
    plt.close()

    # Pie Chart
    summary['profit'].plot(kind='pie', autopct='%1.1f%%')
    plt.title("Profit Distribution")
    plt.ylabel('')
    plt.savefig("static/pie_chart.png")
    plt.close()