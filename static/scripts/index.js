const toggleBtn = document.getElementById('onlineBtn');

toggleBtn.addEventListener('change', function() {
  if (this.checked) {
    console.log('Toggle button is ON');
    // Perform actions when the toggle button is ON

    fetch('http://127.0.0.1:8000/toggle-online/?state=on')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        console.log('Success');
        location.reload();
      })
      .catch(error => {
        console.error('Error:', error);
        // Handle the error
    });


  } else {
    console.log('Toggle button is OFF');

    fetch('http://127.0.0.1:8000/toggle-online/?state=off')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        console.log('Success');
        location.reload();
      })
      .catch(error => {
        console.error('Error:', error);
        // Handle the error
    });
  

    // Perform actions when the toggle button is OFF
  }
});