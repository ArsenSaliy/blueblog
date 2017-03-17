from blog.views import NewBlogView
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
# from django.views.generic import TemplateView
from accounts.views import UserRegistrationView
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from blog.views import HomeView
from blog.views import UpdateBlogView
from blog.views import UpdateBlogPostView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', TemplateView.as_view(template_name='base.html'), name='home'),
    url(r'^new-user/$', UserRegistrationView.as_view(), name='user_registration'),
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page':'/login/'}, name='logout'),
    url(r'^blog/new/$', NewBlogView.as_view(), name='new-blog'),
    # url(r'^$', TemplateView.as_view(), name='home'),
    url(r'^blog/(?P<pk>\d+)/update/$', UpdateBlogView.as_view(), name='update-blog'),
    url(r'blog/post/new/$', NewBlogPostView.as_view(), name='new-blog-post'),
    url(r'blog/post/(?P<pk>\d+)/update/$', UpdateBlogPostView.as_view(), name='update-blog-post'),
    url(r'^blog/post/(?P<pk>\d+)/$', BlogPostDetailsView.as_view(), name='blog-post-details'),
]	
