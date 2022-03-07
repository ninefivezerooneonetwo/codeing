from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping

from board.models import Info


@request_mapping("/info")
class InfoView(View):

    @request_mapping("/", method="get")
    def info(self, request):
        return render(request, 'info.html');

