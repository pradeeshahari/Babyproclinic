function loginform(){
    username=document.getElementById("Admin").value;
    password=document.getElementById("Pass").value;
    if (username==="" && password===""){
        alert("please enter user name password");
         return false
     }else{
         return true

    }
}


