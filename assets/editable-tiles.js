const TILE_SELECTOR =
  ".plan-card, .feature-card, .tool-card, .card-popiol, .focus-card, .timeline-card";
const STORAGE_PREFIX = "kroniki-tiles:";
let tileCounter = 0;
let observerStarted = false;
let storageNoticeRendered = false;

function storageAvailable() {
  try {
    if (typeof window === "undefined" || !("localStorage" in window)) {
      return null;
    }
    const testKey = `${STORAGE_PREFIX}__probe__`;
    window.localStorage.setItem(testKey, "ok");
    window.localStorage.removeItem(testKey);
    return window.localStorage;
  } catch (error) {
    console.warn("Local storage unavailable for editable tiles.", error);
    return null;
  }
}

const storage = storageAvailable();

function slugify(text) {
  return text
    .toLowerCase()
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/[^a-z0-9\-\s_]/g, "")
    .trim()
    .replace(/\s+/g, "-");
}

function renderStorageNotice() {
  if (storage || storageNoticeRendered) {
    return;
  }
  const target =
    document.querySelector(".content-container") ||
    document.querySelector("main") ||
    document.body;
  if (!target) {
    return;
  }
  const notice = document.createElement("div");
  notice.className = "tile-edit-notice";
  notice.setAttribute("role", "status");
  notice.setAttribute("aria-live", "polite");
  notice.textContent =
    "Edycja kafelków jest wyłączona: przeglądarka blokuje pamięć lokalną.";
  target.prepend(notice);
  storageNoticeRendered = true;
}

function ensureContentWrapper(tile) {
  const existing = tile.querySelector("[data-tile-content]");
  if (existing) {
    return existing;
  }
  const wrapper = document.createElement("div");
  wrapper.className = "tile-editable__content";
  wrapper.setAttribute("data-tile-content", "");
  while (tile.firstChild) {
    wrapper.appendChild(tile.firstChild);
  }
  tile.appendChild(wrapper);
  return wrapper;
}

function computeStorageKey(tile, fallbackIndex) {
  const pageKey = window.location.pathname.replace(/^\/+/, "") || "index.html";
  let candidate =
    tile.getAttribute("data-editable-key") ||
    tile.getAttribute("data-thread-key") ||
    tile.id ||
    "";
  if (!candidate) {
    const heading = tile.querySelector("h1, h2, h3, h4, h5, h6");
    if (heading) {
      candidate = heading.textContent || "";
    }
  }
  if (!candidate) {
    candidate = `tile-${fallbackIndex}`;
  }
  const slug = slugify(candidate) || `tile-${fallbackIndex}`;
  return `${STORAGE_PREFIX}${pageKey}:${slug}`;
}

function sanitizeIdFragment(text) {
  return text.replace(/[^a-zA-Z0-9_-]/g, "");
}

function startObserver() {
  if (observerStarted) {
    return;
  }
  const observer = new MutationObserver((mutations) => {
    mutations.forEach((mutation) => {
      mutation.addedNodes.forEach((node) => {
        if (!(node instanceof HTMLElement)) {
          return;
        }
        if (node.matches && node.matches(TILE_SELECTOR)) {
          initTile(node);
        } else {
          node.querySelectorAll?.(TILE_SELECTOR).forEach((nested) => {
            initTile(nested);
          });
        }
      });
    });
  });
  observer.observe(document.body, {
    childList: true,
    subtree: true,
  });
  observerStarted = true;
}

