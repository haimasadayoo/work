$.ajax({
	type: 'GET',
	url: 'https://teamspeak3nosyamoji.s3-ap-northeast-1.amazonaws.com/music1/data2.json',
	dataType: 'json',
	success: function(json){
		var len = json.length;
		for(var i=0; i < len; i++){
			document.write(json[i].user+'  <a href="'+json[i].url+'">'+json[i].name+'</a>'+': '+json[i].score+'<br>');
		}
	}
});