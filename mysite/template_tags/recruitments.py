# from django import template.Librar
from django import template

register = template.Library()

@register.simple_tag
def is_recruiting():
    recruiting = False
    return recruiting