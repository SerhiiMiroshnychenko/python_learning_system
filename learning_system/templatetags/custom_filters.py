from django import template

register = template.Library()


@register.filter(name='add_class')
def add_class(value, arg):
    css_classes = value.field.widget.attrs.get('class', '').split()
    css_classes.append(arg)
    value.field.widget.attrs['class'] = ' '.join(css_classes)
    return value
