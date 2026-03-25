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
    IMG_MAPA = "imagem_mapa_local.jpg"  # Imagem estática do mapa

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
        """Estrutura com Stack e Imagem de Fundo"""
        return ft.Stack(
            expand=True,
            controls=[
                # Camada 1: Imagem de Fundo
                ft.Container(
                    content=ft.Image(
                        src=IMG_CONVITE,
                        fit=ft.BoxFit.FILL,
                        expand=True,
                        width=page.window_width,
                        height=page.window_height,
                        opacity=opacidade_fundo,
                    ),
                    alignment=ft.Alignment.CENTER,
                ),
                # Camada 2: Conteúdo da Interface
                ft.Column(
                    expand=True,
                    spacing=0,
                    controls=[
                        # Área de Conteúdo
                        ft.Container(
                            content=conteudo_superior,
                            alignment=ft.Alignment.CENTER,
                            expand=9,
                            padding=20,
                        ),
                        # Barra de Navegação
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
        
        # URL com as coordenadas fornecidas
        lat, lon = "-7.1818354", "-35.9053116"
        url_maps = f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"
        
        conteudo = ft.Column(
            controls=[
                ft.Text("Local do Evento", size=28, weight="bold", color=ft.Colors.BLACK),
                ft.Container(
                    content=ft.Image(
                        src=IMG_MAPA,
                        width=280,
                        height=180,
                        border_radius=15,
                        fit=ft.BoxFit.COVER,
                    ),
                    margin=ft.margin.only(top=20, bottom=20),
                    border=ft.border.all(1, ft.Colors.BLACK12),
                    border_radius=15,
                ),
                ft.ElevatedButton(
                    "Ver no Google Maps",
                    icon=ft.Icons.MAP_OUTLINED,
                    on_click=lambda _: page.launch_url(url_maps),
                    style=ft.ButtonStyle(
                        color=ft.Colors.WHITE,
                        bgcolor=ft.Colors.BLUE_700,
                        padding=20,
                    )
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        
        page.add(criar_layout_base(conteudo, cor_inferior=ft.Colors.with_opacity(0.5, ft.Colors.WHITE)))
        page.update()

    mostrar_tela_principal()

# Inicialização do App com a pasta de assets definida
ft.app(target=main, assets_dir="assets")