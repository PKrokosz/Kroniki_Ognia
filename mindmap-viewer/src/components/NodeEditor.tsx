import { useEffect, useId, useRef, useState } from "react";
import { MindNode } from "../lib/types";
import { loadContent, saveContent } from "../lib/storage";

type NodeEditorProps = {
  node: MindNode;
};

const NodeEditor = ({ node }: NodeEditorProps) => {
  const textareaId = useId();
  const [value, setValue] = useState(node.content ?? "");
  const [status, setStatus] = useState<string>("");
  const statusRef = useRef<HTMLParagraphElement | null>(null);

  useEffect(() => {
    const stored = loadContent(node.id);
    setValue(stored ?? node.content ?? "");
  }, [node.id, node.content]);

  useEffect(() => {
    if (statusRef.current) {
      statusRef.current.focus();
    }
  }, [status]);

  const handleBlur = () => {
    saveContent(node.id, value);
    setStatus("Zapisano zmiany w pamięci przeglądarki.");
  };

  return (
    <section aria-labelledby={`${textareaId}-label`} className="space-y-4">
      <header>
        <h2 id={`${textareaId}-label`} className="text-2xl font-semibold text-ember-800">
          {node.title}
        </h2>
      </header>
      <textarea
        id={textareaId}
        value={value}
        onChange={(event) => setValue(event.target.value)}
        onBlur={handleBlur}
        rows={12}
        className="w-full rounded-xl border border-ember-200 bg-white/80 p-4 text-ember-900 shadow-sm transition focus:border-ember-400 focus:outline-none focus:ring-2 focus:ring-ember-300"
        placeholder="Dodaj swoje notatki..."
      />
      <p
        ref={statusRef}
        className="text-sm text-ember-500"
        tabIndex={-1}
        aria-live="polite"
      >
        {status || "Zmiany zostaną zapisane lokalnie po wyjściu z pola."}
      </p>
    </section>
  );
};

export default NodeEditor;
