(function () {
  const section = document.querySelector('.visual-key');
  if (!section) {
    return;
  }

  const tiles = Array.from(section.querySelectorAll('.visual-key__tile'));
  const autoplayButton = section.querySelector('[data-visual-key-autoplay]');
  const status = section.querySelector('.visual-key__status');

  if (!tiles.length) {
    return;
  }

  const reducedMotionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
  let currentIndex = 0;
  let autoplayTimer = null;

  const setStatus = (message) => {
    if (status) {
      status.textContent = message || '';
    }
  };

  const deactivateAll = () => {
    tiles.forEach((tile) => tile.classList.remove('is-active'));
  };

  const activateTile = (index) => {
    const nextIndex = (index + tiles.length) % tiles.length;
    currentIndex = nextIndex;
    deactivateAll();
    const target = tiles[nextIndex];
    if (target) {
      target.classList.add('is-active');
      target.querySelector('a')?.setAttribute('aria-current', 'true');
      tiles
        .filter((tile) => tile !== target)
        .forEach((tile) => tile.querySelector('a')?.removeAttribute('aria-current'));
    }
  };

  const stopAutoplay = (announce = false) => {
    if (autoplayTimer) {
      window.clearInterval(autoplayTimer);
      autoplayTimer = null;
    }
    if (autoplayButton) {
      autoplayButton.setAttribute('aria-pressed', 'false');
      autoplayButton.textContent = 'Odtwórz sekwencję';
    }
    if (announce) {
      setStatus('Autoodtwarzanie zatrzymane.');
    } else {
      setStatus('');
    }
  };

  const startAutoplay = () => {
    if (!autoplayButton) {
      return;
    }
    if (reducedMotionQuery.matches) {
      autoplayButton.setAttribute('aria-disabled', 'true');
      autoplayButton.setAttribute('disabled', 'true');
      autoplayButton.classList.add('is-disabled');
      setStatus('Autoodtwarzanie jest wyłączone przez preferencję ograniczonego ruchu.');
      return;
    }
    stopAutoplay();
    autoplayButton.setAttribute('aria-pressed', 'true');
    autoplayButton.removeAttribute('aria-disabled');
    autoplayButton.removeAttribute('disabled');
    autoplayButton.classList.remove('is-disabled');
    autoplayButton.textContent = 'Zatrzymaj sekwencję';
    setStatus('Autoodtwarzanie uruchomione.');
    autoplayTimer = window.setInterval(() => {
      activateTile(currentIndex + 1);
    }, 6000);
  };

  activateTile(0);

  if (reducedMotionQuery.matches && autoplayButton) {
    autoplayButton.setAttribute('aria-disabled', 'true');
    autoplayButton.setAttribute('disabled', 'true');
    autoplayButton.classList.add('is-disabled');
    setStatus('Autoodtwarzanie jest wyłączone przez preferencję ograniczonego ruchu.');
  }

  tiles.forEach((tile, index) => {
    tile.addEventListener('mouseenter', () => {
      stopAutoplay();
      activateTile(index);
    });
    tile.addEventListener('focusin', () => {
      stopAutoplay();
      activateTile(index);
    });
  });

  autoplayButton?.addEventListener('click', () => {
    if (autoplayTimer) {
      stopAutoplay(true);
      return;
    }
    startAutoplay();
  });

  reducedMotionQuery.addEventListener('change', (event) => {
    if (event.matches) {
      stopAutoplay();
      if (autoplayButton) {
        autoplayButton.setAttribute('aria-disabled', 'true');
        autoplayButton.setAttribute('disabled', 'true');
        autoplayButton.classList.add('is-disabled');
        setStatus('Autoodtwarzanie jest wyłączone przez preferencję ograniczonego ruchu.');
      }
    } else if (autoplayButton) {
      autoplayButton.removeAttribute('aria-disabled');
      autoplayButton.removeAttribute('disabled');
      autoplayButton.classList.remove('is-disabled');
      setStatus('');
    }
  });
})();
