export type MindNode = {
  id: string;
  title: string;
  content?: string;
  children?: MindNode[];
};
