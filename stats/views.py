from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView
from .models import Statistics, OnePLayer, TwoGames
from django.contrib.auth.models import User
from users.forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from tournament.models import Four

# Create your views here.
class StatsListView(LoginRequiredMixin, ListView):
    model = OnePLayer
    template_name = 'stats/stats.html'
    context_object_name = 'stats'
    ordering = ['-points'] 
    paginate_by = 10
    title = 'Stats Ranking'


class UserStatsListView(LoginRequiredMixin, ListView):
    model = OnePLayer
    template_name = 'stats/user-stats.html'
    context_object_name = 'stats'
    ordering = ['-points'] 
    title = 'User-Stats-Detail'   

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return OnePLayer.objects.filter(player=user).order_by('-points')

class StatsDetailView(LoginRequiredMixin, DetailView):
    model = OnePLayer
    title = 'Stats-Detail'

class StatsCreateView(LoginRequiredMixin,CreateView):
    model = OnePLayer
    fields = '__all__'
    title = 'Play'

    def form_valid(self, form):
        messages.success(self.request, f'Hey {form.instance.player}, check your rank')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('stat-detail', kwargs={'pk': self.object.pk})

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(StatsCreateView, self).get_form_kwargs(*args, **kwargs)
        return kwargs

class PlayCardCreateView(LoginRequiredMixin, CreateView):
    model = OnePLayer
    fields = '__all__'
    title = 'Play-Card'

    def form_valid(self, form):
        messages.success(self.request, f'Hey {form.instance.player}, compare your stats')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('compare-card', kwargs={'pk': self.object.pk})

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(PlayCardCreateView, self).get_form_kwargs(*args, **kwargs)
        return kwargs

    def get_context_data(self,  *args, **kwargs):
        """ Get context variables for rendering the template. """
        context = super(PlayCardCreateView, self).get_context_data(*args, **kwargs)
        player = get_object_or_404(OnePLayer, pk=self.kwargs['away'])
        context['player'] = player
        return context

class PlayCardDetailView(LoginRequiredMixin, DetailView):
    model = OnePLayer
    title = 'Card-Detail'

    def get_context_data(self, *args, **kwargs):
        context = super(PlayCardDetailView, self).get_context_data(*args, **kwargs)
        player = get_object_or_404(OnePLayer, pk=self.kwargs['away'])
        context['player'] = player
        return context

class TwoGamesCreateView(LoginRequiredMixin, CreateView):
    model = TwoGames
    fields = '__all__'
    title = 'Play-Two'

    def form_valid(self, form):
        messages.success(self.request, f'Hey {form.instance.player}, compare your stats')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('two-games-card', kwargs={'pk': self.object.pk})

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(TwoGamesCreateView, self).get_form_kwargs(*args, **kwargs)
        return kwargs

    def get_context_data(self, *args, **kwargs):
        context = super(TwoGamesCreateView, self).get_context_data(*args, **kwargs)
        challenge = get_object_or_404(Four, pk=self.kwargs['pk'])
        context['challenge'] = challenge
        return context

class TwoGamesDetailView(LoginRequiredMixin, DetailView):
    model = TwoGames
    title = 'Two-Games-Detail'

    