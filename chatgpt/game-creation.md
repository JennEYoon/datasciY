# AI assisted game development.  
I am testing out using AI to write a simple game using only javascript, html, and css.  
It will be a platform game with interactive graphical elements and drawing to canvas.   

engine: ChatGPT4-0314 Version  
chat.openai.com/chat  
https://chat.openai.com/chat/f3f62545-553d-44a1-85a5-68b3df04502d  
Date session 1:  4/2/2023.  


Session 1)  
Prompt: 
I want to create an interactive platform game using only html, css, and javascript. Please write introductory code for me and what files to paste it to.

ChatGPT: 
To create an interactive platform game using HTML, CSS, and JavaScript, you can start by creating a basic HTML file with the necessary structure and adding CSS and JavaScript files to it. Here's some introductory code to get you started:  

index.html:  
<file>
styles.css:  
<file>
game.js:  
<file>

This code sets up the basic structure of an HTML file with a canvas element and includes a CSS file to add a border to the canvas. The JavaScript file **defines a game loop function** and starts the game by calling the game loop using the **requestAnimationFrame** method.

To get started with your platform game, you can add additional JavaScript code to create and control game objects, such as the player, enemies, and obstacles. You can also add **_event listeners_** to handle <em>user input and collisions</em> between objects.

Note that while HTML, CSS, and JavaScript can be used to create simple games, for more complex games, you may want to consider using a game engine or library like Phaser or **Unity**.


Prompt: 
write code to set gameCavas size to popular ipad screen resolution size

ChatGPT:
Sure! One popular iPad screen resolution size is 1024 x 768 pixels. To set the gameCanvas element to this size, you can add some additional code to the HTML file:

```
// Define canvas and context variables
var canvas = document.getElementById("gameCanvas");
var ctx = canvas.getContext("2d");

// Define game loop function
function gameLoop() {
  // Clear canvas
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Draw game objects

  // Update game state

  // Call game loop again
  requestAnimationFrame(gameLoop);
}

// Call game loop to start the game
requestAnimationFrame(gameLoop);
```
  
Prompt: 
Adjust the above code to paste into game.js file and tell me where in the file to past it.

```
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

  // Draw game objects

  // Update game state

  // Call game loop again
  requestAnimationFrame(gameLoop);
}

// Call game loop to start the game
requestAnimationFrame(gameLoop);
```
2 / 2

ChatGPT: 
Sure! You can adjust the game.js file to set the size of the gameCanvas element using JavaScript. Here's an example of how you can modify the code:

In this modified code, the canvas size is set to 1024 x 768 pixels using the canvas.width and canvas.height properties before the gameLoop function is defined. This code should be placed at the beginning of the game.js file, before any other game logic that interacts with the canvas.


Prompt:
How do I change canvas border width to 6 pixels?

ChatGPT:
To change the gameCanvas border width to 6 pixels, you can modify the styles.css file to add a border style for the canvas element. Here's an example of how you can do it:

css
Copy code
#gameCanvas {
  border: 6px solid black;
}

In this CSS code, we're setting the border property for the gameCanvas element to a 6-pixel-wide solid black border. You can adjust the pixel size and border style to match the desired look for your game canvas.

Prompt: 
Draw a solid green horizontal line 6px thick 90% from canvas top and full screen wide.  

ChatGPT: 
To draw a solid green horizontal line 6 pixels thick, 90% from the top of the canvas and full screen wide, you can add some additional code to the game.js file. Here's an example of how you can do it:

javascript
```
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

  // Draw solid green horizontal line
  ctx.beginPath();
  ctx.strokeStyle = "green";
  ctx.lineWidth = 6;
  ctx.moveTo(0, canvas.height * 0.9);
  ctx.lineTo(canvas.width, canvas.height * 0.9);
  ctx.stroke();

  // Update game state

  // Call game loop again
  requestAnimationFrame(gameLoop);
}

// Call game loop to start the game
requestAnimationFrame(gameLoop);
```
  
In this code, we're adding some new code to the gameLoop function to draw a solid green horizontal line 6 pixels thick, 90% from the top of the canvas and full screen wide. We're doing this using the beginPath(), strokeStyle, lineWidth, moveTo(), lineTo(), and stroke() methods of the canvas context.

The moveTo() method sets the starting point for the line to the left edge of the canvas and 90% down from the top, and the lineTo() method draws the line to the right edge of the canvas at the same y-coordinate. Finally, we call the stroke() method to actually draw the line on the canvas.

Prompt:
Where should the above code go if it is for game background?

