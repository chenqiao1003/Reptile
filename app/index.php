<?php
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST,GET');

$tagsInfo = isset($_GET['tagsInfo']) ? trim($_GET['tagsInfo']) : '';
$id = isset($_GET['id']) ? $_GET['id'] : '';


if (empty($tagsInfo) || !in_array($id, [152])) {
    echo json_encode(['content' => []]);
    exit();
}
$data = exec('python /data/www/findBaiduAQ.py ' . $tagsInfo);

$re = json_decode($data, true);

$dataTmp = [];
foreach ($re as $key => &$value) {
    $value = str_replace('´ð£º', '', $value);
    $dataTmp[] = $value;
}

echo json_encode(['content' => $dataTmp]);
