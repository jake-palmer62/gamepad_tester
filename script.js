let gamepadIndex = null;
const status = document.getElementById("status");
const axesDebug = document.getElementById("axes-debug");
const buttonsDebug = document.getElementById("buttons-debug");

const BUTTON_MAPPING = {
  0: "button-a",
  1: "button-b",
  2: "button-x",
  3: "button-y",
  4: "left-bumper",
  5: "right-bumper",
  6: "left-trigger",
  7: "right-trigger",
  8: "button-back",
  9: "button-start",
  10: "left-stick", // L3
  11: "right-stick", // R3
  12: "d-pad-up",
  13: "d-pad-down",
  14: "d-pad-left",
  15: "d-pad-right",
  16: "button-home",
};

window.addEventListener("gamepadconnected", (event) => {
  gamepadIndex = event.gamepad.index;
  status.textContent = `Connected: ${event.gamepad.id}`;
  requestAnimationFrame(updateStatus);
});

window.addEventListener("gamepaddisconnected", (event) => {
  if (gamepadIndex === event.gamepad.index) {
    gamepadIndex = null;
    status.textContent = "No gamepad connected";
    clearActiveStates();
  }
});

function clearActiveStates() {
  // Clear button states
  Object.values(BUTTON_MAPPING).forEach((elementId) => {
    const element = document.getElementById(elementId);
    if (element) {
      element.classList.remove("pressed");
    }
  });

  // Reset stick positions
  ["left-stick", "right-stick"].forEach((stickId) => {
    const stick = document.querySelector(`#${stickId} .stick-dot`);
    if (stick) {
      stick.style.transform = "translate(-50%, -50%)";
    }
  });
}

function updateStatus() {
  if (gamepadIndex !== null) {
    const gamepad = navigator.getGamepads()[gamepadIndex];
    if (!gamepad) return;

    // Update sticks
    updateStick(
      "left-stick",
      gamepad.axes[0],
      gamepad.axes[1],
      gamepad.buttons[10]?.pressed
    );
    updateStick(
      "right-stick",
      gamepad.axes[2],
      gamepad.axes[3],
      gamepad.buttons[11]?.pressed
    );

    // Update buttons
    gamepad.buttons.forEach((button, index) => {
      if (BUTTON_MAPPING[index]) {
        const element = document.getElementById(BUTTON_MAPPING[index]);
        if (element) {
          if (index === 6 || index === 7) {
            // Triggers
            element.classList.toggle("pressed", button.value > 0.5);
          } else {
            // Regular buttons
            element.classList.toggle("pressed", button.pressed);
          }
        }
      }
    });

    // Update debug display
    updateDebugDisplay(gamepad);

    requestAnimationFrame(updateStatus);
  }
}

function updateStick(elementId, x, y, pressed) {
  const stick = document.getElementById(elementId);
  const dot = stick?.querySelector(".stick-dot");

  if (stick && dot) {
    const maxDistance = 15;
    const translateX = -50 + x * maxDistance;
    const translateY = -50 + y * maxDistance;
    dot.style.transform = `translate(${translateX}%, ${translateY}%)`;
    stick.classList.toggle("pressed", pressed);
  }
}

function updateDebugDisplay(gamepad) {
  // Update axes debug info
  let axesHtml = "<h3>Axes</h3>";
  gamepad.axes.forEach((value, i) => {
    axesHtml += `Axis ${i}: ${value.toFixed(4)}<br>`;
  });
  axesDebug.innerHTML = axesHtml;

  // Update buttons debug info
  let buttonsHtml = "<h3>Buttons</h3>";
  gamepad.buttons.forEach((button, i) => {
    buttonsHtml += `Button ${i}: ${
      button.pressed ? "Pressed" : "Released"
    } (${button.value.toFixed(2)})<br>`;
  });
  buttonsDebug.innerHTML = buttonsHtml;
}
