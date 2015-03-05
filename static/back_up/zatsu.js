jQuery(document).ready(function() {
    var url = 'https://api.apigw.smt.docomo.ne.jp/dialogue/v1/dialogue';
    var APIKEY = '4132387542305945724c6e71766a46507a4c2e363566436f67664644567053444e5230324c565465716f42';    
    var req = function(utt) {
	var request = new XMLHttpRequest();
	request.open('POST', url + '?APIKEY=' + APIKEY);
	request.responseType = 'application/json';
	request.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');

	request.onload = function(evt) {
	    alert(request.response); //ここに回答がくる
	}
	    
	var params = {"utt": utt};
	var body = Object.keys(params).map(function(key) {
            return key + '=' + params[key]
        }).join('&');
	
	request.send(JSON.stringify(params));
    }
    
    req('こんにちは');
});
