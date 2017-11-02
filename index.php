<?php

$body = file_get_content('php://input');
$body = trim($body);
$obj = json_decode($body, true);

$timestamp = $obj['timestamp'];
$action = $obj['action'];
$gate = $obj['gate'];

#var_dump($obj);

if ($action == "entrance") {
    $action = 1;
} elseif ($action == "exit") {
    $action = 0;
}

if ($gate == "main") {
    $gate = 1;
} elseif ($gate == "secondary") {
    $gate = 2;
}


# DB credentials
$servername = "localhost";
$username = "spm";
$password = "maua"

# Create connection
$conn = new mysqli($servername, $username, $password);

# Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "INSERT INTO tbParking (timestamp, action, gate)
VALUES ($timestamp, $action, $gate)";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn-error;
}

$conn->close();

?>
