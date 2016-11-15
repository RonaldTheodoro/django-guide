from django.conf.urls import url
from .views import index
from .views import detail
from .views import results
from .views import vote


urlpatterns = [
    # http://localhost:8000/
    url(r'^$', index, name='index'),
    # http://localhost:8000/1/
    url(r'^(?P<question_id>\d+)/$', detail, name='detail'),
    # http://localhost:8000/1/results/
    url(r'^(?P<question_id>\d+)/results/$', results, name='results'),
    # http://localhost:8000/1/vote/
    url(r'^(?P<question_id>\d+)/vote/$', vote, name='vote'),
]