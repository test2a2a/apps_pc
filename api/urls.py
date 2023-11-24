
from django.urls import path, include
from . import views
urlpatterns = [
    path("",views.index),
    #1  http://127.0.0.1:8000/no_rest_no_model
    path("no_rest_no_model",views.no_rest_no_model),
    #2  http://127.0.0.1:8000/no_rest_from_model
    path("no_rest_from_model",views.no_rest_from_model),
    #3.1 GET POST from rest framwork function based view @api_view
    #http://127.0.0.1:8000/fbv_move
    path("fbv_move",views.fbv_move),
    #3.2 GEY PUT DELETE from rest framwork function based view @api_view
    #http://127.0.0.1:8000/fbv_move_id/1
    path("fbv_move_id/<int:id>",views.fbv_move_id),



#====================user==================================
    # http://127.0.0.1:8000/fbv_user
    path("fbv_user",views.fbv_user),

]

