<?php

header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST, PATCH, PUT, DELETE, OPTIONS');
header('Access-Control-Allow-Headers: Origin, Content-Type, X-Auth-Token');

/*
adjust the values of tiers below to expected.
*/
$tier_1 = '1';
$tier_2 = '12';
$tier_3 = '3';

$tiers = array($tier_1,$tier_2,$tier_3);
?>
<html>
<head>
	<title>AirDuka:Draw</title>
</head>
<style>
body, #tier, option{
	font-family: tahoma, calibri, calibri;
}

#outter{
	width: 100%;
	height: 100%;
	background-color: #00639E;
	margin: auto;
}

#section_holder{
	width: 20%;
	font-size: 45px;
	font-family: tahoma,calibri;
	font-weight:bold;
	background-color: #FFF;
	position: absolute;
	top: 25%;
	left: 40%;
	transoform:translate:(-10%,-10%);
}

table{
	width: 85%;
	border: solid 1px #fff;
}

#draw {
}

select {
  /* styling */
  background-color: white;
  border: thin solid #A6A6A6;
  border-radius: 3px;
  display: inline-block;
  font: inherit;
  line-height: 1.5em;
  padding: 0.5em 3.5em 0.5em 1em;

  /* reset */

  margin: 0;      
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
  -webkit-appearance: none;
  -moz-appearance: none;
}

