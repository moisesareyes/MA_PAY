import flet as ft
def main_ret (page:ft.Page,user,theme):
    page.scroll='always'
    rec=ft.ElevatedButton(content=ft.Text("RETIRAR BS.D",color="WHITE",font_family="Berlin Sans FB"),bgcolor=f"{theme['maincolor']}",width=300,on_click=lambda _:page.go("/retiro/bsd"))
    conv=ft.ElevatedButton(content=ft.Text("RETIRAR USD",color="WHITE",font_family="Berlin Sans FB"),bgcolor=f"{theme['maincolor']}",width=300,on_click=lambda _:page.go("/retiro/usd"))
    new=ft.Container(
        content=(
            ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text("RETIRO",color="BLACK",size=32,font_family="Berlin Sans FB")
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
                ]
            )
        )
    )
    if not user=="PEE-35141":
        return new
    else:pass