function register(){
    const username = document.getElementById('username-input').value;
    const password = document.getElementById('password-input').value;
    $.post('/register', 
    {
        username:username,
        password:password
    }
    )
    
}