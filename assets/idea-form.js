import { wireBackendForms } from './js/backend-config.js';

const backendReady = wireBackendForms();

(function () {
  const form = document.getElementById('idea-form');
  if (!form) {
    return;
  }

  const apiKey = form.dataset.apiKey || 'dev-key';

  const titleInput = document.getElementById('idea-title');
  const textarea = document.getElementById('idea-text');
  const tagsInput = document.getElementById('idea-tags');
  const feedback = document.getElementById('idea-feedback');
  const submitButton = form.querySelector('button[type="submit"]');

  const setFeedback = (message, type) => {
    if (!feedback) return;
    feedback.textContent = message;
    feedback.setAttribute('data-status', type);
  };

  const ensureBackendReady = async () => {
    try {
      await backendReady;
      if (!form.action) {
        throw new Error('Missing form action after backend wiring.');
      }
      if (form.dataset.backendReady === 'error') {
        throw new Error('Backend configuration failed.');
      }
      return form.action;
    } catch (error) {
      console.error('Unable to load backend URL', error);
      setFeedback(
        'Nie udało się pobrać konfiguracji backendu. Skontaktuj się z organizatorami.',
        'error',
      );
      throw error;
    }
  };

  backendReady.catch(() => {
    setFeedback(
      'Nie udało się pobrać konfiguracji backendu. Skontaktuj się z organizatorami.',
      'error',
    );
  });

  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    if (!textarea || !titleInput) {
      return;
    }

    const title = titleInput.value.trim();
    const content = textarea.value.trim();
    const tagsRaw = (tagsInput?.value || '').trim();

    if (!title) {
      setFeedback('Nadaj pomysłowi tytuł, zanim go wyślesz.', 'error');
      titleInput.focus();
      return;
    }

    if (!content) {
      setFeedback('Podaj treść pomysłu, zanim go wyślesz.', 'error');
      textarea.focus();
      return;
    }

    const payload = {
      title,
      content,
      ...(tagsRaw ? { tags: tagsRaw.split(',').map((tag) => tag.trim()).filter(Boolean) } : {}),
    };

    submitButton?.setAttribute('disabled', 'true');
    setFeedback('Zapisuję pomysł w archiwum…', 'pending');

    let actionUrl;
    try {
      actionUrl = await ensureBackendReady();
    } catch (error) {
      submitButton?.removeAttribute('disabled');
      return;
    }

    try {
      const response = await fetch(actionUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-API-Key': apiKey,
        },
        body: JSON.stringify(payload),
      });

      const responsePayload = await response.json().catch(() => ({}));

      if (!response.ok) {
        const message = responsePayload?.message || 'Nie udało się zapisać pomysłu. Spróbuj ponownie.';
        setFeedback(message, 'error');
        return;
      }

      setFeedback('Dziękujemy! Pomysł został zapisany.', 'success');
      titleInput.value = '';
      textarea.value = '';
      if (tagsInput) {
        tagsInput.value = '';
      }
      titleInput.focus();
    } catch (error) {
      console.error('Idea submission failed', error);
      setFeedback('Wystąpił błąd sieci. Sprawdź połączenie i spróbuj ponownie.', 'error');
    } finally {
      submitButton?.removeAttribute('disabled');
    }
  });
})();
