from django.conf.urls import patterns, include, url 

urlpatterns = patterns('main.views',
  url(r'^home/$', 'home', name='home'),
  url(r'^connect/gmail/$', 'connect_gmail', name='connect_gmail'),
  url(r'^classify/$', 'classify', name='classify'),
  url(r'^save/$', 'save_contact', name='save_contact'),
  url(r'^search/$', 'search', name='search'),
  url(r'^search/contact/$', 'search_contact', name='search_contact'),
  url(r'^profile/$', 'profile', name='profile'),
  url(r'^tag/$', 'tag', name='tag'),
)
