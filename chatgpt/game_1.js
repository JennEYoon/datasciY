// Define canvas and context variables
var canvas = document.getElementById("gameCanvas");
var ctx = canvas.getContext("2d");

// Set canvas size to popular iPad screen resolution size
canvas.width = 1024;
canvas.height = 768;



// Define game loop function
function gameLoop() {
  // Clear canvas
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Draw sky blue background
  ctx.fillStyle = "skyblue";
  ctx.fillRect(0, 0, canvas.width, canvas.height * 0.9);

  // Draw solid green background - not used.
  // ctx.fillStyle = "green";
  // ctx.fillRect(0, 0, canvas.width, canvas.height * 0.9);

  // Draw solid green horizontal line
  ctx.beginPath();
  ctx.strokeStyle = "green";
  ctx.lineWidth = 6;
  ctx.moveTo(0, canvas.height * 0.9);
  ctx.lineTo(canvas.width, canvas.height * 0.9);
  ctx.stroke();

  // Draw game objects

  // Update game state

  // Call game loop again
  requestAnimationFrame(gameLoop);
}

// Call game loop to start the game
requestAnimationFrame(gameLoop);

//----