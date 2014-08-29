#!/user/bin/python

#
# Time complexity: O(n)
# Space complexity: O(n)
#

class Node:

  def getLeft(self):
    return self.left

  def getRight(self):
    return self.right

  def getVal(self):
    return self.val

  def __init__(self, v):
    self.val = v
    self.left = None
    self.right = None

  def add(self,v):
    if(self.left == None):
      self.left = Node(v)
    else:
      self.left.add(v)

      if(self.right == None):
        n = self.left.val * 10 + v
        if(n <= 26):
          self.right = Node(n)
      else:
        self.right.add(v)

  def nLeafs(self):
    if(self.left == None and self.right == None):
      return 1

    if(self.left != None and self.right != None):
      return self.left.nLeafs() + self.right.nLeafs()

    if(self.left != None):
      return self.left.nLeafs()

    if(self.right != None):
      return self.right.nLeafs()


  def toString(self,indent):
    print "$%s%s" % (indent, self.val)
    if(self.left != None):
      self.left.toString(indent + "  ")
    if(self.right != None):
      self.right.toString(indent + "  ")


def buildtree(tree, n):
  if(n % 10 == 0):
    return
  buildtree(tree, n / 10)
  tree.add(n % 10)


number = 19191919

tree = Node('root')
buildtree(tree, number)

print "Number of ways: ", tree.nLeafs()
