from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load Excel file
data_file = "your_excel_file.xlsx"  # Replace with your actual Excel file name
df = pd.read_excel(data_file)

# Rename columns for clarity
df.columns = ["S.No.", "Name", "Donation", "Locality/From Where Donation Received"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.json.get('query', '').lower()
    results = df[df.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)]
    return jsonify(results.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
