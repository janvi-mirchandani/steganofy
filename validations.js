function validate() {
    if( document.getElementById("username").value == "" && document.getElementById("password").value == "") {
        document.getElementById("username").focus();
        document.getElementById('errfn').innerHTML = "Username should not be empty";
        document.getElementById('errpwd').innerHTML = "Password should not be empty";
        return false;
    }else if( document.getElementById("username").value == "" && document.getElementById("password").value != "") {
        document.getElementById("username").focus() ;
        document.getElementById('errfn').innerHTML="Username should not be empty";
        document.getElementById('errpwd').innerHTML=" ";
        return false;
    }else if( document.getElementById("password").value == "" ) {
        document.getElementById("password").focus() ;
        document.getElementById('errfn').innerHTML=" ";
        document.getElementById('errpwd').innerHTML="Password should not be empty";
        return false;
    }
}
/*function check_ext(){
        if(document.getElementById("oldpath").value != "" ){
        fileName = document.getElementById("oldpath").value;
        fileExtension = fileName.replace(/^.*\./, '');
        fileExt = fileExtension.toLowerCase();
        if(fileExt !='png'){
            document.getElementById("oldpath").focus() ;
            document.getElementById('erroldpath').innerHTML="Only PNG files are allowed";
        }
        else
            document.getElementById('erroldpath').innerHTML=" ";
    }
}*/
function check_msg(){
    if( document.getElementById("msg").value == "" ) {
        document.getElementById("msg").focus();
        document.getElementById('errmsg').innerHTML = "Message should not be empty";
    }
    else
        document.getElementById('errmsg').innerHTML = " ";
}
function check_fname(){
    if( document.getElementById("newpath").value == "" ) {
        document.getElementById("newpath").focus();
        document.getElementById('errnewpath').innerHTML = "New filename should not be empty";
    }
    else
        document.getElementById('errnewpath').innerHTML = " ";
}
function validate_encrypt() {
    var entrycheck=true;
    /*if(document.getElementById("oldpath").value != "" ){
        fileName = document.getElementById("oldpath").value;
        fileExtension = fileName.replace(/^.*\./, '');
        fileExt = fileExtension.toLowerCase();
        if(fileExt !='png'){
            document.getElementById("oldpath").focus() ;
            document.getElementById('erroldpath').innerHTML="Only PNG files are allowed";
        }
        else
            document.getElementById('erroldpath').innerHTML=" ";
    }*/
    if( document.getElementById("oldpath").value == "" ) {
        document.getElementById("oldpath").focus() ;
        document.getElementById('erroldpath').innerHTML="Image path should not be empty";
        entrycheck=false;
    }
    if( document.getElementById("msg").value == "" ) {
        document.getElementById("msg").focus() ;
        document.getElementById('errmsg').innerHTML="Message should not be empty";
        entrycheck=false;
    }
    if( document.getElementById("newpath").value == "" ) {
        document.getElementById("newpath").focus() ;
        document.getElementById('errnewpath').innerHTML="New filename should not be empty";
        entrycheck=false;
    }
    if( document.getElementById("oldpath").value != "" ) {
        document.getElementById("oldpath").focus() ;
        document.getElementById('erroldpath').innerHTML=" ";
    }
    if( document.getElementById("msg").value != "" ) {
        document.getElementById("msg").focus() ;
        document.getElementById('errmsg').innerHTML=" ";
    }
    if( document.getElementById("newpath").value != "" ) {
        document.getElementById("newpath").focus() ;
        document.getElementById('errnewpath').innerHTML=" ";
    }
    return entrycheck;
}

window.onload = function(){
    document.getElementById('fademe').style.opacity = '0';
    document.getElementById('fademe').style.transition = '6s';

}

function charcount(val) {
    var len = val.length;
    var char_rem = 2500-len;
    document.getElementById('charrem').innerHTML="Characters Remaining :" +char_rem+"/2500";
}

function decrypt(val) {
    popUpWindow('http://localhost:5000/message/'+val,'_blank','600','300');
    return false;
}

function popUpWindow(URL, windowName, windowWidth, windowHeight) {
    var centerLeft = (screen.width/2)-(windowWidth/2);
    var centerTop = (screen.height/2)-(windowHeight/2);
    var windowFeatures = 'toolbar=no, location=no, directories=no, status=no, menubar=no, titlebar=no, scrollbars=no, resizable=no, ';
    mywindow=window.open(URL, windowName, windowFeatures +' width='+ windowWidth +', height='+ windowHeight +', top='+ centerTop +', left='+ centerLeft);
    return mywindow;
}