import flet as ft

def main(page: ft.Page):
    page.window_width = 375
    page.window_height = 667
    page.padding = 0
    page.spacing = 0

    # Parte Superior (90%)
    parte_superior = ft.Container(
        content=ft.Text("Conteúdo do Convite", size=30, weight="bold"),
        alignment=ft.Alignment.CENTER,
        bgcolor=ft.Colors.BLUE_50,
        expand=9 
    )

    # Parte Inferior (10%) com 3 botões circulares brancos
    parte_inferior = ft.Container(
        content=ft.Row(
            controls=[
                # Botão 1
                ft.IconButton(
                    icon=ft.Icons.HOME,
                    icon_color=ft.Colors.BLUE_800,
                    bgcolor=ft.Colors.WHITE,
                    icon_size=25,
                    width=50,
                    height=50,
                    style=ft.ButtonStyle(shape=ft.CircleBorder()),
                ),
                # Botão 2
                ft.IconButton(
                    icon=ft.Icons.FAVORITE,
                    icon_color=ft.Colors.RED_400,
                    bgcolor=ft.Colors.WHITE,
                    icon_size=25,
                    width=50,
                    height=50,
                    style=ft.ButtonStyle(shape=ft.CircleBorder()),
                ),
                # Botão 3
                ft.IconButton(
                    icon=ft.Icons.SHARE,
                    icon_color=ft.Colors.BLUE_800,
                    bgcolor=ft.Colors.WHITE,
                    icon_size=25,
                    width=50,
                    height=50,
                    style=ft.ButtonStyle(shape=ft.CircleBorder()),
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY, # Distribui o espaço entre os botões
        ),
        bgcolor=ft.Colors.BLUE_200,
        expand=1 
    )

    page.add(
        ft.Column(
            controls=[parte_superior, parte_inferior],
            expand=True,
            spacing=0
        )
    )

ft.app(target=main)