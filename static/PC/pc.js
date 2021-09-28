function validateForm() {
  let x = document.forms["myForm"]["fname"].value;
    if (x == "OAKLAND") {
        alert("GOOD Job");
        return true;
    } else if (x == "Oakland") {
        alert("GOOD Job");
        return true;
    }else{
    alert("WRONG! try again.");
    return false;
  }
}