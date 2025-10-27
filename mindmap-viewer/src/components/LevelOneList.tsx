import { AnimatePresence, motion } from "framer-motion";
import { MindNode } from "../lib/types";

type LevelOneListProps = {
  nodes: MindNode[];
  selectedId: string | null;
  onSelect: (nodeId: string) => void;
  onOpen: (nodeId: string) => void;
};

const listVariants = {
  initial: { opacity: 0, y: 8 },
  animate: { opacity: 1, y: 0 },
  exit: { opacity: 0, y: -8 }
};

const LevelOneList = ({ nodes, selectedId, onSelect, onOpen }: LevelOneListProps) => (
  <section aria-labelledby="level-one" className="space-y-3">
    <h3 id="level-one" className="text-lg font-semibold text-ember-700">
      Gałęzie poziomu 1
    </h3>
    <div className="grid gap-3 md:grid-cols-1">
      <AnimatePresence>
        {nodes.map((node) => {
          const isSelected = node.id === selectedId;
          return (
            <motion.article
              key={node.id}
              layout
              initial="initial"
              animate="animate"
              exit="exit"
              variants={listVariants}
              className={`rounded-xl border p-4 shadow-sm transition focus-within:ring-2 focus-within:ring-ember-300 ${
                isSelected
                  ? "border-ember-400 bg-white/90"
                  : "border-ember-200 bg-white/70 hover:border-ember-300"
              }`}
            >
              <div className="flex items-center justify-between gap-2">
                <button
                  type="button"
                  onClick={() => onSelect(node.id)}
                  className="text-left text-base font-medium text-ember-800 focus:outline-none focus-visible:ring-2 focus-visible:ring-ember-400"
                >
                  {node.title}
                </button>
                <button
                  type="button"
                  onClick={() => onOpen(node.id)}
                  className="rounded-lg bg-ember-500 px-3 py-1 text-sm font-semibold text-white transition hover:bg-ember-600 focus:outline-none focus-visible:ring-2 focus-visible:ring-ember-300"
                >
                  Otwórz
                </button>
              </div>
              {node.content && <p className="mt-2 text-sm text-ember-600">{node.content}</p>}
            </motion.article>
          );
        })}
      </AnimatePresence>
    </div>
  </section>
);

export default LevelOneList;
