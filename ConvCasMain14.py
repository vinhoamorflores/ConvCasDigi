import flet as ft
import os
import webbrowser

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
        tf_style = {
            "border_color": ft.Colors.BLUE_800,
            "focused_border_color": ft.Colors.BLUE_ACCENT_700,
            "label_style": ft.TextStyle(color=ft.Colors.BLACK54),
            "text_style": ft.TextStyle(color=ft.Colors.BLACK),
            "border_radius": 10,
            "width": 300,
        }

        txt_nome_principal = ft.TextField(label="Nome e Sobrenome do Convidado", **tf_style)
        txt_nome_acomp1 = ft.TextField(label="Nome e Sobrenome do Acompanhante 1", **tf_style)
        txt_nome_acomp2 = ft.TextField(label="Nome e Sobrenome do Acompanhante 2", **tf_style)

        form_confirmacao = ft.Column(
            scroll=ft.ScrollMode.AUTO,
            expand=True,
            spacing=15,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(height=10),
                ft.Text("Confirme sua Presença", size=24, weight="bold", color=ft.Colors.BLACK, text_align=ft.TextAlign.CENTER),
                ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                ft.Text("Convidado Principal", weight="bold", color=ft.Colors.BLUE_900, text_align=ft.TextAlign.CENTER),
                txt_nome_principal,
                ft.Divider(height=20, thickness=1),
                ft.Text("Acompanhantes (Opcional)", weight="bold", color=ft.Colors.BLUE_900, text_align=ft.TextAlign.CENTER),
                txt_nome_acomp1,
                txt_nome_acomp2,
                ft.Container(height=10),
                ft.ElevatedButton(
                    "Confirmar Presença", 
                    color=ft.Colors.WHITE, 
                    bgcolor=ft.Colors.BLUE_800,
                    width=300,
                    height=50,
                    on_click=lambda _: print(f"Confirmado: {txt_nome_principal.value}")
                ),
                ft.Container(height=20),
            ]
        )

        conteudo = ft.Container(content=form_confirmacao, padding=20, alignment=ft.Alignment.TOP_CENTER)
        page.add(criar_layout_base(conteudo, cor_inferior=ft.Colors.with_opacity(0.5, ft.Colors.WHITE)))
        page.update()

    def mostrar_tela_presentes():
        page.controls.clear()
        
        dados_presentes = [
            {"nome": "Cortador de Pizza", "preco": 50.00}, {"nome": "Balança Digital de Cozinha", "preco": 80.00},
            {"nome": "Cesta de Frutas", "preco": 90.00}, {"nome": "Conjunto de Canecas", "preco": 100.00},
            {"nome": "Espremedor de Frutas", "preco": 100.00}, {"nome": "Almofadas Decorativas (2 unid.)", "preco": 160.00},
            {"nome": "Vasos Decorativos", "preco": 150.00}, {"nome": "Relógio de Parede Moderno", "preco": 150.00},
            {"nome": "Cestos de Armazenamento", "preco": 90.00}, {"nome": "Luminárias LED Decorativas", "preco": 80.00},
            {"nome": "Bandejas Decorativas", "preco": 100.00}, {"nome": "Jogo de Facas de Chef", "preco": 250.00},
            {"nome": "Grill Elétrico", "preco": 400.00}, {"nome": "Panela de Arroz Elétrica", "preco": 300.00},
            {"nome": "Conjunto de Copos Térmicos", "preco": 150.00}, {"nome": "Liquidificador", "preco": 250.00},
            {"nome": "Jogo de Panelas de Cerâmica", "preco": 350.00}, {"nome": "Quadros ou Pôsteres Artísticos", "preco": 200.00},
            {"nome": "Cortinas Elegantes", "preco": 300.00}, {"nome": "Luminárias de Mesa", "preco": 180.00},
            {"nome": "Candeeiro de Chão", "preco": 400.00}, {"nome": "Jogo de Talheres (Aço Inox)", "preco": 180.00},
            {"nome": "Arranjos de Flores", "preco": 100.00}, {"nome": "Máquina de Lavar Louça", "preco": 2500.00},
            {"nome": "Micro-ondas", "preco": 600.00}, {"nome": "Batedeira Planetária", "preco": 500.00},
            {"nome": "Tapetes Decorativos", "preco": 300.00}, {"nome": "Jogo de Panelas de Pressão", "preco": 350.00},
            {"nome": "Aparelho de Jantar (20 peças)", "preco": 499.90}, {"nome": "Faqueiro (20 peças)", "preco": 212.77},
            {"nome": "Luminárias Pendentes", "preco": 180.00},
        ]

        dados_ordenados = sorted(dados_presentes, key=lambda x: x["nome"])

        def criar_item_presente(item):
            return ft.Container(
                content=ft.Column(
                    controls=[
                        ft.ListTile(
                            leading=ft.Icon(ft.Icons.CARD_GIFTCARD, color=ft.Colors.BLUE_800),
                            title=ft.Text(item["nome"], size=16, weight="bold", text_align=ft.TextAlign.CENTER),
                            subtitle=ft.Text(f"R$ {item['preco']:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."), color=ft.Colors.GREEN_800, text_align=ft.TextAlign.CENTER),
                        ),
                        ft.Container(
                            content=ft.ElevatedButton(
                                "Presentear", color=ft.Colors.WHITE, bgcolor=ft.Colors.BLUE_800, height=40, width=200,
                                on_click=lambda _: print(f"Escolhido: {item['nome']}")
                            ),
                            alignment=ft.Alignment.CENTER, padding=ft.padding.only(bottom=15)
                        ),
                        ft.Divider(height=1, color=ft.Colors.BLACK12)
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )

        lista_presentes = ft.ListView(expand=1, spacing=10, padding=10, controls=[criar_item_presente(item) for item in dados_ordenados])

        conteudo = ft.Column(
            expand=True, horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(height=20),
                ft.Text("Lista de Presentes", size=24, weight="bold", color=ft.Colors.BLACK),
                ft.Divider(height=20, thickness=1, color=ft.Colors.BLACK12),
                ft.Container(content=lista_presentes, expand=True)
            ]
        )

        page.add(criar_layout_base(conteudo, cor_inferior=ft.Colors.with_opacity(0.5, ft.Colors.WHITE)))
        page.update()

    def mostrar_tela_local():
        page.controls.clear()
        
        # Função para abrir o mapa
        def abrir_mapa(e):
            url = "https://www.google.com/maps/search/?api=1&query=-7.1818871,-35.9050449"
            webbrowser.open(url)

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
                ft.Container(content=mosaico, width=320, alignment=ft.Alignment.CENTER),
                ft.Container(height=20),
                # Botão do Google Maps no estilo do botão de confirmação
                ft.ElevatedButton(
                    "Ver no Google Maps", 
                    icon=ft.Icons.MAP_OUTLINED,
                    color=ft.Colors.WHITE, 
                    bgcolor=ft.Colors.BLUE_800,
                    width=300,
                    height=50,
                    on_click=abrir_mapa
                ),
            ]
        )
        page.add(criar_layout_base(conteudo, cor_inferior=ft.Colors.with_opacity(0.5, ft.Colors.WHITE)))
        page.update()

    mostrar_tela_principal()

ft.app(target=main, assets_dir="assets")