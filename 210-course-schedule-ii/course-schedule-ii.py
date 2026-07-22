from collections import deque

class Solution:
    def findOrder(self, numCourses, prerequisites):

        # Graph
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # Build graph
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        # Queue with indegree 0
        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        ans = []

        # BFS
        while q:
            node = q.popleft()
            ans.append(node)

            for nei in graph[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        # If all courses are taken
        if len(ans) == numCourses:
            return ans

        return []