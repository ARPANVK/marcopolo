

userid = document.getElementById('student_userid').value;
document.getElementById('login_student_gateway').addEventListener('submit',function(event) {
    // Prevent the form from submitting by default
    event.preventDefault;

    if (userid == 'Arpan') {
        this.submit();
    }
    else{
        console.log('not user matched')
    }
})