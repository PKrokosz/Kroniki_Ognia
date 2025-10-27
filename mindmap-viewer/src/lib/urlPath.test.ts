import { describe, expect, it } from "vitest";
import { getPathFromHash } from "./urlPath";

describe("getPathFromHash", () => {
  it("parsuje ścieżkę z hash", () => {
    expect(getPathFromHash("#/path/alpha/beta")).toEqual(["alpha", "beta"]);
  });

  it("ignoruje inne prefiksy", () => {
    expect(getPathFromHash("#/inne/abc")).toEqual([]);
  });

  it("obsługuje kodowanie", () => {
    expect(getPathFromHash("#/path/%C5%BCar")).toEqual(["żar"]);
  });
});
