function validateform(){
    var name=document.signup_form.Fullname.value;
    var email=document.signup_form.Email.value;
    var password=document.signup_form.Password.value;
    var verify_password=document.signup_form.Verify_Password.value;
    var mobile=document.signup_form.Mobile.value;

if (name==null || name==""){
  alert("Name can't be blank");
  return false;
}
if (email==null || email==""){
    alert("Email can't be blank");
    return  false;
}
if(password.length<6){
  alert("Password must be at least 6 characters long.");
  return false;
  }
if(verify_password==password){
    return true;
}
else {
    alert("Password must be same.")
}

}