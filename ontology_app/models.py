from django.db import models


class Habilidade(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Habilidade")
        verbose_name_plural = ("Habilidades")

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("Habilidade_detail", kwargs={"pk": self.pk})


class Perfil(models.Model):
    nome = models.CharField(max_length=50)
    habilidade = models.ForeignKey(Habilidade, on_delete=models.PROTECT)

    class Meta:
        verbose_name = ("Perfil")
        verbose_name_plural = ("Perfis")

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("Perfil_detail", kwargs={"pk": self.pk})


class Sujeito(models.Model):
    nome = models.CharField('Objeto do jogo', max_length=50)

    class Meta:
        verbose_name = ("Sujeito")
        verbose_name_plural = ("Sujeitos")

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("Sujeito_detail", kwargs={"pk": self.pk})


class Jogo(models.Model):
    nome = models.CharField(max_length=50)
    sujeito = models.ForeignKey(Sujeito, on_delete=models.PROTECT)

    class Meta:
        verbose_name = ("Jogo")
        verbose_name_plural = ("Jogos")

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("Jogo_detail", kwargs={"pk": self.pk})


class Jogador(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Jogador")
        verbose_name_plural = ("Jogadores")

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("Jogador_detail", kwargs={"pk": self.pk})
