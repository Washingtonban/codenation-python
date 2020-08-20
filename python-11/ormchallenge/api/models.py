from django.core.validators import (
    MinLengthValidator,
    EmailValidator,
    validate_ipv4_address
)
from django.db import models
import datetime

# Create your models here.
LEVEL_CHOICES = [
    ('critical', 'critical.'),
    ('debug', 'debug'),
    ('error', 'error'),
    ('warning', 'warning'),
    ('information', 'info'),
]

min_validator = MinLengthValidator(8, 'the password cant be small then 8')

class UserManager(models.Manager):
    def get_active_users(self):
        #  Traga todos os uarios ativos, seu último login deve ser menor que 10 dias.
        today_less_ten = datetime.date.today() - datetime.timedelta(10)
        queryset = User.objects.filter(last_login__gte=today_less_ten)
        return queryset
    
    def get_amount_users(self):
        #  Retorne a quantidade total de usuarios do sistema
        quertset = User.objects.count()
        return quertset


    def get_admin_users(self):
        #  Traga todos os usuarios com grupo = 'admin'
        queryset = User.objects.filter(group__name='admin')
        return queryset
    

class EventManager(models.Manager):
    #  Traga todos os eventos com tipo debug
    def get_all_debug_events(self):
        queryset = Event.objects.filter(level='debug')
        return queryset
    
    #  Traga todos os eventos do tipo critico de um usuário específico
    def get_all_critical_events_by_user(self, agent):
        queryset = Event.objects.filter(level='critical', agent=agent)
        return queryset
    

class AgentManager(models.Manager):
    #  Traga todos os agentes de associados a um usuário pelo nome do usuário
    def get_all_agents_by_user(self, username):
        queryset = Agent.objects.filter(user__name=username)
        return queryset


class GroupManager(models.Manager):
    #  Traga todos os grupos que contenham alguem que possua um agente que possuem eventos do   tipo information
    def get_all_events_by_group(self):
        queryset = Group.objects.filter(user__agent__event__level='information')
        return queryset


class Group(models.Model):
    objects = GroupManager()
    name = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class User(models.Model):
    objects = UserManager()
    name = models.CharField(max_length=50)
    email = models.EmailField(validators=[EmailValidator], null=True)
    password = models.CharField(max_length=50, validators=[min_validator])
    last_login = models.DateField(default=datetime.date.today)
    group = models.ManyToManyField(Group)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Agent(models.Model):
    objects = AgentManager()
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    address = models.GenericIPAddressField(validators=[validate_ipv4_address], null=True)
    status = models.BooleanField(default=False)
    env = models.CharField(max_length=20)
    version = models.CharField(max_length=5)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Event(models.Model):
    objects = EventManager()
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    data = models.TextField(max_length=500)
    agent = models.OneToOneField(Agent, on_delete=models.PROTECT)
    arquivado = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.level +' in ' + self.agent.name

    class Meta:
        ordering = ['date']