function initTile(tile) {
  if (!(tile instanceof HTMLElement)) {
    return;
  }
  if (tile.dataset.editableInitialized === "true") {
    return;
  }
  tile.dataset.editableInitialized = "true";
  tile.classList.add("tile-editable");
  const content = ensureContentWrapper(tile);
  if (!content.hasAttribute("tabindex")) {
    content.setAttribute("tabindex", "-1");
  }
  const key = computeStorageKey(tile, ++tileCounter);
  const panelId = `tile-edit-panel-${sanitizeIdFragment(key)}-${tileCounter}`;
  if (storage) {
    const stored = storage.getItem(key);
    if (stored) {
      content.innerHTML = stored;
    }
  }

  const heading = tile.querySelector("h1, h2, h3, h4, h5, h6");
  const labelTarget = heading ? heading.textContent?.trim() || "kafelek" : "kafelek";

  const tab = document.createElement("button");
  tab.type = "button";
  tab.className = "tile-edit-tab";
  tab.setAttribute("aria-expanded", "false");
  tab.setAttribute("aria-controls", panelId);
  tab.setAttribute("title", "Edytuj treść kafelka");
  tab.innerHTML =
    '<span class="tile-edit-tab__icon" aria-hidden="true">✏️</span>' +
    '<span class="tile-edit-tab__label">Edytuj</span>';
  tab.setAttribute("aria-label", `Edytuj kafelek: ${labelTarget}`);
  tile.appendChild(tab);

  const panel = document.createElement("div");
  panel.className = "tile-edit-panel";
  panel.id = panelId;
  panel.setAttribute("hidden", "");

  const intro = document.createElement("p");
  intro.className = "tile-edit-panel__intro";
  intro.textContent =
    "Tryb edycji pozwala na bezpośrednią zmianę tekstu w kafelku. Zapis utrwala zmiany w tej przeglądarce.";
  panel.appendChild(intro);

  const helper = document.createElement("p");
  helper.className = "tile-edit-panel__helper";
  helper.textContent = "Skróty: Ctrl+S / Cmd+S zapisuje, Esc anuluje zmiany.";
  panel.appendChild(helper);

  const actions = document.createElement("div");
  actions.className = "tile-edit-panel__actions";

  const saveButton = document.createElement("button");
  saveButton.type = "button";
  saveButton.className = "tile-edit-panel__button tile-edit-panel__button--save badge-outline";
  saveButton.textContent = "Zapisz zmiany";

  const cancelButton = document.createElement("button");
  cancelButton.type = "button";
  cancelButton.className = "tile-edit-panel__button tile-edit-panel__button--cancel badge-outline";
  cancelButton.textContent = "Anuluj";

  actions.appendChild(saveButton);
  actions.appendChild(cancelButton);
  panel.appendChild(actions);

  const status = document.createElement("p");
  status.className = "tile-edit-status";
  status.setAttribute("role", "status");
  status.setAttribute("aria-live", "polite");
  panel.appendChild(status);

  tile.appendChild(panel);

  if (!storage) {
    tab.disabled = true;
    tab.setAttribute("aria-disabled", "true");
    tab.setAttribute(
      "title",
      "Edycja wymaga localStorage. Odblokuj pamięć przeglądarki, aby zapisywać zmiany."
    );
    panel.setAttribute(
      "data-editing-disabled",
      "Edycja zablokowana — localStorage jest niedostępny."
    );
    return;
  }

  let snapshot = content.innerHTML;

  function openEditor() {
    snapshot = content.innerHTML;
    tile.classList.add("tile-editing");
    tab.setAttribute("aria-expanded", "true");
    panel.removeAttribute("hidden");
    content.setAttribute("contenteditable", "true");
    content.focus();
    status.textContent = "Tryb edycji aktywny. Wprowadź zmiany i zapisz.";
  }

  function closeEditor(message) {
    content.removeAttribute("contenteditable");
    tile.classList.remove("tile-editing");
    tab.setAttribute("aria-expanded", "false");
    panel.setAttribute("hidden", "");
    if (message) {
      status.textContent = message;
    }
  }

  function handleSave() {
    const newContent = content.innerHTML.trim();
    storage.setItem(key, newContent);
    snapshot = newContent;
    closeEditor("Zmiany zapisane lokalnie.");
  }

  function handleCancel() {
    content.innerHTML = snapshot;
    closeEditor("Przywrócono poprzednią treść.");
  }

  tab.addEventListener("click", () => {
    if (tile.classList.contains("tile-editing")) {
      handleCancel();
    } else {
      openEditor();
    }
  });

  saveButton.addEventListener("click", handleSave);
  cancelButton.addEventListener("click", handleCancel);

  content.addEventListener("keydown", (event) => {
    if (!tile.classList.contains("tile-editing")) {
      return;
    }
    if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === "s") {
      event.preventDefault();
      handleSave();
    } else if (event.key === "Escape") {
      event.preventDefault();
      handleCancel();
    }
  });
}

function initEditableTiles() {
  if (!document.body) {
    return;
  }
  if (!storage) {
    renderStorageNotice();
  }
  document.querySelectorAll(TILE_SELECTOR).forEach((tile) => {
    initTile(tile);
  });
  startObserver();
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", () => {
    renderStorageNotice();
    initEditableTiles();
  });
} else {
  renderStorageNotice();
  initEditableTiles();
}
