from django.shortcuts import render
from django.http import JsonResponse, FileResponse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import json
import datetime
from .models import * 
from django.views.decorators.csrf import csrf_exempt
from .utils import cookieCart, cartData, guestOrder

from urllib import request

@login_required
def store(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/store.html', context)

@login_required
def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/cart.html', context)

@login_required
def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)

@login_required
def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

@login_required
def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)

@login_required
def sobre(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/sobre.html', context)

@login_required
def promocoes(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/promocoes.html', context)

@login_required
def atendimento(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/atendimento.html', context)

@login_required
def cadastro(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/cadastro.html', context)

@login_required
def relatorios(request):
    context = {}
    return render(request, 'store/relatorios.html', context)

@login_required
def exportarRelatorio(request):
    produtos = Product.objects.all()

    produtos_list = []

    for produto in produtos:
        produtos_list.append({
            'name': produto.name,
            'price': produto.price,
            'digital': produto.digital,
            'imageURL': produto.imageURL,
        })

    produtos_json = json.dumps(produtos_list, indent=2)
   
    response = HttpResponse(content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="relatorio_produtos.json"'
    
    response.write(produtos_json)

    return response

@csrf_exempt
def importarProdutos(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.POST.get('jsonData'))

            for produto_data in json_data:
                nome_produto = produto_data.get('name')
                imagem_produto = produto_data.get('imageURL')

                produto, created = Product.objects.get_or_create(
                    name=nome_produto,
                    defaults={
                        'price': produto_data.get('price'),
                        'digital': produto_data.get('digital', False),
                        'image': produto_data.get('imageURL'),  # Caminho absoluto corrigido
                    }
                )

                if not created:
                    produto.price = produto_data.get('price')
                    produto.digital = produto_data.get('digital', False)
                    produto.image = produto_data.get('imageURL')  # Caminho absoluto corrigido
                    produto.save()

            return JsonResponse({'message': 'Produtos importados com sucesso.'})

        except json.JSONDecodeError as e:
            return JsonResponse({'error': f'Erro ao decodificar JSON: {str(e)}'}, status=400)

    return JsonResponse({'error': 'Método não permitido'}, status=405) 
