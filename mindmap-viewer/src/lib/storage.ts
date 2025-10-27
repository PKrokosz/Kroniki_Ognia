const STORAGE_KEY_PREFIX = "mindmap-node:";

type StorageLike = Pick<Storage, "getItem" | "setItem">;

const getStorage = (): StorageLike | undefined => {
  if (typeof window === "undefined") {
    return undefined;
  }

  try {
    const { localStorage } = window;
    const testKey = "__storage_test__";
    localStorage.setItem(testKey, testKey);
    localStorage.removeItem(testKey);
    return localStorage;
  } catch (error) {
    console.warn("Local storage unavailable", error);
    return undefined;
  }
};

export const loadContent = (nodeId: string): string | undefined => {
  const storage = getStorage();
  if (!storage) {
    return undefined;
  }
  return storage.getItem(`${STORAGE_KEY_PREFIX}${nodeId}`) ?? undefined;
};

export const saveContent = (nodeId: string, text: string): void => {
  const storage = getStorage();
  if (!storage) {
    return;
  }
  storage.setItem(`${STORAGE_KEY_PREFIX}${nodeId}`, text);
};
