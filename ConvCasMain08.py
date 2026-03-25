import flet as ft
import os

def main(page: ft.Page):
    # Configurações iniciais da página
    page.window_width = 375
    page.window_height = 667
    page.padding = 0
    page.spacing = 0
    
    # Nome da imagem principal
    nome_imagem = "Convite.jpg"
    caminho_assets = "assets"
    caminho_completo = os.path.join(caminho_assets, nome_imagem)
    tem_imagem = os.path.exists(caminho_completo)

    def criar_layout_base(conteudo_superior, cor_inferior=ft.Colors.BLUE_200):
        """Gera a estrutura 90/10 solicitada"""
        return ft.Column(
            expand=True,
            spacing=0,
            controls=[
                # Parte Superior (90%)
                ft.Container(
                    content=conteudo_superior,
                    alignment=ft.Alignment.CENTER,
                    expand=9
                ),
                # Parte Inferior (10%)
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.IconButton(
                                icon=ft.Icons.HOME,
                                icon_color=ft.Colors.BLUE_800,
                                bgcolor=ft.Colors.WHITE,
                                on_click=lambda _: mostrar_tela_principal()
                            ),
                            ft.IconButton(
                                icon=ft.Icons.FAVORITE,
                                icon_color=ft.Colors.RED_400,
                                bgcolor=ft.Colors.WHITE,
                                on_click=lambda _: mostrar_tela_favoritos()
                            ),
                            ft.IconButton(
                                icon=ft.Icons.SHARE,
                                icon_color=ft.Colors.BLUE_800,
                                bgcolor=ft.Colors.WHITE,
                                on_click=lambda _: mostrar_tela_compartilhar()
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    ),
                    bgcolor=cor_inferior,
                    expand=1
                )
            ]
        )

    # --- Funções de Troca de Tela ---

    def mostrar_tela_principal():
        page.controls.clear()
        conteudo = ft.Image(
            src=nome_imagem,
            fit=ft.BoxFit.COVER,
        ) if tem_imagem else ft.Text("Convite Principal", size=30, weight="bold")
        
        page.add(criar_layout_base(conteudo))
        page.update()

    def mostrar_tela_favoritos():
        page.controls.clear()
        # Exemplo de conteúdo para a nova tela
        conteudo = ft.Column(
            controls=[
                ft.Icon(ft.Icons.FAVORITE, size=50, color=ft.Colors.RED),
                ft.Text("Lista de Presentes / Favoritos", size=20)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        page.add(criar_layout_base(conteudo, cor_inferior=ft.Colors.PINK_100))
        page.update()

    def mostrar_tela_compartilhar():
        page.controls.clear()
        conteudo = ft.Text("Opções de Compartilhamento", size=20, weight="bold")
        page.add(criar_layout_base(conteudo, cor_inferior=ft.Colors.GREEN_100))
        page.update()

    # Inicia o app na tela principal
    mostrar_tela_principal()

# O parâmetro assets_dir é fundamental para que o Flet reconheça a pasta
ft.app(target=main, assets_dir="assets")