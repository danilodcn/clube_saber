import os
from mimetypes import guess_type

from django import template

register = template.Library()

ICON_MAP = {
    'zip': 'zipper',
    'pptx': 'powerpoint',
    'xlsx': 'word',
    'xls': 'word',
    'txt': 'lines',
}


@register.filter(name='mimetype')
def get_mimetype(value, *args):
    type, _ = guess_type(value)
    return type


@register.filter(name='file_name')
def get_file_name(value, n=None):
    _, file_name = os.path.split(value)
    name, extension = os.path.splitext(file_name)
    if name and n and len(name) > n and n > 3:
        name = f'{name[:n-3]}...'
        file_name = name + extension

    return file_name


@register.filter(name='file_icon')
def get_file_icon(value, *args):
    _, extension = os.path.splitext(value)

    if str(extension).startswith('.'):
        extension = extension[1:]
    icon_name = ICON_MAP.get(extension)

    if icon_name:
        return f'fa-file-{icon_name}'

    return 'fa-file'
