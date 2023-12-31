from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
    path('sobre/', views.sobre, name="sobre"),
    path('cadastro/', views.cadastro, name="cadastro"),
    path('promocoes/', views.promocoes, name="promocoes"),
    path('atendimento/', views.atendimento, name="atendimento"),
	path('relatorio/', views.relatorios, name="relatorios"),
	path('exportar-relatorio/', views.exportarRelatorio, name='exportar_relatorio'),
	path('importar-produtos/', views.importarProdutos, name='importar_produtos'),
]