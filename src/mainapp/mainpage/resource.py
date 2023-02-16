from django.shortcuts import render
from django.views.generic import View


class MainPage(View):
    @staticmethod
    def get(request):
        return render(
            request=request,
            template_name='main.html',
            context={},
            status=200
        )
