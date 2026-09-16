(function () {
  "use strict";

  var scrollSpeed = 650;

  function getNavHeight() {
    var nav = document.querySelector("#navbar-top .navbar-default");
    return nav ? nav.offsetHeight + 2 : 70;
  }

  function getScrollTop() {
    return window.pageYOffset || document.documentElement.scrollTop || 0;
  }

  function closeMobileMenu() {
    var collapse = document.querySelector("#site-navigation");
    var toggle = document.querySelector("#navbar-top .navbar-toggle");
    var checkbox = document.querySelector("#mobile-nav-check");

    if (collapse) {
      collapse.classList.remove("is-open");
      collapse.style.display = "none";
    }

    if (toggle) {
      toggle.setAttribute("aria-expanded", "false");
    }

    if (checkbox) {
      checkbox.checked = false;
    }

    var backdrop = document.querySelector("#navbar-top .mobile-nav-backdrop");

    if (backdrop) {
      backdrop.style.display = "none";
      backdrop.style.pointerEvents = "none";
    }

    document.body.classList.remove("mobile-nav-open");
  }

  function setActiveNav(currentId) {
    var navItems = document.querySelectorAll("#navbar-top .navbar-nav li");

    Array.prototype.forEach.call(navItems, function (item) {
      item.classList.remove("active");
    });

    if (!currentId) {
      return;
    }

    var activeLink = document.querySelector("#navbar-top .navbar-nav a[href='" + currentId + "']");

    if (activeLink && activeLink.parentNode) {
      activeLink.parentNode.classList.add("active");
    }
  }

  function updateActiveNav() {
    var scrollTop = getScrollTop();
    var scrollPosition = scrollTop + getNavHeight() + 12;
    var links = document.querySelectorAll("#navbar-top .navbar-nav a[href^='#']");
    var currentId = scrollTop < 12 ? "#home" : "";

    Array.prototype.forEach.call(links, function (link) {
      var href = link.getAttribute("href");
      var section = href && document.querySelector(href);

      if (href !== "#home" && section && section.offsetTop <= scrollPosition) {
        currentId = href;
      }
    });

    if (scrollTop + window.innerHeight >= document.documentElement.scrollHeight - 4 && links.length) {
      currentId = links[links.length - 1].getAttribute("href") || currentId;
    }

    setActiveNav(currentId);
  }

  function scrollToTarget(targetId) {
    var target = document.querySelector(targetId);

    if (!target) {
      return;
    }

    window.scrollTo({
      top: Math.max(0, target.offsetTop - getNavHeight()),
      behavior: "smooth"
    });
  }

  function initNavbar() {
    var toggle = document.querySelector("#navbar-top .navbar-toggle");
    var collapse = document.querySelector("#site-navigation");
    var backdrop = document.querySelector("#navbar-top .mobile-nav-backdrop");
    var checkbox = document.querySelector("#mobile-nav-check");
    var navLinks = document.querySelectorAll("#navbar-top a[href^='#'], .nav-external[href^='#']");

    function syncMobileMenu() {
      var isOpen = checkbox && checkbox.checked;

      if (collapse) {
        collapse.classList.toggle("is-open", !!isOpen);
        collapse.style.display = isOpen ? "block" : "none";
      }

      if (toggle) {
        toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
      }

      document.body.classList.toggle("mobile-nav-open", !!isOpen);

      if (backdrop) {
        backdrop.style.display = isOpen ? "block" : "none";
        backdrop.style.pointerEvents = isOpen ? "auto" : "none";
      }
    }

    if (checkbox) {
      checkbox.addEventListener("change", syncMobileMenu);
    }

    if (toggle && checkbox) {
      toggle.addEventListener("keydown", function (event) {
        if (event.key === "Enter" || event.key === " ") {
          event.preventDefault();
          checkbox.checked = !checkbox.checked;
          syncMobileMenu();
        }
      });
    }

    if (backdrop) {
      backdrop.addEventListener("click", function (event) {
        event.preventDefault();
        closeMobileMenu();
      });
    }

    document.addEventListener("click", function (event) {
      if (!document.body.classList.contains("mobile-nav-open") || !collapse || !toggle) {
        return;
      }

      if (!collapse.contains(event.target) && !toggle.contains(event.target)) {
        closeMobileMenu();
      }
    });

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape") {
        closeMobileMenu();
      }
    });

    Array.prototype.forEach.call(navLinks, function (link) {
      link.addEventListener("click", function (event) {
        var href = link.getAttribute("href");

        if (href && document.querySelector(href)) {
          event.preventDefault();
          scrollToTarget(href);
          closeMobileMenu();
          setActiveNav(href === "#home" ? "#home" : href);
        }
      });
    });

    window.addEventListener("scroll", updateActiveNav);
    window.addEventListener("resize", updateActiveNav);
    updateActiveNav();
  }

  function initPortfolio() {
    var $ = window.jQuery;

    if (!$ || !$.fn || !$.fn.isotope) {
      return;
    }

    var portfolio = $("#portfolio");
    var items = $(".items", portfolio);
    var filters = $(".filters li a", portfolio);

    if (!portfolio.length || !items.length) {
      return;
    }

    var layoutItems = function () {
      items.isotope({
        itemSelector: ".item",
        layoutMode: "fitRows",
        transitionDuration: "0.35s"
      });
    };

    if ($.fn.imagesLoaded) {
      items.imagesLoaded(layoutItems);
    } else {
      layoutItems();
    }

    filters.on("click", function (event) {
      event.preventDefault();
      var el = $(this);
      filters.removeClass("active");
      el.addClass("active");
      items.isotope({ filter: el.attr("data-filter") });
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    initNavbar();
    initPortfolio();
  });
})();
