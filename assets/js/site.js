/* Consolidated Engineers, rebuilt site behaviour */
(function () {
  "use strict";

  function bindHeader() {
    var header = document.querySelector("[data-header]");
    if (header) {
      var onScroll = function () {
        header.classList.toggle("is-stuck", window.scrollY > 8);
      };
      onScroll();
      window.addEventListener("scroll", onScroll, { passive: true });
    }

    var toggle = document.querySelector("[data-menu-toggle]");
    var nav = document.querySelector("[data-nav]");
    if (toggle && nav) {
      toggle.addEventListener("click", function () {
        var open = nav.classList.toggle("is-open");
        toggle.setAttribute("aria-expanded", open ? "true" : "false");
        document.body.classList.toggle("is-locked", open);
      });
    }
  }

  function bindCapabilities() {
    var items = document.querySelectorAll("[data-cap]");
    var image = document.querySelector("[data-cap-image]");
    var label = document.querySelector("[data-cap-label]");
    var index = document.querySelector("[data-cap-index]");
    if (!items.length || !image) return;

    function activate(item) {
      items.forEach(function (other) {
        other.classList.remove("is-active");
      });
      item.classList.add("is-active");
      var source = item.getAttribute("data-img");
      if (source) image.src = source;
      if (label) label.textContent = item.getAttribute("data-label") || "";
      if (index) index.textContent = item.getAttribute("data-index") || "";
    }

    items.forEach(function (item) {
      item.addEventListener("mouseenter", function () {
        activate(item);
      });
      item.addEventListener("focus", function () {
        activate(item);
      });
    });
  }

  function bindReveal() {
    var nodes = document.querySelectorAll("[data-reveal]");
    if (!nodes.length) return;
    if (!("IntersectionObserver" in window)) {
      nodes.forEach(function (node) {
        node.classList.add("is-in");
      });
      return;
    }
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-in");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12 }
    );
    nodes.forEach(function (node) {
      observer.observe(node);
    });
  }

  function bindEnquiry() {
    var form = document.querySelector("[data-enquiry-form]");
    if (!form) return;
    var status = document.querySelector("[data-form-status]");
    var mailLink = document.querySelector("[data-form-mail]");

    form.addEventListener("submit", function (event) {
      event.preventDefault();
      var data = new FormData(form);
      var lines = [];
      data.forEach(function (value, key) {
        if (value) lines.push(key + ": " + value);
      });
      var subject = "Website enquiry: " + (data.get("category") || "General");
      var body = lines.join("\n");
      var mailto =
        "mailto:info@cedefense.com?subject=" +
        encodeURIComponent(subject) +
        "&body=" +
        encodeURIComponent(body);

      if (mailLink) mailLink.href = mailto;
      if (status) {
        status.textContent =
          "This demonstration does not send the form. Use the email draft link below, or write to info@cedefense.com.";
      }
    });
  }

  function bindProgress() {
    var bar = document.querySelector("[data-progress]");
    var article = document.querySelector("[data-article]");
    if (!bar || !article) return;
    var update = function () {
      var rect = article.getBoundingClientRect();
      var total = article.offsetHeight - window.innerHeight * 0.4;
      var progress = total > 0 ? Math.min(1, Math.max(0, -rect.top / total)) : 0;
      bar.style.width = (progress * 100).toFixed(2) + "%";
    };
    update();
    window.addEventListener("scroll", update, { passive: true });
    window.addEventListener("resize", update);
  }

  function bindYear() {
    document.querySelectorAll("[data-year]").forEach(function (node) {
      node.textContent = new Date().getFullYear();
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    bindHeader();
    bindCapabilities();
    bindReveal();
    bindEnquiry();
    bindProgress();
    bindYear();
  });
})();
