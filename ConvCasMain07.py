import flet as ft
import os

def main(page: ft.Page):
    # --- CONFIGURAÇÃO DA IMAGEM ---
    # Apenas o nome do arquivo. Ele deve estar dentro da pasta 'assets'
    nome_imagem = "Convite.jpg" 
    # ------------------------------

    page.window_width = 375
    page.window_height = 667
    page.padding = 0
    page.spacing = 0

    # Define o caminho esperado (Pasta assets + nome do arquivo)
    caminho_assets = "assets"
    caminho_completo = os.path.join(caminho_assets, nome_imagem)

    # Verifica se o arquivo físico existe no diretório
    tem_imagem = os.path.exists(caminho_completo)

    # Parte Superior (90%)
    parte_superior = ft.Container(
        content=ft.Image(
            src=nome_imagem,
            fit=ft.BoxFit.COVER,
        ) if tem_imagem else ft.Text("Conteúdo do Convite", size=30, weight="bold"),
        
        alignment=ft.Alignment.CENTER,
        # Mantém a cor BLUE_50 apenas se a imagem não existir
        bgcolor=ft.Colors.BLUE_50 if not tem_imagem else None,
        expand=9 
    )

    # Parte Inferior (10%) com os botões
    parte_inferior = ft.Container(
        content=ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.Icons.HOME,
                    icon_color=ft.Colors.BLUE_800,
                    bgcolor=ft.Colors.WHITE,
                    width=50, height=50,
                    style=ft.ButtonStyle(shape=ft.CircleBorder()),
                ),
                ft.IconButton(
                    icon=ft.Icons.FAVORITE,
                    icon_color=ft.Colors.RED_400,
                    bgcolor=ft.Colors.WHITE,
                    width=50, height=50,
                    style=ft.ButtonStyle(shape=ft.CircleBorder()),
                ),
                ft.IconButton(
                    icon=ft.Icons.SHARE,
                    icon_color=ft.Colors.BLUE_800,
                    bgcolor=ft.Colors.WHITE,
                    width=50, height=50,
                    style=ft.ButtonStyle(shape=ft.CircleBorder()),
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
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

# O parâmetro assets_dir é fundamental para que o Flet reconheça a pasta
ft.app(target=main, assets_dir="assets")