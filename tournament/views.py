from django.shortcuts import render, get_object_or_404, reverse
from django.core import serializers
from django.forms.models import model_to_dict
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Four, FourPomodoro
import simplejson as json
from stats.models import TwoGames
from pomodoro.models import Pomodoro
from rest_framework import viewsets
from .serializers import FourSerializer, FourPomodoroSerializer

# Create your views here.

class TournamentListView(ListView):
    model = Four
    template_name = 'tournament/tournament.html'
    context_object_name = 'minData'
    paginate_by = 1
    title = 'Tournaments'
    

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        print(json_dump)
        context['minData'] = json_dump
        return context

class FourPlayersListView(LoginRequiredMixin, ListView):
    model = Four
    template_name = 'tournament/four-list.html'
    context_object_name = 'players'
    ordering = ['-date_posted']
    title = 'Four-Tournaments'
    
class FourPlayersCreateView(LoginRequiredMixin, CreateView):
    model = Four
    template_name = 'tournament/four-players.html'
    fields = [ 'player_one', 'player_two', 'player_three', 'player_four']
    title = 'Challenge-Four'

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, f'{form.instance.player_one} vs {form.instance.player_two} | {form.instance.player_three} vs {form.instance.player_four}')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("tournament:four-detail", kwargs={'pk': self.object.pk})

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(FourPlayersCreateView, self).get_form_kwargs(*args, **kwargs)
        return kwargs

class FourPlayersDetailView(DetailView):
    model = Four
    template_name = 'tournament/four-detail.html'
    context_object_name = 'minData'
    title = 'Four-Detail'


    def get_context_data(self, **kwargs):
        context = super(FourPlayersDetailView, self).get_context_data(**kwargs)
        challenge = get_object_or_404(Four, pk=self.kwargs['pk'])
        
        # Player One Data
        player_one_name = challenge.player_one.username
        player_one_first = 0
        player_one_second = 0
        player_one_firstPoints = 0
        player_one_secondPoints = 0
        player_one_challenge_id = ''

        # Player Two Data
        player_two_name = challenge.player_two.username
        player_two_first = 0
        player_two_second = 0
        player_two_firstPoints = 0
        player_two_secondPoints = 0
        player_two_challenge_id = ''

        # Player Three Data
        player_three_name = challenge.player_three.username
        player_three_first = 0
        player_three_second = 0
        player_three_firstPoints = 0
        player_three_secondPoints = 0
        player_three_challenge_id = ''

        # Player Four Data
        player_four_name = challenge.player_four.username
        player_four_first = 0
        player_four_second = 0
        player_four_firstPoints = 0
        player_four_secondPoints = 0
        player_four_challenge_id = ''

        # Games query
        games = TwoGames.objects.filter(four=challenge.id)
        for game in games:
            if challenge.player_one == game.player:
                player_one_first = game.firstHome
                player_one_second = game.secondHome
                player_one_firstPoints = game.firstPoints
                player_one_secondPoints = game.secondPoints
                player_one_challenge_id = game.id
                context['player_one_final'] = game.secondFinal
            elif challenge.player_two == game.player:
                player_two_first = game.firstHome
                player_two_second = game.secondHome
                player_two_firstPoints = game.firstPoints
                player_two_secondPoints = game.secondPoints
                player_two_challenge_id = game.id
                context['player_two_final'] = game.secondFinal 
            elif challenge.player_three == game.player:
                player_three_first = game.firstHome
                player_three_second = game.secondHome
                player_three_firstPoints = game.firstPoints
                player_three_secondPoints = game.secondPoints
                player_three_challenge_id = game.id
                context['player_three_final'] = game.secondFinal
            else:
                player_four_first = game.firstHome
                player_four_second = game.secondHome
                player_four_firstPoints = game.firstPoints
                player_four_secondPoints = game.secondPoints
                player_four_challenge_id = game.id
                context['player_four_final'] = game.secondFinal
                
        # Check if all teams played
        try:
            if context['player_one_final'] and context['player_two_final'] and context['player_three_final'] and context['player_four_final']:
                challenge.ended = True
                challenge.save()
        except KeyError:
            pass
         
        
        
        # Handle Ties by points Player One and Two Match
        if player_one_first == player_two_first and player_one_challenge_id == challenge.id and player_two_challenge_id == challenge.id:
            if player_one_firstPoints > player_two_firstPoints:
                player_one_first += 1
            elif player_one_firstPoints < player_two_firstPoints:
                player_two_first += 1
            else:
                one_overall = player_one_firstPoints + player_one_secondPoints
                two_overall = player_two_firstPoints + player_two_secondPoints
                if one_overall > two_overall:
                    player_one_first += 1
                else:
                    player_two_first += 1
        
        # Handle Ties by points Player Three and Four Match
        if player_three_first == player_four_first and player_three_challenge_id == challenge.id and player_four_challenge_id == challenge.id:
            if player_three_firstPoints > player_four_firstPoints:
                player_three_first += 1
            elif player_three_firstPoints < player_four_firstPoints:
                player_four_first += 1
            else:
                three_overall = player_three_firstPoints + player_three_secondPoints
                four_overall = player_four_firstPoints + player_four_secondPoints
                if three_overall > four_overall:
                    player_three_first += 1
                else:
                    player_four_first += 1

        
        # Match for first place
        first_game_winner = player_one_second if player_one_first > player_two_first else player_two_second
        second_game_winner = player_three_second if player_three_first > player_four_first else player_four_second
        

        # Handle tie for the first place
        first_game_winner_points = player_one_secondPoints if player_one_first > player_two_first else player_two_secondPoints
        second_game_winner_points = player_three_secondPoints if player_three_first > player_four_first else player_four_secondPoints

        if first_game_winner == second_game_winner and first_game_winner + second_game_winner > 0:
            if first_game_winner_points > second_game_winner_points:
                first_game_winner += 1
            elif first_game_winner_points < second_game_winner_points:
                second_game_winner += 1
        

        # Match for the 3 place
        first_game_loser = player_one_second if player_one_first < player_two_first else player_two_second
        second_game_loser = player_three_second if player_three_first < player_four_first else player_four_second

        # Handle tie for the 3 place
        first_game_loser_points = player_one_secondPoints if player_one_first > player_two_first else player_two_secondPoints
        second_game_loser_points = player_three_secondPoints if player_three_first > player_four_first else player_four_secondPoints

        if first_game_loser == second_game_loser and first_game_loser + second_game_loser > 0:
            if first_game_loser_points > second_game_loser_points:
                first_game_loser += 1
            elif first_game_loser_points < second_game_loser_points:
                second_game_loser += 1

        # Create Bracket Object
        minData = {'teams': [[player_one_name, player_two_name], [player_three_name, player_four_name]], 'results': [[[[player_one_first,player_two_first],[player_three_first,player_four_first]],[[first_game_winner,second_game_winner],[first_game_loser, second_game_loser]]]]}
        # Seriliaze Data
        json_dump = json.dumps(minData, separators=(',', ':'))
        context['minData'] = json_dump
        return context

