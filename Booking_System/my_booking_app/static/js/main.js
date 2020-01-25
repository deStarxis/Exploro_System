function openForm() {
    document.getElementById("form").style.display = "block";
}
function openBookingForm() {
    document.getElementById("booking_form").style.display = "block";
}
// function closeForm() {
//     document.getElementById("myForm").style.display = "none";
// }
// Get the modal
var bookingModal = document.getElementById('booking_form');
var modal = document.getElementById('form');
var signup = document.getElementById('signup_modal');

// Get the modal
// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        form.style.display = "none";
    }
}
function opensignup() {
    document.getElementById("signup_modal").style.display = "block";
}

