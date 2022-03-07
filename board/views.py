from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping

from board.models import Board


@request_mapping("")
class MyView(View):

    @request_mapping("/", method="get")
    def home(self,request):
        objs = Board.objects.all();
        context = {
            'objs': objs
        };
        return render(request,'home.html',context);

    @request_mapping("/notice", method="get") #공지사항
    def notice(self, request):
        objs = Board.objects.all();
        context = {
            'objs': objs
        };
        return render(request, 'notice.html', context);

    @request_mapping("/info", method="get") #정보게시판
    def info(self, request):
        objs = Board.objects.all();
        context = {
            'objs': objs
        };
        return render(request, 'info.html', context);

    @request_mapping("/free", method="get") #자유게시판
    def free(self, request):
        objs = Board.objects.all();
        context = {
            'objs':objs
        };
        return render(request, 'free.html',context);

    @request_mapping("/qna", method="get") #질문게시판
    def qna(self, request):
        objs = Board.objects.all();
        context = {
            'objs': objs
        };
        return render(request, 'qna.html',context);

    @request_mapping("/project", method="get") #프로젝트
    def project(self, request):
        objs = Board.objects.all();
        context = {
            'objs': objs
        };
        return render(request, 'project.html', context);

    @request_mapping("/study", method="get") #스터디
    def study(self, request):
        objs = Board.objects.all();
        context = {
            'objs': objs
        };
        return render(request, 'study.html',context);

    @request_mapping("/post", method="get")
    def post(self, request):
        return render(request, 'post.html');

    @request_mapping("/codeingwiki", method="get")
    def wiki(self, request):
        return render(request, 'wiki.html');