from django import template

register = template.Library()


@register.filter(name='starcount')
def rating(val):
	return range(val)


@register.filter(name='review_text')
def reviewText(val):
	c=''
	val = val.split('.')
	for i in val:
		i = i.strip()
		i = i[:1].upper()+i[1:]
		c+=i+". "
	return c


@register.filter(name='reviewer')
def reviewer(val):
	return val.upper()