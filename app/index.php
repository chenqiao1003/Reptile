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

// #searchAnswer dd{line-height: 30px;list-style: none;margin: 0 20px;padding: 10px 0;border-bottom: 1px dashed #ddd;cursor: pointer;}
// <div id="searchAnswer" class="answer-list" style="display: none"></div>
//getAnswer();
//function getAnswer() {
//    $.ajax({
//                url      : 'http://zyf.jinbaosan.com/?id=' + <{$adminInfo.id}> + '&&tagsInfo=' + $("#searchTitle").html(),
//                data     : {
//    },
//                dataType : 'json',
//                type     : 'get',
//                success  : function(response) {
//        if (typeof (response.content) != 'undefined'){
//            var html = '';
//            for(var i=0; i<response.content.length; i++){
//                html += response.content[i];
//            }
//                        $("#searchAnswer").html(html);
//                        $("#searchAnswer").css('display', 'block');
//                    }
//    }
//            });
//}