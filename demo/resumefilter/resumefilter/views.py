from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

class TestPage(TemplateView):
    '''
    For testing the page
    '''
    template_name = 'test.html'

class ThanksPage(TemplateView):
    '''
    For thank you page
    '''
    template_name = 'thanks.html'

class AboutPage(TemplateView):
    '''
    For About page
    '''
    template_name = 'about.html'

class HomePage(TemplateView):
    '''
    For Home page
    '''
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        '''
        If the user is authenticated then he will be redirected to login confirmation page
        '''
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("test"))
        return super().get(request, *args, **kwargs)
