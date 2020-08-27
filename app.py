import os
from flask import Flask, request, redirect, url_for

APIKEY = os.environ.get('TEST_APIKEY')
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('form_example'))

@app.route('/query-example')
def query_example():
    return 'TODO'

@app.route('/form-example', methods=['POST'])
def form_example():
    return '''<form method="POST">
                  Domain: <input type="text" name="domain"><br>
                  Page Path: <input type="text" name="page_path"><br>
                  Title: <input type="text" name="title"><br>
                  Overview:<br>
                  <textarea rows="10" cols="80" name="overview" placeholder="50 - 250 words"></textarea><br>
                  Features and Specifications:<br>
                  <textarea rows="10" cols="80" name="features_and_specifications" placeholder="More than 50 words"></textarea><br>
                  Potential Applications: <input type="text" name="potential_applications"><br>
                  Market Trends Opportunities: <input type="text" name="market_trends_opportunities"><br>
                  Customer Benefits: <input type="text" name="customer_benefits"><br>
                  Image Upload: <br>
                  Technology Categories: <input type="text" name="technology_categories"><br>
                  <input type="checkbox" id="help_market" name="ipi_to_help_market" value="1">
                  <label for="help_market">IPI to Help Market</label><br>
                  <input type="submit" value="Submit">
              </form>'''

if __name__ == '__main__':
    app.run(debug=True)
