function getValue(idname){
    var result = document.getElementById(idname).value;
    var regexp = /([\u{3005}\u{3007}\u{303b}\u{3400}-\u{9FFF}\u{F900}-\u{FAFF}\u{20000}-\u{2FFFF}][\u{E0100}-\u{E01EF}\u{FE00}-\u{FE02}]?)/mu;
    var i=0
    var ans=""
    for(i=0;i<result.length;i++){
	var a = result[i]
	if(regexp.test(a))
	    ans=ans+a
    }
    var demo2 = document.getElementById("samurai");
    demo2.innerHTML = result+"<br><br>↓<br><br>"+ans;
}


function getValue2(idname){
    var txt=document.getElementById(idname).value
    var url = "http://www.utamap.com/phpflash/flashfalsephp.php?unum="+txt
    var texto=""
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url);
    xhr.responseType = 'text';
    xhr.overrideMimeType('text/plain; charset=utf-8');
    xhr.send();
    xhr.onload = function () {
	if(xhr.response==null)
	    document.getElementById("txt1").value ="error"
	if (xhr.readyState === xhr.DONE) {
	    if (xhr.status === 200) {
		var temp = xhr.response
		var count = 0
		var i=0
		while(count<2){
		    if(temp[0]=='=')
			count+=1
		    temp = temp.slice(1)
		}
		document.getElementById("txt1").value =temp
            }
    	}
    };
}



