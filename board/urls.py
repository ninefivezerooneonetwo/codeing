from django_request_mapping import UrlPattern

from board.views import MyView
from board.views_info import InfoView

urlpatterns = UrlPattern();
urlpatterns.register(MyView);
urlpatterns.register(InfoView);