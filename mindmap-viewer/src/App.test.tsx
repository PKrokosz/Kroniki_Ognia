import { render, screen } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";
import App from "./App";
import { setPathInHash } from "./lib/urlPath";

vi.mock("./lib/storage", () => ({
  loadContent: () => undefined,
  saveContent: () => undefined
}));

describe("App", () => {
  beforeEach(() => {
    window.location.hash = "";
  });

  it("renderuje główny węzeł bez błędów", () => {
    render(<App />);
    expect(screen.getByRole("heading", { level: 2, name: /Kroniki Ognia — Drzewo/ })).toBeInTheDocument();
  });

  it("nawiguje na podstawie hash path", () => {
    setPathInHash(["struktury-klasztoru", "nowicjat"]);
    render(<App />);
    expect(screen.getByRole("heading", { level: 2, name: /Nowicjat/ })).toBeInTheDocument();
  });
});
