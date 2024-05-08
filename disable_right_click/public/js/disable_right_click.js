document.addEventListener("contextmenu", function (event) {
  event.preventDefault();
});

// Block opening of inspect element on Windows
document.addEventListener("keydown", function (event) {
  // Check for F12 key or Ctrl+Shift+I (Inspect Element shortcut)
  if (
    event.key === "F12" ||
    (event.ctrlKey && event.shiftKey && event.key === "I")
  ) {
    event.preventDefault();
  }
});

// Block opening of inspect element on Mac
document.addEventListener("keydown", function (event) {
  // Check for Cmd+Option+I (Inspect Element shortcut)
  if (event.metaKey && event.altKey && event.key === "I") {
    event.preventDefault();
  }
});
