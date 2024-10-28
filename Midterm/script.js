function sendName() {
    var name = document.getElementById('name').value;
    
    fetch('/api/welcome', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name: name })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('welcome-message').innerText = data.message;
    })
    .catch(error => console.error('Error:', error));
}
