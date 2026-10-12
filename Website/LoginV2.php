<?php

    session_start();

    $Username = 'Banana';
    $Password = 'Kiwi';

    if(isset($_SESSION['loged_in']) && $_SESSION['logged_in'] == true) {
        header("location: success_page.php");
    }

    if (isset($_POST['Username']) && isset($_POST['Password'])) {
        if ($_POST['Username'] == $Username && $_POST['Password'] == $Password) {
            
        $_SESSION['logged_in'] = true;
        header("location: success_page.php");



     }


?>

<html>
    <head>
        <link rel="stylesheet" href="style.css">
        <meta charset="UTF-8">
        <title>Login</title>
    </head>
        <body>

        <form method="post" action="LoginV2.php">
            Username:<br/>
            <input type="text" name="Username">
            Password<br/>
            <input type="text" name="Password">
            <input type="submit" value="Login">
        </form>
    
    
        </body>
</html>
