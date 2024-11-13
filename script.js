const status = document.getElementById('status');
const buttonsContainer = document.getElementById('buttons');
const axesContainer = document.getElementById('axes');
let gamepadIndex = null;

// Event listener for connecting the gamepad
window.addEventListener("gamepadconnected", (event) => {
  status.innerText = `Gamepad connected: ${event.gamepad.id}`;
  gamepadIndex = event.gamepad.index;
  createGamepadDisplay(event.gamepad);
  requestAnimationFrame(updateGamepadStatus);
});

// Event listener for disconnecting the gamepad
window.addEventListener("gamepaddisconnected", () => {
  status.innerText = "No gamepad connected.";
  buttonsContainer.innerHTML = '';
  axesContainer.innerHTML = '';
  gamepadIndex = null;
});

// Create the display for buttons and axes
function createGamepadDisplay(gamepad) {
  buttonsContainer.innerHTML = '';
  axesContainer.innerHTML = '';

  // Create button elements
  gamepad.buttons.forEach((_, i) => {
    const buttonDiv = document.createElement('div');
    buttonDiv.innerText = `Button ${i}`;
    buttonDiv.id = `button-${i}`;
    buttonsContainer.appendChild(buttonDiv);
  });

  // Create axis elements
  gamepad.axes.forEach((_, i) => {
    const axisDiv = document.createElement('div');
    axisDiv.innerText = `Axis ${i}: 0.00`;
    axisDiv.id = `axis-${i}`;
    axesContainer.appendChild(axisDiv);
  });
}

// Poll the gamepad state and update the display
function updateGamepadStatus() {
  // Ensure a gamepad is connected
  const gamepad = navigator.getGamepads()[gamepadIndex];
  if (!gamepad) return;

  // Update button states
  gamepad.buttons.forEach((button, i) => {
    const buttonDiv = document.getElementById(`button-${i}`);
    if (buttonDiv) {
      buttonDiv.classList.toggle('pressed', button.pressed);
    }
  });

  // Update axis states
  gamepad.axes.forEach((value, i) => {
    const axisDiv = document.getElementById(`axis-${i}`);
    if (axisDiv) {
      axisDiv.innerText = `Axis ${i}: ${value.toFixed(2)}`;
    }
  });

  // Continuously request the next frame for smooth updates
  requestAnimationFrame(updateGamepadStatus);
}
