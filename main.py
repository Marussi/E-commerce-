from flet import *
from data import produtos_description
from landingpage import Landing
from productspage import Products, Cart


def main(page:Page):

    def router(route):
        page.views.clear()
        if page.route == '/':
            landing = Landing(page)
            page.views.append(landing)

        if page.route == '/products':
            products = Products(page)
            page.views.append(products)

        if page.route == '/cart':
            cart = Cart(page)
            page.views.append(cart)

        page.update()

    
    page.on_route_change = router
    page.go('/')

app(target=main)