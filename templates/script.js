const lampStatus = document.getElementById("lamp-status");
const lampText = document.getElementById("lamp-text");
const lampButton = document.getElementById("lamp-button");

const sirenStatus = document.getElementById("siren-status");
const sirenText = document.getElementById("siren-text");
const sirenButton = document.getElementById("siren-button");

let isLampOn = false;
let isSirenOn = false;

lampButton.addEventListener("click", () => {
  isLampOn = !isLampOn;
  updateLampStatus();
});

sirenButton.addEventListener("click", () => {
  isSirenOn = !isSirenOn;
  updateSirenStatus();
});

function updateLampStatus() {
  if (isLampOn) {
    lampStatus.classList.add("lamp-on");
    lampStatus.classList.remove("lamp-off");
    lampText.textContent = "On";
  } else {
    lampStatus.classList.add("lamp-off");
    lampStatus.classList.remove("lamp-on");
    lampText.textContent = "Off";
  }
}

function updateSirenStatus() {
  if (isSirenOn) {
    sirenStatus.classList.add("siren-on");
    sirenStatus.classList.remove("siren-off");
    sirenText.textContent = "On";
  } else {
    sirenStatus.classList.add("siren-off");
    sirenStatus.classList.remove("siren-on");
    sirenText.textContent = "Off";
  }
}

const led1StatusElement = document.getElementById("led1-status");
const led2StatusElement = document.getElementById("led2-status");
const led1Button = document.getElementById("led1-button");
const led2Button = document.getElementById("led2-button");

let isLed1On = false;
let isLed2On = false;

led1Button.addEventListener("click", () => {
  isLed1On = !isLed1On;
  updateLed1Status();
});

led2Button.addEventListener("click", () => {
  isLed2On = !isLed2On;
  updateLed2Status();
});

function updateLed1Status() {
  if (isLed1On) {
    led1StatusElement.style.backgroundColor = "green"; // Trạng thái bật
  } else {
    led1StatusElement.style.backgroundColor = "#c8c8c8"; // Trạng thái tắt
  }
}

function updateLed2Status() {
  if (isLed2On) {
    led2StatusElement.style.backgroundColor = "green"; // Trạng thái bật
  } else {
    led2StatusElement.style.backgroundColor = "#c8c8c8"; // Trạng thái tắt
  }
}

// Simulate sensor data updates
setInterval(() => {
  const randomTemperatureValue = Math.floor(Math.random() * 50) + 10;
  const randomHumidityValue = Math.floor(Math.random() * 50) + 40;
  const currentTime = new Date();
  const timeString = `${currentTime.getHours()}:${currentTime.getMinutes()}:${currentTime.getSeconds()}`;
temperatureElement.textContent = `${randomTemperatureValue}°C`;
  humidityElement.textContent = `${randomHumidityValue}%`;
  currentTimeElement.textContent = timeString;
}, 10000); // Simulate data updates every 10 seconds


// Simulate data updates
setInterval(() => {
  const randomTemperature = Math.floor(Math.random() * 30 + 20);
  const randomHumidity = Math.floor(Math.random() * 50 + 30);
  const now = new Date();
  const currentTime = `${now.getHours()}:${now.getMinutes()}:${now.getSeconds()}`;
  temperatureElement.textContent = `${randomTemperature} °C`;
  humidityElement.textContent = `${randomHumidity}%`;
  currentTimeElement.textContent = currentTime;
}, 5000); // Simulate data updates every 5 seconds

const lightSensorElement = document.getElementById("light-sensor");
const distanceSensorElement = document.getElementById("distance-sensor");
const vibrationStatusElement = document.getElementById("vibration-status");
const relayStatusElement = document.getElementById("relay-status");
const vibrationButton = document.getElementById("vibration-button");
const relayButton = document.getElementById("relay-button");

let isVibrationOn = false;
let isRelayOn = false;

vibrationButton.addEventListener("click", () => {
  isVibrationOn = !isVibrationOn;
  updateVibrationStatus();
});

relayButton.addEventListener("click", () => {
  isRelayOn = !isRelayOn;
  updateRelayStatus();
});

function updateVibrationStatus() {
  if (isVibrationOn) {
    vibrationStatusElement.style.backgroundColor = "green"; // Trạng thái rung
  } else {
    vibrationStatusElement.style.backgroundColor = "#c8c8c8"; // Trạng thái tắt
  }
}

function updateRelayStatus() {
  if (isRelayOn) {
    relayStatusElement.style.backgroundColor = "green"; // Trạng thái bật
  } else {
    relayStatusElement.style.backgroundColor = "#c8c8c8"; // Trạng thái tắt
  }
}

// Simulate sensor data updates
setInterval(() => {
  const randomLightSensorValue = Math.floor(Math.random() * 500) + 1;
  const randomDistanceSensorValue = Math.floor(Math.random() * 100) + 1;
  lightSensorElement.textContent = `${randomLightSensorValue} lux`;
  distanceSensorElement.textContent = `${randomDistanceSensorValue} cm`;
}, 5000); // Simulate data updates every 5 seconds


