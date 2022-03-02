<?php
/*
================================================================================
#-.php curl.
================================================================================
*/
Function _curlPostToApi($url,$data){
	//-.init curl.
	$ch = curl_init($url);
	curl_setopt($ch,CURLOPT_POSTFIELDS,json_encode($data));
	curl_setopt($ch,CURLOPT_HEADER,array('Content-Type: application/json'));
	curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);
	//-.send request.
	$result = curl_exec($ch);
	curl_close($ch);
	$result = preg_replace('/HTTP(.*)UTF-8/s',"",$result);
	return $result;
}
?>
