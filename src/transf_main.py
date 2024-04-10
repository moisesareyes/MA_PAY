import flet as ft
def transf_main (page:ft.Page,user,theme):
        def onclickshow(e):
            oculto.controls.append(show)
            page.update()
        page.scroll='always'
        show=ft.Container(
                width=300,
                content=(
                    ft.Column(
                        [
                            ft.Row([ft.Text("PAGO MOVIL",color="BLACK",size=18,font_family="Berlin Sans FB")],alignment=ft.MainAxisAlignment.CENTER),
                            ft.Row([ft.Text("Telefono: 0424",color="BLACK",size=14,font_family="Berlin Sans FB")]),
                            ft.Row([ft.Text("Cedula: 30000000",color="BLACK",size=14,font_family="Berlin Sans FB")]),
                            ft.Row([ft.Text("Banco: Banco MA 0424",color="BLACK",size=14,font_family="Berlin Sans FB")]),
                            ft.Row([ft.Text("Telefono: 0424",color="BLACK",size=14,font_family="Berlin Sans FB")]),
                            ft.Row([ft.Text("TRANSFERENCIAS",color="BLACK",size=18,font_family="Berlin Sans FB")],alignment=ft.MainAxisAlignment.CENTER),
                            ft.Row([ft.Text("Cuenta: 0101010110110",color="BLACK",size=14,font_family="Berlin Sans FB")]),
                            ft.Row([ft.Text("Paypal",color="BLACK",size=18,font_family="Berlin Sans FB")],alignment=ft.MainAxisAlignment.CENTER),
                            ft.Row([ft.Text("Correo: mapaypal@gm.com",color="BLACK",size=14,font_family="Berlin Sans FB")]),
                        ]
                    )
                )
        )
        oculto = ft.Row(alignment=ft.MainAxisAlignment.CENTER)
        rec=ft.ElevatedButton(content=ft.Text("RECARGAR",color="WHITE",font_family="Berlin Sans FB"),bgcolor=f"{theme['maincolor']}",width=300,on_click=lambda _: page.go("/transf/recarga"))
        conv=ft.ElevatedButton(content=ft.Text("CONVERTIR",color="WHITE",font_family="Berlin Sans FB"),bgcolor=f"{theme['maincolor']}",width=300,on_click=lambda _: page.go("/transf/converse"))
        transf=ft.ElevatedButton(content=ft.Text("TRANSFERENCIAS",color="WHITE",font_family="Berlin Sans FB"),bgcolor=f"{theme['maincolor']}",width=300,on_click=lambda _:page.go("/transf/transferencia"))
        new=ft.Container(
            content=(
                ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Text("TRANSFERENCIAS",color="BLACK",size=32,font_family="Berlin Sans FB")
                            ],alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                            [
                                rec
                            ],alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                            [
                                conv
                            ],alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                            [
                                transf
                            ],alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row([ft.IconButton(icon=ft.icons.INFO_OUTLINED,icon_color="WHITE",bgcolor=f"{theme['maincolor']}",icon_size=24,on_click=onclickshow)],alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row(
                            [
                                oculto
                            ],alignment=ft.MainAxisAlignment.CENTER
                        )
                    ]
                )
            )
        )
        if not user=="PEE-35141":return new
        else:pass