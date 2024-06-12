document.getElementById('calculator-form').addEventListener('submit', function(e) {
    e.preventDefault();
    // Prevent the form from submitting the traditional way

    const number = document.getElementById('number').value;
    // Get the number entered by the user

    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ number: number }),
    })
    .then(response => response.json())
    .then(data => {
        // Display the results returned from the server
        const resultDiv = document.getElementById('result');
        resultDiv.innerHTML = `
            <p>Number: ${data.number}</p>
            <p>Prime: ${data.prime ? 'Yes' : 'No'}</p>
            <p>Factorial: ${data.factorial}</p>
        `;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
    // Fetch request to the server to calculate prime and factorial
});

document.querySelectorAll('.key').forEach(key => {
    key.addEventListener('click', () => {
        const input = document.getElementById('number');
        // Add event listener to each key on the virtual keyboard
        if (key.classList.contains('delete')) {
            input.value = input.value.slice(0, -1);
            // Remove the last character from the input field
        } else if (key.classList.contains('clear')) {
            input.value = '';
            // Clear the input field
        } else {
            input.value += key.textContent;
            // Add the clicked key's text content to the input field
        }
    });
});
