from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.http import JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from django.core.exceptions import ValidationError
from .serializers import ProfileSerializer
from .models import Profile
from rest_framework.decorators import api_view
from rest_framework import viewsets
import json


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
    form = False
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


def loadUser(request):
    if request.auth:
        token = request.auth
        user = Token.objects.get(key=token).user
        return user

    if request.user:
        return request.user


@api_view(['GET'])
def me(request):
    user = loadUser(request)
    profile = ProfileSerializer(user.profile)
    return JsonResponse(profile.data, safe=False, status=200)


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)
