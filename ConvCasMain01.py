import flet as ft
import os

def main(page: ft.Page):
    # --- CONFIGURAÇÃO DE ARQUIVOS ---
    IMG_FUNDO = "fundo.jpg"
    IMG_LOCAL = "botao_local.jpg"
    IMG_PRESENTES = "botao_presentes.jpg"
    IMG_CONFIRMAR = "botao_confirmar.jpg"
    
    COR_FUNDO_PADRAO = "#E3ECF5"
    COR_BOTAO_PADRAO = "#F9F1DC"

    page.title = "Convite Interativo"
    page.theme_mode = "light"
    page.padding = 0
    # Forçamos o alinhamento para garantir visibilidade
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    def verificar_arquivo(nome):
        return os.path.exists(os.path.join(os.getcwd(), nome))

    def navegar_para(rota):
        page.route = rota
        # Chamamos o construtor de rotas manualmente para garantir a atualização
        renderizar_telas(None)

    def criar_botao_redondo(icone, label, rota, arquivo_img):
        tem_img = verificar_arquivo(arquivo_img)
        return ft.Column(
            horizontal_alignment="center",
            spacing=8,
            controls=[
                ft.Container(
                    width=85, height=85, border_radius=45,
                    clip_behavior="antiAlias",
                    on_click=lambda _: navegar_para(rota),
                    shadow=ft.BoxShadow(blur_radius=12, color="black26"),
                    content=ft.Stack(
                        controls=[
                            ft.Container(
                                bgcolor=COR_BOTAO_PADRAO if not tem_img else None,
                                content=ft.Image(src=arquivo_img, fit="cover", visible=tem_img)
                            ),
                            ft.Container(
                                alignment=ft.Alignment(0, 0),
                                content=ft.Icon(icon=icone, color="#B8860B", size=32)
                            )
                        ]
                    )
                ),
                ft.Text(label, size=11, weight="bold", color="#1A3A5A")
            ]
        )

    def renderizar_telas(e):
        page.views.clear()
        
        # --- TELA PRINCIPAL ---
        if page.route == "/" or page.route == "":
            tem_fundo = verificar_arquivo(IMG_FUNDO)
            background = []
            if tem_fundo:
                background.append(
                    ft.Image(src=IMG_FUNDO, fit="cover", expand=True, 
                             width=page.window_width, height=page.window_height)
                )

            page.views.append(
                ft.View(
                    route="/",
                    padding=0,
                    bgcolor=COR_FUNDO_PADRAO if not tem_fundo else None,
                    controls=[
                        ft.Stack(
                            expand=True,
                            controls=[
                                *background,
                                ft.Container(
                                    expand=True,
                                    alignment=ft.Alignment(0, 0.6),
                                    content=ft.Row(
                                        alignment="center",
                                        spacing=20,
                                        controls=[
                                            criar_botao_redondo("location_on", "LOCAL", "/local", IMG_LOCAL),
                                            criar_botao_redondo("card_giftcard", "PRESENTES", "/presentes", IMG_PRESENTES),
                                            criar_botao_redondo("check_circle", "CONFIRMAR", "/confirmar", IMG_CONFIRMAR),
                                        ]
                                    )
                                )
                            ]
                        )
                    ]
                )
            )

        # --- TELAS DE DESTINO ---
        elif page.route in ["/local", "/presentes", "/confirmar"]:
            titulo = page.route.replace("/", "").upper()
            page.views.append(
                ft.View(
                    route=page.route,
                    vertical_alignment="center",
                    horizontal_alignment="center",
                    bgcolor="white",
                    controls=[
                        ft.Icon(icon="info_outline", size=60, color="#B8860B"),
                        ft.Text(f"Informações: {titulo}", size=24, weight="bold"),
                        ft.Container(height=30),
                        ft.ElevatedButton(
                            "VOLTAR", 
                            icon="arrow_back",
                            on_click=lambda _: navegar_para("/")
                        )
                    ]
                )
            )
        page.update()

    # Handlers oficiais
    page.on_route_change = renderizar_telas
    page.on_view_pop = lambda e: navegar_para("/")
    
    # INICIALIZAÇÃO FORÇADA: 
    # Definimos a rota e chamamos a função de renderização manualmente uma vez.
    page.route = "/"
    renderizar_telas(None)

if __name__ == "__main__":
    ft.app(target=main)