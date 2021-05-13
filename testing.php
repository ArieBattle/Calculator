<?php
echo "Python MAtrix Calculator <br><br>"

$command = escapeshellcmd('python Calculator/pyMatrix.py 2>&1');

$output = system($command);

echo $output;

//system("python pyMatrix.py ".$_POST["name"]);
?>
