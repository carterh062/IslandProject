from django.conf.urls import patterns, url

urlpatterns = patterns('Home.views',
	url(r'^$', 'home', name='home'),
)
