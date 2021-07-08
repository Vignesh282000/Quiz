from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('createquestion',views.createquestion,name='createquestion'),
    path('createquestion_DB',views.createquestion_DB,name='createquestion_DB'),
    path('taketest',views.taketest,name='taketest'),
    path('get_data',views.get_data,name='get_data'),
    path('staff_dash',views.staff_dash,name='staff_dash'),
    path('stud_dashboard',views.stud_dashboard,name='stud_dashboard'),
    path('stud_result',views.stud_result,name='stud_result'),
    path('staff_login',views.staff_login,name='staff_login'),
    path('stud_re',views.stud_re,name='stud_re'),
    path('stud_login',views.stud_login,name='stud_login'),
    path('stud_reg_DB',views.stud_reg_DB,name='stud_reg_DB'),
    path('logout',views.logout,name='logout'),
    path('qno_disp',views.qno_disp,name='qno_disp'),
    path('answerquestion/<int:id>',views.answerquestion,name='answerquestion'),
    path('staff_result',views.staff_result,name='staff_result'),
    path('staff_logout',views.staff_logout,name='staff_logout'),
    path('stud_record',views.stud_record,name='stud_record'),
    path('recorded_ques',views.recorded_ques,name='recorded_ques')
]