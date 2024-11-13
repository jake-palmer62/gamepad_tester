let gamepadIndex = null;

function updateGamepadStatus() {
  const gamepad = navigator.getGamepads()[gamepadIndex];

  if (gamepad) {
    // Update gamepad status
    document.getElementById('gamepadStatus').innerText = `Gamepad ${gamepad.index + 1} connected`;
    
    // Update buttons
    let buttonHTML = '';
    gamepad.buttons.forEach((button, index) => {
      buttonHTML += `<div>Button ${index}: ${button.pressed ? 'Pressed' : 'Released'}</div>`;
    });
    document.getElementById('buttons').innerHTML = buttonHTML;

    // Update axes
    let axisHTML = '';
    gamepad.axes.forEach((axis, index) => {
      axisHTML += `<div>Axis ${index}: ${axis.toFixed(2)}</div>`;
    });
    document.getElementById('axes').innerHTML = axisHTML;
  }
}

function detectGamepad() {
  const gamepads = navigator.getGamepads();
  
  for (let i = 0; i < gamepads.length; i++) {
    if (gamepads[i]) {
      gamepadIndex = i;
      document.getElementById('gamepadStatus').innerText = `Gamepad ${i + 1} connected`;
      return;
    }
  }
  
  document.getElementById('gamepadStatus').innerText = 'No gamepad connected';
}

function gamepadLoop() {
  detectGamepad();

  if (gamepadIndex !== null) {
    updateGamepadStatus();
  }

  requestAnimationFrame(gamepadLoop);
}

// Start the loop
gamepadLoop();
