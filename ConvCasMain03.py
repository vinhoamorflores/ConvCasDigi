import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Row(
            controls=[         
                ft.Container(
                    content=ft.Text("Container 1"),
                    bgcolor=ft.Colors.AMBER,
                    height=50,
                    width=100,
                    alignment=ft.Alignment.CENTER, # Aligns content inside the container
                ),
                ft.Container(
                    content=ft.Text("Container 2"),
                    bgcolor=ft.Colors.BLUE,
                    height=100,
                    width=100,
                    alignment=ft.Alignment.CENTER,
                ),
                ft.Container(
                    content=ft.Text("Container 3"),
                    bgcolor=ft.Colors.GREEN,
                    height=150,
                    width=100,
                    alignment=ft.Alignment.CENTER,
                ),
            ],
            # This is the key property for vertical alignment in a Row
            expand=True,            
            width=page.width,
            height=page.height,            
            #vertical_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main)