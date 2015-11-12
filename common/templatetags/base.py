from django import template

register = template.Library()

box_class = "col-lg-6 col-lg-offset-3 col-md-6 col-md-offset-3 content-box"
open_row_div = ''.join([
    '<div class="container-fluid outer-content-box">',
    '<div class="row">',
    '<div class="'+ box_class +'">'
])
close_row_div = '</div></div></div>'


class Open_Box_Node(template.Node):
    def render(self, context):
        return open_row_div

class Close_Box_Node(template.Node):
    def render(self, context):
        return close_row_div


@register.tag(name="open_box")
def do_open_box(parse, token):
    return Open_Box_Node()

@register.tag(name="close_box")
def do_close_box(parse, token):
    return Close_Box_Node()
