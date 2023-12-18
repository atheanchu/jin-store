function createOrder(item_id) {
    const orderData = {
        username: "ironman",
        item_id
    }

    const url = "/orders"
    const headers = {
        'Content-Type': 'application/json',
    };

    fetch(url, {
        method: 'POST',
        headers: headers,
        body: JSON.stringify(orderData),
    })
        .then((response) => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            
            return response.json();
        })
        .then((data) => {
            const myModal = new bootstrap.Modal(document.getElementById('exampleModal'), {keyboard: false});
            myModal.show()
            
            // Handle the response data here
            console.log('Order created successfully:', data);
            // Optionally, you can redirect to a different page or show a success message
        })
        .catch((error) => {
            // Handle any errors that occurred during the fetch
            console.error('Error:', error);
            // Optionally, you can show an error message to the user
        });
}