from django.http.response import JsonResponse
from products.models import *
from informations.models import *


def getInformations(request):
    combo_info = Products.objects.filter(product='combo').order_by('id')[0]
    fit_info = Products.objects.filter(product='fit').order_by('id')[0]
    lowcarb_info = Products.objects.filter(product='lowcarb').order_by('id')[0]
    about_info = About.objects.all()[0]
    contact_info = Contact.objects.all()[0]
    delivery_info = Delivery.objects.all()[0]
    order_info = Order.objects.all()[0]

    data = {
        'products': {
            'lunches': {
                'fits': getFits(),
                'lowcarbs': getLowCarbs()
            },
            'combos': getCombos()
        },
        'info': {
            'combo': {
                'title': 'combo caseiro',
                'type': 'combo',
                'content': [
                    combo_info.about,
                    f'Embalagem de {combo_info.amount}ml (cada porção).'
                ]
            },
            'fit': {
                'title': 'marmita fit',
                'type': 'fit',
                'content': [
                    fit_info.about,
                    f'Embalagem de {fit_info.amount}ml.'
                ]
            },
            'lowcarb': {
                'title': 'marmita low carb',
                'type': 'lowcarb',
                'content': [
                    lowcarb_info.about,
                    f'Embalagem de {lowcarb_info.amount}ml.'
                ]
            },
            'about': [about_info.info_one, about_info.info_two],
            'contact': [
                f'(21) {contact_info.whatsapp[:5]}-{contact_info.whatsapp[4:]}',
                contact_info.instagram
            ],
            'delivery': [delivery_info.info_one, delivery_info.info_two],
            'order': [order_info.info_one, order_info.info_two],
        }
    }

    return JsonResponse(data)


def getFits():
    fits = Fit.objects.filter(active=True).order_by('id')
    data = []
    for fit in fits:
        data.append({
            'id': fit.id,
            'title': fit.type,
            'name': fit.name,
            'price': fit.price,
            'active': fit.active,
            'hot': fit.discount,
            'type': 'fit',
            'sale': fit.sale,
            'amount': 0,
            'itemType': 'lunch'
        })

    return data


def getLowCarbs():
    lowcarbs = LowCarb.objects.filter(active=True).order_by('id')
    data = []
    for lowcarb in lowcarbs:
        data.append({
            'id': lowcarb.id,
            'title': lowcarb.type,
            'name': lowcarb.name,
            'price': lowcarb.price,
            'active': lowcarb.active,
            'hot': lowcarb.discount,
            'type': 'lowcarb',
            'sale': lowcarb.sale,
            'amount': 0,
            'itemType': 'lunch'
        })

    return data


def getCombos():

    combos = Combo.objects.filter(active=True).order_by('id')
    data = []
    for combo in combos:
        if combo.active == True:
            data.append({
                'id': combo.id,
                'title': combo.name,
                'active': combo.active,
                'portions': getPortions(combo)
            })

    return data


def getPortions(combo):
    data = []
    combo.acompanhamentos > 0 and data.append(
        {
            'id': 1,
            'name': 'acompanhamentos',
            'choice_amount': combo.acompanhamentos,
            'items': getPortionItems(1)
        }
    )

    combo.carnes > 0 and data.append(
        {
            'id': 2,
            'name': 'carnes',
            'choice_amount': combo.carnes,
            'items': getPortionItems(2)
        }
    )

    combo.frangos > 0 and data.append(
        {
            'id': 3,
            'name': 'frangos',
            'choice_amount': combo.frangos,
            'items': getPortionItems(3)
        }
    )

    combo.massas > 0 and data.append(
        {
            'id': 4,
            'name': 'massas',
            'choice_amount': combo.massas,
            'items': getPortionItems(4)
        }
    )

    combo.peixe > 0 and data.append(
        {
            'id': 5,
            'name': 'peixes',
            'choice_amount': combo.peixe,
            'items': getPortionItems(5)
        }
    )

    return data


def getPortionItems(portion):
    items = Portion.objects.filter(active=True, type=portion).order_by('id')

    data = []

    for item in items:
        if item.active:
            data.append(
                {
                    'id': item.id,
                    'name': item.name,
                    'price': item.price,
                    'active': item.active,
                    'hot': item.discount,
                    'sale': item.sale
                }
            )
    return data
