// Define canvas and context variables
var canvas = document.getElementById("gameCanvas");
var ctx = canvas.getContext("2d");

// Set canvas size to popular iPad screen resolution size
canvas.width = 1024;
canvas.height = 768;

// Define game objects ### new ###
var box1 = {
  x: 0,
  y: canvas.height * 0.9 - 20, // Same height as green horizontal line
  width: 10,
  height: 20,
  color: "pink"
};

// Define game loop function
function gameLoop() {
  // Clear canvas
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Draw sky blue background
  ctx.fillStyle = "skyblue";
  ctx.fillRect(0, 0, canvas.width, canvas.height * 0.9);

  // Draw solid green horizontal line
  ctx.beginPath();
  ctx.strokeStyle = "green";
  ctx.lineWidth = 6;
  ctx.moveTo(0, canvas.height * 0.9);
  ctx.lineTo(canvas.width, canvas.height * 0.9);
  ctx.stroke();


  // Move box1 when right or left arrow key is pressed
  if (rightPressed) {
    if (box1.x + box1.width < canvas.width) { // Check if box1 is within canvas bounds
      box1.x += 4;
    } else {
      box1.x = canvas.width - box1.width; // Set box1 position to the right edge of canvas
    }
  }
      
  if (leftPressed) {
    if (box1.x > 0) { // Check if box1 is within canvas bounds
      box1.x -= 4;
    } else {
      box1.x = 0; // Set box1 position to the left edge of canvas
    }
  }

  // Draw box1 object ### new ###
  ctx.fillStyle = box1.color;
  ctx.fillRect(box1.x, box1.y, box1.width, box1.height);

  // Call game loop again
  requestAnimationFrame(gameLoop);
}

// event listeners

// Define keyboard event listeners  ### new ###
var rightPressed = false;
var leftPressed = false;
document.addEventListener("keydown", keyDownHandler, false);
document.addEventListener("keyup", keyUpHandler, false);

// add left key down
function keyDownHandler(event) {
  if (event.keyCode === 39) {
    rightPressed = true;
  } else if (event.keyCode === 37) {
    leftPressed = true;  
  }
}

// add left key up
function keyUpHandler(event) {
  if (event.keyCode === 39) {
    rightPressed = false;
  } else if (event.keyCode === 37) {
    leftPressed = false;  
  }
}

// Call game loop to start the game
requestAnimationFrame(gameLoop);
