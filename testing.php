<!DOCTYPE html>
<?php
//displays all errors or warnings
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);
?>


<html lang="en">
<div class="wrapper">
<head>

<meta charset="UTF-8">
<link  rel="stylesheet" type="text/css" href="style.css?version=51">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <script src="pyMatrix.py"></script>
<title>Python Calculator</title>

</head>

<body>

<div class="menu">

<h1>Python Matrix Calculator</h1>
<form action="pyMatrix.py" method="POST">
<div class="InsideMenu">

<?php
$command = escapeshellcmd('python pyMatrix.py 2>&1');

$output = system($command);

print($output);

?>

</div>
<!--this will get user input from html-->
<br>

<input type="text" id="select" name="selection"><br><br> 
<input type="submit" name="submit" value="submit">

<?php
echo $_GET["selection"];

?>
</form>
</div>
</body>
</div>
</html>
