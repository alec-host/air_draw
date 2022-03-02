<?php
session_start();

require_once('include/function.php');

try
{
	#-.Getting records (listAction)
	if($_GET["action"] == "list")
	{
			$jTableResult = array();

			if(isset($_REQUEST['search_name']) && trim($_REQUEST['search_name']) != ""){
					$searchFilter = $_REQUEST['search_name'];
			}else{
					$searchFilter = "0";
			}

			$apiUrl = 'http://127.0.0.1:8000/getCustomerEntries/';

			$result = _curlGetToApi($apiUrl,$searchFilter,'0',$_GET['jtPageSize']);

			print($result);

			exit(0);
	}
	#-.Creating a new record (createAction)
	else if($_GET["action"] == "create")
	{
		$jTableResult = array();
			
		$jTableResult['Result'] = "OK";
		$jTableResult['Record'] = array("message" => "hello world");
	
		print(json_encode($jTableResult));		

		exit(0);
	}
	#-.Updating a record (updateAction)
	else if($_GET["action"] == "update")
	{
		$jTableResult = array();
		
		$jTableResult['Result'] = "OK";
		
		print(json_encode($jTableResult));

		exit(0);
	}
	#-.Deleting a record (deleteAction)
	else if($_GET["action"] == "delete")
	{
		$jTableResult = array();
		
		$jTableResult['Result'] = "OK";
		
		print(json_encode($jTableResult));	

		exit(0);
	}
}
catch(Exception $ex)
{
    #-.Return error message
	$jTableResult = array();
	$jTableResult['Result'] = "ERROR";
	$jTableResult['Message'] = $ex->getMessage();
	
	print(json_encode($jTableResult));
	
	exit(0);
}
?>