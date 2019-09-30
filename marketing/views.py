from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.models import User
from .models import Groups
from rest_framework import viewsets
from .serializers import GroupsSerializer

class HomePage(ListView):
    model = Groups
    template_name = 'marketing/home.html'
    context_object_name = 'group'
    paginate_by = 1
    ordering = ['-created_at']
    title = 'Tournament'

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        try:
            group1 = get_object_or_404(Groups, group=1)
            context['group1'] = group1
            group2 = get_object_or_404(Groups, group=2)
            context['group2'] = group2
        except:
            pass
        
        return context

class GroupAPI(viewsets.ModelViewSet):
    queryset = Groups.objects.all()
    serializer_class = GroupsSerializer

    

