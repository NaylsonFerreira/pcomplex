from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.http import JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .serializers import ProfileSerializer
import json
from .models import Profile
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from django.core.exceptions import ValidationError


@csrf_exempt
def singup_json(request):
    try:
        dados = json.loads(request.body)
        email = dados['email']
        password = dados['password']
    except BaseException:
        email = request.POST.get('email')
        password = request.POST.get('password')

    if not email or not password:
        resultado = {
            "error": "campos obrigatorios faltando",
            "campos": {
                "email": "",
                "password": ""
            }
        }
        return JsonResponse(resultado, safe=False, status=400)

    try:
        validate_email(email)
    except BaseException:
        resultado = {'email': 'E-mail inválido'}
        return JsonResponse(resultado, safe=False, status=400)

    form = UserCreationForm({
        'username': email,
        'password1': password,
        'password2': password
    })
    if form.is_valid():
        form.save()
        user = authenticate(username=email, password=password)
        token = Token.objects.get(user=user)
        return JsonResponse({'token': token.key}, safe=False, status=200)
    errors = json.loads(form.errors.as_json())
    return JsonResponse(errors, safe=False, status=400)


def singup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            try:
                validate_email(username)
            except ValidationError:
                return render(request, 'core_app/singup.html', {
                    'form': form,
                    'erros': {'email': 'Por favor digite um Email valido'},
                }, status=400)
            form.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    if form:
        status = 400
    else:
        status = 200
        form = UserCreationForm()
    return render(request, 'core_app/singup.html',
                  {'form': form}, status=status)


class ProfileJson(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileListView(ListView):
    model = Profile
    paginate_by = 10
    ordering = 'email'


class ProfileUpdateView(UpdateView):
    model = Profile
    fields = [
        'email',
        'nome',
        'apelido',
        'foto',
        'sobre',
        'whatsapp',
        'instagram',
        'idade',
        'genero'
    ]
    template_name = 'core_app/form.html'

    def dispatch(self, request, *args, **kwargs):
        instancia = self.get_object()
        if instancia.user.pk != request.user.pk and not request.user.is_superuser:
            return redirect(instancia)
        return super(ProfileUpdateView, self).dispatch(
            request, *args, **kwargs)
