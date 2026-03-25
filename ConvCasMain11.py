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

    def criar_layout_base(conteudo_superior, cor_inferior=ft.Colors.with_opacity(0.3, ft.Colors.BLUE_200), opacidade_fundo=0.15):
        """Estrutura com Stack e Imagem Centralizada"""
        return ft.Stack(
            expand=True,
            controls=[
                # Camada 1: Imagem de Fundo CENTRALIZADA
                ft.Container(
                    content=ft.Image(
                        src=IMG_CONVITE,
                        #fit=ft.BoxFit.COVER,       # Imagem Preenche a tela mantendo a proporção
                        fit=ft.BoxFit.FILL,         # Imagem Estica para preencher a tela
                        expand=True,                # Força expansão no Stack
                        width=page.window_width,    # Garante largura total
                        height=page.window_height,  # Garante altura total                        
                        opacity=opacidade_fundo,
                    ),
                    alignment=ft.Alignment.CENTER,  # Força a centralização
                    expand=True,
                ),
                # Camada 2: Conteúdo da Interface
                ft.Column(
                    expand=True,
                    spacing=0,
                    controls=[
                        # Área de Conteúdo (90%)
                        ft.Container(
                            content=conteudo_superior,
                            alignment=ft.Alignment.CENTER,
                            expand=9,
                        ),
                        # Barra de Navegação (10%)
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

    # --- Funções de Troca de Tela ---
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
        conteudo = ft.Text("Local do Evento", size=28, weight="bold", color=ft.Colors.BLACK)
        page.add(criar_layout_base(conteudo, cor_inferior=ft.Colors.with_opacity(0.5, ft.Colors.WHITE)))
        page.update()

    mostrar_tela_principal()

ft.app(target=main, assets_dir="assets")