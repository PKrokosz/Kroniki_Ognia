let backendUrlPromise;

function resolveConfigPath() {
  const basePath = window.location.pathname.replace(/\/[^/]*$/, '/');
  return `${basePath}config.json`;
}

async function getBackendUrl() {
  if (!backendUrlPromise) {
    backendUrlPromise = fetch(resolveConfigPath(), { cache: 'no-store' })
      .then((res) => {
        if (!res.ok) {
          throw new Error(`Failed to load config.json: ${res.status}`);
        }
        return res.json();
      })
      .then((cfg) => {
        if (!cfg.BACKEND_URL) {
          throw new Error('Missing BACKEND_URL in config.json');
        }
        return cfg.BACKEND_URL;
      });
  }
  return backendUrlPromise;
}

(function () {
  const form = document.getElementById('idea-form');
  if (!form) {
    return;
  }

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

  const ensureBackendUrl = async () => {
    try {
      const api = await getBackendUrl();
      form.action = `${api}/api/ideas`;
      return api;
    } catch (error) {
      console.error('Unable to load backend URL', error);
      setFeedback(
        'Nie udało się pobrać konfiguracji backendu. Skontaktuj się z organizatorami.',
        'error',
      );
      throw error;
    }
  };

  document.addEventListener('DOMContentLoaded', () => {
    ensureBackendUrl().catch(() => {
      /* feedback already handled */
    });
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

    try {
      const api = await ensureBackendUrl();
      const response = await fetch(`${api}/api/ideas`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
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
      if (error.message?.includes('config')) {
        return;
      }
      setFeedback('Wystąpił błąd sieci. Sprawdź połączenie i spróbuj ponownie.', 'error');
    } finally {
      submitButton?.removeAttribute('disabled');
    }
  });
})();
