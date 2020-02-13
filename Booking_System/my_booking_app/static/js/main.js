//function for opening the pop-up login form
function openForm() {
    document.getElementById("form").style.display = "block";
}
//function for opening the pop-up signup form
function opensignup() {
    document.getElementById("signup_modal").style.display = "block";
}
//function for opening the pop-up booking form
function openBookingForm() {
    document.getElementById("booking_form").style.display = "block";
}

//for closing the poped-up login form via event
var modal = document.getElementById('form');
window.onclick = function(event) {
    if (event.target == modal) {
        form.style.display = "none";
    }
}


