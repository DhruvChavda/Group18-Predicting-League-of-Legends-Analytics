from django import template
register = template.Library()

@register.simple_tag
def field_value(field):
    """ returns field value """
    return field.form.initial.get(field.name, '')