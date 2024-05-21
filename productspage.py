from flet import *
from data import produtos_description
#CLASSE PRODUTOS PAGINA
class Product(UserControl):
    def __init__(self, description, quantity, img, price, preco_valor, page:Page):
        super().__init__()
        

        self.description = description
        self.quantity = quantity
        self.img = img
        self.price = price
        self.preco_valor = preco_valor

        def add_cart(e):
            self.quantity+=1
            if self.quantity > 1:
                print('ja adicionou')
            else:
                global cart_product
                cart_product = Cart.Cart_Product(self.description, self.img, self.price, self.quantity, self.preco_valor, page)
                coluna.controls.append(cart_product)


        self.button = IconButton(icon=icons.ADD,icon_size=10, icon_color='black', on_click=add_cart)

    def build(self):
        description = self.description
        img = self.img
        price = self.price

        return Card(
                    content= Container(bgcolor='white',
                    border_radius=10,
                    shadow=BoxShadow(
                        spread_radius=1,
                        blur_radius=6,
                        color=colors.GREY,
                        offset=Offset(0, 0),
                        blur_style=ShadowBlurStyle.OUTER,
            ),
                    content=Column(controls=[
                                Image(
                            src=img,
                            width=220,
                            height=300,
                            border_radius=10,
                            fit=ImageFit.FILL,
                                ),
                                Container(
                                    padding=padding.only(left=8),
                                    content=Column([
                                        Row(controls=[
                                            Text(description, size=10),
                                            self.button],
                                            alignment='spaceBetween'),
                                            Text(price, size=10)
                                    ]),
                                ),
                                
                        ])),
                    
                )
    def add_carttwo(e):
        pass
i = 0    

class Products(View):
    def __init__(self, page:Page):
        super(Products, self).__init__(route='/products')
        self.page = page

        self.menu = AppBar(
            toolbar_height=50,
            bgcolor='white',
            leading=IconButton(icon=icons.MENU, on_click=lambda e: self.page.go('/'), icon_size=20),
            leading_width=30,
            actions=[
                IconButton(icon=icons.SHOPPING_CART_OUTLINED, icon_size=20, on_click=lambda e: self.page.go('/cart')),
                PopupMenuButton(
                    
                    items=[
                    PopupMenuItem(text='Your account', icon=icons.PERSON_OUTLINE),
                    PopupMenuItem(text='Favorites', icon = icons.STAR_OUTLINE),
                    PopupMenuItem(text='On course', icon=icons.FIRE_TRUCK_OUTLINED)
                    
                ])
            ]
            
        )
        self.title = Text('Shop', size=30)
        self.subtitle = Text('Your best purchasing option is here', size=10)
        self.show = show
        global i

        for x in produtos_description:
            if i < 8:
                i+=1
                produto = Product(x['description'], x['quantity'], x['img'], x['price'],x['preco_valor'], page)
                show.controls.append(produto)
            if i > 8:
                self.show = show


        self.bottom = BottomAppBar(
                bgcolor='black',
                height=90,
                content=Column(controls=[
                    Row(controls=[
                        Text('About', size=10, color="white"),
                        Icon(icons.QUESTION_ANSWER, color='white', size = 10)
                    ]),
                    Row(controls=[
                        Text('Privacy & Terms', size=10, color="white"),
                        Icon(icons.PERSON_OUTLINE, size=10, color='white')
                    ]),
                    Row( controls=[
                        Text('Accessibility', size=10, color="white"),
                        Icon(icons.ENGINEERING_OUTLINED, size = 10,color='white')
                    ])
                ])
        )

        self.controls=[
            self.menu,
            self.title,
            self.subtitle,
            self.bottom,
            self.show
        ]

#CLASSE CARRINHO PÁGINA
coluna = Column([])
show = Row(controls=[], scroll="auto")
total = 0
c=0

