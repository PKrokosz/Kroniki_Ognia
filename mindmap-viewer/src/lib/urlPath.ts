const PATH_PREFIX = "#/path";

export const getPathFromHash = (hash: string = window.location.hash): string[] => {
  if (!hash.startsWith(PATH_PREFIX)) {
    return [];
  }

  const raw = hash.slice(PATH_PREFIX.length);
  if (raw.length === 0) {
    return [];
  }

  const segments = raw.split("/").filter(Boolean);
  return segments.map((segment) => decodeURIComponent(segment));
};

export const setPathInHash = (ids: string[]): void => {
  const encodedSegments = ids.map((id) => encodeURIComponent(id));
  const nextHash = `${PATH_PREFIX}${encodedSegments.length ? "/" + encodedSegments.join("/") : ""}`;
  if (window.location.hash !== nextHash) {
    window.location.hash = nextHash;
  }
};
