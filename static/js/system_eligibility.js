        // Function to handle click event on 'Start Exam' link
        function handleClick() {
            // Check if 'click' item exists in localStorage and its value is '1'
            if (localStorage.getItem('click') === '1') {
                // Set the value of 'click' item to '0'
                localStorage.setItem('click', '0');
            }
        }
        
        if (document.getElementById('lic_data').innerText == 'pass') {
            document.getElementById('lic_pass').style.display = 'block';
            document.getElementById('status').innerText = 'Hello buddy! You are successfully pass your eligibility.'
            document.getElementById('status').style.color = 'green'
            document.getElementById('status').style.display = 'block';
            
        } else {
            document.getElementById('lic_pass').style.display = 'none';
            document.getElementById('status').innerText = '*Please enter correct unique code. Remember it was valid for only one time.'
            document.getElementById('status').style.color = 'red'
            document.getElementById('status').style.display = 'block';
        }