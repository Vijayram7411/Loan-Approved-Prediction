from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Function to predict loan approval
def predict_loan_approval(data):
    if data['credit_score'] >= 700 and data['income'] >= 30000:
        return {'prediction': 'Approved', 'probability': 95}
    elif data['credit_score'] >= 600:
        return {'prediction': 'Conditionally Approved', 'probability': 75}
    else:
        return {'prediction': 'Rejected', 'probability': 20}

# Route to render the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle form submission
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse form data
        data = {
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'phone': request.form.get('phone'),
            'income': int(request.form.get('income', 0)),
            'credit_score': int(request.form.get('credit_score', 0)),
            'pancard_number': request.form.get('pancard_number'),
            'existing_loans': request.form.get('existing_loans'),
            'pincode': request.form.get('pincode')
        }

        # Validate mandatory fields
        if not data['name'] or not data['email'] or not data['phone']:
            return jsonify({'error': 'Name, email, and phone are mandatory fields.'}), 400

        # Save data to SQLite database
        conn = sqlite3.connect('loan_applications.db')
        cursor = conn.cursor()

        cursor.execute('''
        INSERT INTO applications (name, email, phone, income, credit_score, pancard_number, existing_loans, pincode)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (data['name'], data['email'], data['phone'], data['income'], data['credit_score'],
              data['pancard_number'], data['existing_loans'], data['pincode']))

        conn.commit()
        conn.close()

        # Predict loan approval
        result = predict_loan_approval(data)

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.2', port=5005, debug=True)

















