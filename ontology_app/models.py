from django.db import models
from django.urls import reverse
from django.contrib import admin
from django.utils import timezone, text
from django.core import validators
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage


SERVIDOR_FTP_WEB = FileSystemStorage()


class Ontology(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    file = models.FileField(
        'Arquivo',
        upload_to="ontologies/",
        storage=SERVIDOR_FTP_WEB,
        validators=[validators.FileExtensionValidator(['owl'])])

    class Meta:
        verbose_name = ("Ontology")
        verbose_name_plural = ("Ontologies")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ontology_app:OntologyDetail", kwargs={"pk": self.pk})


@receiver(pre_save, sender=Ontology)
def save_ontology(sender, instance, **kwargs):
    if not instance.slug:
        slug = "%s%s" % (instance.name, instance.created_at.microsecond)
        instance.slug = text.get_valid_filename(slug)


class OntologyAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user', 'slug', 'created_at', 'updated_at')
    readonly_fields = ('slug', 'created_at', 'updated_at')  # 'user',
    list_display_links = ('__str__',)
    empty_value_display = '--'
    fieldsets = [
        ('Informações gerais', {'fields': ['name', 'file']}),
        ('Informações geradas automaticamente', {'classes': (
            'collapse',), 'fields': ['user', 'slug', 'created_at', 'updated_at']}),
    ]

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.user = request.user
        super().save_model(request, obj, form, change)


class Jogo(models.Model):
    nome = models.CharField(max_length=50)
    link = models.URLField(max_length=200, null=True, blank=True)
    icon = models.URLField(max_length=200, null=True, blank=True)
    slug = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Jogo"
        verbose_name_plural = "Jogos"

    def __str__(self):
        return self.nome


class JogoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'slug', 'created_at', 'updated_at')
    readonly_fields = ('slug', 'created_at', 'updated_at')
    list_display_links = ('__str__',)
    empty_value_display = '--'
    search_fields = ['nome', 'slug']


@receiver(pre_save, sender=Jogo)
def save_jogo(sender, instance, **kwargs):
    if instance.link:
        slug = instance.link.split('?id=')[-1].split('&')[0]
        instance.slug = slug
