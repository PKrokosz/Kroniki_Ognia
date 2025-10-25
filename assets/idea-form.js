(function () {
  const form = document.getElementById('idea-form');
  if (!form) {
    return;
  }

  const textarea = document.getElementById('idea-text');
  const feedback = document.getElementById('idea-feedback');
  const submitButton = form.querySelector('button[type="submit"]');

  const setFeedback = (message, type) => {
    if (!feedback) return;
    feedback.textContent = message;
    feedback.setAttribute('data-status', type);
  };

  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    if (!textarea) {
      return;
    }

    const value = textarea.value.trim();
    if (!value) {
      setFeedback('Podaj treść pomysłu, zanim go wyślesz.', 'error');
      textarea.focus();
      return;
    }

    submitButton?.setAttribute('disabled', 'true');
    setFeedback('Zapisuję pomysł w archiwum…', 'pending');

    try {
      const response = await fetch('/api/ideas', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ idea: value }),
      });

      const payload = await response.json().catch(() => ({}));

      if (!response.ok) {
        const message = payload?.message || 'Nie udało się zapisać pomysłu. Spróbuj ponownie.';
        setFeedback(message, 'error');
        return;
      }

      const message = payload?.message || 'Dziękujemy! Pomysł został zapisany.';
      setFeedback(message, 'success');
      textarea.value = '';
      textarea.focus();
    } catch (error) {
      console.error('Idea submission failed', error);
      setFeedback('Wystąpił błąd sieci. Sprawdź połączenie i spróbuj ponownie.', 'error');
    } finally {
      submitButton?.removeAttribute('disabled');
    }
  });
})();
