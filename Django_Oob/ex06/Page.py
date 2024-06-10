from elements import *

class Page:
    def __init__(self, elements):
        if not isinstance(elements, (Elem, Text)):
            raise Elem.ValidationError("Invalid elements")
        self.elements = elements
    
    def is_valid(self):
        return self.__is_elem_valid(self.elements)
  
    def __str__(self):
        if isinstance(self.elements, Html):
            return '<!DOCTYPE html>\n' + str(self.elements)
        else:
            return str(self.elements)
    
    def write_to_file(self, filename: str):
        with open(filename, 'w') as f:
            f.write(str(self))

    def __is_elem_valid(self, elem: Elem) -> bool:
        elem_classes = (Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br)
        if not (isinstance(elem, elem_classes) or isinstance(elem, Text)):
            return False
        
        # Html must contain a Head, then a Body.
        if isinstance(elem, Html):
            if len(elem.content) != 2:
                return False
            if not isinstance(elem.content[0], Head):
                return False
            if not isinstance(elem.content[1], Body):
                return False
      
        # Head must contain one Title.
        if isinstance(elem, Head):
            if len(elem.content) != 1:
                return False
            if not isinstance(elem.content[0], Title):
                return False

        # Body and Div can contain specific types of elements.
        if isinstance(elem, (Body, Div)):
            if not all([isinstance(e, (H1, H2, Div, Table, Ul, Ol, Span, Text)) for e in elem.content]):
                return False
            
        # Title, H1, H2, Li, Th, Td must contain one Text.
        if isinstance(elem, (Title, H1, H2, Li, Th, Td)):
            if len(elem.content) != 1:
                return False
            if not isinstance(elem.content[0], Text):
                return False
    
        # P must only contain Text.
        if isinstance(elem, P):
            if not all([isinstance(e, Text) for e in elem.content]):
                return False
    
        # Span must only contain Text or some P.
        if isinstance(elem, Span):
            if not all([isinstance(e, (Text, P)) for e in elem.content]):
                return False
    
        # Ul and Ol must contain at least one Li and only some Li.
        if isinstance(elem, (Ul, Ol)):
            if len([e for e in elem.content if isinstance(e, Li)]) < 1:
                return False
            if not all([isinstance(e, Li) for e in elem.content]):
                return False
        
        # Table must only contain Tr and only some Tr.
        if isinstance(elem, Table):
            if not all([isinstance(e, Tr) for e in elem.content]):
                return False
    
        # Tr must contain at least one Th or Td and only some Th or Td. 
        # The Th and the Td must be mutually exclusive.
        if isinstance(elem, Tr):
            if len([e for e in elem.content if isinstance(e, (Th, Td))]) < 1:
                return False
            if not all([isinstance(e, (Th, Td)) for e in elem.content]):
                return False
            if any(isinstance(e, Th) for e in elem.content) and any(isinstance(e, Td) for e in elem.content):
                return False
    
        if isinstance(elem, Elem) and elem.content is not None and len(elem.content) > 0:
            return all([self.__is_elem_valid(e) for e in elem.content])
    
        return True

def main():
    head = Head(Title(Text('Hello World')))
    ul = Ul([Li(Text('test ul')), Li(Text('test li'))])
    div = Div([Text('a div'), ul])
    h1 = H1(Text('Oh no, not again!'))
    img = Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'})
    body = Body([h1, img, div])
    html = Html([head, body])
    print(Html([Head(), Body()]))
    print(html)

if __name__ == '__main__':
    main()
