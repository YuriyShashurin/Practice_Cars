from django.shortcuts import render
from cars_filter import models
from django.views.generic.list import ListView
from django.db.models import Q


# Create your views here.

class CarsView(ListView):
    model = models.Car
    template_name = 'cars_filter/index.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars'] = models.Car.objects.order_by().values_list('creater').distinct()
        context['models'] = models.Car.objects.order_by().values_list('model').distinct()
        context['transmission'] = models.Car.objects.order_by().values_list('transmission').distinct()
        context['colors'] = models.Car.objects.order_by().values_list('color').distinct()
        context['year_create'] = models.Car.objects.order_by().values_list('year_create').distinct()
        return context

    def get_queryset(self):
        if self.request.GET:
            get_query = Q()
            request_get = {}

            request_get['creater'] = self.request.GET.getlist('creater[]', None)
            request_get['model'] = self.request.GET.getlist('model[]', None)
            request_get['transmission'] = self.request.GET.getlist('transmission[]', None)
            request_get['color'] = self.request.GET.getlist('color[]', None)
            request_get['year_create'] = self.request.GET.getlist('year_create[]', None)

            for key, value in request_get.items():
                category = Q()
                print(key)
                for a in value:
                    category |= Q(**{key: a})
                get_query &= category
                print(get_query)

            return models.Car.objects.filter(get_query)

        else:
            return models.Car.objects.all()


