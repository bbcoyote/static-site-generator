from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        if value is None:
            raise ValueError("A value must be provided")
        props = {}
        super().__init__(tag=tag, value=value, children=None, props=props if props is not None else {})

    def to_html(self):
        if self.value is None:
            raise ValueError("A value must be provided for a LeafNode.")
        
        if self.tag is None:
            return self.value
        
        props_string = ' '.join(f"'{key}={value}'" for key, value in self.props.items())
        if props_string:
            props_string = ' ' + props_string

        return f'<{self.tag}{props_string}>{self.value}</{self.tag}>'