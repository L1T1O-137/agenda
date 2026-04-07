from django.contrib import messages
from django.core.paginator import Paginator
from django.views.generic import TemplateView, ListView


class IndexView(TemplateView):
    template_name = 'index.html'



