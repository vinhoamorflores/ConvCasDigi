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
    COR_PRIMARIA = "#B8860B"
    COR_TEXTO = "#1A3A5A"

    page.title = "Convite Interativo"
    page.theme_mode = "light"
    page.padding = 0
    page.spacing = 0

    def verificar_arquivo(nome):
        return os.path.exists(os.path.join(os.getcwd(), nome))

    def navegar_para(rota):
        page.route = rota
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
                                content=ft.Icon(icon=icone, color=COR_PRIMARIA, size=32)
                            )
                        ]
                    )
                ),
                ft.Text(label, size=11, weight="bold", color=COR_TEXTO)
            ]
        )

    def renderizar_telas(e):
        page.views.clear()
        
        # --- TELA PRINCIPAL ---
        if page.route == "/" or page.route == "":
            tem_fundo = verificar_arquivo(IMG_FUNDO)
            
            page.views.append(
                ft.View(
                    route="/",
                    padding=0,
                    controls=[
                        ft.Stack(
                            expand=True,
                            controls=[
                                # 1. Imagem de Fundo
                                ft.Image(
                                    src=IMG_FUNDO, 
                                    fit="cover", 
                                    width=page.width,
                                    height=page.height,
                                    visible=tem_fundo
                                ),                                
                                # 2. Container dos Botões (Posicionamento Manual)
                                ft.Container(
                                    expand=True,
                                    #alignment=ft.Alignment.CENTER,                                                      
                                    content=ft.Row(
                                        alignment="center",
                                        spacing=50,
                                        controls=[
                                            criar_botao_redondo("location_on", "LOCAL", "/local", IMG_LOCAL),
                                            criar_botao_redondo("card_giftcard", "PRESENTES", "/presentes", IMG_PRESENTES),
                                            criar_botao_redondo("check_circle", "CONFIRMAR", "/confirmar", IMG_CONFIRMAR),
                                        ],
                                        # This is the key property for vertical alignment in a Row
                                        #width=page.width,
                                        #height=page.height,            
                                        #expand=True,            
                                        #vertical_alignment=ft.Alignment.BOTTOM_CENTER
                                        #alignment=ft.CrossAxisAlignment.CENTER 
                                        #alignment=ft.MainAxisAlignment.START
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
                        ft.Icon(icon="info_outline", size=60, color=COR_PRIMARIA),
                        ft.Text(f"Informações: {titulo}", size=24, weight="bold", color=COR_TEXTO),
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

    page.on_route_change = renderizar_telas
    page.on_view_pop = lambda e: navegar_para("/")
    page.on_resize = lambda e: page.update()

    page.route = "/"
    renderizar_telas(None)

if __name__ == "__main__":
    ft.app(target=main)