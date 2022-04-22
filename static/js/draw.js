
$(function() {
	var colorPicker = new iro.ColorPicker('#picker', {
		layout: [
			{ 
			component: iro.ui.Box,
			},
			{ 
      		component: iro.ui.Slider,
			options: {
				sliderType: 'hue'
				}
    		}
		]
	});
	var currentColor = {
		r: 0,
		g: 0,
		b: 0
	}
	colorPicker.on('color:change', function(color, changes){
		currentColor = color.rgb
	})
	var xPos = 0
	var yPos =0
    var canvas = document.getElementById('drawCanvas');
    var ctx = canvas.getContext('2d');
    var img = new Image();   // Create new img element
	img.src = `${window.static_folder}`;

	function load() {
		var hRatio = canvas.width  / img.width    ;
		var vRatio =  canvas.height / img.height  ;
		var ratio  = Math.min ( hRatio, vRatio );
		var centerShift_x = ( canvas.width - img.width*ratio ) / 2;
		var centerShift_y = ( canvas.height - img.height*ratio ) / 2;  
		ctx.clearRect(0,0,canvas.width, canvas.height);
        ctx.drawImage(img, 0,0, img.width, img.height,
                      centerShift_x,centerShift_y,img.width*ratio, img.height*ratio);
		requestAnimationFrame(load)
	}
	requestAnimationFrame(load);

    img.addEventListener('load', function() {
		load()
    }, false);

	$('#drawCanvas').bind('click', function(e){
		fill(e)
		// get location where clicked

		canvas.toBlob(function(blob) {
			//var url = URL.createObjectURL(blob);
			var imgURL = canvas.toDataURL();
			$.post("/bgprocess", 
				{imgUrl: imgURL,
			     x: xPos, 
				 y: yPos,
				 color: JSON.stringify(currentColor) 
				}).then(function(res){
					var image = new Image();
					img.src = 'data:image/png;base64,' + res.result;
					load()
				})
			})
		})

	// $('#drawCanvas').bind('click', function(evt){
	// 	fill(evt)
	// 	// get location where clicked
	// 	var x,y = [evt.clientX , evt.clientY]
	// 	var desColor = [255,3,0]
	// 	var newImg = document.createElement('img')
	// 	//
	// 	$.getJSON('/bg_process', {
	// 		xCoord: x,
	// 		yCoord: y,
	// 		color: desColor
	// 	}, function(data){
	// 		console.log("done")
	// 		//URL.revokeObjectURL(link.href);
	// 		// replace canvas image with newly updated image
	// 	});
	// 	return false;
	

	function fill(evt) {
		var pos = getMousePos(canvas, evt);

		ctx.fillStyle = "#fdb813";
		xPos = pos.x
		yPos = pos.y 
		console.log(pos.x,pos.y)
		ctx.fillRect (pos.x, pos.y, 8, 8);
	}

	function getMousePos(canvas, evt) {
		var rect = canvas.getBoundingClientRect();
		return {
			x: evt.clientX - rect.left,
			y: evt.clientY - rect.top
		};
	}
})

