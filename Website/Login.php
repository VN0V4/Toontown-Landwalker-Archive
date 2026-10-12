<?php
$host="localhost";
$user="root";
$password="";
$db="toontown";

mysql_connect("localhost","user","");
mysql_select_db($db);
$mysqli = new mysqli($host,$user,$password);

if(isset($_POST['submit'])){
    
    $uname=$_POST['username'];
    $password=$_POST['password'];
    
    $sql="select*from loginform where User='".$uname."'AND Pass='".$password."' limit 1";
    
    $result=mysql_query($sql);
    
    if(mysql_num_rows($result)==1){
        echo " You have successfully logged in.";
            exit();
        
        
        
    }
    
    else{
        echo " You have entered an incorrect password.";
        exit();
    }
    
    
    
}
    
    
?>
<!DOCTYPE html>
<html lang="en">
<head>
   <link rel="stylesheet" href="style.css">
    <meta charset="UTF-8">
    <title>Login</title>
</head>
<body>
    <div class="box"><a href="index.php">Home</a></div>

        <form action="Login.php" method="post"></form>
        
        <script src="script-Login.js"></script>
        
                <h2>Login</h2>
        <div class="login-box">
        <form>
            
            <div class="inputBox">
                <input type="text" placeholder="" name="text" required="Banana">
                <label>Username</label>
                <span id="uNameError"></span>
            
            </div>
            <div class="inputBox">
                <input type="password" placeholder="" name="password" required="Kiwi">
                <label>Password</label>
                <span id="pWordError"></span>
            
            </div>
            <input type="submit" name="submit" value="submit">
        </form>
        </div>
        
        
        
        <script src="JavaScrips/script-Login.js"></script>
        
        
    
    
</body>
</html>