let currentSlide = 1;
let userResponses = [];

function showSlide(slideNumber) {
    document.getElementById(`slide${currentSlide}`).classList.remove('active');
    document.getElementById(`slide${slideNumber}`).classList.add('active');
    currentSlide = slideNumber;
}

function submitAnswer(questionNumber) {
    const form = document.getElementById(`form${questionNumber}`);
    const selectedOption = form.querySelector('input[name="answer' + questionNumber + '"]:checked');
    if (selectedOption) {
        userResponses[questionNumber - 1] = selectedOption.value;
        if (questionNumber == 15) {
            showSlide(questionNumber);
        }
        else {
            showSlide(questionNumber + 1);
        }
    }
    else {
        userResponses[questionNumber - 1] = 'empty';
    }
    return false; // Prevent form submission
}

function submitQuiz() {
    console.log('User Responses:', userResponses);
    document.getElementById('user_resp_send').value = userResponses;
    // You can send userResponses to the server using AJAX or include it in a form submission
    document.getElementById('aleart_box').style.display = 'block'
    document.getElementById('view_score').style.display = 'none';
}

// <<Code for block Right Click means inspact option.>>
// document.addEventListener('contextmenu', function (event) {
//     event.preventDefault();
// });
// Code for block Control+Shift+I(inspact) option.
// document.addEventListener("keydown", function(event) {
//     // Check if Shift+Control+I is pressed
//     if (event.shiftKey && event.ctrlKey && event.key === "I") {
//         event.preventDefault();
//     }})


// <<if you click in Submit all button once, then clickcount incress 0 to 1 and store it in local storage.>>
clickcount = 0
document.getElementById('submit_all').addEventListener('click', () => {
    clickcount++;
    // console.log('my click time', clickcount)
    localStorage.setItem('click', clickcount);
})

// <<Candidate did not attend the exam again after submit all.>>
// <<Logic is, if count 1 then only you can check score.>>
storedClickCount = localStorage.getItem('click');
if (storedClickCount > 0) {
    document.getElementById('view_score').style.display = 'block';
    document.getElementById('overlay').style.display = 'block';
}



// Set the duration in seconds (30 minutes = 30 * 60 seconds)
const durationInSeconds = 20 * 60;

// Update the countdown every second
const countdownElement = document.getElementById('countdown');

let remainingSeconds = durationInSeconds;

function updateCountdown() {
    const minutes = Math.floor(remainingSeconds / 60);
    const seconds = remainingSeconds % 60;

    countdownElement.innerHTML = `${minutes} Min ${seconds} Sec`;

    if (remainingSeconds <= 0) {
        clearInterval(intervalId);
        countdownElement.innerHTML = 'Countdown expired';
    } else {
        remainingSeconds--;
    }

    if (document.getElementById('countdown').innerText == 'Countdown expired') {
        document.getElementById('submit_exam').click();
        document.getElementById('submit_all').click();
        // console.log('yea done')
    }
}

// Call updateCountdown() initially to avoid delay
updateCountdown();

// Update countdown every second
const intervalId = setInterval(updateCountdown, 1000);





