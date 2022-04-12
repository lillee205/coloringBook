
$(function() {
    var canvas = document.getElementById('drawCanvas');
    var ctx = canvas.getContext('2d');
    var img = new Image();   // Create new img element
	img.src = `${window.static_folder}`;

    img.addEventListener('load', function() {
		var hRatio = canvas.width  / img.width    ;
		var vRatio =  canvas.height / img.height  ;
		var ratio  = Math.min ( hRatio, vRatio );
		var centerShift_x = ( canvas.width - img.width*ratio ) / 2;
		var centerShift_y = ( canvas.height - img.height*ratio ) / 2;  
		ctx.clearRect(0,0,canvas.width, canvas.height);
        ctx.drawImage(img, 0,0, img.width, img.height,
                      centerShift_x,centerShift_y,img.width*ratio, img.height*ratio);
    }, false);

	$('#drawCanvas').bind('click', function(evt){
		fill(evt)
		// get location where clicked
		var x,y = [evt.clientX , evt.clientY]
		var desColor = [255,3,0]
		var newImg = document.createElement('img')
		//url = URL.createObjectURL(blob);
		$.getJSON('/bg_process', {
			xCoord: x,
			yCoord: y,
			color: desColor
		}, function(data){
			URL.revokeObjectURL(link.href);
			// replace canvas image with newly updated image
		});
		return false;
	})

	function fill(evt) {
		var pos = getMousePos(canvas, evt);

		ctx.fillStyle = "#000000";
		ctx.fillRect (pos.x, pos.y, 4, 4);
	}

	function getMousePos(canvas, evt) {
		var rect = canvas.getBoundingClientRect();
		return {
			x: evt.clientX - rect.left,
			y: evt.clientY - rect.top
		};
	}
})

