import matplotlib.colors as mcolors
import heapq
from exercise4 import build_tree_from_heap, draw_tree


def darken_color(color, amount=0.1):
    c = mcolors.to_rgb(color)
    c = [max(0, min(1, x - amount)) for x in c]
    return mcolors.to_hex(c)


def dfs_visualize(root, total_steps):
    visited, stack = set(), [root]
    colors = {}
    step = 0

    while stack and step < total_steps:
        node = stack.pop()
        if node is not None and node.id not in visited:
            visited.add(node.id)
            darker_color = darken_color("skyblue", amount=step * 0.05)
            colors[node.id] = darker_color
            step += 1
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    draw_tree(root, colors)


def bfs_visualize(root, total_steps):
    visited, queue = set(), [root]
    colors = {}
    step = 0

    while queue and step < total_steps:
        node = queue.pop(0)
        if node is not None and node.id not in visited:
            visited.add(node.id)
            darker_color = darken_color("skyblue", amount=step * 0.06)
            colors[node.id] = darker_color
            step += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    draw_tree(root, colors)


heap = [0, 10, 12, 4, 8, 1, 5, 7, 10, 3]
heapq.heapify(heap)
root = build_tree_from_heap(heap)
dfs_visualize(root, total_steps=len(heap))
bfs_visualize(root, total_steps=len(heap))
