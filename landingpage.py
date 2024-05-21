from flet import *

class Landing(View):
    def __init__(self, page:Page):
        super(Landing, self).__init__(route='/', horizontal_alignment='center', vertical_alignment='center')

        self.page = page

        self.cart = Icon(icons.SHOPPING_CART_OUTLINED, size=64)
        self.menssage = Text("MARUSSI'S STORE".upper(), weight='bold', size=25)
        self.subtittle = Text('My E-commerce shop', size=10)
        self.button = IconButton(
            icon=icons.ARROW_FORWARD,
            width=54,
            height=54,
            style=ButtonStyle(
                bgcolor={'': '#E3E4E1'},
                shape={'': RoundedRectangleBorder(radius=8)},
                side={'': BorderSide(2, 'black')}
            ),
            on_click=lambda e: self.page.go('/products')
        )

        self.controls=[
            self.cart,
            self.menssage,
            self.subtittle,
            self.button
        ]