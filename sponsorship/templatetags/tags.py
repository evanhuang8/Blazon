from django import template

register = template.Library()

@register.filter
def formatMoney(value):
  value = int(value) / 100
  return '{0:.2f}'.format(value)