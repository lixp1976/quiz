from django import template

__author__ = 'djud'

register = template.Library()

@register.filter
def to_str(value):
    if value is None:
        return ''
    return "{0}".format(value)