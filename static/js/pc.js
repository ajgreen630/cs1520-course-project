function validateForm() {
  let x = document.forms["myForm"]["fname"].value;
    if (x == "OAKLAND") {
      alert("Good Job");
      document.location.href = '../HillmanLibrary/HillmanLibrary.html';
      //return true;
    } else if (x == "Oakland") {
      alert("Good Job");
      document.location.href = '../HillmanLibrary/HillmanLibrary.html';
      //return true;
    }else{
    alert("WRONG! try again.");
    return false;
  }
}