/* ============================================================
   LATENCA — APP SHELL (single source of truth)
   One definition of the sidebar + top bar + mobile tab bar, used by
   every mockup so the chrome can never drift between screens.

   Usage in a page:
     <body data-active="explore">                     <- which nav item is current
       <div class="app">
         <aside class="side" id="appSide"></aside>     <- filled here
         <main class="main">
           <div class="topbar" id="topbar"></div>      <- filled here
           ... page content ...
         </main>
       </div>
       <nav class="tabbar" id="appTabbar"></nav>        <- filled here
       <script src="shared/shell.js"></script>          <- BEFORE the page's own script
       <script> ...page-specific JS... </script>

   The page must NOT define its own theme / rail / search-dropdown /
   topbar-sticky handlers — the shell owns them.
   ============================================================ */
(function () {
  var active = (document.body && document.body.dataset.active) || 'explore';
  var on = function (k) { return active === k ? ' active' : ''; };
  var svg = function (p) { return '<svg viewBox="0 0 24 24">' + p + '</svg>'; };

  var ICON = {
    explore: '<circle cx="12" cy="12" r="9"/><path d="M15.6 8.4l-2 5.2-5.2 2 2-5.2z"/>',
    design: '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M5.6 5.6l2.8 2.8M15.6 15.6l2.8 2.8M18.4 5.6l-2.8 2.8M8.4 15.6l-2.8 2.8"/>',
    projects: '<path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>',
    collections: '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18"/>',
    artists: '<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/>',
    search: '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
    sparkle: '<path d="M12 3l1.9 4.6L18 9l-4.1 1.4L12 15l-1.9-4.6L6 9l4.1-1.4z"/>',
    heart: '<path d="M12 21s-7-4.5-9.5-9C1 9 2.5 5.5 6 5.5c2 0 3.2 1.2 4 2.3.8-1.1 2-2.3 4-2.3 3.5 0 5 3.5 3.5 6.5C19 16.5 12 21 12 21z"/>',
    cart: '<path d="M5 7h14l-1 13H6z"/><path d="M8.5 7a3.5 3.5 0 0 1 7 0"/>',
    menu: '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M9 3v18"/>',
    sun: '<circle cx="12" cy="12" r="5.25"/><path d="M12 1v3M12 20v3M1 12h3M20 12h3M4 4l2.1 2.1M17.9 17.9l2.1 2.1M20 4l-2.1 2.1M4 20l2.1-2.1"/>',
    moon: '<path d="M21 12.8A8.5 8.5 0 1 1 11.2 3a6.5 6.5 0 0 0 9.8 9.8z"/>'
  };

  var SIDEBAR =
    '<div class="sidehead"><div class="brand"><span class="full">Latenca</span><span class="mark">L</span></div></div>' +
    '<div class="navgroup">' +
      '<a class="nav' + on('explore') + '">' + svg(ICON.explore) + '<span>Explore</span></a>' +
      '<a class="nav navai' + on('design') + '">' + svg(ICON.design) + '<span>Design my wall</span></a>' +
    '</div>' +
    '<div class="navgroup"><div class="navlabel">You</div>' +
      '<a class="nav' + on('projects') + '">' + svg(ICON.projects) + '<span>My projects</span></a>' +
    '</div>' +
    '<div class="navgroup"><div class="navlabel">Browse</div>' +
      '<a class="nav' + on('collections') + '">' + svg(ICON.collections) + '<span>Collections</span></a>' +
      '<a class="nav' + on('artists') + '">' + svg(ICON.artists) + '<span>Artists</span></a>' +
    '</div>' +
    '<div class="spacer"></div>' +
    '<a class="sell">' + svg('<path d="M12 5v14M5 12h14"/>') + '<span>Sell your art</span></a>' +
    '<a class="account"><span class="avatar"></span><span class="who">Sign in<small>Guest</small></span></a>';

  var SDROP =
    '<div class="sdrop" id="sdrop">' +
      '<div class="shint">' + svg(ICON.sparkle) + 'Describe what you want &mdash; our search understands plain language</div>' +
      '<div class="sgroup"><div class="slabel">Popular subjects</div>' +
        '<a class="sitem">' + svg(ICON.search) + 'Abstract<span class="tag">612 works</span></a>' +
        '<a class="sitem">' + svg(ICON.search) + 'Celestial &amp; space<span class="tag">470 works</span></a>' +
        '<a class="sitem">' + svg(ICON.search) + 'Minimalist line art<span class="tag">320 works</span></a>' +
      '</div>' +
      '<div class="sgroup"><div class="slabel">Collections</div>' +
        '<a class="sitem">' + svg(ICON.collections) + 'Celestial Echoes<span class="tag">26 pieces</span></a>' +
        '<a class="sitem">' + svg(ICON.collections) + 'Nordic Calm<span class="tag">40 pieces</span></a>' +
      '</div>' +
      '<div class="sgroup"><div class="slabel">Artists</div>' +
        '<a class="sitem"><span class="av"></span>Aria Vela<span class="tag">Curator</span></a>' +
        '<a class="sitem"><span class="av"></span>Studio Vreeken<span class="tag">Creator</span></a>' +
      '</div>' +
    '</div>';

  var TOPBAR =
    '<button class="railtoggle" id="railToggle" title="Collapse menu">' + svg(ICON.menu) + '</button>' +
    '<a class="brand-m">Latenca</a>' +
    '<div class="searchwrap">' +
      '<button class="search" id="searchBtn">' + svg(ICON.search) + '<span>Search the collection &mdash; try &ldquo;calm terracotta abstract for a bedroom&rdquo;</span><span class="kbd">&#8984;K</span></button>' +
      SDROP +
    '</div>' +
    '<div class="right">' +
      '<button class="icobtn" id="themeBtn" title="Toggle theme"><svg id="themeIcon" viewBox="0 0 24 24">' + ICON.sun + '</svg></button>' +
      '<button class="icobtn" title="Saved">' + svg(ICON.heart) + '</button>' +
      '<button class="icobtn cart">' + svg(ICON.cart) + '<span class="badge">2</span></button>' +
      '<button class="signin">Sign in</button>' +
    '</div>';

  var TABBAR =
    '<a class="tab' + on('explore') + '">' + svg(ICON.explore) + 'Explore</a>' +
    '<a class="tab' + on('design') + '">' + svg(ICON.design) + 'Design</a>' +
    '<a class="tab' + on('collections') + '">' + svg(ICON.collections) + 'Collections</a>' +
    '<a class="tab' + on('artists') + '">' + svg(ICON.artists) + 'Artists</a>' +
    '<a class="tab' + on('projects') + '">' + svg(ICON.projects) + 'You</a>';

  var side = document.getElementById('appSide'); if (side) side.innerHTML = SIDEBAR;
  var top = document.getElementById('topbar'); if (top) top.innerHTML = TOPBAR;
  var tab = document.getElementById('appTabbar'); if (tab) tab.innerHTML = TABBAR;

  /* ── shared behaviours (owned here, never in the page) ── */
  var rootEl = document.documentElement;
  var themeBtn = document.getElementById('themeBtn');
  var themeIcon = document.getElementById('themeIcon');
  if (themeBtn) themeBtn.onclick = function () {
    var d = rootEl.dataset.theme !== 'dark';
    rootEl.dataset.theme = d ? 'dark' : 'light';
    if (themeIcon) themeIcon.innerHTML = d ? ICON.moon : ICON.sun;
  };

  var railToggle = document.getElementById('railToggle');
  if (railToggle) railToggle.onclick = function () {
    document.querySelector('.app').classList.toggle('rail');
  };

  if (top && 'IntersectionObserver' in window) {
    new IntersectionObserver(function (e) {
      top.classList.toggle('stuck', e[0].intersectionRatio < 1);
    }, { threshold: [1] }).observe(top);
  }

  var searchBtn = document.getElementById('searchBtn');
  var sdrop = document.getElementById('sdrop');
  if (searchBtn && sdrop) {
    var openS = function () { sdrop.classList.add('open'); searchBtn.classList.add('act'); };
    var closeS = function () { sdrop.classList.remove('open'); searchBtn.classList.remove('act'); };
    searchBtn.onclick = function (e) {
      e.stopPropagation();
      sdrop.classList.contains('open') ? closeS() : openS();
    };
    document.addEventListener('click', function (e) {
      if (!e.target.closest('.searchwrap')) closeS();
    });
  }
})();
