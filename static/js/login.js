document.addEventListener("DOMContentLoaded", () => {
	const loginForm = document.querySelector("#login");
	const createAccountForm = document.querySelector("#createAccount");

	document.querySelector("#linkCreateAccount").addEventListener("click", e => {
		e.preventDefault();
		loginForm.classList.add("form--hidden");
		createAccountForm.classList.remove("form--hidden");
	});

	document.querySelector("#linkLogin").addEventListener("click", e => {
		e.preventDefault();
		loginForm.classList.remove("form--hidden");
		createAccountForm.classList.add("form--hidden");
	});
});

//Using Datastore will change the whole function and syntax associated with it
function validation()
{
	//Username variable
	var username = document.querySelector("#uname");
	//Password variable
	var password = document.querySelector("#pwd");
	//Login button variable
	var login_btn = document.querySelector("#login_btn");
	//Constant error message to display the error whenever the conditions are not met
	const display_error_message = document.querySelector("#error_msg");

	//Conditions
	//For if either of the input fields dont meet the required conditions
	if(username.value.length < 5 || password.value.length < 5)
	{
		//If both input fields are wrong, then display error for both
		if(username.value.length < 5 && password.value.length < 5)
		{
			username.classList.add("form__input--error");
			password.classList.add("form__input--error");
		}
		//If username is wrong, display error
		else if(username.value.length < 5)
		{
			username.classList.add("form__input--error");
			password.classList.remove("form__input--error");
		}
		//if password is wrong, display error
		else if(password.value.length < 5)
		{
			username.classList.remove("form__input--error");
			password.classList.add("form__input--error");
		}
		//alert("Invalid Length. Please correct");

		//Since atleast one of the two fields do not meet the requirements,
		//remove the no__display class from the error_msg so that the message can be displayed.
		display_error_message.classList.remove("no__display");
		//window.location: "file:///C:/Users/parth/Desktop/Login-Sign%20UP%20Page/Main%20page/index.html?";
		return false;
	}
	else
	{
		display_error_message.classList.add("no__display");
	}
}

