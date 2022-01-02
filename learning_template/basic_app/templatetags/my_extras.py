from django import template

register = template.Library()

@register.filter(name="newcut") ##Using decoraters for register.filter(relative template flitering)
def newcut(value,arg):
    return value.replace(arg, '')

@register.filter(name="subt_new") ##Using decoraters for register.filter(relative template flitering)
def subtract_new(value,newval):
    return (int(value)-int(newval))

# register.filter('cut_new', newcut)
# register.filter("sub_new",subtract_new)
