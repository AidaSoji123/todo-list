function login() {
    // Add your login logic here
    alert('Login button clicked');
  }
  
  function register() {
    // Add your registration logic here
    alert('Register button clicked');
  }
  
  function forgotPassword() {
    // Add your forgot password logic here
    alert('Forgot Password button clicked');
  }
  
  function showRegisterForm() {
    document.getElementById('signinForm').style.display = 'none';
    document.getElementById('forgotPasswordForm').style.display = 'none';
    document.getElementById('registerForm').style.display = 'block';
  }
  
  function showForgotPasswordForm() {
    document.getElementById('signinForm').style.display = 'none';
    document.getElementById('registerForm').style.display = 'none';
    document.getElementById('forgotPasswordForm').style.display = 'block';
  }
  
  function showSigninForm() {
    document.getElementById('registerForm').style.display = 'none';
    document.getElementById('forgotPasswordForm').style.display = 'none';
    document.getElementById('signinForm').style.display = 'block';
  }
  