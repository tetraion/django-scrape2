from django.views.generic import FormView
from requests.api import request
from requests.models import Response

from . import forms

from . import scraping 

import json
import requests


class IndexView(FormView):
    form_class = forms.TextForm
    template_name = "index.html"

    def a(request):
        a = request.post
        print(a)


    def form_valid(self, form):
        data = form.cleaned_data
        search = data["search"]
        request = self.request

        

        if request.method == 'POST':
            if "nomal" in request.POST:
                data_rakuten = scraping.sea(search)
                total = 0
                for datum in data_rakuten:
                    total = total + datum[3]
                    
                ave_price = total/len(data_rakuten)
                ave_price = "平均価格"+str(ave_price)
            elif "min"  in request.POST:
                data_rakuten = scraping.sea_min(search)

                ave_price = data_rakuten[0][3]
                ave_price = "最安価格"+str(ave_price)
        
        
        kekka = "楽天"


        ctxt = self.get_context_data(data_rakuten=data_rakuten, kekka="検索結果_"+kekka, form=form, ave_price=ave_price)
        return self.render_to_response(ctxt)
