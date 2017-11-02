<?php

$body = file_get_content('php://input');
$body = trim($body);
$obj = json_decode($body, true);

$timestamp = $obj['timestamp'];
$action = $obj['action'];
$gate = $obj['gate'];

#var_dump($obj);

$sql = "SELECT * FROM tbParking WHERE gate = ".$gate;

#echo $sql;
