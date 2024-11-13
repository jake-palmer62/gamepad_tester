let gamepadIndex = null;
const status = document.getElementById('status');
const axesDebug = document.getElementById('axes-debug');
const buttonsDebug = document.getElementById('buttons-debug');

const BUTTON_MAPPING = {
    0: 'button-a',
    1: 'button-b',
    2: 'button-x',
    3: 'button-y',
    4: 'left-bumper',
    5: 'right-bumper',
    8: 'select',
    9: 'start',
    16: 'home',
    12: 'dpad-up',
    13: 'dpad-down',
    14: 'dpad-left',
    15: 'dpad-right'
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
    }
});

function updateStatus() {
    if (gamepadIndex !== null) {
        const gamepad = navigator.getGamepads()[gamepadIndex];
        if (!gamepad) return;

        // Update stick
        updateStick('left-stick', gamepad.axes[0], gamepad.axes[1]);

        // Update all buttons
        gamepad.buttons.forEach((button, index) => {
            if (BUTTON_MAPPING[index]) {
                updateButton(BUTTON_MAPPING[index], button.pressed);
            }
        });

        // Update debug info
        updateDebugDisplay(gamepad);

        requestAnimationFrame(updateStatus);
    }
}

function updateStick(elementId, x, y) {
    const dot = document.querySelector(`#${elementId} .stick-dot`);
    const maxDistance = 15;
    dot.style.transform = `translate(calc(-50% + ${x * maxDistance}px), calc(-50% + ${y * maxDistance}px))`;
}

function updateButton(elementId, pressed) {
    const element = document.getElementById(elementId);
    if (element) {
        element.classList.toggle('pressed', pressed);
    }
}

function updateDebugDisplay(gamepad) {
    // Update axes debug info
    let axesHtml = '<h3>Axes</h3>';
    gamepad.axes.forEach((value, i) => {
        axesHtml += `Axis ${i}: ${value.toFixed(4)}<br>`;
    });
    axesDebug.innerHTML = axesHtml;

    // Update buttons debug info
    let buttonsHtml = '<h3>Buttons</h3>';
    gamepad.buttons.forEach((button, i) => {
        buttonsHtml += `Button ${i}: ${button.pressed ? 'Pressed' : 'Released'} (${button.value.toFixed(2)})<br>`;
    });
    buttonsDebug.innerHTML = buttonsHtml;
}