(function () {
  var CONTACT = "alyssa.dehart@utahadvocacycoalition.org";
  var toggle = document.getElementById("nav-toggle");
  var menu = document.getElementById("nav-menu");
  if (toggle && menu) {
    toggle.addEventListener("click", function () {
      var open = menu.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.textContent = open ? "Close" : "Menu";
    });
    menu.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        menu.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.textContent = "Menu";
      });
    });
  }

  /* Join the list: PLACEHOLDER delivery via mailto until an email platform is connected */
  document.querySelectorAll("form.join-form").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var name = (form.querySelector('[name="name"]') || {}).value || "";
      var email = (form.querySelector('[name="email"]') || {}).value || "";
      var roleEl = form.querySelector('[name="role"]:checked');
      var role = roleEl ? roleEl.value : "";
      var body = "Please add me to the IHLab list.\n\nName: " + name.trim() + "\nEmail: " + email.trim() + "\nI'm a: " + role + "\nSigned up from: " + location.pathname;
      window.location.href = "mailto:" + CONTACT + "?subject=" + encodeURIComponent("Join the IHLab list (" + (role || "role not set") + ")") + "&body=" + encodeURIComponent(body);
      var status = form.querySelector(".form-status");
      if (status) status.textContent = "Your email app should open with your details filled in. Press send to finish joining.";
    });
  });

  /* Sticky mobile CTA appears after the hero scrolls away and steps aside over the footer */
  var bar = document.querySelector(".mobile-cta");
  var hero = document.querySelector(".hero, .page-hero");
  var foot = document.querySelector(".footer");
  if (bar && hero && "IntersectionObserver" in window) {
    document.body.classList.add("has-mobile-cta");
    var heroVisible = true, footVisible = false;
    var update = function () { bar.classList.toggle("show", !heroVisible && !footVisible); };
    new IntersectionObserver(function (entries) { heroVisible = entries[0].isIntersecting; update(); }).observe(hero);
    if (foot) new IntersectionObserver(function (entries) { footVisible = entries[0].isIntersecting; update(); }).observe(foot);
  }

  var y = document.getElementById("year");
  if (y) y.textContent = String(new Date().getFullYear());
})();
