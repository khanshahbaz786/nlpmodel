<html>
<body>

Welcome <?php echo $_POST["name"]; ?><br>
Your email address is: <?php echo $_POST["email"]; ?>

Python Data
<br>


<?php
$data = "PHP";

// Execute the python script with the JSON data
$result = exec("script.py $data");

// Decode the result
//$resultData = json_decode($result, true);

// This will contain: array('status' => 'Yes!')
//var_dump($resultData);
print $result;
?>


</body>
</html>