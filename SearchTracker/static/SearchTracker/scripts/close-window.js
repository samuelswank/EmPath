window.addEventListener("beforeunload", () => {
  //   fetch("{% url 'SearchTracker:close' %}", { keepalive: true });
  navigator.sendBeacon("{% url 'SearchTracker:close' %}", "");
});
