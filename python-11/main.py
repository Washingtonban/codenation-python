from api.models import User, Agent, Event, Group
import datetime

def get_active_users():
    return User.objects.filter(last_login__gte=(datetime.date.today() - datetime.timedelta(10)))


def get_amount_users():
    return User.objects.count()


def get_admin_users():
    return User.objects.filter(group__name='admin')


def get_all_debug_events():
    return Event.objects.filter(level='debug')


def get_all_critical_events_by_user(agent):
    return Event.objects.filter(level='critical', agent=agent)


def get_all_agents_by_user(username):
    return Agent.objects.filter(user__name=username)


def get_all_events_by_group():
    return Group.objects.filter(user__agent__event__level='information')
