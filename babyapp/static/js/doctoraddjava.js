function clearbox(){
    document.getElementById("clear").value=""
    
    }

    function formvalidation(){
        var username=document.getElementById("username").value;
        var password=document.getElementById("password").value;
        var id=document.getElementById("id").value;
        var name=document.getElementById("name").value;
        var age=document.getElementById("age").value;
        var gender=document.getElementById("gender").value;
        var phonenumber=document.getElementById("phonenumber").value;
        if(username==""||password==""||id==""||name==""||age==""||gender==""||phonenumber==""){
            document.getElementById("error").innerHTML="please fill the all boxes"
            return false;
        }
        else;
         return true;


        }


        
    
    
    
   