select.classic {
  background-image:
    linear-gradient(45deg, transparent 50%, blue 50%),
    linear-gradient(135deg, blue 50%, transparent 50%),
    linear-gradient(to right, #EF7727, #EF7727);
  background-position:
    calc(100% - 20px) calc(1em + 2px),
    calc(100% - 15px) calc(1em + 2px),
    100% 0;
  background-size:
    5px 5px,
    5px 5px,
    2.5em 2.5em;
  background-repeat: no-repeat;
}

select.classic:focus {
  background-image:
    linear-gradient(45deg, white 50%, transparent 50%),
    linear-gradient(135deg, transparent 50%, white 50%),
    linear-gradient(to right, gray, gray);
  background-position:
    calc(100% - 15px) 1em,
    calc(100% - 20px) 1em,
    100% 0;
  background-size:
    5px 5px,
    5px 5px,
    2.5em 2.5em;
  background-repeat: no-repeat;
  border-color: grey;
  outline: 0;
}

select.round {
  background-image:
    linear-gradient(45deg, transparent 50%, gray 50%),
    linear-gradient(135deg, gray 50%, transparent 50%),
    radial-gradient(#ddd 70%, transparent 72%);
  background-position:
    calc(100% - 20px) calc(1em + 2px),
    calc(100% - 15px) calc(1em + 2px),
    calc(100% - .5em) .5em;
  background-size:
    5px 5px,
    5px 5px,
    1.5em 1.5em;
  background-repeat: no-repeat;
}

select.round:focus {
  background-image:
    linear-gradient(45deg, white 50%, transparent 50%),
    linear-gradient(135deg, transparent 50%, white 50%),
    radial-gradient(gray 70%, transparent 72%);
  background-position:
    calc(100% - 15px) 1em,
    calc(100% - 20px) 1em,
    calc(100% - .5em) .5em;
  background-size:
    5px 5px,
    5px 5px,
    1.5em 1.5em;
  background-repeat: no-repeat;
  border-color: green;
  outline: 0;
}

a.button1{
	width: 150px;
	display:inline-block;
	padding:0.45em 1.2em;
	line-height: 1.5em;
	border:0.1em solid #A6A6A6;
	#margin:0 0.3em 0.3em 0;
	border-radius:0.12em;
	box-sizing: border-box;
	text-decoration:none;
	font-family: calibri,tahoma,'Roboto',sans-serif;
	font-weight:300;
	color:#A6A6A6;
	text-align:center;
	transition: all 0.2s;
}

a.button1:hover{
	color:#000000;
	background-color:#FFFFFF;
}

@media all and (max-width:30em){
	.button1{
		display:block;
		margin:0.4em auto;
	}
}

.bouncy{
	animation:bouncy 5s infinite linear;
	position:relative;
}

@keyframes bouncy {
	0%{top:0em}
	40%{top:0em}
	43%{top:-0.9em}
	46%{top:0em}
	48%{top:-0.4em}
	50%{top:0em}
	100%{top:0em;}
}

/* The alert message box */
.alert {
  padding: 20px;
  background-color: #f44336; /* Red */
  color: white;
  margin-bottom: 15px;
}

/* The close button */
.closebtn {
  margin-left: 15px;
  color: white;
  font-weight: bold;
  float: right;
  font-size: 22px;
  line-height: 20px;
  cursor: pointer;
  transition: 0.3s;
}

/* When moving the mouse over the close button */
.closebtn:hover {
  color: black;
}

.disabled {
	pointer-events:none;
	cursor: default;
}

.card {
	box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
	transition: 0.3s;
	border-radius: 5px;
}

.card: hover{
	box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
	
}
</style>
<body bgcolor="#fff">
<center>
<div id="outter">
	<div style="width:100%;text-align:right">
		<a href="#" class="button1" style="border:0.1em solid #EF822E;color:#fff;border-radius:20px;margin:10px;background-color:#EF822E;font-weight:bold" id="reset" onclick="reset_page();">RESET</a>
	</div>
	<div class="alert" id="message_box" style="display:none"><span id="message">&nbsp;</span></div>
	<div style="width:100%"><img src="logo.png" alt="airduka log"></div>
	<div id="section_holder">
		<div class="card">
			<br/>
			<div id="display_holder"></div>
			<br/>
			<table border="0">
				<tr>
					<td colspan="2">&nbsp;</td>
				</tr>			
				<tr>
					<td colspan="2" align="right"><kbd style="font-size:16px"><span id="display_winner_info"></span></kbd></td>
				</tr>			
				<tr>
					<td colspan="2">&nbsp;</td>
				</tr>
				<tr>
					<td>
						<select class="classic" id="tier">
							<option value=''>SELECT TIER</option>
							<option value='<?=$tiers[0]?>'><?=$tiers[0]?></option>
							<option value='<?=$tiers[1]?>'><?=$tiers[1]?></option>
							<option value='<?=$tiers[2]?>'><?=$tiers[2]?></option>
						</select>
					</td>
					<td><a href="#" class="button1 bouncy" id="draw" onclick="run_draw();">RUN DRAW</a></td>
				</tr>
				<tr>
					<td>&nbsp;</td>
					<td><a href="#" class="button1 bouncy"id="details" style="display:none" onclick="get_customer_info();">GET DETAILS</a></td>
				</tr>
				<tr>
					<td colspan="2"><input type='hidden' id="cache" readonly /></td>
				</tr>
				<tr>
					<td colspan="2">&nbsp;</td>
				</tr>
			</table>
			<br/>
		</div>
	</div>
</div>
<center>
</body>
<script>
var GET_WINNER_ENDPOINT    = 'https://c914-41-139-151-158.ngrok.io/getFinalDrawWinner/';
var WINNER_DETAIL_ENDPOINT = 'https://c914-41-139-151-158.ngrok.io/getWinnerDetails/';
var DUMMY_POOL             = ["AD_SML9QHO","AD_4CNHE1O","AD_HGJRR2O","AD_EQX8J4O","AD_J28IRSO","AD_UUE8ICO","AD_T69JKYO","AD_2SOICQO","AD_CWHQQZO","AD_MXYBCQO","AD_M2SF8IO","AD_84QIS3O","AD_UB5BHJO","AD_C5QJ55O","AD_Z85LHZO","AD_1A2HXVO","AD_77LVI0O","AD_3Z13CXO","AD_PWRWX0O","AD_WY5A5LO","AD_SML9QHO","AD_4CNHE1O","AD_HGJRR2O","AD_EQX8J4O","AD_J28IRSO","AD_UUE8ICO","AD_T69JKYO","AD_2SOICQO","AD_CWHQQZO","AD_MXYBCQO","AD_M2SF8IO","AD_84QIS3O","AD_UB5BHJO","AD_C5QJ55O","AD_Z85LHZO","AD_1A2HXVO","AD_77LVI0O","AD_3Z13CXO","AD_PWRWX0O","AD_WY5A5LO","AD_SML9QHO","AD_4CNHE1O","AD_HGJRR2O","AD_EQX8J4O","AD_J28IRSO","AD_UUE8ICO","AD_T69JKYO","AD_2SOICQO","AD_CWHQQZO","AD_MXYBCQO","AD_M2SF8IO","AD_84QIS3O","AD_UB5BHJO","AD_C5QJ55O","AD_Z85LHZO","AD_1A2HXVO","AD_77LVI0O","AD_3Z13CXO","AD_PWRWX0O","AD_WY5A5LO","AD_SML9QHO","AD_4CNHE1O","AD_HGJRR2O","AD_EQX8J4O","AD_J28IRSO","AD_UUE8ICO","AD_T69JKYO","AD_2SOICQO","AD_CWHQQZO","AD_MXYBCQO","AD_M2SF8IO","AD_84QIS3O","AD_UB5BHJO","AD_C5QJ55O","AD_Z85LHZO","AD_1A2HXVO","AD_77LVI0O","AD_3Z13CXO","AD_PWRWX0O","AD_WY5A5LO"];
var COUNTER                = 0;

var display_holder = document.getElementById("display_holder");
var message_box    = document.getElementById("message_box");
/*
-.pick draw winner.
*/
function get_winner() {
  var cached_winner = document.getElementById("cache");
  display_holder.innerHTML = DUMMY_POOL[COUNTER];
  COUNTER++;
  if (COUNTER >= DUMMY_POOL.length) {
    //COUNTER = 0;
    //clearInterval(inst); // uncomment this if you want to stop refreshing after one cycle
	display_holder.innerHTML = cached_winner.value;
  } 
}
/*
-.method run draw.
*/
function run_draw(){ 
	var response = validate_select();
	if(response == true){
		message_box.style.display= 'none';
		var select_option = document.getElementById("tier");
		setInterval(get_winner, 50);
		data_handler(select_option.value);
	}else{
		var message = document.getElementById("message");
		message.innerHTML = 'Tier has to be checked.';
		message_box.style.display= 'block';
	}
}
/*
validate html select. 
*/
function validate_select(){
	var bool = false;
	var select_option = document.getElementById("tier");
	var message = document.getElementById("message");
	if(select_option.value != "" && select_option.value.length > 0) {
		bool = true;
	}
	return bool;
}
/*
-.get winner.
*/
function data_handler(data){
	var xhr = new XMLHttpRequest();
	var cached_winner = document.getElementById("cache");
	var btn_draw = document.getElementById("draw");
	var btn_details = document.getElementById("details");
	xhr.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			var obj = JSON.parse(this.responseText);
			cached_winner.value = obj.MESSAGE;
			btn_draw.setAttribute('class','disabled');
			btn_draw.setAttribute('style','display:none');
			setTimeout(function(){
				btn_details.setAttribute('style','display:');
			},3500);
			
		}
	};
	xhr.open("GET", GET_WINNER_ENDPOINT + data, true);
	xhr.send();
}
/*
-.customer info.
*/
function get_customer_info(){
	var cache = document.getElementById("cache");
	data_handler_2(cache.value);	
}
/*
-.get customer info.
*/
function data_handler_2(data){
	var display_winner_info = document.getElementById("display_winner_info");
	var xhr = new XMLHttpRequest();
	xhr.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			var obj = JSON.parse(this.responseText);
			display_winner_info.innerHTML=obj.MESSAGE.toUpperCase();
		}
	};
	xhr.open("GET", WINNER_DETAIL_ENDPOINT + data, true);
	xhr.send();
}
/*
reset page
*/
function reset_page() {
	document.getElementById("tier").innerHTML = "";
	window.location.reload();
}
</script>
</html>