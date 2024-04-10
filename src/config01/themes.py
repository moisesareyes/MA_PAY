import flet as ft
import json
class themess (ft.UserControl):
    def build(self):
        normie=ft.IconButton(icon=ft.icons.FORMAT_PAINT, bgcolor='#c4394d',icon_color="WHITE",icon_size=48,on_click=self.on_click_change,data='normie')
        morado=ft.IconButton(icon=ft.icons.FORMAT_PAINT, bgcolor='#7139c4',icon_color="WHITE",icon_size=48,on_click=self.on_click_change,data='morado')
        azulado=ft.IconButton(icon=ft.icons.FORMAT_PAINT, bgcolor='#0438b3',icon_color="WHITE",icon_size=48,on_click=self.on_click_change,data='azulado')
        verde=ft.IconButton(icon=ft.icons.FORMAT_PAINT, bgcolor='#06cf3c',icon_color="WHITE",icon_size=48,on_click=self.on_click_change,data='verde')
        cyan=ft.IconButton(icon=ft.icons.FORMAT_PAINT, bgcolor='#00ffff',icon_color="WHITE",icon_size=48,on_click=self.on_click_change,data='cyan')
        veceleste=ft.IconButton(icon=ft.icons.FORMAT_PAINT, bgcolor='#13f28e',icon_color="WHITE",icon_size=48,on_click=self.on_click_change,data='veceleste')
        naranja=ft.IconButton(icon=ft.icons.FORMAT_PAINT, bgcolor='#fa8314',icon_color="WHITE",icon_size=48,on_click=self.on_click_change,data='naranja')
        anaranjado=ft.IconButton(icon=ft.icons.FORMAT_PAINT, bgcolor='#f7bd1b',icon_color="WHITE",icon_size=48,on_click=self.on_click_change,data='anaranjado')
        dorado=ft.IconButton(icon=ft.icons.FORMAT_PAINT, bgcolor='#D4AF37',icon_color="WHITE",icon_size=48,on_click=self.on_click_change,data='dorado')
        dark=ft.IconButton(icon=ft.icons.FORMAT_PAINT, bgcolor='BLACK',icon_color="WHITE",icon_size=48,on_click=self.on_click_change,data='dark')
        ttt=ft.Text("TEMAS",color="BLACK",size=32,font_family="Berlin Sans FB")
        return ft.Container(
            content=(
                ft.Column(
                    [
                        ft.Row(
                            [
                                ttt
                            ],alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                            [
                                normie,morado,azulado
                            ],alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                            [
                                verde,veceleste,cyan
                            ],alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                            [
                                naranja,dorado,anaranjado
                            ],alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                            [
                                dark
                            ],alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                            [
                                ft.Text("ES NECESARIO REINICIAR DESPUES DE UN CAMBIO",color="BLACK",size=12,font_family="Berlin Sans FB")
                            ],alignment=ft.MainAxisAlignment.CENTER
                        )
                    ]
                )
            )
        )
    def on_click_change(self, e):
        data = e.control.data
        with open ('usr.json','r') as file:
            inf=file.read()
        infj=json.loads(inf)
        user=infj['user']
        futurejson={'user':f'{user}','theme':f'{data}'}
        with open ('usr.json','w') as file:
            json.dump(futurejson,file)
def newthemes(page: ft.Page):
    calc = themess()
    return calc
