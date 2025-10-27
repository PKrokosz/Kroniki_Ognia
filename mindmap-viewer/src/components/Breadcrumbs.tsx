import { MindNode } from "../lib/types";
import { setPathInHash } from "../lib/urlPath";

type BreadcrumbsProps = {
  path: MindNode[];
};

const Breadcrumbs = ({ path }: BreadcrumbsProps) => {
  const handleNavigate = (index: number) => {
    const ids = path.slice(1, index + 1).map((node) => node.id);
    setPathInHash(ids);
  };

  return (
    <nav aria-label="Breadcrumb" className="mb-4 flex flex-wrap items-center gap-2 text-sm text-ember-600">
      {path.map((node, index) => {
        const isLast = index === path.length - 1;
        return (
          <div key={node.id} className="flex items-center gap-2">
            <button
              type="button"
              onClick={() => handleNavigate(index)}
              disabled={isLast}
              className={`rounded-md px-2 py-1 transition focus:outline-none focus-visible:ring-2 focus-visible:ring-ember-400 ${
                isLast
                  ? "cursor-default bg-ember-200 font-semibold text-ember-900"
                  : "bg-ember-100 text-ember-700 hover:bg-ember-200"
              }`}
            >
              {node.title}
            </button>
            {!isLast && <span className="text-ember-400">/</span>}
          </div>
        );
      })}
    </nav>
  );
};

export default Breadcrumbs;
