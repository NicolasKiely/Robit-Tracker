/**
 * Validator code for registering new accounts
 * On-page fields:
 *  - username
 *  - email
 *  - password
 *  - repass
 */

/**
 * Checks to make sure password fields match each other
 */
function checkPassword(){
  var passVal = $('#password').val();
  var repassVal = $('#repass').val();

  if (passVal.length < 6){
    return 'Password must be at least six characters long';

  } else if (passVal !== repassVal){
    return 'Password fields do not match';
  }
}

/**
 * Checks to make sure username is okay
 */
function checkUsername(x){
  var username = $(x).val();
  if (username.length < 5){
    return 'User name must be at least 5 characters long';
  } else if (!/^[A-Za-z0-9_]+$/.test(username)){
    return 'Bad user name. Valid charcters: Letters, numbers, and _';
  } else if (username.length > 64){
    return 'User name may not be more than 64 characters long';
  }
}

/**
 * Checks email address
 */
function checkEmail(x){
  if (!/.+@.+/.test($(x).val())){
    return 'Invalid email address';
  }
}


jQuery().validate({
  '#username': checkUsername,
  '#email': checkEmail,
  '#password': checkPassword,
  '#repass': checkPassword
}).prepost('/signup/validate/');
