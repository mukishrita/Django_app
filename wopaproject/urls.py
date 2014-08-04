from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from blog import views

urlpatterns = patterns('',
# url(r'^$', views.post_list),
#url(r'^blog/(?P<pk>[0-9]+)/$', views.post_detail),
url(r'^admin/', include(admin.site.urls)),


#url(r'^blog/new/$', views.post_new,name="newblog")),

url(r'^post/new/$', views.post_new,name="newpost"),

url(r'^$', 'blog.views.index'),
url(
    r'^blog/view/(?P<slug>[^\.]+).html', 
    'blog.views.view_post', name='view_blog_post'),
url(
    r'^blog/category/(?P<slug>[^\.]+).html', 
    'blog.views.view_category', 
    name='view_blog_category'),

)