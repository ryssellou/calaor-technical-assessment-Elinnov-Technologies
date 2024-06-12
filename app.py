from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    if n <= 3:
        return True  # 2 and 3 are prime numbers
    if n % 2 == 0 or n % 3 == 0:
        return False  # Exclude multiples of 2 and 3
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False  # Check for factors up to the square root of n
        i += 6
    return True

def calculate_factorial(n):
    """Calculate the factorial of a number."""
    if n < 0:
        return "Undefined for negative numbers"  # Factorial is not defined for negative numbers
    if n == 0:
        return 1  # The factorial of 0 is 1
    result = 1
    for i in range(1, n + 1):
        result *= i  # Multiply the result by each number up to n
    return result

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')  # Render the HTML template

@app.route('/calculate', methods=['POST'])
def calculate():
    """Calculate prime and factorial."""
    data = request.json  # Get the JSON data from the request
    number = int(data['number'])  # Convert the input to an integer
    prime = is_prime(number)  # Check if the number is prime
    factorial = calculate_factorial(number)  # Calculate the factorial
    return jsonify({
        'number': number,
        'prime': prime,
        'factorial': factorial
    })  # Return the results as JSON

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode
