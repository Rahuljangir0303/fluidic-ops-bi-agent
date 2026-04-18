from flask import Flask, render_template, request, redirect, url_for, session
from agent import run_agent
from chatbot import answer_query
from auth import check_login
import pandas as pd
import os
from report_generator import create_pdf
from flask import send_file


app = Flask(__name__)
app.secret_key = "secret123"


# 🔐 LOGIN ROUTE
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            return "Please enter username and password"

        if check_login(username, password):
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            return "Invalid Credentials"

    return render_template("login.html")


# 📊 DASHBOARD ROUTE
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))

    import os
    import pandas as pd

    file_path = "data/business_data.csv"
    response = ""

    # Upload
    if request.method == 'POST' and 'file' in request.files:
        file = request.files['file']
        if file.filename != "":
            file_path = os.path.join("data", file.filename)
            file.save(file_path)

    result = run_agent()

    if result is None:
        return "Error loading data"

    # Chatbot
    if request.method == 'POST' and 'query' in request.form:
        query = request.form.get('query')
        summary = pd.DataFrame(result["summary"])
        response = answer_query(query, summary)

    # Filter
    dept_filter = request.form.get('department')

    if dept_filter and dept_filter != "All":
        insights = [f"Showing data for {dept_filter}"]
        recommendations = [f"Analyze {dept_filter} carefully"]
    else:
        insights = result["insights"]
        recommendations = result["recommendations"]

    return render_template(
        "dashboard.html",
        insights=insights,
        recommendations=recommendations,
        ranking=result["ranking"],
        response=response
    )
    

# 🚪 LOGOUT ROUTE
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/download')
def download():
    result = run_agent()
    create_pdf(result["insights"], result["recommendations"])
    return send_file("reports/report.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)