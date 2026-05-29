(() => {
  const toggle = document.querySelector('[data-menu-toggle]');
  const menu = document.querySelector('[data-menu]');

  function closeMenu() {
    if (!menu || !toggle) return;
    menu.classList.remove('is-open');
    toggle.setAttribute('aria-expanded', 'false');
  }

  if (toggle && menu) {
    toggle.addEventListener('click', () => {
      const open = menu.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', String(open));
    });

    menu.querySelectorAll('a').forEach((link) => link.addEventListener('click', closeMenu));
    window.addEventListener('keydown', (event) => {
      if (event.key === 'Escape') closeMenu();
    });
  }
})();
