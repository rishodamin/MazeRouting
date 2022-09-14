from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.child = deque()
        self.parent = None
    
    def addChild(self, child):
         child.parent = self
         self.child.append(child)
         
    @staticmethod
    def getLevel(node,count=0):
        if not node.parent:
            return count
        return TreeNode.getLevel(node.parent,count+1)
     
    def show(self):
        print("  "*TreeNode.getLevel(self)+"|_"+str(self.data))
        if self.child:
            for child in self.child:
                child.show()
    @staticmethod           
    def datasFromGod(node,data=deque()):
        data.append(node.data)
        if not node.parent:
            #data.clear()
            return data
        return TreeNode.datasFromGod(node.parent,data)