# 
class FourPomodoroListView(LoginRequiredMixin, ListView):
    model = FourPomodoro
    template_name = 'tournament/pomodoro-list.html'
    context_object_name = 'players'
    ordering = ['-date_posted']
    title = 'Four-Tournaments'
    
class FourPomodoroCreateView(LoginRequiredMixin, CreateView):
    model = FourPomodoro
    template_name = 'tournament/pomodoro-players.html'
    fields = [ 'player_one', 'player_two', 'player_three', 'player_four']
    title = 'Challenge-Four'

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, f'{form.instance.player_one} vs {form.instance.player_two} | {form.instance.player_three} vs {form.instance.player_four}')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("tournament:pomodoro-detail", kwargs={'pk': self.object.pk})

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(FourPomodoroCreateView, self).get_form_kwargs(*args, **kwargs)
        return kwargs

class FourPomodoroDetailView(DetailView):
    model = FourPomodoro
    template_name = 'tournament/pomodoro-detail.html'
    context_object_name = 'minData'
    title = 'Four-Detail'


    def get_context_data(self, **kwargs):
        context = super(FourPomodoroDetailView, self).get_context_data(**kwargs)
        challenge = get_object_or_404(FourPomodoro, pk=self.kwargs['pk'])
        
        # Player One Data
        player_one_name = challenge.player_one.username
        player_one_first = 0
        player_one_second = 0
        player_one_firstPoints = 0
        player_one_secondPoints = 0
        player_one_challenge_id = ''

        # Player Two Data
        player_two_name = challenge.player_two.username
        player_two_first = 0
        player_two_second = 0
        player_two_firstPoints = 0
        player_two_secondPoints = 0
        player_two_challenge_id = ''

        # Player Three Data
        player_three_name = challenge.player_three.username
        player_three_first = 0
        player_three_second = 0
        player_three_firstPoints = 0
        player_three_secondPoints = 0
        player_three_challenge_id = ''

        # Player Four Data
        player_four_name = challenge.player_four.username
        player_four_first = 0
        player_four_second = 0
        player_four_firstPoints = 0
        player_four_secondPoints = 0
        player_four_challenge_id = ''

        # Games query
        games = Pomodoro.objects.filter(four=challenge.id)
        for game in games:
            if challenge.player_one == game.player:
                player_one_first = game.firstHome
                player_one_second = game.home
                player_one_firstPoints = game.firstPoints
                player_one_secondPoints = game.points
                player_one_challenge_id = game.id
                context['player_one_final'] = game.final
            elif challenge.player_two == game.player:
                player_two_first = game.firstHome
                player_two_second = game.home
                player_two_firstPoints = game.firstPoints
                player_two_secondPoints = game.points
                player_two_challenge_id = game.id
                context['player_two_final'] = game.final 
            elif challenge.player_three == game.player:
                player_three_first = game.firstHome
                player_three_second = game.home
                player_three_firstPoints = game.firstPoints
                player_three_secondPoints = game.points
                player_three_challenge_id = game.id
                context['player_three_final'] = game.final
            else:
                player_four_first = game.firstHome
                player_four_second = game.home
                player_four_firstPoints = game.firstPoints
                player_four_secondPoints = game.points
                player_four_challenge_id = game.id
                context['player_four_final'] = game.final
                
        # Check if all teams played
        try:
            if context['player_one_final'] and context['player_two_final'] and context['player_three_final'] and context['player_four_final']:
                challenge.ended = True
                challenge.save()
        except KeyError:
            pass
         
        
        
        # Handle Ties by points Player One and Two Match
        if player_one_first == player_two_first and player_one_challenge_id == challenge.id and player_two_challenge_id == challenge.id:
            if player_one_firstPoints > player_two_firstPoints:
                player_one_first += 1
            elif player_one_firstPoints < player_two_firstPoints:
                player_two_first += 1
            else:
                one_overall = player_one_firstPoints + player_one_secondPoints
                two_overall = player_two_firstPoints + player_two_secondPoints
                if one_overall > two_overall:
                    player_one_first += 1
                else:
                    player_two_first += 1
        
        # Handle Ties by points Player Three and Four Match
        if player_three_first == player_four_first and player_three_challenge_id == challenge.id and player_four_challenge_id == challenge.id:
            if player_three_firstPoints > player_four_firstPoints:
                player_three_first += 1
            elif player_three_firstPoints < player_four_firstPoints:
                player_four_first += 1
            else:
                three_overall = player_three_firstPoints + player_three_secondPoints
                four_overall = player_four_firstPoints + player_four_secondPoints
                if three_overall > four_overall:
                    player_three_first += 1
                else:
                    player_four_first += 1

        
        # Match for first place
        first_game_winner = player_one_second if player_one_first > player_two_first else player_two_second
        second_game_winner = player_three_second if player_three_first > player_four_first else player_four_second
        

        # Handle tie for the first place
        first_game_winner_points = player_one_secondPoints if player_one_first > player_two_first else player_two_secondPoints
        second_game_winner_points = player_three_secondPoints if player_three_first > player_four_first else player_four_secondPoints

        if first_game_winner == second_game_winner and first_game_winner + second_game_winner > 0:
            if first_game_winner_points > second_game_winner_points:
                first_game_winner += 1
            elif first_game_winner_points < second_game_winner_points:
                second_game_winner += 1
        

        # Match for the 3 place
        first_game_loser = player_one_second if player_one_first < player_two_first else player_two_second
        second_game_loser = player_three_second if player_three_first < player_four_first else player_four_second

        # Handle tie for the 3 place
        first_game_loser_points = player_one_secondPoints if player_one_first > player_two_first else player_two_secondPoints
        second_game_loser_points = player_three_secondPoints if player_three_first > player_four_first else player_four_secondPoints

        if first_game_loser == second_game_loser and first_game_loser + second_game_loser > 0:
            if first_game_loser_points > second_game_loser_points:
                first_game_loser += 1
            elif first_game_loser_points < second_game_loser_points:
                second_game_loser += 1

        # Create Bracket Object
        minData = {'teams': [[player_one_name, player_two_name], [player_three_name, player_four_name]], 'results': [[[[player_one_first,player_two_first],[player_three_first,player_four_first]],[[first_game_winner,second_game_winner],[first_game_loser, second_game_loser]]]]}
        # Seriliaze Data
        json_dump = json.dumps(minData, separators=(',', ':'))
        context['minData'] = json_dump
        return context


class FourPlayersAPI(viewsets.ModelViewSet):
    queryset = Four.objects.all()
    serializer_class = FourSerializer

class FourPomodoroAPI(viewsets.ModelViewSet):
    queryset = FourPomodoro.objects.all()
    serializer_class = FourPomodoroSerializer