//Using Datastore will change the whole function and syntax associated with it
function createAccountValidation()
{
	var username = document.querySelector("#cauname");										//Username variable
	var password = document.querySelector("#capwd");										//User created Password
	var email = document.querySelector("#email");											//User entered Email
	var lowerCaseLetters = /[a-z]/g;														//LowerCase Check Variable
	var upperCaseLetters = /[A-Z]/g;														//UpperCase Check Variable
	var numbers = /[0-9]/g;																	//Number Check Variable
	var confirmPassword = document.querySelector("#cacpwd");								//Confirm Password Variable
	const display_error_message = document.querySelector("#caerror_msg");					//Main error message
	const username_error_message1 = document.querySelector("#cauname_error_msg1");			//Username error message 1
	const username_error_message2 = document.querySelector("#cauname_error_msg2");			//Username error message 2
	const email_error_message = document.querySelector("#caemail_error_msg");				//Email error message
	const password_error_message1 = document.querySelector("#capwd_error_msg1");			//Password error message 1
	const password_error_message2 = document.querySelector("#capwd_error_msg2");			//Password error message 2
	const password_error_message3 = document.querySelector("#capwd_error_msg3");			//Password error message 3
	const password_error_message4 = document.querySelector("#capwd_error_msg4");			//Password error message 4
	const confirm_password_error_message = document.querySelector("#cacpwd_error_msg");		//Confirm password error message
	//Acceptable password
	/*
		one uppercase letter, one lowercase letter, one number, minimum 8 characters.
	*/
	let validPassword = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$/;
	//Acceptable Email
	let validEmail = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	let validUsername = /^[a-zA-Z0-9]{5,10}$/;												//Acceptable username with conditions

	//Conditions
	//For if either of the input fields dont meet the required conditions
	if(!(validUsername.test(username.value)) || (!(validPassword.test(password.value))) || !(validEmail.test(email.value)) || (document.getElementById("cacpwd").value != document.getElementById("capwd").value))
	{
		/*-----------------------------------------------------------------------------------------------------------------------------|
															USERNAME VALIDATION 													   |
		  -----------------------------------------------------------------------------------------------------------------------------|
		*/
		//For an invalid username
		if(!(validUsername.test(username.value)))
		{
			username.classList.add("form__input--error");						//Makes the border red

			if(username.value.length < 5 || username.value.length > 10)			//Length not between including 5 - 10
			{
				username_error_message1.classList.remove("no__display");		//Displays the error message by removing the no__display class
				username_error_message2.classList.add("no__display");			//Hides the unrelated error
			}
			else
			{
				username_error_message1.classList.add("no__display");			//Displays the specific error
				username_error_message2.classList.remove("no__display");		//Hides the unrelated error
			}
		}
		else
		{
			username.classList.remove("form__input--error");
			username_error_message1.classList.add("no__display");
			username_error_message2.classList.add("no__display");
		}

		/*-----------------------------------------------------------------------------------------------------------------------------|
															EMAIL VALIDATION 													       |
		  -----------------------------------------------------------------------------------------------------------------------------|
		*/

		if(!(validEmail.test(email.value)))
		{
			email.classList.add("form__input--error");
			email_error_message.classList.remove("no__display");
		}
		else
		{
			email.classList.remove("form__input--error");
			email_error_message.classList.add("no__display");
		}

		/*-----------------------------------------------------------------------------------------------------------------------------|
		  													PASSWORD VALIDATION 													   |
		  -----------------------------------------------------------------------------------------------------------------------------|
		*/
		//For an invalid password
		if(!(validPassword.test(password.value)))
		{
			//username.classList.remove("form__input--error");
			password.classList.add("form__input--error");
			//Then check which of the conditions fail.
			//First, check for a lowerCase letter
			if((!password.value.match(lowerCaseLetters)) || (!password.value.match(upperCaseLetters)) ||(!password.value.match(numbers)) || password.value.length < 8)
			{
				if((!password.value.match(lowerCaseLetters)))
				{
					capwd_error_msg1.classList.remove("no__display");
				}
				else
				{
					capwd_error_msg1.classList.add("no__display");
				}
				if((!password.value.match(upperCaseLetters)))
				{
					capwd_error_msg2.classList.remove("no__display");
				}
				else
				{
					capwd_error_msg2.classList.add("no__display");
				}
				if((!password.value.match(numbers)))
				{
					capwd_error_msg3.classList.remove("no__display");
				}
				else
				{
					capwd_error_msg3.classList.add("no__display");
				}
				if(password.value.length < 8)
				{
					capwd_error_msg4.classList.remove("no__display");
				}
				else
				{
					capwd_error_msg4.classList.add("no__display");
				}
			}
		}
		else
		{
			password.classList.remove("form__input--error");
			capwd_error_msg1.classList.add("no__display");
			capwd_error_msg2.classList.add("no__display");
			capwd_error_msg3.classList.add("no__display");
			capwd_error_msg4.classList.add("no__display");
		}
		
		/*-----------------------------------------------------------------------------------------------------------------------------|
															CONFIRM PASSWORD 														   |
		  -----------------------------------------------------------------------------------------------------------------------------|
		*/
		if(document.getElementById("cacpwd").value != document.getElementById("capwd").value || document.getElementById("cacpwd").value.length < 8)
		{
			confirmPassword.classList.add("form__input--error");
			cacpwd_error_msg.classList.remove("no__display");
		}
		else
		{
			confirmPassword.classList.remove("form__input--error");
			cacpwd_error_msg.classList.add("no__display");
		}

		//Since atleast one of the two fields do not meet the requirements,
		//remove the no__display class from the error_msg so that the message can be displayed.
		display_error_message.classList.remove("no__display");
		return false;
	}
	else
	{
		display_error_message.classList.add("no__display");
	}
}