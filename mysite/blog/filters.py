import django_filters
from .models import Post
from django import forms


class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='search', 
                    widget=forms.TextInput(attrs={'placeholder': 'Search'}))

    class Meta:
        model = Post
        fields = ['title']

    