const INACTIVITY_LIMIT = 60 * 60 * 1000; // 1 Hour
const HEARTBEAT_INTERVAL = 120000; // 10 seconds

let inactivityTimer = null;
let heartbeatIntervalId = null;

function sendHeartbeat() {
  fetch(window.HEARTBEAT_URL, {
    method: "POST",
    headers: {
      "X-Requested-With": "XMLHttpRequest",
    },
  }).catch((err) => {
    console.log("Heartbeat failed, shutting down...", err);
  });
}

function resetInactivityTimer() {
  if (inactivityTimer) clearTimeout(inactivityTimer);
  inactivityTimer = setTimeout(() => {
    if (heartbeatIntervalId) {
      clearInterval(heartbeatIntervalId);
      heartbeatIntervalId = null;
    }
  }, INACTIVITY_LIMIT);
}

function startHeartbeats() {
  if (heartbeatIntervalId) return;
  sendHeartbeat();
  heartbeatIntervalId = setInterval(sendHeartbeat, HEARTBEAT_INTERVAL);
}

const activityEvents = [
  "mousemove",
  "click",
  "keydown",
  "scroll",
  "touchstart",
];

activityEvents.forEach((event) => {
  resetInactivityTimer();
  startHeartbeats();
});

resetInactivityTimer();
startHeartbeats();

const heartbeatInterval = setInterval(sendHeartbeat, 10000);
