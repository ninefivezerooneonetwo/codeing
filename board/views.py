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

    @request_mapping("/notice/notice", method="get") #공지사항
    def notice(self, request):
        objs = Board.objects.all();
        context = {
            'objs': objs
        };
        return render(request, 'notice/notice.html', context);

    @request_mapping("/info/info", method="get") #정보게시판
    def info(self, request):
        objs = Board.objects.all();
        context = {
            'objs': objs
        };
        return render(request, 'info/info.html', context);

    @request_mapping("/free/free", method="get") #자유게시판
    def free(self, request):
        objs = Board.objects.all();
        context = {
            'objs':objs
        };
        return render(request, 'free/free.html',context);

    @request_mapping("/qna/qna", method="get") #질문게시판
    def qna(self, request):
        objs = Board.objects.all();
        context = {
            'objs': objs
        };
        return render(request, 'qna/qna.html',context);

    @request_mapping("/project/project", method="get") #프로젝트
    def project(self, request):
        objs = Board.objects.all();
        context = {
            'objs': objs
        };
        return render(request, 'project/project.html', context);

    @request_mapping("/study/study", method="get") #스터디
    def study(self, request):
        objs = Board.objects.all();
        context = {
            'objs': objs
        };
        return render(request, 'study/study.html',context);

    @request_mapping("/post", method="get")
    def post(self, request):
        return render(request, 'post.html');

    @request_mapping("/wiki/wiki", method="get")
    def wiki(self, request):
        return render(request, 'wiki/wiki.html');