from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, children, tag=None, props=None):
        super().__init__(tag, children, props)
        if self.tag is None:
            raise ValueError("A tag must be given.")
        props = {}

    def to_html(self):
        if self.tag is None:
            raise ValueError("A tag is required!")
        if len(self.children) <= 0:
            raise ValueError("A child is required for a parent node!")
        else:
            return f""
        

# So children are a a list, every child is a HTMLNode, each HTMLNode is either a parent node or a leaf node. essentially it is a list of lists.
# We will exit out of the recursion once we get to the end of the parent's list of children once the list is empty.
# test that a tag and children are given