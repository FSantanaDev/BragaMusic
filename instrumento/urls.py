#instrumento/urls.py

from django.urls import path,include
from . import views 
from django.conf.urls.static import static
from django.conf import settings
from .views import detalhe_instrumento,login_view,cadastrar_cliente, filtro_instrumentos,adicionar_ao_carrinho,remover_do_carrinho,carrinho,logout_view,homepage,finalizar_pedido,pagamento_retorno
from instrumento.management_views import run_migrations
from instrumento.management_users import create_superuser

urlpatterns = [
    path('', homepage, name='homepage'),     
    path('instrumento/<int:instrumento_id>/', detalhe_instrumento, name='detalhe_instrumento'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('pre-login/', views.pre_login, name='pre_login'),    
    path('cadastro/', cadastrar_cliente, name='cadastro_cliente'),
    path('filtro/', filtro_instrumentos, name='filtro_instrumentos'),   
    path('adicionar_ao_carrinho/<int:instrumento_id>/', adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('carrinho/', carrinho, name='carrinho'),
    path('remover-do-carrinho/<int:instrumento_id>/',remover_do_carrinho, name='remover_do_carrinho'),
    path('finalizar-pedido/', finalizar_pedido, name='finalizar_pedido'),
    path('pagamento/retorno/', views.pagamento_retorno, name='pagamento_retorno'),
    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),
    path('verificar_email/', views.verificar_email, name='verificar_email'),
    path('exibir_politica/', views.exibir_politica, name='exibir_politica'),
    path('run-migrations/', run_migrations, name='run-migrations'),
    path('create_superuser/', create_superuser, name='create-superuser'),     
    
    
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)