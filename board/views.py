from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping

from board.models import Board


@request_mapping("")
class MyView(View):

    @request_mapping("/", method="get")
    def home(self,request):
        return render(request,'home.html');

    @request_mapping("/notice", method="get")
    def notice(self, request):
        return render(request, 'notice.html');

    @request_mapping("/codeingwiki", method="get")
    def wiki(self, request):
        return render(request, 'wiki.html');

    @request_mapping("/free", method="get")
    def free(self, request):
        objs = Board.objects.all();
        context = {
            'objs':objs
        };
        return render(request, 'free.html',context);

    @request_mapping("/create", method="get")
    def create(self, request):
        return render(request, 'create_form.html');