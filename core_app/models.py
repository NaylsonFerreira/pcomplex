from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from storages.backends.ftp import FTPStorage
from rest_framework.authtoken.models import Token
SERVIDOR_FTP_WEB = FTPStorage()

GENERO = (('M', 'Masculino'), ('F', 'Feminino'))


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, null=True)
    nome = models.CharField(
        'Nome completo',
        max_length=50,
        null=True,
        blank=True)
    apelido = models.CharField(
        'Como gostaria de ser chamado?',
        max_length=50,
        null=True,
        blank=True)
    foto = models.ImageField(
        "Foto do perfil",
        upload_to='profiles/',
        storage=SERVIDOR_FTP_WEB,
        null=True,
        blank=True)
    sobre = models.TextField("Escreva algo sobre você", null=True, blank=True)
    whatsapp = models.CharField(max_length=50, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    idade = models.IntegerField('Idade', default=18, null=True, blank=True)
    genero = models.CharField(
        'Gênero',
        choices=GENERO,
        max_length=10,
        default='M',
        null=True,
        blank=True)

    def __str__(self):
        return str(self.email)

    def get_absolute_url(self):
        return ('/profile')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, **kwargs):
    Profile.objects.get_or_create(user=instance, email=instance.username)
    Token.objects.get_or_create(user=instance)


@receiver(post_save, sender=Profile)
def save_user_profile(sender, instance, created, ** kwargs):
    if instance.user.username != instance.email:
        instance.user.username = instance.email
    if instance.user.email != instance.email:
        instance.user.email = instance.email
    instance.user.save()
