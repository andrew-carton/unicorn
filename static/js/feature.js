function onSubmitComment(comment) {

	var commentObj = new Object();
	commentObj.id = bugId;
	commentObj.comment = document.getElementById("mycomment").value;
    // AJAX post request
    var xmlhttp = new XMLHttpRequest(); 
	var csrftoken = $("[name=csrfmiddlewaretoken]").val();
    xmlhttp.open("POST", "/issues/comment");
    xmlhttp.setRequestHeader("Content-Type", "application/json");
	xmlhttp.setRequestHeader("X-CSRFToken", csrftoken);
	xmlhttp.onreadystatechange = function() {
		if (xmlhttp.readyState === 4) {
			window.location.replace("/issues/" + bugId + "/feature");
		}
	}
	
    // Serialise object to JSON and send
    xmlhttp.send(JSON.stringify(commentObj));

	
}
