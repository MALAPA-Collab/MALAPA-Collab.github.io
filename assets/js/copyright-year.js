// Keep the footer copyright year current. Runs on every page view,
// including instant-navigation page changes (Material's document$).
document$.subscribe(function () {
  document.querySelectorAll(".copyright-year").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
});
