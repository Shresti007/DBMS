class TreeNode:
    def __init__(self, data):
        self.data = data      # representing data of mode obj
        self.children = [ ]   # instance of tree node class
        self.parent = None    # it stores parent of particular node

    def add_child(self, child):
        child.parent = self         # here from now on assuming child.parent as self ie it is an object
        self.children.append(child) # adding the children item

    def get_level(self):           # here we want to crate levl hirearchy betwen parent n child
       level = 0
       p = self.parent
       while p:
           level += 1
           p = p.parent
       return level

    def print_tree(self):
        spaces = ' ' * self.get_level()*3     # here we are using t get hierarchy
        prefix = spaces +"--" if self.parent else ""
        print(prefix + self.data)  # it print root electronic for this func
        if self.children:     # that is present which can be also represent as len(self.children) > 0
            for child in self.children:
                child.print_tree()     # now it prints the children available in children

def build_product_tree():
    root = TreeNode("Electronics")   # it stores in root node

    laptop = TreeNode("laptop")      #
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iphone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)            # now laptop brand is child of electronics
    root.add_child(cellphone)
    root.add_child(tv)

    return root



if __name__ == '__main__':
    root = build_product_tree()
    #print(root.get_level())
    root.print_tree()



class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, level):
        if self.get_level() > level:
            return
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_location_tree():
    root = TreeNode("Global")

    india = TreeNode("India")

    gujarat = TreeNode("Gujarat")
    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))

    karnataka = TreeNode("Karnataka")
    karnataka.add_child(TreeNode("Bangluru"))
    karnataka.add_child(TreeNode("Mysore"))

    india.add_child(gujarat)
    india.add_child(karnataka)

    usa = TreeNode("USA")

    nj = TreeNode("New Jersey")
    nj.add_child(TreeNode("Princeton"))
    nj.add_child(TreeNode("Trenton"))

    california = TreeNode("California")
    california.add_child(TreeNode("San Francisco"))
    california.add_child(TreeNode("Mountain View"))
    california.add_child(TreeNode("Palo Alto"))

    usa.add_child(nj)
    usa.add_child(california)

    root.add_child(india)
    root.add_child(usa)

    return root


if __name__ == '__main__':
    root_node = build_location_tree()
    root_node.print_tree(3)

