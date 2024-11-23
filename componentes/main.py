import flet as ft


def main(page: ft.Page):
    #Configuracion del appBar
    page.appbar=ft.CupertinoAppBar(
        leading=ft.Icon(ft.icons.MENU,color="white"),
        bgcolor=ft.colors.TEAL_800,
        middle=ft.Text(value="Primera App",color="white",weight=ft.FontWeight.BOLD)
        )
    
    #Configuracion de la barra de navegacion
    page.navigation_bar=ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(label="Inicio",icon=ft.icons.HOME),
            ft.NavigationDestination(label="Productos",icon=ft.icons.STORE_MALL_DIRECTORY),
            ft.NavigationDestination(label="Carrito", icon=ft.icons.SHOPPING_CART),
            ft.NavigationDestination(label="Perfil",icon=ft.icons.SETTINGS)
        ],bgcolor=ft.colors.TEAL_800,indicator_color=ft.colors.WHITE,
        surface_tint_color=ft.colors.RED_50,


    )
    #Funcion para obtener el texto de la entrada de datos textField
    def textoEntrada(e):
        value.value=e.control.value
        page.update()
    value=ft.Text()
    #Contenedor para componentes
    contenidoApp=ft.Column([
        ft.Text(value="Aplicacion Multiplataforma",size=30,weight=ft.FontWeight.BOLD),
        ft.CupertinoFilledButton(text="Boton1",icon=ft.icons.FACE),
        ft.Checkbox(label="Opcion 1"),
        ft.CupertinoCheckbox(label="Opcion 2"),
        ft.Radio(label="Opcion 3"),
        ft.RadioGroup(content=ft.Column([
            ft.CupertinoRadio(label="Opcion 1", value="Opcion1"),
            ft.CupertinoRadio(label="Opcion 2", value="Opcion2"),
            ft.CupertinoRadio(label="Opcion 3", value="Opcion3"),
            ft.CupertinoRadio(label="Opcion 4", value="Opcion4")
        ])),
        ft.TextField(label="Ingrese su nombre",icon=ft.icons.PERSON, on_change=textoEntrada),
        ft.TextField(label="Ingrese su correo",icon=ft.icons.EMAIL, password=True),
        ft.CupertinoTextField(placeholder_text="Ingrese su celular"),
        ft.CupertinoTextField(placeholder_text="Contraseña",password=True)

    ])

    page.add(contenidoApp,value)


ft.app(main)
