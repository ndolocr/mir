// JavaScript Document

/* Initializing Global variables */
var low_quality_studies=[];

function capture_low_quality_studies(id_no){
	low_quality_studies.push(id_no);
	/*for(i=0; i<low_quality_studies.length, i++){
		document.write(low_quality_studies[i]);
	}
	low_quality_studies++;

	var output = document.getElementsByClassName('display_low_quality_studies');
	output.innerHTML = "<a href=#>"+id_no+"</a>";*/
}

function display_study_id(){
	var i;
	for(i=0; i<low_quality_studies.length; i++){
		document.write(low_quality_studies[i]);
	}
}

function reset_array(){
	low_quality_studies=[];	
}