import { useEffect, useMemo, useState } from "react";
import Breadcrumbs from "./components/Breadcrumbs";
import LevelOneList from "./components/LevelOneList";
import LevelTwoList from "./components/LevelTwoList";
import NodeEditor from "./components/NodeEditor";
import { ROOT_NODE } from "./data/mindmap";
import { MindNode } from "./lib/types";
import { getPathFromHash, setPathInHash } from "./lib/urlPath";

type PathResolution = {
  nodes: MindNode[];
  current: MindNode;
  levelOne: MindNode[];
};

const resolvePath = (pathIds: string[]): PathResolution => {
  const pathNodes: MindNode[] = [ROOT_NODE];
  let current = ROOT_NODE;

  for (const id of pathIds) {
    const next = current.children?.find((child) => child.id === id);
    if (!next) {
      break;
    }
    pathNodes.push(next);
    current = next;
  }

  return {
    nodes: pathNodes,
    current,
    levelOne: current.children ?? []
  };
};

const App = () => {
  const [pathIds, setPathIds] = useState<string[]>(() => getPathFromHash());
  const { nodes, current, levelOne } = useMemo(() => resolvePath(pathIds), [pathIds]);
  const [focusedChildId, setFocusedChildId] = useState<string | null>(null);

  useEffect(() => {
    const handleHashChange = () => {
      setPathIds(getPathFromHash());
    };
    window.addEventListener("hashchange", handleHashChange);
    return () => window.removeEventListener("hashchange", handleHashChange);
  }, []);

  useEffect(() => {
    const firstChild = levelOne[0]?.id ?? null;
    setFocusedChildId((currentFocus) => {
      if (!currentFocus) {
        return firstChild;
      }
      const stillExists = levelOne.some((node) => node.id === currentFocus);
      return stillExists ? currentFocus : firstChild;
    });
  }, [levelOne]);

  useEffect(() => {
    if (nodes.length === 1 && window.location.hash === "") {
      setPathInHash([]);
    }
  }, [nodes.length]);

  useEffect(() => {
    const handleKeyDown = (event: KeyboardEvent) => {
      const activeElement = document.activeElement;
      if (activeElement && (activeElement.tagName === "INPUT" || activeElement.tagName === "TEXTAREA")) {
        return;
      }

      if (event.key === "ArrowLeft" || event.key === "ArrowRight") {
        if (!levelOne.length) {
          return;
        }
        event.preventDefault();
        const currentIndex = levelOne.findIndex((node) => node.id === focusedChildId);
        const step = event.key === "ArrowLeft" ? -1 : 1;
        const nextIndex = currentIndex === -1 ? 0 : (currentIndex + step + levelOne.length) % levelOne.length;
        setFocusedChildId(levelOne[nextIndex].id);
      }

      if (event.key === "ArrowUp") {
        event.preventDefault();
        if (nodes.length > 1) {
          const nextPath = pathIds.slice(0, -1);
          setPathInHash(nextPath);
        }
      }

      if (event.key === "Enter") {
        if (focusedChildId) {
          event.preventDefault();
          setPathInHash([...pathIds, focusedChildId]);
        }
      }
    };

    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [focusedChildId, levelOne, nodes.length, pathIds]);

  const handleSelectChild = (childId: string) => {
    setFocusedChildId(childId);
  };

  const handleOpenChild = (childId: string) => {
    setPathInHash([...pathIds, childId]);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-ember-50 via-amber-50 to-ember-100 px-4 py-6">
      <div className="mx-auto flex w-full max-w-6xl flex-col gap-6">
        <header className="rounded-3xl bg-white/80 p-6 shadow-sm">
          <Breadcrumbs path={nodes} />
          <p className="text-sm text-ember-600">
            Nawiguj między gałęziami, aby przeglądać struktury Kronik Ognia. Strzałki ←/→ zmieniają zaznaczenie, ↑ wraca, Enter
            wchodzi głębiej.
          </p>
        </header>
        <main className="grid gap-6 lg:grid-cols-[18rem_minmax(0,1fr)_22rem]">
          <aside className="order-2 lg:order-1">
            <div className="sticky top-6 space-y-4 rounded-3xl bg-white/80 p-5 shadow-sm">
              <LevelOneList
                nodes={levelOne}
                selectedId={focusedChildId}
                onSelect={handleSelectChild}
                onOpen={handleOpenChild}
              />
            </div>
          </aside>
          <section className="order-1 lg:order-2">
            <div className="space-y-4 rounded-3xl bg-white/90 p-6 shadow-md">
              <NodeEditor node={current} />
            </div>
          </section>
          <aside className="order-3">
            <div className="space-y-4 rounded-3xl bg-white/80 p-5 shadow-sm">
              <LevelTwoList parent={levelOne.find((node) => node.id === focusedChildId) ?? null} />
            </div>
          </aside>
        </main>
      </div>
    </div>
  );
};

export default App;
