<?php
$servername = "sql12.freesqldatabase.com";
$username = "sql12651137";
$password = "YGUSAty7ft";
$dbname = "sql12651137";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Fetch data from the table
$sql = "SELECT * FROM students";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // Output data of each row
    while($row = $result->fetch_assoc()) {
        echo "ID: " . $row["student_id"]. " - Name: " . $row["first_name"]. " " . $row["last_name"]. " - Age: " . $row["age"]. " - Grade: " . $row["grade"]. "<br>";
    }
} else {
    echo "0 results";
}

// Close connection
$conn->close();
?>
