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
    


 