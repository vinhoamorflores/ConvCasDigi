import flet as ft
import os

def main(page: ft.Page):
    # --- Configurações de Janela e Título ---
    page.title = "Convite Digital"
    page.window_width = 375
    page.window_height = 667
    page.window_resizable = False
    page.padding = 0
    page.spacing = 0
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # --- Configurações de Arquivos (Assets) ---
    CAMINHO_ASSETS = "assets"
    IMG_CONVITE = "imagem_principal.jpg"
    IMG_BTN_HOME = "btn_home.png"
    IMG_BTN_CONFIRMAR = "btn_confirmar.png"
    IMG_BTN_PRESENTES = "btn_presentes.png"
    IMG_BTN_LOCAL = "btn_local.png"

    IMAGENS_MOSAICO = [
        "imagem_local1.jpg", "imagem_local2.jpg", "imagem_local3.jpg",
        "imagem_local4.jpg", "imagem_local5.jpg", "imagem_local6.jpg",
        "imagem_local7.jpg", "imagem_local8.jpg", "imagem_local9.jpg",
    ]

    # --- Funções de Utilidade (Verificação de Assets) ---

    def obter_imagem_principal(opacidade):
        """Verifica se a imagem de fundo principal existe."""
        caminho_foto = os.path.join(CAMINHO_ASSETS, IMG_CONVITE)
        if os.path.exists(caminho_foto):
            return ft.Image(
                src=IMG_CONVITE,
                fit=ft.BoxFit.FILL,
                width=page.window_width,
                height=page.window_height,
                opacity=opacidade,
            )
        else:
            # Retorno caso a imagem principal suma: um fundo suave com ícone discreto
            return ft.Container(
                content=ft.Icon(ft.Icons.IMAGE_NOT_SUPPORTED_OUTLINED, color=ft.Colors.BLUE_GREY_100, size=50),
                bgcolor=ft.Colors.BLUE_GREY_50,
                width=page.window_width,
                height=page.window_height,
                alignment=ft.Alignment.CENTER,
            )

    def obter_imagem_botao(nome_arquivo, icone_reserva, acao):
        caminho_foto = os.path.join(CAMINHO_ASSETS, nome_arquivo)
        if os.path.exists(caminho_foto):
            return ft.GestureDetector(
                content=ft.Image(src=nome_arquivo, width=35, height=35, fit=ft.BoxFit.CONTAIN),
                on_tap=acao
            )
        else:
            return ft.IconButton(
                icon=icone_reserva,
                icon_color=ft.Colors.BLUE_800,
                on_click=acao
            )

    def obter_imagem_mosaico(nome_arquivo):
        caminho_foto = os.path.join(CAMINHO_ASSETS, nome_arquivo)
        if os.path.exists(caminho_foto):
            return ft.Image(
                src=nome_arquivo,
                fit=ft.BoxFit.COVER,
                border_radius=ft.border_radius.all(8)
            )
        else:
            return ft.Container(
                content=ft.Icon(ft.Icons.IMAGE_OUTLINED, color=ft.Colors.GREY_400),
                bgcolor=ft.Colors.GREY_100,
                alignment=ft.Alignment.CENTER,
                border_radius=ft.border_radius.all(8)
            )

    # --- Layout Base ---

    def criar_layout_base(conteudo_superior, cor_inferior=ft.Colors.with_opacity(0.3, ft.Colors.BLUE_200), opacidade_fundo=0.15):
        return ft.Stack(
            expand=True,
            controls=[
                # Aplicando a nova função de verificação para a imagem de fundo
                ft.Container(
                    content=obter_imagem_principal(opacidade_fundo),
                    alignment=ft.Alignment.CENTER,
                ),
                ft.Column(
                    expand=True,
                    spacing=0,
                    controls=[
                        ft.Container(
                            content=conteudo_superior,
                            alignment=ft.Alignment.CENTER,
                            expand=9,
                        ),
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    obter_imagem_botao(IMG_BTN_HOME, ft.Icons.HOME, lambda _: mostrar_tela_principal()),
                                    obter_imagem_botao(IMG_BTN_CONFIRMAR, ft.Icons.CHECK_CIRCLE, lambda _: mostrar_tela_confirmar()),
                                    obter_imagem_botao(IMG_BTN_PRESENTES, ft.Icons.CARD_GIFTCARD, lambda _: mostrar_tela_presentes()),
                                    obter_imagem_botao(IMG_BTN_LOCAL, ft.Icons.LOCATION_ON, lambda _: mostrar_tela_local()),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                            ),
                            bgcolor=cor_inferior,
                            expand=1,
                            blur=ft.Blur(10, 10) if opacidade_fundo < 1 else None
                        )
                    ]
                )
            ]
        )

    # --- Telas de Navegação ---

    def mostrar_tela_principal():
        page.controls.clear()
        page.add(criar_layout_base(None, cor_inferior=ft.Colors.with_opacity(0.75, ft.Colors.WHITE), opacidade_fundo=1.0))
        page.update()

    def mostrar_tela_confirmar():
        page.controls.clear()
        conteudo = ft.Text("Confirmar Presença", size=28, weight="bold", color=ft.Colors.BLACK)
        page.add(criar_layout_base(conteudo, cor_inferior=ft.Colors.with_opacity(0.5, ft.Colors.WHITE)))
        page.update()

    def mostrar_tela_presentes():
        page.controls.clear()
        conteudo = ft.Text("Lista de Presentes", size=28, weight="bold", color=ft.Colors.BLACK)
        page.add(criar_layout_base(conteudo, cor_inferior=ft.Colors.with_opacity(0.5, ft.Colors.WHITE)))
        page.update()

    def mostrar_tela_local():
        page.controls.clear()
        mosaico = ft.GridView(
            runs_count=3,
            max_extent=100,
            child_aspect_ratio=1.0,
            spacing=10,
            run_spacing=10,
            height=330, 
            controls=[
                ft.Container(
                    content=obter_imagem_mosaico(img),
                    border=ft.border.all(0.5, ft.Colors.BLACK12),
                    border_radius=ft.border_radius.all(8),
                ) for img in IMAGENS_MOSAICO
            ]
        )

        conteudo = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Text("Espaço Imbituba", size=24, weight="bold", color=ft.Colors.BLACK),
                ft.Container(height=10), 
                ft.Container(
                    content=mosaico,
                    width=320, 
                    alignment=ft.Alignment.CENTER
                )
            ]
        )
        page.add(criar_layout_base(conteudo, cor_inferior=ft.Colors.with_opacity(0.5, ft.Colors.WHITE)))
        page.update()

    mostrar_tela_principal()

ft.app(target=main, assets_dir="assets")