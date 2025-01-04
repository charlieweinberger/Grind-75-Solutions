# https://leetcode.com/problems/clone-graph

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node is None:
            return None

        queue = [node]
        visited = {node.val: Node(node.val)}

        while len(queue) > 0:

            current = queue[0]
            del queue[0]
            currentClone = visited[current.val]
    
            for neighbor in current.neighbors:
                if neighbor.val not in visited:
                    visited[neighbor.val] = Node(neighbor.val)
                    queue.append(neighbor)
                currentClone.neighbors.append(visited[neighbor.val])

        return visited[node.val]