from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, permissions
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from .serializers import CustomUserSerializers
from .permissions import IsStudent, IsCustodian, IsAdmin, IsCustodianOrAdmin

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


class Login(LoginView):
    template_name = 'accounts/login.html'


class Logout(LogoutView):
    template_name = 'accounts/logged_out.html'


@login_required
def profile(request):
    return render(request, 'accounts/profile.html', {'user': request.user})


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by("-date_joined")
    serializer_class = CustomUserSerializers
    permission_classes = [permissions.IsAuthenticated & IsCustodianOrAdmin]
    filterset_fields = ['role', 'username']
    search_fields = ['username', 'first_name', 'last_name', 'email']
    ordering_fields = ['date_joined', 'username']
