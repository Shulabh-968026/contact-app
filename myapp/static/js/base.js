
function validation(){
    //e.preventDefault()
    console.log("Hello From Django!!")
    var name=document.getElementById('name').value;
    var email=document.getElementById('email').value;
    var phone=document.getElementById('phone').value;
    if(name==='' || email==='' || phone==='')
    {
        alert('Input field can not empty!!')
        return false;
    }
    if(phone.length!=10)
    {
        alert('Phone Number must be 10 digit')
        return false;
    }
    console.log(name,email,phone)
    return true;
};
