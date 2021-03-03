// When the user scrolls down 20px from the top of the document, show the topbtn
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    document.getElementById("topbtn").style.display = "block";
  } else {
    document.getElementById("topbtn").style.display = "none";
  }
}

// When the user clicks on the topbtn, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

// When topbtn reaches 15px above footer, its position changes from fixed to absolute
function checkOffset() {
	var topbtn = document.querySelector('#topbtn');
	var footer = document.querySelector('footer');
	
	function getRectTop(el){
		var rect = el.getBoundingClientRect();
		return rect.top;
	}
	if((getRectTop(topbtn) + document.body.scrollTop) + topbtn.offsetHeight >= (getRectTop(footer) + document.body.scrollTop) - 15)
		topbtn.style.position = 'absolute';
	if(document.body.scrollTop + window.innerHeight < (getRectTop(footer) + document.body.scrollTop))
		topbtn.style.position = 'fixed'; // restore when you scroll up
	
}

document.addEventListener("scroll", function(){
  checkOffset();
});

//Performance report dates generated from form values
var dateValue1 = document.getElementById("startdateid").value;
var dateValue2 = document.getElementById("enddateid").value;
document.getElementById("date1").innerHTML = dateValue1;
document.getElementById("date2").innerHTML = dateValue2;

//book order id generated from form value
var book = document.getElementById("bookid").value;
document.getElementById("book").innerHTML = book;

//Publisher Name generated from form value
var publisher = document.getElementById("publisherid").value;
document.getElementById("publisher").innerHTML = publisher;