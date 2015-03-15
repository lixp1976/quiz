from django import template
import time

__author__ = 'djud'

register = template.Library()


@register.filter
def quiz_duration(quiz_object):
    def timestamp(dt):
        return int(time.mktime(dt.timetuple()))
    return human_duration(
        timestamp(quiz_object.finished) -
        timestamp(quiz_object.started))


@register.filter
def human_duration(seconds):
    minutes = 0
    hours = 0
    days = 0
    seconds = int(seconds)
    if seconds >= 60:
        minutes = int(seconds / 60)
        seconds -= minutes * 60
    if minutes >= 60:
        hours = int(minutes / 60)
        minutes -= hours * 60
        if hours >= 24:
            days = int(hours / 24)
            hours -= days * 24
    result = " %d сек." % seconds
    if minutes:
        result = " %d мин." % minutes + result
    if hours:
        result = " %d ч." % hours + result
    if days:
        result = " %d д." % days + result

    return result
