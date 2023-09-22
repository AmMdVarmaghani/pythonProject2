# AmirmohammadVarmaghani
from flask import Flask, request, render_template

app = Flask(__name__)

# Define a route for the form submission page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the student number, first name, and last name from the form
        student_number = request.form.get('student_number')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')

        # Process the data (you can customize this part)
        # For now, let's just print the received data
        print(f'Student Number: {student_number}')
        print(f'First Name: {first_name}')
        print(f'Last Name: {last_name}')

        # You can also store this data in a database or perform other actions here

        # Return a response or redirect to another page
        return f'Student Number: {student_number}<br>First Name: {first_name}<br>Last Name: {last_name}'

    # Render the HTML form
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

