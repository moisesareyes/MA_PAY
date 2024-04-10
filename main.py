import flet as ft
import json
from user_controls.navbar import nav_bar
from user_controls.appbar import app_bar
from user_controls.themes import *
import mysql.connector 
import time
def main(page:ft.Page):
    page.fonts = {
        "Berlin Sans FB": "fonts/Berlir.ttf",
    }
    page.title="MA Pay"
    while True:
        try:
            mydb=mysql.connector.connect(host="192.168.0.100",user="root",password="",database="test")
        except Exception as e:
            page.clean()
            page.bgcolor='#f5abb8'
            page.add(
                ft.Container(
                    content=(
                        ft.Column(
                            [
                                ft.Container(height=20),
                                ft.Row(
                                    [
                                        ft.Image(
                                                height=100,
                                                src=f"/images/banner.png",
                                                fit=ft.ImageFit.CONTAIN
                                            )
                                    ],alignment=ft.MainAxisAlignment.CENTER
                                ),
                                ft.Row(
                                    [
                                        ft.Text(value="ERROR DE CONEXIÓN",color="BLACK",size=32,font_family="Berlin Sans FB")
                                    ],alignment=ft.MainAxisAlignment.CENTER
                                ),
                                ft.Row(
                                    [
                                        ft.Text(value="INTENTANDO CONECTAR AL SERVIDOR",color="BLACK",size=16,font_family="Berlin Sans FB")
                                    ],alignment=ft.MainAxisAlignment.CENTER
                                )
                            ]
                        )
                    )
                )
            )
        else:
            from router import router
            page.clean()
            def running(user,theme):
                myRout=router(page,ft,theme)
                page.add(myRout.body)
                page.on_route_change = myRout.route_change
                page.bgcolor=f"{theme['fondo']}"
                if not user=="PEE-35141":
                    page.appbar=app_bar(page,theme)
                    page.bottom_appbar=nav_bar(page,theme)
                    page.go('/')
                else:
                    page.go('/index')
            with open ('usr.json','r') as file:
                inf=file.read()
            infj=json.loads(inf)
            user=infj['user']
            theme=infj['theme']
            if theme=='normie':running(user,normie)
            elif theme=='morado':running(user,morado)
            elif theme=='azulado':running(user,azulado)
            elif theme=='verde':running(user,verde)
            elif theme=='cyan':running(user,cyan)
            elif theme=='veceleste':running(user,veceleste)
            elif theme=='anaranjado':running(user,anaranjado)
            elif theme=='naranja':running(user,naranja)
            elif theme=='dorado':running(user,dorado)
            elif theme=='dark':running(user,dark)
            break
        finally:time.sleep(1)
ft.app(main,assets_dir="assets")