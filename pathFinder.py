from collections import deque
from tree import TreeNode

class FindPath:
    def __init__(self, maze): 
        self.maze = maze        
        self.row = len(maze)
        self.col = len(maze[0])    
        self.path_history = deque()
        self.steps = None
        self.calls = 0
        
    def find_path(self,start,goal):
        stack = deque()
        root = TreeNode(start)
        searched = {start:root}            
        stack.append(start)#row, col, steps
        while stack:
            self.calls += 1
            curr = stack.pop()
            if curr == goal:
                while True:
                    if self.path_history[-1]==goal:
                        del self.path_history[-1]
                        break
                    del self.path_history[-1]
                break
            if curr[0]+1<self.row and not self.maze[curr[0]+1][curr[1]]  and (curr[0]+1,curr[1]) not in searched:
                stack.appendleft((curr[0]+1,curr[1]))
                node = TreeNode((curr[0]+1,curr[1]))
                searched[curr].addChild(node)
                searched[(curr[0]+1,curr[1])] = node
                self.path_history .append((curr[0]+1,curr[1]))
            if curr[0]-1>=0 and not self.maze[curr[0]-1][curr[1]]  and (curr[0]-1,curr[1]) not in searched:
                stack.appendleft((curr[0]-1,curr[1]))
                node = TreeNode((curr[0]-1,curr[1]))
                searched[curr].addChild(node)
                searched[(curr[0]-1,curr[1])] = node
                self.path_history .append((curr[0]-1,curr[1]))
            if curr[1]-1>=0 and not self.maze[curr[0]][curr[1]-1]  and (curr[0],curr[1]-1) not in searched:
                stack.appendleft((curr[0],curr[1]-1))
                node = TreeNode((curr[0],curr[1]-1))
                searched[curr].addChild(node)
                searched[(curr[0],curr[1]-1)] = node
                self.path_history .append((curr[0],curr[1]-1))
            if curr[1]+1<self.col and not self.maze[curr[0]][curr[1]+1]  and (curr[0],curr[1]+1) not in searched:
                stack.appendleft((curr[0],curr[1]+1))
                node = TreeNode((curr[0],curr[1]+1))
                searched[curr].addChild(node)
                searched[(curr[0],curr[1]+1)] = node
                self.path_history .append((curr[0],curr[1]+1))
        route = TreeNode.datasFromGod(searched[curr]) 
        self.steps = len(route)-1
        return route


