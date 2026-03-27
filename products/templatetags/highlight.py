import re
from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def highlight(text, query):
    if not query:
        return text

    escaped_text = escape(text)
    escaped_query = re.escape(escape(query))

    highlighted = re.sub(
        f'({escaped_query})',
        r'<mark style="background-color: #ede9fe; color: #5b21b6; padding: 0 2px; border-radius: 3px;">\1</mark>',
        escaped_text,
        flags=re.IGNORECASE
    )

    return mark_safe(highlighted)