
console.log("setting up level")

var winPlace = null;
var losePlaces = [];

for (var x = 5; x < 410; x+=50){
	var gridX= new Path.Line(new Point(x,5), new Point(x,205))
	gridX.strokeColor =  new Color(0,0,0,0.5);
	gridX.strokeWidth = 1;
}

for (var y = 5; y < 210; y+=50){
	var gridY= new Path.Line(new Point(5,y), new Point(405,y))
	gridY.strokeColor =  new Color(0,0,0,0.5);
	gridY.strokeWidth = 1;
}


function DrawAppleAt(x,y){
	var apple = new Path.Circle({
		center: [0,0],
		radius: 10,
		fillColor: "green",
	});
	
	var stem = new Path({
		segments: [[-4, -12], [0, -8], [5, -15]],
		strokeColor: "#bd5800",
		strokeWidth: 3,
	});
	
	
	apple.translate(x*50 + 5 + 25, y*50 +5 + 25);
	stem.translate(x*50 + 5 + 25, y*50 +5 + 25);
	
	winPlace = new Point(x*50 + 5 + 25, y*50 +5 + 25);
}

function DrawDeadlyCellAt (x,y){
	var deadlyCell = new Path.Rectangle({
		point: [-23,-23],
		size: [46, 46],
		fillColor: 'red'
	});
	
	deadlyCell.translate(x*50 + 5 + 25, y*50 +5 + 25);
	
	losePlaces.push(new Point(x*50 + 5 + 25, y*50 +5 + 25));
}

// use orientation=0 for bridge going from left-right and 1 for top-bottom
function DrawBridgeAt (x, y, orientation){
	var deadlyCell = new Path.Rectangle({
		point: [-23,-23],
		size: [46, 46],
		fillColor: 'red'
	});
	
	deadlyCell.translate(x*50 + 5 + 25, y*50 +5 + 25);
	
	var xsize = 46 + 20;
	var ysize = 46 + 20;
	var xoffset = 0;
	var yoffset = 0;
	
	if(orientation == 0){
		ysize = 20;
		yoffset = 13;
		xoffset = -10;
	}else{
		xsize = 20;
		xoffset = 13;
		yoffset = -10;
	}
	
	var bridge = new Path.Rectangle({
		point: [-23 + xoffset,-23 + yoffset],
		size: [xsize, ysize],
		fillColor: '#ab5f37'
	});
	
	bridge.translate(x*50 + 5 + 25, y*50 +5 + 25);
}



console.log("level setup complete!")