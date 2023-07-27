from django.http import HttpResponse
from django.template import loader
from .models import detale, zamowienia
from django.http import Http404
from django.shortcuts import render,redirect
from .forms import zamowienia_forma
from django.utils import timezone

def home(request):
  template = loader.get_template('./home.html')
  return HttpResponse(template.render())



def lista_detali(request):
    lista_detali_najnowsze = detale.objects.order_by("id")[:5]
    template = loader.get_template("./lista_detali.html")
    contex = {
       "lista_detali_najnowsze" : lista_detali_najnowsze
    }
    return HttpResponse(template.render(contex, request))


def szczegoly_detalu(request, detal_id):
    template = loader.get_template("./szczegoly_detalu.html")
    try:
        detal = detale.objects.get(pk = detal_id)
    except detale.DoesNotExist:
        raise Http404("Qobietk nie istnieje")
    contex = {
        "detal": detal}
    return HttpResponse(template.render(contex, request))

def zamowienia(request):
    dzisiejsza_data = timezone.now().date()
    forma_zamowienia = zamowienia_forma()
    contex = {
        'forma_zamowienia': forma_zamowienia,
        'dzisiejsza_data' : dzisiejsza_data,
    }
    if request.method == 'POST':
        forma_zamowienia = zamowienia_forma(request.POST)
        if forma_zamowienia.is_valid():
            forma_zamowienia.save()
        return redirect('zamowienia:popup_view')  # Redirect to a success page after form submission
    else:
        forma_zamowienia = zamowienia_forma()
    return render(request, './zamowienia_forma.html',contex)


def popup_view(request):
    # Your view logic here
    return render(request, './pop_up.html')


    
