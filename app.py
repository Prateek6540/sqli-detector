from flask import Flask, render_template, request
import sys
from detector import scan_sql_injection

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        result = scan_sql_injection(url)
        
        # Extract results from the result_data dictionary
        logs = result.get("logs", [])
        form_list = result.get("form_list", [])
        sqli_detected = result.get("sqli_detected", [])
        risk_state = result.get("risk_state", [])
        db = result.get("db", [])
        
        # Pass the results to the HTML template
        return render_template('result.html', logs=logs, form_list=form_list, sqli_detected=sqli_detected, risk_state=risk_state, db=db)
    
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
