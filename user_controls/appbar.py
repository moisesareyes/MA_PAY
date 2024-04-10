import flet as ft

def app_bar(page:ft.Page,theme):
    img=ft.Image(
        height=100,
        src=f"/images/banner.png",
        fit=ft.ImageFit.CONTAIN
    )
    def onclickre(e):
        page.go('/a')
        page.go('/')
    ApB = ft.AppBar(
        actions=[
            ft.IconButton(ft.icons.REFRESH,icon_color=ft.colors.WHITE,on_click=onclickre)
        ],
        toolbar_height=65,
        leading_width=40,
        title=img,
        center_title=True,
        bgcolor=f"{theme['maincolor']}"
    )
    return ApB