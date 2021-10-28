function validateForm(word, guess) {
    console.log("In validateForm()!");
    console.log(word);
    console.log(guess);
    if (guess.toLowerCase() == word.toLowerCase()) {
        alert("Good Job!");
        return true;
    } else {
        alert("WRONG! Try again.");
        event.preventDefault();
        return false;
    }
    return true;  
}