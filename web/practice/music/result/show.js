$.ajax({
	type: 'GET',
	url: 'https://teamspeak3nosyamoji.s3-ap-northeast-1.amazonaws.com/music1/data.json',
	dataType: 'json',
	success: function(json){
		var len = json.length;
		console.log("len:"+len)
		var users=[];
		var scores=[];
		for(var i=0; i < len; i++){
			for(var j=0; j<users.length+1;j++){
				if(json[i].user == users[j] ){
					scores[j]=parseInt(scores[j])+parseInt(json[i].score);
					break;
				}
				if(j==users.length){
					users.push(json[i].user)
					scores.push(parseInt(json[i].score))
					break;
				}
			}
		}
	var max=scores[0]
	for(var i=1;i<scores.length;i++){
	if(max<scores[i])
		max=scores[i]
	}




	var rank=1;
	for(var i=max; i>=0; i--){
		for(var j=0;j<scores.length;j++){
			if(scores[j]==i){
				document.write(rank+" : "+users[j]+" : "+i+"<br>")
					for(var k=0; k<len; k++){
						if(json[k].user==users[j]){
							document.write('<a href="'+json[k].url+'">'+json[k].name+'</a>'+': '+json[k].score+'<br>');
						}
						
					}
				rank=rank+1;
			document.write("<br>")
			}
		}
	}
	}
});