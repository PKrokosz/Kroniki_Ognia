let backendUrlPromise = null;

function resolveConfigUrls() {
  const { href } = window.location;
  const candidates = [
    'config.json',
    './config.json',
    '../config.json',
    '/config.json',
    'public/config.json',
  ];
  const seen = new Set();
  const urls = [];

  for (const candidate of candidates) {
    try {
      const url = new URL(candidate, href).toString();
      if (!seen.has(url)) {
        seen.add(url);
        urls.push(url);
      }
    } catch (error) {
      console.warn('Ignoring invalid config path candidate', candidate, error);
    }
  }

  return urls;
}

async function loadBackendUrl() {
  const attempts = [];

  for (const candidate of resolveConfigUrls()) {
    try {
      const response = await fetch(candidate, { cache: 'no-store' });
      if (!response.ok) {
        attempts.push(`${candidate}: HTTP ${response.status}`);
        continue;
      }

      const config = await response.json();
      const backendUrl = config?.BACKEND_URL;

      if (!backendUrl || typeof backendUrl !== 'string') {
        attempts.push(`${candidate}: missing BACKEND_URL`);
        continue;
      }

      // Aktualizacja: zwracamy adres backendu bez końcowych ukośników zgodnie z config.json.
      return backendUrl.replace(/\/+$/u, "");
    } catch (error) {
      attempts.push(`${candidate}: ${error instanceof Error ? error.message : String(error)}`);
    }
  }

  throw new Error(`Unable to resolve backend URL. Attempts -> ${attempts.join(' | ')}`);
}

function normaliseEndpoint(endpoint) {
  if (!endpoint) {
    return null;
  }

  const trimmed = endpoint.trim();

  if (!trimmed) {
    return null;
  }

  if (trimmed.startsWith('/')) {
    return trimmed;
  }

  const clean = trimmed.replace(/^\/+/u, '');
  return `/api/${clean}`;
}

function endpointForForm(form) {
  const datasetEndpoint = form.getAttribute('data-api');
  if (datasetEndpoint) {
    return normaliseEndpoint(datasetEndpoint);
  }

  if (form.id === 'idea-form') {
    return '/api/ideas';
  }

  return null;
}

export function getBackendUrl() {
  if (!backendUrlPromise) {
    backendUrlPromise = loadBackendUrl();
  }

  return backendUrlPromise;
}

export function wireBackendForms(root = document) {
  const forms = Array.from(root.querySelectorAll('form[data-api], form#idea-form'));

  if (forms.length === 0) {
    return Promise.resolve(null);
  }

  return getBackendUrl()
    .then((backendUrl) => {
      const baseUrl = backendUrl.replace(/\/+$/u, '');

      for (const form of forms) {
        const endpoint = endpointForForm(form);
        if (!endpoint) {
          continue;
        }

        form.action = `${baseUrl}${endpoint}`;
        form.dataset.backendReady = 'true';
      }

      return backendUrl;
    })
    .catch((error) => {
      for (const form of forms) {
        form.dataset.backendReady = 'error';
      }
      throw error;
    });
}

function autoWire() {
  wireBackendForms().catch((error) => {
    console.error('Failed to wire backend forms', error);
  });
}

if (typeof window !== 'undefined' && typeof document !== 'undefined') {
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', autoWire, { once: true });
  } else {
    autoWire();
  }
}
