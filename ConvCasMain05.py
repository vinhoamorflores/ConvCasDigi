import flet as ft

def main(page: ft.Page):
    # Configurações para simular a tela de um celular
    page.window_width = 375
    page.window_height = 667
    page.padding = 0
    page.spacing = 0

    # Parte Superior - 90% do espaço
    # Ocupará a maior parte da tela para o conteúdo principal (como o convite)
    parte_superior = ft.Container(
        content=ft.Text("Parte Superior (90%)", size=30, weight="bold"),
        alignment=ft.Alignment.CENTER,
        bgcolor=ft.Colors.BLUE_50,
        expand=9 # Define a proporção de 9/10
    )

    # Parte Inferior - 10% do espaço
    # Ideal para menus, botões de ação ou rodapés
    parte_inferior = ft.Container(
        content=ft.Text("Parte Inferior (10%)", size=15),
        alignment=ft.Alignment.CENTER,
        bgcolor=ft.Colors.BLUE_200,
        expand=1 # Define a proporção de 1/10
    )

    # Layout Principal
    page.add(
        ft.Column(
            controls=[
                parte_superior,
                parte_inferior
            ],
            expand=True, # Faz a coluna ocupar a altura total da página
            spacing=0    # Remove espaços entre os containers
        )
    )

ft.app(target=main)