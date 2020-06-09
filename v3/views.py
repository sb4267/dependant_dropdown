from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse_lazy
from .forms import update_cars
from django.views.generic import ListView, CreateView, UpdateView
from . models import Models_name,Brand,V_type,Main_table
from . project_imp import Predict_Value


def load_cities(request):
    brand_id = request.GET.get('country')
    models_name = Models_name.objects.filter(model_name_id=brand_id)

    return render(request, 'v3/model_list_option.html', {'models_name': models_name})

def load_vehicle_type(request):
    model_id_vehicle = request.GET.get('vid')
    vehicles_type = V_type.objects.filter(model_n_id=model_id_vehicle)
    return render(request, 'v3/vehicle_list_option.html', {'vehicles_type': vehicles_type})

class PersonCreateView(CreateView):
    model = Main_table
    form_class = update_cars
    success_url = '/thanks/'

    def form_valid(self, form_class):
        my_var = self.request.POST.get('brand_name_1')
        selected_mod=Brand.objects.filter(id=my_var)
        brand=self.request.POST.get('model_name')
        selected_brand=Models_name.objects.filter(id=brand)
        v_tup=self.request.POST.get('model_n')
        selected_v_tup=V_type.objects.filter(id=v_tup)
        gb=str(self.request.POST.get('gearbox'))
        pp=int(self.request.POST.get('power_ps'))
        km=int(self.request.POST.get('kilometer'))
        ft=str(self.request.POST.get('fuel_type'))
        va=int(self.request.POST.get('duration'))
        vt = str(selected_v_tup)
        m = str(selected_brand)
        b = str(selected_mod)
        price_value=Predict_Value(vt,gb,pp,m,km,ft,b,va)
        html = "<html><body><h1>Estimated Price is: %s </h1></body></html>" % price_value[0]
        return HttpResponse(html)