ChatGPT:
If you want to draw a solid green horizontal line 6 pixels thick, 90% from the top of the canvas and full screen wide to serve as the background for your game, you can modify the game.js file to include this code in the gameLoop() function before any other game objects are drawn. Here's an example:

...
// Define game loop function
function gameLoop() {
  // Clear canvas
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Draw solid green background
  ctx.fillStyle = "green";
  ctx.fillRect(0, 0, canvas.width, canvas.height * 0.9);

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


In this code, we're adding two new lines to draw a solid green background before drawing any game objects. We're using the fillStyle and fillRect() methods to fill the canvas with a solid green color from the top to 90% down. We're then drawing the solid green horizontal line as described before.

By adding the background and the line at the beginning of the gameLoop() function, we ensure that they are drawn first and appear behind any game objects that are drawn later.

Prompt:
Change above fill color from green to sky blue

ChatGPT:
To change the fill color of the background from green to sky blue, you can modify the game.js file to set the fillStyle to "skyblue" instead of "green" in the gameLoop() function. Here's an updated example:

 ```
 // Draw sky blue background
  ctx.fillStyle = "skyblue";
  ctx.fillRect(0, 0, canvas.width, canvas.height * 0.9);
  ```
  
In this code, we're simply changing the fillStyle to "skyblue" to set the background fill color to sky blue. This will be reflected in the call to fillRect() that follows.


Prompt: 
Draw a moveable box1 object, a rectangle 20 pixels high by 10 pixels wide in pink color.  This object starts in left-edge of screen border and same height as green horizontal line.  It moves right to right-edge border when keyboard right arrow is pressed. 

ChatGPT: 
To draw a moveable box1 object, a rectangle 20 pixels high by 10 pixels wide in pink color that starts at the left-edge of the screen border and moves to the right-edge border when the right arrow key is pressed, you can modify the game.js file. Here's an example:

```
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

  // Move box1 when right arrow key is pressed
  if (rightPressed) {
    box1.x += 5;
  }

  // Draw box1 object
  ctx.fillStyle = box1.color;
  ctx.fillRect(box1.x, box1.y, box1.width, box1.height);

  // Call game loop again
  requestAnimationFrame(gameLoop);
}

// Define keyboard event listeners
var rightPressed = false;
document.addEventListener("keydown", keyDownHandler, false);
document.addEventListener("keyup", keyUpHandler, false);

function keyDownHandler(event) {
  if (event.keyCode === 39) {
    rightPressed = true;
  }
}

function keyUpHandler(event) {
  if (event.keyCode === 39) {
    rightPressed = false;
  }
}

// Call game loop to start the game
requestAnimationFrame(gameLoop);
```

In this code, we've defined a new game object box1 that has a starting position of x: 0 (left-edge of screen border) and y: canvas.height * 0.9 - 20 (same height as the green horizontal line). It also has a width of 10 pixels and a height of 20 pixels, and a pink color.

We've also added a new variable rightPressed that keeps track of whether the right arrow key is currently being pressed or not. We've defined two event listeners for the keyboard events "keydown" and "keyup" that set or unset rightPressed based on whether the right arrow key is pressed or released.

In the gameLoop() function, we're checking if rightPressed is true, and if so, we're incrementing box1.x by 5 pixels per frame, which causes it to move to the right. We're then drawing box1 using the fillStyle and fillRect() methods.

You can adjust the dimensions and positioning of box1 to fit your game's needs.

Prompt: 
Add collision detector for box1 object.  It cannot move beyond right horizontal border edge during key press event.

ChatGPT: 
To add collision detection for the box1 object so that it cannot move beyond the right horizontal border edge during the key press event, you can modify the game.js file. Here's an example:

```
  // Move box1 when right arrow key is pressed
  if (rightPressed) {
    if (box1.x + box1.width < canvas.width) { // Check if box1 is within canvas bounds
      box1.x += 5;
    } else {
      box1.x = canvas.width - box1.width; // Set box1 position to the right edge of canvas
    }
  }

  // Draw box1 object
  ctx.fillStyle = box1.color;
  ctx.fillRect(box1.x, box1.y, box1.width, box1.height);

```

In this code, we've added a conditional statement inside the if (rightPressed) block that checks whether the box1 object's position, box1.x + box1.width, is less than the canvas width. If it is, we increment box1.x by 5 pixels per frame as before. Otherwise, we set box1.x to the right edge of the canvas, canvas.width - box1.width, to prevent box1 from moving beyond the right horizontal border edge.

You can adjust the collision detection code to fit your game's needs. For example, you can add similar conditional statements for detecting collisions with the left, top, or bottom borders of the canvas.


Prompt:
Add box1 left move when left arrow key is pressed

ChatGPT:
To add a left movement for the box1 object when the left arrow key is pressed, you can modify the game.js file again. Here's an example:

```
  // Move box1 when right or left arrow key is pressed
  if (rightPressed) {
    if (box1.x + box1.width < canvas.width) { // Check if box1 is within canvas bounds
      box1.x += 5;
    } else {
      box1.x = canvas.width - box1.width; // Set box1 position to the right edge of canvas
    }
  }

  if (leftPressed) {
    if (box1.x > 0) { // Check if box1 is within canvas bounds
      box1.x -= 5;
    } else {
      box1.x = 0; // Set box1 position to the left edge of canvas
    }
  }

  // Draw box1 object
  ctx.fillStyle = box1.color;
  ctx.fillRect(box1.x, box1.y, box1.width, box1.height);
```

In this code, we've added a similar conditional statement inside the if (leftPressed) block that checks whether the box1 object's position, box1.x, is greater than 0. If it is, we decrement box1.x by 5 pixels per frame as before. Otherwise, we set box1.x to the left edge of the canvas, 0, to prevent box1 from moving beyond the left horizontal border edge.

We've also added event listeners for the left arrow key, and modified the keyDownHandler and keyUpHandler functions to set and unset the leftPressed variable accordingly.

```
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
      box1.x += 5;
    } else {
      box1.x = canvas.width - box1.width; // Set box1 position to the right edge of canvas
    }
  }

  if (leftPressed) {
    if (box1.x > 0) { // Check if box1 is within canvas bounds
      box1.x -= 5;
    } else {
      box1.x = 0; // Set box1 position to the left edge of canvas
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
document.addEventListener("keydown", keyDownHandler, false);
document.addEventListener("keyup", keyUpHandler, false);

function keyDownHandler(event) {
  if (event.keyCode === 39) {
    rightPressed = true;
  } else if (event.keyCode === 37) {
    leftPressed = true;
  }
}

function keyUpHandler(event) {
  if (event.keyCode === 39) {
    rightPressed = false;
  } else if (event.keyCode === 37) {
    leftPressed = false;
  }
}

// Call game loop to start the game
requestAnimationFrame(gameLoop);
```
  
Prompt: 
Add jump event tied to enter key. box1 should move up by 20 pixels and "continue in current direction by 10 pixels". May have been confused by this.  

2 / 2
ChatGPT:
To add a jump event tied to the enter key, you can modify the game.js file once again. Here's an example:

> code in game.js  
  box1 jumps up, but stays there. Does not come back down.  
  Down event never happens.  

Prompt:
modify jump event to move box1 up and then down

ChatGPT
In the previous solution, the box1 object was moving up during the first half of the jump and then moving down during the second half of the jump. If you want to modify the jump event to move the box1 object up and then down, you can update the code inside the if (enterPressed) block to something like this:

```javascript

if (enterPressed) {
  if (!box1.isJumping) { // Only jump if not already jumping
    box1.isJumping = true;
    box1.jumpCounter = 0;
    box1.startY = box1.y; // Store box1's starting position for the jump
  }
}

if (box1.isJumping) {
  var jumpHeight = 20; // The height of the jump in pixels
  var jumpDuration = 20; // The duration of the jump in frames
  var jumpProgress = box1.jumpCounter / jumpDuration; // The progress of the jump from 0 to 1
  var jumpDelta = (Math.sin(jumpProgress * Math.PI) * jumpHeight); // The distance to move during the jump

  if (box1.jumpCounter < jumpDuration / 2) { // During the first half of the jump, move up
    box1.y = box1.startY - jumpDelta;
    // increase box1.x by sine wave. Need to know direcion it ismfacing, momentum.                          
  } else if (box1.jumpCounter < jumpDuration) { // During the second half of the jump, move down
    box1.y = box1.startY - (jumpHeight - jumpDelta);
    // increase box1.x second half.  
  } else { // After the jump, stop jumping
    box1.isJumping = false;
  }

  box1.jumpCounter++; // Increment the jump counter
}
```

This code uses a sine wave function to calculate the vertical position of the box1 object during the jump, which creates a smooth up-and-down motion. The jumpHeight variable determines how high the box1 object should jump, and the jumpDuration variable determines how long the jump should take (in frames). The jumpProgress variable calculates the progress of the jump from 0 to 1, and the jumpDelta variable calculates the distance the box1 object should move vertically during the jump. The if statements inside the box1.isJumping block use these values to move the box1 object up and down during the jump.
