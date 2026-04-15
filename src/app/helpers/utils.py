from django.utils.text import slugify

def make_slug(value):
    return slugify(value)
