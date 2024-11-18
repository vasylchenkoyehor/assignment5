<?php

$input_values = [
    'a' => isset($_GET['a']) ? $_GET['a'] : 0,
    'b' => isset($_GET['b']) ? $_GET['b'] : 0,
    'c' => isset($_GET['c']) ? $_GET['c'] : 0,
    'd' => isset($_GET['d']) ? $_GET['d'] : 0,
    'e' => isset($_GET['e']) ? $_GET['e'] : 0,
];

$a = escapeshellarg($input_values['a']);
$b = escapeshellarg($input_values['b']);
$c = escapeshellarg($input_values['c']);
$d = escapeshellarg($input_values['d']);
$e = escapeshellarg($input_values['e']);

$output = shell_exec("pyhton3 data_management.py a=$a b=$b c=$c d=$d e=$e")

echo "<html><body>";
echo "<h3>Results:</h3>";

$output_lines = explode("/n", $output);

foreach ($output_lines as $line) {
    echo "<p>" . htmlspecialchars($line) . </p>;
}

echo "</body></html>";