import uuid

import networkx as nx
import matplotlib.pyplot as plt
import heapq


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Використання id та збереження значення вузла
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, colors={'skyblue': 'skyblue'}):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    labels = {node[0]: node[1]['label'] for node in tree.nodes(
        data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=[colors.get(node, "skyblue") for node in tree.nodes()])
    plt.show()


def build_tree_from_heap(heap):
    if not heap:
        return None

    def build_node(index):
        if index >= len(heap):
            return None
        node = Node(heap[index])
        node.left = build_node(2 * index + 1)
        node.right = build_node(2 * index + 2)
        return node

    return build_node(0)


if __name__ == '__main__':
    heap = [0, 10, 12, 4, 8, 1, 5, 7, 10, 3]
    heapq.heapify(heap)
    root = build_tree_from_heap(heap)
    draw_tree(root)
