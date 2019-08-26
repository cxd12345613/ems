from django.urls import path
from emplist_app import views

app_name='emplist_app'

urlpatterns=[

    path('emp/',views.emplist,name='emp'),
    path('empadd/',views.addEmployee,name='empadd'),
    path('empaddlogic/',views.addEmplogic,name='empaddlogic'),
    path('updataEmp/',views.updateEmp,name='updataEmp'),
    path('updataEmplogic/',views.updateEmplogic,name='updataEmplogic'),
    path('delEmp/',views.delEmp,name='delEmp'),

]