class Cart(View):
    def __init__(self, page:Page):
        super(Cart, self).__init__(route='/cart')
        self.page = page
        self.menu = AppBar(
            toolbar_height=50,
            leading=IconButton(icon=icons.ARROW_BACK, icon_size=20, on_click=lambda e: self.page.go('/products')),
            leading_width=30,
            title=Text('Your Cart', size= 20),
        )
        self.products_view = coluna
        global total
        global c
        
        self.bottomview = BottomAppBar(
            height=110,
            bgcolor='white',
            content=Column(controls=[
                Row(alignment='spaceBetween', controls=[
                    Text(f'Itens:{c}', color='grey', size=10),
                    Text(f'R${total}', weight='bold', size=20, color='black')]),
                Row(expand=True, controls=[
                    ElevatedButton('Buy', expand=True, bgcolor='grey', color='white')
                ])
            ])
            
        )

        self.controls=[
            self.menu,
            self.products_view,
            self.bottomview
        ]

    class Cart_Product(UserControl):
        def __init__(self, description, img, price, quantity,preco_valor, page:Page):
            super().__init__()
            def diminuir(e):
                self.alerttext.value = str(int(self.alerttext.value) - 1)
                if self.alerttext.value < '0':
                    self.alerttext.value = '0'
                page.update()
            def somar(e):
                self.alerttext.value = str(int(self.alerttext.value) + 1)
                page.update()

            self.page = page
            self.description = description
            self.img = img
            self.price = price
            self.quantity = quantity
            campo_texto = TextField(value=str(self.quantity),width=40, height=45, border_color='white', text_size=10, text_align='center')
            self.campo_texto = campo_texto
            self.alerttext = TextField(value=campo_texto.value, expand=True, border_color='black', cursor_color='black', label='Quantity')
            botao_menos = IconButton(icons.REMOVE,icon_color='black', on_click=diminuir, icon_size=25)
            botao_mais = IconButton(icons.ADD, icon_color='black', on_click=somar)
            global total
            total += (preco_valor*int(self.alerttext.value))
            x=1
            self.x = x
            global c
            c+=1

            def close_dlg(e):
                dlg_modal.open = False
                page.update()
            
            def close_dlg_add(e):
                global total
                global c
                if self.alerttext.value.isnumeric() == True:
                    y = int(campo_texto.value)
                    campo_texto.value = self.alerttext.value
                    self.price = f'R${preco_valor*int(self.alerttext.value)}'
                    z = self.x
                    self.x = int(self.alerttext.value)
                    if z < self.x:
                        add = self.x - z
                        preco_add = add * preco_valor
                        total+= preco_add
                        soma = int(self.alerttext.value) - y
                        c+=soma

                    elif z > self.x:
                        sub = self.x - z
                        preco_sub = sub * preco_valor
                        total += preco_sub
                        subtrai = int(self.alerttext.value) - y
                        c+=subtrai

                    dlg_modal.open = False
                    page.update()
                    print('=-'*20)
                else:
                    campo_texto.value = '0'
                    self.alerttext.value = '0'
                    self.price=f'R${int(campo_texto.value)*int(self.alerttext.value)}'
                    dlg_modal.open = False
                    page.update()
                    

            dlg_modal = AlertDialog(
                modal=True,
                title=Text("Do you want to add more to cart?"),
                content=Row([botao_menos ,self.alerttext, botao_mais]),
                actions=[
                    TextButton("Confirm", on_click=close_dlg_add),
                    TextButton("Cancel", on_click=close_dlg),
                ],
                actions_alignment=MainAxisAlignment.END,
                on_dismiss=lambda e: self.page.go('/products')
            )
            
            def open_dlg_modal(e):
                page.dialog = dlg_modal
                dlg_modal.open = True
                page.update()
            
            def remove(e):
                global coluna
                global cart_product
                

            self.button = IconButton(icons.ADD, icon_size=10, icon_color='black', on_click=open_dlg_modal)
            self.remove = IconButton(icons.DELETE_OUTLINE, icon_size=15, icon_color='black', on_click=remove)
            

        def build(self):
            return Card(
                content= Container(
                bgcolor='white',    
                border_radius=5,
                content=Row(alignment='spaceBetween',controls=[
                    Row([
                Container(content=Image(
                    width=43,
                    height=60,
                    src=self.img,
                    fit=ImageFit.FILL,
                    border_radius=5
                    
                )),
                Container(
                    Row(controls=[Text(self.description, size = 10, color='black')]),
                )]),
                Container(Row([Row([self.button,self.campo_texto]), Text(self.price, size=10,),self.remove]), padding=padding.only(right=30))
            ])
            ))

