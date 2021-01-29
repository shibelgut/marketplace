from django import template
from django.template.defaultfilters import stringfilter
import datetime
import pytz

register = template.Library()


@register.filter
@stringfilter
def inverse(value):
    return value[::-1]


@register.simple_tag
def current_time(format_string):
    tz_tomsk = pytz.timezone('Asia/Tomsk')
    return datetime.datetime.now(tz_tomsk).strftime(format_string)