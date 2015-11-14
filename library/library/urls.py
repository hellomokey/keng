from django.conf.urls import patterns, include, url

from django.contrib import admin
from mylib.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'library.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	
	(r'^update_book/$', updata),
	#(r'^search_author/$', search_author),
	(r'^search_result/$', search_result),
	(r'^books/$', books),
	(r'^delete/$', del_book),
	(r'^add_author/$', add_author),
	(r'^add_book/$', add_book),
	(r'^book_information/$', book_information),
	#(r'^main/$', main),
	#url(r'$', main),
	
)
