from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from store.models import Customer 

def register(request):
    form = UserCreationForm()  # Use UserCreationForm padrão para criar superusuário

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_superuser = True
            user.is_staff = True   # Defina is_staff como True para conceder privilégios de superusuário
            user.save()

            # Autentique e faça login automaticamente após o registro
            user = authenticate(username=user.username, password=form.cleaned_data['password1'])

            customer = Customer.objects.create(user=user, name = user.username, email=user.email)
            customer.save()

            login(request, user)

            messages.success(request, 'Superusuário registrado com sucesso. Agora faça o login para começar!')
            return redirect('store')
        else:
            print('Detalhes de registro inválidos')

    return render(request, "registration/register.html", {"form": form})