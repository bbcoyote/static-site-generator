class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("This method is not yet implemented.")
    
    def props_to_html(self):
        result = ""
        if self.props is not None:
            for key, value in self.props.items():
                result += f' {key}="{value}"'
            return result
        else:
            return result

    def __repr__(self) -> str:
        return f'HTMLNode(tag={self.tag!r}, value={self.value!r}, children={self.children!r}, props={self.props!r})'
    
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

 