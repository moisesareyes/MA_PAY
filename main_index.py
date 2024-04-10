import flet as ft

def indexforusr(page:ft.Page,theme):
    titt=ft.Text(value="OPCION DE USUARIO",color="BLACK",size=32,font_family="Berlin Sans FB")
    btnop2=ft.ElevatedButton(content=ft.Text("REGISTRO DE USUARIO",color="WHITE",font_family="Berlin Sans FB"),bgcolor=f"{theme['maincolor']}",width=300,on_click=lambda _: page.go("/index/reg"))
    btn=ft.ElevatedButton(content=ft.Text("INICIAR SESION",color="WHITE",font_family="Berlin Sans FB"),bgcolor=f"{theme['maincolor']}",width=300,on_click=lambda _: page.go("/index/login"))
    new=( 
        ft.Container(
            content=(
                ft.Column([
                    ft.Row([ft.Image(height=100,src=f"/images/banner.png",fit=ft.ImageFit.CONTAIN)],alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row(
                        [
                            titt
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            btn
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            btnop2
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            ft.TextButton(
                                content=ft.Container(
                                    content=ft.Column([ 
                                        ft.Row([
                                            ft.Text(value="TERMINOS Y CONDICIONES", size=12,color="BLACK"),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,)]
                                    ),
                                ),
                                on_click=lambda _: page.go('/config/terminos')
                            )
                        ],alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        [
                            ft.IconButton(icon=ft.icons.PALETTE,icon_color="WHITE",bgcolor=theme['maincolor'],icon_size=32,on_click=lambda _: page.go('/config/theme'))
                        ],alignment=ft.MainAxisAlignment.CENTER
                    )
                ]
                )
            )
        )
    )
    return new