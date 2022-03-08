
from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping
from board.models import Board, User
from django.utils import timezone

@request_mapping("")
class MyView(View):

    @request_mapping("/", method="get")
    def home(self,request):
        request.session['sessionid'] = 'naise1'
        objs = Board.objects.all();
        context = {
            'objs': objs
        };
        return render(request,'home.html',context);
    # ================================================================
    @request_mapping("/notice/notice", method="get") #공지사항
    def notice(self, request):
        objs = Board.objects.all();
        context = {
            'objs': objs
        };
        return render(request, 'notice/notice.html', context);

    @request_mapping("/notice/post", method="get")  # 공지사항
    def noticepost(self, request):

        return render(request, 'notice/post.html');

    @request_mapping("/notice/notice/p", method="post")  # 공지사항
    def notice_post(self, request):
        title = request.POST['title'];
        text = request.POST['content'];
        try:
            if request.session['sessionid'] == 'naise1':

                data = Board(board_title=title, board='공지', user_id=request.session['sessionid'], wiki_id='1', board_content=text,
                             board_date=timezone.now());
                data.save()
                return render(request, 'notice/postok.html');
            else:
                raise Exception;
        except:  # id 값이 없으므로 에러가 남
            return render(request, 'notice/postfail.html');

    # ================================================================

    @request_mapping("/info/info", method="get") #정보게시판
    def info(self, request):
        objs = Board.objects.all();
        context = {
            'objs': objs
        };
        return render(request, 'info/info.html', context);

    @request_mapping("/info/post", method="get")  # 공지사항
    def infopost(self, request):
        return render(request, 'info/post.html');

    @request_mapping("/info/info/p", method="post")  # 공지사항
    def info_post(self, request):
        title = request.POST['title'];
        text = request.POST['content'];
        try:
                data = Board(board_title=title, board='정보', user_id=request.session['sessionid'], wiki_id='1',
                             board_content=text,
                             board_date= timezone.now());
                data.save()
                return render(request, 'info/postok.html');
        except:  # id 값이 없으므로 에러가 남
            return render(request, 'postfail.html');

    # ================================================================
    @request_mapping("/free/free", method="get") #자유게시판
    def free(self, request):
        objs = Board.objects.all();
        context = {
            'objs':objs
        };
        return render(request, 'free/free.html',context);

    @request_mapping("/free/post", method="get")  # 공지사항
    def freepost(self, request):

        return render(request, 'free/post.html');

    @request_mapping("/free/free/p", method="post")  # 공지사항
    def free_insert(self, request):
        title = request.POST['title'];
        text = request.POST['content'];
        objs = User.objects.all();
        request.session['sessionid'] = 'naise1'
        try:
                data = Board(board_title=title, board='자유', user_id=request.session['sessionid'], wiki_id='1',
                             board_content=text,
                             board_date=timezone.now());
                data.save()
                return render(request, 'free/postok.html');
        except:  # id 값이 없으므로 에러가 남
            return render(request, 'postfail.html');

    # ================================================================
    @request_mapping("/qna/qna", method="get") #질문게시판
    def qna(self, request):
        objs = Board.objects.all();
        context = {
            'objs': objs
        };
        print(context)
        return render(request, 'qna/qna.html',context);

    @request_mapping("/qna/post", method="get")  # 공지사항
    def qnapost(self, request):

        return render(request, 'qna/post.html');

    @request_mapping("/qna/qna/p", method="post")  # 질문
    def qna_insert(self, request):
        title = request.POST['title'];
        text = request.POST['content'];
        try:
            data = Board(board_title=title, board='질문', user_id=request.session['sessionid'], wiki_id='1',
                         board_content=text,
                         board_date=timezone.now());
            data.save()
            return render(request, 'qna/postok.html');
        except:  # id 값이 없으므로 에러가 남
            return render(request, 'postfail.html');

    # ================================================================
    @request_mapping("/project/project", method="get") #프로젝트
    def project(self, request):
        objs = Board.objects.all();
        context = {
            'objs': objs
        };
        return render(request, 'project/project.html', context);

    @request_mapping("/project/post", method="get")  # 스터디로
    def projectpost(self, request):

        return render(request, 'project/post.html');

    @request_mapping("/project/project/p", method="post")  # 질문
    def project_insert(self, request):
        title = request.POST['board_title'];
        content = request.POST['board_content'];
        num = request.POST['board_num'];
        place = request.POST['board_place'];
        recruitdate = request.POST['board_recruitdate'];
        time = request.POST['board_time'];
        on_off = request.POST['board_on_off'];
        phone = request.POST['board_phone'];
        try:
            data = Board(board_title=title, board='프로젝트', user_id=request.session['sessionid'], wiki_id='1',
                         board_content=content,
                         board_date=timezone.now(),board_num = num, board_place = place,
                         board_recruitdate = recruitdate, board_time = time, board_on_off = on_off,
                         board_phone = phone);
            data.save()
            return render(request, 'project/postok.html');
        except:  # id 값이 없으므로 에러가 남
            return render(request, 'postfail.html');

    # ================================================================
    @request_mapping("/study/study", method="get") #스터디
    def study(self, request):
        objs = Board.objects.all();
        context = {
            'objs': objs
        };
        return render(request, 'study/study.html',context);

    @request_mapping("/study/post", method="get")  # 스터디로
    def studypost(self, request):

        return render(request, 'study/post.html');

    @request_mapping("/study/study/p", method="post")  # 질문
    def study_insert(self, request):
        title = request.POST['board_title'];
        content = request.POST['board_content'];
        num = request.POST['board_num'];
        place = request.POST['board_place'];
        recruitdate = request.POST['board_recruitdate'];
        time = request.POST['board_time'];
        on_off = request.POST['board_on_off'];
        phone = request.POST['board_phone'];
        try:
            data = Board(board_title=title, board='스터디', user_id=request.session['sessionid'], wiki_id='1',
                         board_content=content,
                         board_date=timezone.now(),board_num = num, board_place = place,
                         board_recruitdate = recruitdate, board_time = time, board_on_off = on_off,
                         board_phone = phone);
            data.save()
            return render(request, 'study/postok.html');
        except:  # id 값이 없으므로 에러가 남
            return render(request, 'postfail.html');

    # ================================================================
    @request_mapping("/post", method="get")
    def post(self, request):
        return render(request, 'post.html');

    @request_mapping("/wiki/wiki", method="get")
    def wiki(self, request):
        return render(request, 'wiki/wiki.html');

