from django import template
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter


register = template.Library()

@register.filter(name='pygmentize')
def pygmentize_code(code, language):
    lexer = get_lexer_by_name(language)
    formatter = HtmlFormatter()
    # print(HtmlFormatter().get_style_defs('.highlight'))
    return highlight(code, lexer, formatter)
