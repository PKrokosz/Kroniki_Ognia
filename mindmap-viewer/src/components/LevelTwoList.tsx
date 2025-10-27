import { AnimatePresence, motion } from "framer-motion";
import { MindNode } from "../lib/types";

type LevelTwoListProps = {
  parent: MindNode | null;
};

const LevelTwoList = ({ parent }: LevelTwoListProps) => {
  if (!parent) {
    return (
      <section aria-labelledby="level-two" className="space-y-3">
        <h3 id="level-two" className="text-lg font-semibold text-ember-700">
          Poziom 2
        </h3>
        <p className="text-sm text-ember-500">Wybierz gałąź z poziomu 1, aby zobaczyć szczegóły.</p>
      </section>
    );
  }

  const children = parent.children ?? [];

  return (
    <section aria-labelledby="level-two" className="space-y-3">
      <div className="flex items-center justify-between">
        <h3 id="level-two" className="text-lg font-semibold text-ember-700">
          Poziom 2 — {parent.title}
        </h3>
        <span className="text-xs font-medium uppercase tracking-wide text-ember-500">
          {children.length} gałęzi
        </span>
      </div>
      <div className="flex gap-3 overflow-x-auto pb-2 pt-1 snap-x snap-mandatory [scrollbar-width:thin]">
        <AnimatePresence initial={false}>
          {children.length === 0 ? (
            <motion.p
              key="placeholder"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              className="rounded-xl border border-dashed border-ember-300 bg-white/70 px-4 py-6 text-sm text-ember-500"
            >
              Brak dalszych gałęzi.
            </motion.p>
          ) : (
            children.map((child) => (
              <motion.article
                key={child.id}
                layout
                initial={{ opacity: 0, scale: 0.95 }}
                animate={{ opacity: 1, scale: 1 }}
                exit={{ opacity: 0, scale: 0.95 }}
                transition={{ duration: 0.18 }}
                className="min-w-[16rem] flex-1 snap-start rounded-xl border border-ember-200 bg-white/80 p-4 text-ember-800 shadow-sm"
              >
                <h4 className="text-base font-semibold">{child.title}</h4>
                {child.content && <p className="mt-2 text-sm text-ember-600">{child.content}</p>}
              </motion.article>
            ))
          )}
        </AnimatePresence>
      </div>
    </section>
  );
};

export default LevelTwoList;
