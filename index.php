<?php

# Receive post data
$body = file_get_contents('php://input');
$body = trim($body);
$obj = json_decode($body, true);

# Set variables to post data
$timestamp = $obj['timestamp'];
$action = $obj['action'];
$gate = $obj['gate'];

# Show post data
var_dump($obj);
echo "<br>";

# Convert post variables to DB format
if ($action == "exit") {
    $action = 0;
} elseif ($action == "entrance") {
    $action = 1;
}

if ($gate == "main") {
    $gate = 1;
} elseif ($gate == "secondary") {
    $gate = 2;
}

# Set DB credentials
$servername = 'localhost';
$username = 'id3479526_maua';
$password = 'smartparking';
$dbname = 'id3479526_spmdb';
$dbtable = 'tbParking';

# Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

# Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

# Create query
$sql = "INSERT INTO $dbtable (timestamp, action, gate)
VALUES (FROM_UNIXTIME($timestamp), $action, $gate)";

# Show SQL query
echo "SQL query: " . $sql . "<br>";

# Check query
if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

# Close connection
$conn->close();

?>
