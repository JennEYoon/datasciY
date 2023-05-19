// Define canvas and context variables
var canvas = document.getElementById("gameCanvas");
var ctx = canvas.getContext("2d");

// Set canvas size to popular iPad screen resolution size
canvas.width = 1024;
canvas.height = 768;

// Define game objects
var box1 = {
  x: 0,
  y: canvas.height * 0.9 - 20, // Same height as green horizontal line
  width: 10,
  height: 20,
  color: "pink",
  isJumping: false,
  jumpCounter: 0,
  direction: 1
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
      box1.x += 5;
      box1.direction = 1;
    } else {
      box1.x = canvas.width - box1.width; // Set box1 position to the right edge of canvas
    }
  }

  if (leftPressed) {
    if (box1.x > 0) { // Check if box1 is within canvas bounds
      box1.x -= 5;
      box1.direction = -1;  
    } else {
      box1.x = 0; // Set box1 position to the left edge of canvas
    }
  }

  // Move box1 up by 20 pixels and continue in current direction by 10 pixels when enter key is pressed
  if (enterPressed) {
    if (!box1.isJumping) { // Only jump if not already jumping
      box1.isJumping = true;
      box1.jumpCounter = 0;
    }
  }

    // ### sub w Math.sin, move x-axis too during jump. Also need facing direction. ### 
    // how is jumpCounter looped?  
    if (box1.isJumping) { // error missed 2 indent spaces bol.  
      box1.y -= 5; 
      box1.x += 2 * box1.direction;
    
      // Move box1 up by 5 pixels per frame during the first half of the jump
      // box1.x = box1.jumpCounter * box1.direction;
    
    if (box1.jumpCounter >= 20) {
      // After 20 frames, move box1 down by 5 pixels per frame during the second half of the jump
      box1.y += 10;  // returns to bottom, but faster speed.  
      box1.x += 2 * box1.direction;
    }
       // where to put increment counter?  
       box1.jumpCounter++;  
    if (box1.jumpCounter === 40) { // After 40 frames, finish the jump
      box1.isJumping = false;
    }
  }

  // Draw box1 object
  ctx.fillStyle = box1.color;
  ctx.fillRect(box1.x, box1.y, box1.width, box1.height);

  // Call game loop again
  requestAnimationFrame(gameLoop);
}

// Define keyboard event listeners
var rightPressed = false;
var leftPressed = false;
var enterPressed = false;
document.addEventListener("keydown", keyDownHandler, false);
document.addEventListener("keyup", keyUpHandler, false);

function keyDownHandler(event) {
  if (event.keyCode === 39) {
    rightPressed = true;
  } else if (event.keyCode === 37) {
    leftPressed = true;
  } else if (event.keyCode === 13) {
    enterPressed = true;
  }
}

function keyUpHandler(event) {
  if (event.keyCode === 39) {
    rightPressed = false;
  } else if (event.keyCode === 37) {
    leftPressed = false;  
  } else if (event.keyCode === 13) {
    enterPressed = false;
  }
}

// Call game loop to start the game
requestAnimationFrame(gameLoop);
