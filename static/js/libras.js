(function($) {

	var ytplayer;
	var params = { allowScriptAccess: "always", wmode: 'opaque' };
	var atts = { id: "myytplayer" };
	function setList(list){
		
	}
    function getYtVid(url){
        // http://www.youtube.com/watch?v=6P95FCsUvAg
        url = url.replace(/&amp;/g, '&');
        var arr = url.split("?")[1];
        arr = arr.split("&");
        for(var i = 0; i < arr.length; i++){
            var kv = arr[i].split("=");
            if(kv[0] == "v"){
                return kv[1];
            }
        }
        return null;
    }
	$.fn.vinilTube = function(settings) {
		var config = {vid: 'w72R_LVWiSs', list:'lista', start: 0};
            
        if(settings.url){
            settings.vid = getYtVid(settings.url);
        } 
		if (settings) $.extend(config, settings);
 
		this.each(function() {
			swfobject.embedSWF("http://www.youtube.com/v/" + config.vid + "&enablejsapi=1&playerapiid=ytplayer&autoplay=1&version=3&rel=0"+(config.start != 0 ? '&start=' + config.start : ''), 
				this.id, "425", "356", "8", null, null, params, atts);
		});
 
		return this;
 
   };
 
 })(jQuery);
