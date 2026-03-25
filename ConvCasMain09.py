import flet as ft
import os

def main(page: ft.Page):
    # --- Configurações de Arquivos (Assets) ---
    CAMINHO_ASSETS = "assets"
    IMG_CONVITE = "Convite.jpg"
    IMG_BTN_HOME = "btn_home.png"
    IMG_BTN_CONFIRMAR = "btn_confirmar.png"
    IMG_BTN_PRESENTES = "btn_presentes.png"
    IMG_BTN_LOCAL = "btn_local.png"

    # Configurações iniciais da página
    page.title = "Convite Digital Interativo"
    page.window_width = 375
    page.window_height = 667
    page.padding = 0
    page.spacing = 0

    def obter_imagem_principal(nome_arquivo, texto_reserva):
        """Verifica se a imagem do convite existe e retorna o componente adequado"""
        caminho_foto = os.path.join(CAMINHO_ASSETS, nome_arquivo)
        
        if os.path.exists(caminho_foto):
            return ft.Image(
                src=nome_arquivo,
                fit=ft.BoxFit.COVER,
                expand=True
            )
        else:
            return ft.Text(texto_reserva, size=30, weight="bold", textAlign=ft.TextAlign.CENTER)

    def obter_imagem_botao(nome_arquivo, icone_reserva, acao):
        """Verifica existência da imagem para o botão ou usa ícone de reserva"""
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
                bgcolor=ft.Colors.WHITE,
                on_click=acao
            )

    def criar_layout_base(conteudo_superior, cor_inferior=ft.Colors.BLUE_200):
        """Estrutura 90/10 com 4 botões"""
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
                # Parte Inferior (10%) - Agora com 4 botões
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
                    expand=1
                )
            ]
        )

    # --- Funções de Troca de Tela ---

    def mostrar_tela_principal():
        page.controls.clear()
        conteudo = obter_imagem_principal(IMG_CONVITE, "Convite Principal")
        page.add(criar_layout_base(conteudo))
        page.update()

    def mostrar_tela_confirmar():
        page.controls.clear()
        conteudo = ft.Text("Confirmar Presença", size=20, weight="bold")
        page.add(criar_layout_base(conteudo, cor_inferior=ft.Colors.GREEN_100))
        page.update()

    def mostrar_tela_presentes():
        page.controls.clear()
        page.controls.clear()
        conteudo = ft.Text("Lista de Presentes", size=20, weight="bold")
        page.add(criar_layout_base(conteudo, cor_inferior=ft.Colors.BROWN_400))
        page.update()

    def mostrar_tela_local():
        page.controls.clear()
        conteudo = ft.Text("Local do Evento", size=20, weight="bold")
        page.add(criar_layout_base(conteudo, cor_inferior=ft.Colors.RED_100))
        page.update()

    # Inicia o app
    mostrar_tela_principal()

ft.app(target=main, assets_dir="assets")