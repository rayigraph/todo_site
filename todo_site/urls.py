from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from todo import views

urlpatterns = [
    #####################home_page###########################################
    path('', views.index, name="todo"),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('logout', views.logout, name="logout"),
    ####################give id no. item_id name or item_id=i.id ############
    # pass item_id as primary key to remove that the todo with given id
    path('del/<str:item_id>', views.remove, name="del"),
    path('details/<str:item_id>', views.viewDetails, name="details"),
    ########################################################################
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)