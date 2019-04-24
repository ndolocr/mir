//Javascript Document
//Initializing Global variables 
var total_studies = 0;


/*
 * Function to determine 
 * number of total studies 
 * in the database
*/

function total_study_counter(val){
	total_studies = val;
	//document.write(total_studies);
}

function calculate_cell_one_low(val){
	var cell_width =((val/total_studies)*100);
	
	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
		
	

	var length = cell_width+"px";
	
	document.getElementsByClassName("one_low")[0].style.width = length;
	document.getElementsByClassName("one_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_one_high(val){
	var cell_width = ((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("one_high")[0].style.width = length;
	document.getElementsByClassName("one_high")[0].style.height = length;
	document.write(length);
}

function calculate_cell_one_medium(val){
	var cell_width = ((val/total_studies)*100);	
	
	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("one_medium")[0].style.width = length;
	document.getElementsByClassName("one_medium")[0].style.height = length;
	document.write(length);
}


function calculate_cell_two_low(val){
	var cell_width =((val/total_studies)*100);	
	
	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("two_low")[0].style.width = length;
	document.getElementsByClassName("two_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_two_high(val){
	var cell_width =((val/total_studies)*100);
	
	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("two_high")[0].style.width = length;
	document.getElementsByClassName("two_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_two_medium(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("two_medium")[0].style.width = length;
	document.getElementsByClassName("two_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_three_low(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("three_low")[0].style.width = length;
	document.getElementsByClassName("three_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_three_high(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("three_high")[0].style.width = length;
	document.getElementsByClassName("three_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_three_medium(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("three_medium")[0].style.width = length;
	document.getElementsByClassName("three_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_four_low(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("four_low")[0].style.width = length;
	document.getElementsByClassName("four_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_four_high(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("four_high")[0].style.width = length;
	document.getElementsByClassName("four_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_four_medium(val){
	var cell_width =((val/total_studies)*100);	
	
	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("four_medium")[0].style.width = length;
	document.getElementsByClassName("four_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_five_low(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("five_low")[0].style.width = length;
	document.getElementsByClassName("five_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_five_high(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("five_high")[0].style.width = length;
	document.getElementsByClassName("five_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_five_medium(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("five_medium")[0].style.width = length;
	document.getElementsByClassName("five_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_six_low(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("six_low")[0].style.width = length;
	document.getElementsByClassName("six_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_six_high(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("six_high")[0].style.width = length;
	document.getElementsByClassName("six_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_six_medium(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("six_medium")[0].style.width = length;
	document.getElementsByClassName("six_medium")[0].style.height = length;

	document.write(length);
}


function calculate_cell_seven_low(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("seven_low")[0].style.width = length;
	document.getElementsByClassName("seven_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_seven_high(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("seven_high")[0].style.width = length;
	document.getElementsByClassName("seven_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_seven_medium(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("seven_medium")[0].style.width = length;
	document.getElementsByClassName("seven_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_eight_low(val){
	var cell_width =((val/total_studies)*100);	
	
	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("eight_low")[0].style.width = length;
	document.getElementsByClassName("eight_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_eight_high(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("eight_high")[0].style.width = length;
	document.getElementsByClassName("eight_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_eight_medium(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("eight_medium")[0].style.width = length;
	document.getElementsByClassName("eight_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_nine_low(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("nine_low")[0].style.width = length;
	document.getElementsByClassName("nine_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_nine_high(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("nine_high")[0].style.width = length;
	document.getElementsByClassName("nine_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_nine_medium(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("nine_medium")[0].style.width = length;
	document.getElementsByClassName("nine_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_ten_low(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("ten_low")[0].style.width = length;
	document.getElementsByClassName("ten_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_ten_high(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("ten_high")[0].style.width = length;
	document.getElementsByClassName("ten_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_ten_medium(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("ten_medium")[0].style.width = length;
	document.getElementsByClassName("ten_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_eleven_low(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("eleven_low")[0].style.width = length;
	document.getElementsByClassName("eleven_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_eleven_high(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("eleven_high")[0].style.width = length;
	document.getElementsByClassName("eleven_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_eleven_medium(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("eleven_medium")[0].style.width = length;
	document.getElementsByClassName("eleven_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_twelve_low(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("twelve_low")[0].style.width = length;
	document.getElementsByClassName("twelve_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_twelve_high(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("twelve_high")[0].style.width = length;
	document.getElementsByClassName("twelve_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_twelve_medium(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("twelve_medium")[0].style.width = length;
	document.getElementsByClassName("twelve_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_thirteen_low(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("thirteen_low")[0].style.width = length;
	document.getElementsByClassName("thirteen_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_thirteen_high(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("thirteen_high")[0].style.width = length;
	document.getElementsByClassName("thirteen_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_thirteen_medium(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("thirteen_medium")[0].style.width = length;
	document.getElementsByClassName("thirteen_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_fourteen_low(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("fourteen_low")[0].style.width = length;
	document.getElementsByClassName("fourteen_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_fourteen_high(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("fourteen_high")[0].style.width = length;
	document.getElementsByClassName("fourteen_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_fourteen_medium(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("fourteen_medium")[0].style.width = length;
	document.getElementsByClassName("fourteen_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_fifteen_low(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("fifteen_low")[0].style.width = length;
	document.getElementsByClassName("fifteen_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_fifteen_high(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("fifteen_high")[0].style.width = length;
	document.getElementsByClassName("fifteen_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_fifteen_medium(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("fifteen_medium")[0].style.width = length;
	document.getElementsByClassName("fifteen_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_sixteen_low(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("sixteen_low")[0].style.width = length;
	document.getElementsByClassName("sixteen_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_sixteen_high(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("sixteen_high")[0].style.width = length;
	document.getElementsByClassName("sixteen_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_sixteen_medium(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("sixteen_medium")[0].style.width = length;
	document.getElementsByClassName("sixteen_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_seventeen_low(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("seventeen_low")[0].style.width = length;
	document.getElementsByClassName("seventeen_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_seventeen_high(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("seventeen_high")[0].style.width = length;
	document.getElementsByClassName("seventeen_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_seventeen_medium(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("seventeen_medium")[0].style.width = length;
	document.getElementsByClassName("seventeen_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_eighteen_low(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("eighteen_low")[0].style.width = length;
	document.getElementsByClassName("eighteen_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_eighteen_high(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("eighteen_high")[0].style.width = length;
	document.getElementsByClassName("eighteen_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_eighteen_medium(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("eighteen_medium")[0].style.width = length;
	document.getElementsByClassName("eighteen_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_nineteen_low(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("nineteen_low")[0].style.width = length;
	document.getElementsByClassName("nineteen_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_nineteen_high(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("nineteen_high")[0].style.width = length;
	document.getElementsByClassName("nineteen_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_nineteen_medium(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("nineteen_medium")[0].style.width = length;
	document.getElementsByClassName("nineteen_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_twenty_low(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("twenty_low")[0].style.width = length;
	document.getElementsByClassName("twenty_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_twenty_high(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("twenty_high")[0].style.width = length;
	document.getElementsByClassName("twenty_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_twenty_medium(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("twenty_medium")[0].style.width = length;
	document.getElementsByClassName("twenty_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_twenty_one_low(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("twenty_one_low")[0].style.width = length;
	document.getElementsByClassName("twenty_one_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_twenty_one_high(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("twenty_one_high")[0].style.width = length;
	document.getElementsByClassName("twenty_one_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_twenty_one_medium(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("twenty_one_medium")[0].style.width = length;
	document.getElementsByClassName("twenty_one_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_twenty_two_low(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("twenty_two_low")[0].style.width = length;
	document.getElementsByClassName("twenty_two_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_twenty_two_high(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("twenty_two_high")[0].style.width = length;
	document.getElementsByClassName("twenty_two_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_twenty_two_medium(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("twenty_two_medium")[0].style.width = length;
	document.getElementsByClassName("twenty_two_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_twenty_three_low(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("twenty_three_low")[0].style.width = length;
	document.getElementsByClassName("twenty_three_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_twenty_three_high(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("twenty_three_high")[0].style.width = length;
	document.getElementsByClassName("twenty_three_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_twenty_three_medium(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("twenty_three_medium")[0].style.width = length;
	document.getElementsByClassName("twenty_three_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_twenty_four_low(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("twenty_four_low")[0].style.width = length;
	document.getElementsByClassName("twenty_four_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_twenty_four_high(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("twenty_four_high")[0].style.width = length;
	document.getElementsByClassName("twenty_four_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_twenty_four_medium(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("twenty_four_medium")[0].style.width = length;
	document.getElementsByClassName("twenty_four_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_twenty_five_low(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("twenty_five_low")[0].style.width = length;
	document.getElementsByClassName("twenty_five_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_twenty_five_high(val){
	var cell_width =((val/total_studies)*100);	
	
	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("twenty_five_high")[0].style.width = length;
	document.getElementsByClassName("twenty_five_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_twenty_five_medium(val){
	var cell_width =((val/total_studies)*100);	
	
	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("twenty_five_medium")[0].style.width = length;
	document.getElementsByClassName("twenty_five_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_twenty_six_low(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("twenty_six_low")[0].style.width = length;
	document.getElementsByClassName("twenty_six_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_twenty_six_high(val){
	var cell_width =((val/total_studies)*100);	
	
	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("twenty_six_high")[0].style.width = length;
	document.getElementsByClassName("twenty_six_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_twenty_six_medium(val){
	var cell_width =((val/total_studies)*100);	
	
	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("twenty_six_medium")[0].style.width = length;
	document.getElementsByClassName("twenty_six_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_twenty_seven_low(val){
	var cell_width =((val/total_studies)*100);	
	
	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("twenty_seven_low")[0].style.width = length;
	document.getElementsByClassName("twenty_seven_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_twenty_seven_high(val){
	var cell_width =((val/total_studies)*100);	
	
	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("twenty_seven_high")[0].style.width = length;
	document.getElementsByClassName("twenty_seven_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_twenty_seven_medium(val){
	var cell_width =((val/total_studies)*100);	
	
	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("twenty_seven_medium")[0].style.width = length;
	document.getElementsByClassName("twenty_seven_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_twenty_eight_low(val){
	var cell_width =((val/total_studies)*100);	
	
	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("twenty_eight_low")[0].style.width = length;
	document.getElementsByClassName("twenty_eight_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_twenty_eight_high(val){
	var cell_width =((val/total_studies)*100);	
	
	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("twenty_eight_high")[0].style.width = length;
	document.getElementsByClassName("twenty_eight_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_twenty_eight_medium(val){
	var cell_width =((val/total_studies)*100);	
	
	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("twenty_eight_medium")[0].style.width = length;
	document.getElementsByClassName("twenty_eight_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_twenty_nine_low(val){
	var cell_width =((val/total_studies)*100);	
	
	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("twenty_nine_low")[0].style.width = length;
	document.getElementsByClassName("twenty_nine_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_twenty_nine_high(val){
	var cell_width =((val/total_studies)*100);	
	
	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("twenty_nine_high")[0].style.width = length;
	document.getElementsByClassName("twenty_nine_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_twenty_nine_medium(val){
	var cell_width =((val/total_studies)*100);	
	
	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("twenty_nine_medium")[0].style.width = length;
	document.getElementsByClassName("twenty_nine_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_thirty_low(val){
	var cell_width =((val/total_studies)*100);
	
	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("thirty_low")[0].style.width = length;
	document.getElementsByClassName("thirty_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_thirty_high(val){
	var cell_width =((val/total_studies)*100);	
	
	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("thirty_high")[0].style.width = length;
	document.getElementsByClassName("thirty_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_thirty_medium(val){
	var cell_width =((val/total_studies)*100);	
	
	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("thirty_medium")[0].style.width = length;
	document.getElementsByClassName("thirty_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_thirty_one_low(val){
	var cell_width =((val/total_studies)*100);	
	
	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("thirty_one_low")[0].style.width = length;
	document.getElementsByClassName("thirty_one_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_thirty_one_high(val){
	var cell_width =((val/total_studies)*100);	
	
	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("thirty_one_high")[0].style.width = length;
	document.getElementsByClassName("thirty_one_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_thirty_one_medium(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("thirty_one_medium")[0].style.width = length;
	document.getElementsByClassName("thirty_one_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_thirty_two_low(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("thirty_two_low")[0].style.width = length;
	document.getElementsByClassName("thirty_two_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_thirty_two_high(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("thirty_two_high")[0].style.width = length;
	document.getElementsByClassName("thirty_two_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_thirty_two_medium(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("thirty_two_medium")[0].style.width = length;
	document.getElementsByClassName("thirty_two_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_thirty_three_low(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("thirty_three_low")[0].style.width = length;
	document.getElementsByClassName("thirty_three_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_thirty_three_high(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("thirty_three_high")[0].style.width = length;
	document.getElementsByClassName("thirty_three_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_thirty_three_medium(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("thirty_three_medium")[0].style.width = length;
	document.getElementsByClassName("thirty_three_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_thirty_four_low(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("thirty_four_low")[0].style.width = length;
	document.getElementsByClassName("thirty_four_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_thirty_four_high(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("thirty_four_high")[0].style.width = length;
	document.getElementsByClassName("thirty_four_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_thirty_four_medium(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("thirty_four_medium")[0].style.width = length;
	document.getElementsByClassName("thirty_four_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_thirty_five_low(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("thirty_five_low")[0].style.width = length;
	document.getElementsByClassName("thirty_five_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_thirty_five_high(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("thirty_five_high")[0].style.width = length;
	document.getElementsByClassName("thirty_five_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_thirty_five_medium(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("thirty_five_medium")[0].style.width = length;
	document.getElementsByClassName("thirty_five_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_thirty_six_low(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("thirty_six_low")[0].style.width = length;
	document.getElementsByClassName("thirty_six_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_thirty_six_high(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("thirty_six_high")[0].style.width = length;
	document.getElementsByClassName("thirty_six_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_thirty_six_medium(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("thirty_six_medium")[0].style.width = length;
	document.getElementsByClassName("thirty_six_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_thirty_seven_low(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("thirty_seven_low")[0].style.width = length;
	document.getElementsByClassName("thirty_seven_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_thirty_seven_high(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("thirty_seven_high")[0].style.width = length;
	document.getElementsByClassName("thirty_seven_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_thirty_seven_medium(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("thirty_seven_medium")[0].style.width = length;
	document.getElementsByClassName("thirty_seven_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_thirty_eight_low(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("thirty_eight_low")[0].style.width = length;
	document.getElementsByClassName("thirty_eight_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_thirty_eight_high(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("thirty_eight_high")[0].style.width = length;
	document.getElementsByClassName("thirty_eight_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_thirty_eight_medium(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("thirty_eight_medium")[0].style.width = length;
	document.getElementsByClassName("thirty_eight_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_thirty_nine_low(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("thirty_nine_low")[0].style.width = length;
	document.getElementsByClassName("thirty_nine_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_thirty_nine_high(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("thirty_nine_high")[0].style.width = length;
	document.getElementsByClassName("thirty_nine_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_thirty_nine_medium(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("thirty_nine_medium")[0].style.width = length;
	document.getElementsByClassName("thirty_nine_medium")[0].style.height = length;

	document.write(length);
}

function calculate_cell_fourty_low(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("fourty_low")[0].style.width = length;
	document.getElementsByClassName("fourty_low")[0].style.height = length;

	document.write(length);
}

function calculate_cell_fourty_high(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("fourty_high")[0].style.width = length;
	document.getElementsByClassName("fourty_high")[0].style.height = length;

	document.write(length);
}

function calculate_cell_fourty_medium(val){
	var cell_width =((val/total_studies)*100);	

	if(cell_width<=1){
		cell_width = 15;	
	}else if(cell_width<=10){
		cell_width = 20;	
	}else if(cell_width<=20){
		cell_width = 25;	
	}else if(cell_width<=30){
		cell_width = 30;
	}else if(cell_width<=40){
		cell_width = 40;	
	}else if(cell_width<=50){
		cell_width = 50;
	}else if(cell_width<=60){
		cell_width = 60;
	}else if(cell_width<=70){
		cell_width = 70;
	}else if(cell_width<=80){
		cell_width = 80;
	}else if(cell_width<=90){
		cell_width = 90;
	}else if(cell_width<=100){
		cell_width = 100;
	}	
	
	var length = cell_width+"px";
	
	document.getElementsByClassName("fourty_medium")[0].style.width = length;
	document.getElementsByClassName("fourty_medium")[0].style.height = length;

	document.write(length);
}
