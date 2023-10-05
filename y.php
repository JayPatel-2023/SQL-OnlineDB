<?php
// example.php

function getData() {
    // Your existing PHP code to fetch data from the database
    // ...
        $data = 'heloow world';
    // Return the data
    return $data;
}

function anotherFunction() {
    // Another function in your PHP code
    // ...
    $result = 'Jay';
    // Return the result
    return $result;
}

// Check if a function parameter is provided in the URL
if (isset($_GET['function'])) {
    $functionName = $_GET['function'];

    // Call the specified function
    if (function_exists($functionName)) {
        $result = call_user_func($functionName);

        // Return the result as JSON
        echo json_encode($result);
    } else {
        echo json_encode(["error" => "Function not found"]);
    }
} else {
    echo json_encode(["error" => "Function parameter missing"]);
}
?>

