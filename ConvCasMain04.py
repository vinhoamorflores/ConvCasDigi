import flet as ft
import os

def main(page: ft.Page):
    # --- CONFIGURAÇÃO DE ARQUIVOS ---
    IMG_FUNDO = "fundo.jpg"
    IMG_LOCAL = "botao_local.jpg"
    IMG_PRESENTES = "botao_presentes.jpg"
    IMG_CONFIRMAR = "botao_confirmar.jpg"
    IMG_VOLTAR = "botao_voltar.jpg"
    
    COR_FUNDO_PADRAO = "#E3ECF5"
    COR_BOTAO_PADRAO = "#F9F1DC"
    COR_PRIMARIA = "#B8860B"
    COR_TEXTO = "#1A3A5A"

    page.title = "Convite Interativo"
    page.theme_mode = "light"
    page.padding = 0
    page.vertical_alignment = "stretch" 
    page.horizontal_alignment = "center"

    def verificar_arquivo(nome):
        return os.path.exists(os.path.join(os.getcwd(), nome))

    def navegar_para(rota):
        page.route = rota
        renderizar_telas(None)

    def criar_botao_redondo(icone, label, rota, arquivo_img, cor_fundo_custom=None):
        tem_img = verificar_arquivo(arquivo_img)
        cor_final = cor_fundo_custom if cor_fundo_custom else COR_BOTAO_PADRAO
        return ft.Column(
            horizontal_alignment="center",
            spacing=8,
            controls=[
                ft.Container(
                    width=80, height=80, border_radius=40,
                    clip_behavior="antiAlias",
                    on_click=lambda _: navegar_para(rota),
                    border=ft.border.all(1, COR_PRIMARIA),
                    shadow=ft.BoxShadow(blur_radius=10, color="black26"),
                    content=ft.Stack(
                        controls=[
                            ft.Container(
                                bgcolor=cor_final,
                                content=ft.Image(src=arquivo_img, fit="cover", visible=tem_img)
                            ),
                            ft.Container(
                                alignment=ft.Alignment(0, 0),
                                content=ft.Icon(icon=icone, color=COR_PRIMARIA, size=30)
                            )
                        ]
                    )
                ),
                ft.Text(label, size=10, weight="bold", color=COR_TEXTO)
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
                                # CORREÇÃO AQUI: Usando page.width e page.height
                                ft.Image(
                                    src=IMG_FUNDO, 
                                    fit="cover", 
                                    width=page.width,
                                    height=page.height,
                                    visible=tem_fundo
                                ),
                                ft.Container(
                                    expand=True,
                                    alignment=ft.Alignment(0, 0.8), # Terço inferior
                                    content=ft.Row(
                                        alignment="center",
                                        spacing=15,
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
                    padding=0,
                    #bgcolor=COR_BOTAO_PADRAO,
                    #vertical_alignment="center",
                    #horizontal_alignment="center",
                    controls=[
                        ft.Column(
                            #horizontal_alignment="center",
                            #alignment="center",
                            controls=[
                                ft.Icon(icon="info_outline", size=50, color=COR_PRIMARIA),
                                ft.Text(f"{titulo}", size=22, weight="bold", color=COR_TEXTO),
                                ft.Container(height=30),
                                criar_botao_redondo("arrow_back", "VOLTAR", "/", IMG_VOLTAR, "white")
                            ]
                        )
                    ]
                )
            )
        page.update()

    # Listener para redimensionamento (ajusta a imagem se o usuário girar o celular ou mudar o navegador)
    page.on_resize = lambda e: page.update()
    
    page.on_route_change = renderizar_telas
    page.on_view_pop = lambda e: navegar_para("/")
    page.route = "/"
    renderizar_telas(None)

if __name__ == "__main__":
    ft.app(target=main)