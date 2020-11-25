from django.http.response import JsonResponse
from products.models import *
from informations.models import *


def getInformations(request):
    combo_info = Products.objects.filter(product='combo')[0]
    fit_info = Products.objects.filter(product='fit')[0]
    lowcarb_info = Products.objects.filter(product='lowcarb')[0]
    about_info = About.objects.all()[0]
    contact_info = Contact.objects.all()[0]
    delivery_info = Delivery.objects.all()[0]
    order_info = Order.objects.all()[0]

    data = {
        'fit': getFits(),
        'lowcarb': getLowCarbs(),
        'combos': getCombos(),
        'acompnhamentos': getPortions(1),
        'carnes': getPortions(2),
        'frangos': getPortions(3),
        'massas': getPortions(4),
        'peixes': getPortions(5),
        'info': {
            'cards': [
                {
                    'title': 'combo caseiro',
                    'type': 'combo',
                    'content': [
                        combo_info.about,
                        f'Embalagem de {combo_info.amount}ml (cada porção).'
                    ]
                },
                {
                    'title': 'marmita fit',
                    'type': 'fit',
                    'content': [
                        fit_info.about,
                        f'Embalagem de {fit_info.amount}ml.'
                    ]
                },
                {
                    'title': 'marmita low carb',
                    'type': 'lowcarb',
                    'content': [
                        lowcarb_info.about,
                        f'Embalagem de {lowcarb_info.amount}ml.'
                    ]
                }
            ],
            'about': [about_info.info_one, about_info.info_two],
            'contact': [
                f'(21) {contact_info.whatsapp[:5]}-{contact_info.whatsapp[4:]}',
                contact_info.instagram
            ],
            'delivery': [delivery_info.info_one, delivery_info.info_two],
            'order': [order_info.info_one, order_info.info_two]
        }

    }
    return JsonResponse(data)


def getFits():
    fits = Fit.objects.filter(active=True)
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
            'amount': 0
        })

    return data


def getLowCarbs():
    lowcarbs = LowCarb.objects.filter(active=True)
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
            'amount': 0
        })

    return data


def getCombos():

    combos = Combo.objects.filter(active=True)
    data = []
    for combo in combos:
        data.append({
            "id": combo.id,
            "title": combo.name,
            combo.acompanhamentos and "acompanhamento": combo.acompanhamentos,
            combo.carnes and "carne": combo.carnes,
            combo.frangos and "frango": combo.frangos,
            combo.massas and "massa": combo.massas,
            combo.peixe and "peixe": combo.peixe,
            combo.active and "active": combo.active
        })

    return data


def getPortions(portion_type):
    portions = Portion.objects.filter(active=True, type=portion_type)
    data = []
    for portion in portions:
        data.append({
            "id": portion.id,
            "name": portion.name,
            "price": portion.price,
            "active": portion.active,
            "hot": portion.discount,
            "sale": portion.sale
        })

    return data
