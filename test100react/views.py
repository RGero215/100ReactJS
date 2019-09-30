from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Test100React
from django.contrib import messages
from rest_framework import viewsets
from .serializers import Test100ReactSerializer

# Create your views here.
class Test100ReactListView(ListView):
    model = Test100React
    template_name = 'test100react/index.html'
    context_object_name = 'tests'
    ordering = ['-points'] 
    paginate_by = 10
    title = 'Tests-Ranking'

class Test100ReactDetailView(DetailView):
    model = Test100React
    title = 'Test-Detail'

class Test100ReactCreate(CreateView):
    model = Test100React
    fields = '__all__'
    title = 'Take-Test'
    
    def form_valid(self, form):
        messages.success(self.request, f'Hey {form.instance.player}, check your test100react rank')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('test-detail',  kwargs={'pk' : self.object.pk})

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(Test100ReactCreate, self).get_form_kwargs(
            *args, **kwargs)
        return kwargs

class Test100ReactPlayCreate(CreateView):
    model = Test100React
    fields = '__all__'
    title = 'Play-Test'

    def form_valid(self, form):
        messages.success(self.request, f'Hey {form.instance.player}, compare your stats')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('play-detail', kwargs={'away': self.kwargs['away'], 'pk' : self.object.pk})

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(Test100ReactPlayCreate, self).get_form_kwargs(
            *args, **kwargs)
        return kwargs

    def get_context_data(self,  *args, **kwargs):
        """ Get context variables for rendering the template. """
        context = super(Test100ReactPlayCreate, self).get_context_data(*args, **kwargs)
        player = get_object_or_404(Test100React, pk=self.kwargs['away'])
        context['player'] = player
        return context

class Test100ReactPlayDetailView(DetailView):
    model = Test100React
    title = 'Player-Detail'

    def get_context_data(self, *args, **kwargs):
        """ Get context variables for rendering the template. """
        context = super(Test100ReactPlayDetailView, self).get_context_data(*args, **kwargs)
        player = get_object_or_404(Test100React, pk=self.kwargs['away'])
        context['player'] = player
        return context

class PlayerListView(ListView):
    model = Test100React
    template_name = 'test100react/player-list.html'
    context_object_name = 'tests'
    ordering = ['-points']
    title = 'Player Detail'

    def get_queryset(self):
        return Test100React.objects.filter(player=self.kwargs.get('player')).order_by('-points')


class Test100ReactAPI(viewsets.ModelViewSet):
    queryset = Test100React.objects.all()
    serializer_class = Test100ReactSerializer