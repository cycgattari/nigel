from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection

from . models import Page, Unidades, Mediciones
from .forms import ContactForm

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


def index(request, pagename):
    pagename = '/' + pagename
    pg = get_object_or_404(Page, permalink=pagename)
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        'page_list': Page.objects.all()
    }
    return render(request, 'pages/page.html', context)

def contact(request):
    submitted = False
    if request.method == 'POST': # if there is info
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # assert False
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
                connection=con
                )
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'pages/contact.html', {
    'form': form,
    'page_list': Page.objects.all(),
    'submitted': submitted})


def deptos(request):
    unidades = Unidades.objects.filter().order_by('unidad')
    return render(request, 'pages/deptos.html', {'unidades': unidades})

def mediciones(request):
    unidades = Mediciones.objects.filter().order_by('mes_medicion')
    return render(request, 'pages/mediciones.html', {'unidades': unidades})

#class Register(CreateView):
#   template_name = 'registration/register.html'
#    form_class = UserCreationForm # form to use
#    success_url = reverse_lazy('register-success') # rediect cuando esta todo OK!
# reverse o r.lazy va un nivel para arriba
#    def form_valid(self, form):# buil it method to save to database
#        form.save()
#        return HttpResponseRedirect(self.success_url)
