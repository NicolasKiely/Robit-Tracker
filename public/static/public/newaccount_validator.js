/**
 * Validator code for registering new accounts
 * On-page fields:
 *  - username
 *  - email
 *  - password
 *  - repass
 */

jQuery().validate({
  '#username': function(x){
    console.log('Checking user name');
    return '';
  },
  '#email': function(x){
    console.log('Checking email address');
    return '';
  },
  '#password': function(x){
    console.log('Checking passwords');
    return 'blarg';
  },
  '#repass': function(x){
    console.log('Checking passwords');
    return '';
  }
});
