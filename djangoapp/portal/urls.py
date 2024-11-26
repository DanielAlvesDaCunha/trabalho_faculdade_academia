from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView,LoginView


from portal.views.avaliacao_view import AvaliacaoUpdateView
from portal.views.agendamento_view import AgendamentoCreateView
from portal.views.dashboard import UserDashboardView
from portal.views import(
    SignUp,
    UserContaView,
    UserInfoEditView ,
    UserInfoCreateView,
    CriarAvaliacaoView

    
    )
app_name = 'portal'

urlpatterns = [

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', SignUp.as_view(), name='register'),
    path('user_info_create/',UserInfoCreateView.as_view(), name='user-info-create'),
    path('dashboard/',UserDashboardView.as_view(), name='dashboard'),
    path('dashboard/edit_conta/',UserContaView.as_view(), name='edit-conta'),
    path('dashboard/edit_pessoais/',UserInfoEditView.as_view(), name='edit-info'),
    path('agendamento/', AgendamentoCreateView.as_view(), name='agendamento'),
    path('avaliacao/', AvaliacaoUpdateView.as_view(), name='avaliacao'),
    path('criar_avaliacao/', CriarAvaliacaoView.as_view(), name='criar-avaliacao'),
    
    ]
