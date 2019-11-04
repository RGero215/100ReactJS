from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib import messages
from .models import Deck
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework import viewsets
from .serializers import DeckSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)


class DeckListView(ListView):
    model = Deck
    template_name = 'deck/user_decks.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'deck'
    ordering = ['-date_posted']
    paginate_by = 5
    title = 'Deck'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Deck.objects.filter(user=user).order_by('-date_posted')


class DeckCreateView(CreateView):
    model = Deck
    title = 'Deck-Create'
    fields = ['icon', 'title', 'subject', 'rating', 'screenshoot1', 'screenshoot2', 'screenshoot3']

    def form_valid(self, form):
        print('Form: ', self.request)
        form.instance.user = self.request.user
        messages.success(self.request, f'Hey {form.instance.user}, your deck is ready')
        return super(DeckCreateView, self).form_valid(form)
        

    def get_success_url(self):
        return reverse('deck-detail', kwargs={'pk': self.object.pk})

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(DeckCreateView, self).get_form_kwargs(*args, **kwargs)
        return kwargs

    
class DeckDetailView(DetailView):
    model = Deck
    title = 'Deck'

class DeckUpdateView(UpdateView):
    model = Deck
    fields = ['icon', 'title', 'subject', 'rating',]
    title = 'Update-Deck'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        deck = self.get_object()
        if self.request.user == deck.user:
            return True
        return False

class DeckDeleteView(DeleteView):
    model = Deck
    success_url = '/deck'
    title = 'Delete-Deck'

    def test_func(self):
        deck = self.get_object()
        if self.request.user == deck.user:
            return True
        return False

class DeckAPI(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer