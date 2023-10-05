<?php
// example.php

function getData() {
    // Your existing PHP code to fetch data from the database
    // ...
    $result = 'jay';
    // Return the data as an associative array
    $data = array(
        'message' => 'Hello from getData function!',
        'result' => $result
    );

    // Convert the array to JSON and echo it
    echo json_encode($data);
}

function anotherFunction() {
    // Another function in your PHP code
    // ...
    $data = 'jay';
    // Return the result as an associative array
    $result = array(
        'message' => 'Hello from anotherFunction!',
        'data' => $data
    );

    // Convert the array to JSON and echo it
    echo json_encode($result);
}

// Check if a function parameter is provided in the URL
if (isset($_GET['function'])) {
    $functionName = $_GET['function'];

    // Call the specified function
    if (function_exists($functionName)) {
        // Disable HTML rendering
        header('Content-Type: application/json');

        // Call the specified function
        call_user_func($functionName);
    } else {
        // Function not found
        echo json_encode(["error" => "Function not found"]);
    }
} else {
    // Function parameter missing
    echo json_encode(["error" => "Function parameter missing"]);
}
?>
