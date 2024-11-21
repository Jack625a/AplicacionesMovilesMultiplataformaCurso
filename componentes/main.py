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



    page.add(ft.SafeArea(ft.Text("Aplicacion en tiempo real")))


ft.app(main)
