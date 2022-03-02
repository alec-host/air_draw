<!DOCTYPE html>
<html lang="en">
  <head>

	<link href="ui/jquery-ui.min.css" rel="stylesheet" type="text/css" />
	<script src="ui/jquery-ui.min.js" type="text/javascript"></script>
	
	<link href="themes/metro/lightgray/jtable.min.css" rel="stylesheet" type="text/css" />
	
	<link href="validate/validationEngine.css" rel="stylesheet" type="text/css" />
	
	<script src="scripts/jquery-1.9.1.js" type="text/javascript"></script>
	<script src="scripts/jquery-ui-1.10.0.min.js" type="text/javascript"></script>
    <script src="jTable/jquery.jtable.min.js" type="text/javascript"></script>
	
	<script src="validate/jquery.validationEngine-en.js" type="text/javascript" charset="utf-8"></script>
    <script src="validate/jquery.validationEngine.js" type="text/javascript" charset="utf-8"></script>	
	
	<style type="text/css">
	html{
		padding:1px;
	}
	
	.card:hover {
		box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
	}

	.container {
		padding: 2px 0px;
	}
		
	.ui-button, .ui-button-text, .ui-button, .jtable-input-label{
		font-size: 13px !important;
	}
	
	.jtable-left-area,.jtable-right-area,.jtable-column-header,.jtable-command-column-header,.ui-widget-header{
		background-color: #4A6EC7;
		font-family: Calibri,Arial,Tahoma;
		font-size: 14px;
		height: 25px;
	}	
	
	.jtable-title-text, div.jtable-main-container > div.jtable-title,.jtable-toolbar{
		background-color: #f9f9f9;
	}
	
	div.jtable-main-container > div.jtable-title div.jtable-toolbar span.jtable-toolbar-item {
		background-color: #FE806E;
		border-radius: 2px;
		padding: 10px;
		color: #fff;
	}
	
	.ui-dialog {
		background-color: #f9f9f9;
		position: absolute;
		left: 0;
		right: 400;
		margin-left: 0%;
		margin-right: 50%;
	}
	
	.formErrorContent {
		/* width: 100%; */
		/* left: -1px; */
	}
	
	button {
		width: 100px;
	}
	 
	</style>
	<script type="text/javascript">
		$(document).ready(function () {
		    //-.prepare jTable.
			$('#DataViewTable').jtable({
				title: '&nbsp;',
				toolbar:{
					items: [{
						tooltip: 'Click to download',
						icon: 'img/excel.png',
						text: 'DOWNLOAD',
						click: function (){
							window.location = '#';
							e.preventDefault();
						}
					}]
				},
				paging: true,	
				pageSize: 10,				
				openChildAsAccordion: true,
				messages: {
					addNewRecord: 'ADD '
				},
				columnResizable: false,
				actions: {
					listAction: 'entries_fetch.php?action=list&jtStartIndex=0&jtPageSize=10&jtSorting=null',
					/*createAction: 'entries_fetch.php?action=create',*/
					/*updateAction: 'entries_fetch.php?action=update',*/
					/*deleteAction: 'entries_fetch.php?action=delete'*/
				},
				fields: {
						_Id: {
							key: true,
							create: false,
							edit: false,
							list: false
						},
						company_name: {
							title: 'Company name',							
							width: '10%',
							create: true,
							edit: true,	
							display: function(data){
								return data.record.company_name;
							}							
						},						
						company_identifier: {
							title: 'Identifier',
							width: '10%',
							create: true,
							edit: true,
							display: function(data){
								return data.record.company_identifier;
							}
						},
						name: {
							title: 'Name',
							width: '10%',
							create: true,
							edit: true,
							display: function(data){
								return data.record.name;
							}
						},
						tier: {
							title: 'Tier',
							width: '10%',
							create: true,
							edit: true,
							display: function(data){
								return data.record.tier;
							}
						},
						amount: {
							title: 'Amount',
							width: '10%',
							create: true,
							edit: true,
							display: function(data){
								return data.record.amount;
							}
						},
						ticket_no: {
							title: 'Ticket no',
							width: '10%',
							create: true,
							edit: true,
							display: function(data){
								return data.record.ticket_no;
							}
						},
						date_created: {
							title: 'Mobile no',
							width: '10%',
							create: true,
							edit: true,
							display: function(data){
								return data.record.date_created;
							}
						},
					},
					//-.
					formCreated: function(event, data){
						//-.resize the form.
						data.form.parent().css('width','350px');
						data.form.parent().css('height','250px');
						//-.style html components.
						data.form.find('input').css('border','solid 1px #444');
						data.form.find('select').css('border','solid 1px #444');
						//-.
						data.form.find('input').css('width','100%');
						data.form.find('input').css('padding','1px');
						data.form.find('input').css('font-size','14px');
						data.form.find('input').css('height','25px');
						data.form.find('select').css('height','25px');
						//-.
						data.form.find('input').addClass('ui-corner-all');
						data.form.find('select').addClass('ui-corner-all');						
						//-.define prompt position.
						data.form.validationEngine('attach',{promptPosition: "topLeft", scroll: false});
					},
					//-.validate form when it is been submitted
					formSubmitting: function (event, data){
						return data.form.validationEngine('validate');
					},
					//-.dispose validation logic when form is closed.
					formClosed: function (event, data){
						data.form.validationEngine('hide');
						data.form.validationEngine('detach');
					},
					//-.reload main datatable upon creation of a new record.
					formAdded: function (event, data){
						$('#DataViewTable').jtable('reload');					
					}
			});			
			//-.load person list from server.
			$('#DataViewTable').jtable('load',{'empty':'empty'});		
			//-.
			$('#LoadRecordsButton').click(function (e) {
				e.preventDefault();
				$('#DataViewTable').jtable('load', {
					search_name: $('#word').val()
				});
			});
			//-.
			$('#LoadRecordsButton').click();
		});
	</script>	
  </head>
  <body>
	<span><h5>DRAW ENTRIES</h5></span>
	<div class="card">
		<div class="container">
			<div class="filtering" >
				<form>
					<span>&nbsp;</span><input type="text" name="word" id="word" style="" placeholder=" TYPE MSISDN TO SEARCH..."/>
					<button type="submit" id="LoadRecordsButton" class="btn2">&nbsp;Search&nbsp;</button>
				</form>
			</div>
		</div>
	</div>
	<br/>
	<div id="DataViewTable" style="width: 100%;"></div>		
  </body>
</html>