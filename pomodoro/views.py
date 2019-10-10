from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Pomodoro
from django.contrib.auth.models import User
from users.forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from tournament.models import FourPomodoro
from rest_framework import viewsets
from .serializers import PomodoroSerializer
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)




# Create your views here.
class PomodoroListView(LoginRequiredMixin, ListView):
    model = Pomodoro
    template_name: 'pomodoro/pomodoros.html'
    ordering = ['-createdAt']
    context_object_name = 'pomodoros'
    paginate_by = 10
    title = 'Pomodoros'
     
     
class PomodoroDetailView(LoginRequiredMixin, DetailView): 
    model = Pomodoro
    title = 'Pomodoro-Detail'

#
class PomodoroCreateView(LoginRequiredMixin, CreateView):
    model = Pomodoro
    title = 'Pomodoro-Create'
    fields = ['title','task_one', 'task_two', 'task_three', 
        'task_four']

    def form_valid(self, form):
        form.instance.player = self.request.user
        messages.success(self.request, f'Hey {form.instance.player}, time to get in the zone')
        return super(PomodoroCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('single-play', kwargs={'pk': self.object.pk})

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(PomodoroCreateView, self).get_form_kwargs(*args, **kwargs)
        return kwargs

#
class PomodoroSingleUpdateView(LoginRequiredMixin, UpdateView):
    model = Pomodoro
    title = 'Pomodoro-Play'
    fields = '__all__'

    def form_valid(self, form):
        form.instance.player = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        task = self.get_object()
        if self.request.user == task.player:
            return True
        return False


class PomodoroGroupCreateView(LoginRequiredMixin, CreateView):
    model = Pomodoro
    title = 'Pomodoro-Create'
    fields = ['title','task_one', 'task_two', 'task_three', 
        'task_four', 'donation']

    def form_valid(self, form):
        form.instance.player = self.request.user
        messages.success(self.request, f'Hey {form.instance.player}, time to get in the zone')
        return super(PomodoroGroupCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('pomodoro-play', kwargs={'challenge': self.kwargs['challenge'], 'pk': self.object.pk})

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(PomodoroGroupCreateView, self).get_form_kwargs(*args, **kwargs)
        return kwargs

    def get_context_data(self, *args, **kwargs):
        context = super(PomodoroGroupCreateView, self).get_context_data(*args, **kwargs)
        challenge = get_object_or_404(FourPomodoro, pk=self.kwargs['challenge'])
        context['challenge'] = challenge
        return context


class PomodoroUpdateView(LoginRequiredMixin, UpdateView):
    model = Pomodoro
    title = 'Pomodoro-Play'
    fields = '__all__'

    def form_valid(self, form):
        form.instance.player = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        task = self.get_object()
        if self.request.user == task.player:
            return True
        return False

    def get_context_data(self, *args, **kwargs):
        context = super(PomodoroUpdateView, self).get_context_data(*args, **kwargs)
        challenge = get_object_or_404(FourPomodoro, pk=self.kwargs['challenge'])
        context['challenge'] = challenge
        return context

class PomodoroAPI(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Pomodoro.objects.all()
    serializer_class = PomodoroSerializer