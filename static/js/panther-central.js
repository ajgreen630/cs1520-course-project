function validateForm(word, guess) {
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