<?php

require_once('include/function.php');
#http://localhost/draw/dashboard/table/entries_fetch.php?action=list&jtStartIndex=0&jtPageSize=10&jtSorting=null&jtStartIndex=0&jtPageSize=50
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

			$apiUrl = 'https://c914-41-139-151-158.ngrok.io/getCustomerEntries/';

			$result = curlToPythonApi($apiUrl,$searchFilter);

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