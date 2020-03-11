from datetime import date, timedelta
from django import template

register = template.Library()


@register.simple_tag
def is_allowed(user_obj: object) -> str:
    born = user_obj.birthday
    test_date = date(born.year+13, born.month, 1)
    test_date += timedelta(days=born.day-1)
    if test_date <= date.today():
        return 'allowed' 
    else: 
        return 'blocked'


@register.simple_tag
def bizzfuzz(user_num: int) -> str:
    if user_num % 3 == 0 and user_num % 5 == 0:
        return 'BizzFuzz'
    elif user_num % 5 == 0:
        return 'Fuzz'
    elif user_num % 3 == 0:
        return 'Bizz'
    else:
        return user_num
