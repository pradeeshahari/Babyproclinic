function loginform(){
    username=document.getElementById("Doctor").value;
    password=document.getElementById("Pass").value;
    if (username==="" || password===""){
        document.getElementById("error").innerHTML= "Enter username and password";
         document.getElementById('error').style.color="red";
         return false
     }else {
         
        return true

    }
}