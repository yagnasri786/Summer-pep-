from collections import deque

class Solution:
    def isBipartite(self, graph):
        n = len(graph)
        color = [-1] * n   # -1 = not colored

        for i in range(n):
            if color[i] != -1:
                continue

            q = deque([i])
            color[i] = 0

            while q:
                node = q.popleft()

                for nei in graph[node]:
                    if color[nei] == -1:
                        color[nei] = 1 - color[node]
                        q.append(nei)

                    elif color[nei] == color[node]:
                        return False

        return True