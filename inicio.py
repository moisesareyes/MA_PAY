import flet as ft
import json
from user_controls.themes import *
from user_controls.navbar import nav_bar
from user_controls.appbar import app_bar
from user_controls.sql import conector
def redirr (page,theme):
    page.appbar=app_bar(page,theme)
    page.bottom_appbar=nav_bar(page,theme)
    page.go('/')
def loginp(page:ft.Page,theme):
    mydb=conector()
    crs=mydb.cursor()
    def on_click_lgoin(e):
        def comp(user,passw):
            ver=list()
            if not user.value:
                user.bgcolor="#ff0000"
                user.hint_text="OBLIGATORIO"
                page.update()
                ver.append(False)
            else:ver.append(True)
            if not passw.value:
                passw.hint_text="OBLIGATORIO"
                passw.border_color="#ff0000"
                page.update()
                ver.append(False)
            else:ver.append(True)
            verificacion=all(ver)
            return verificacion
        varr=comp(inp_usr,inp_pass)
        if varr==True:
            sql=f"SELECT `UserID`,`User_name`, `Email`, `Pass`, `Tlf` FROM `usuario` WHERE `User_name`='{inp_usr.value}' OR `Email`='{inp_usr.value}' OR `Tlf`='{inp_usr.value}'"
            crs.execute(sql)
            newval=crs.fetchone()
            sql=f"SELECT `razon`, `tiempo` FROM `bans` WHERE `user`='{newval[0]}'"
            crs.execute(sql)
            banconfirm=crs.fetchone()
            mydb.close()
            if not banconfirm:
                if newval:
                    if newval[3]==inp_pass.value:
                        with open ('usr.json','r') as file:
                            inf=file.read()
                        infj=json.loads(inf)
                        theme=infj['theme']
                        titt.color="#32a852"
                        futurejson={'user':f'{newval[0]}','theme':f'{theme}'}
                        with open ('usr.json','w') as file:
                            json.dump(futurejson,file)
                        page.update()
                        if theme=='normie':redirr(page,normie)
                        elif theme=='morado':redirr(page,morado)
                        elif theme=='azulado':redirr(page,azulado)
                        elif theme=='verde':redirr(page,verde)
                        elif theme=='cyan':redirr(page,cyan)
                        elif theme=='veceleste':redirr(page,veceleste)
                        elif theme=='anaranjado':redirr(page,anaranjado)
                        elif theme=='naranja':redirr(page,naranja)
                        elif theme=='dorado':redirr(page,dorado)
                        elif theme=='dark':redirr(page,dark)
                    else:
                        inp_pass.label="CONTRASEÑA INCORRECTA"
                        inp_pass.hint_text="CONTRASEÑA INCORRECTA"
                        inp_pass.border_color="#ff0000"
                        titt.color="#ff0025"
                        page.update()
                else:
                    titt.color="#ff0025"
                    inp_usr.label="USUARIO INCORRECTO"
                    inp_usr.hint_text="USUARIO INCORRECTA"
                    inp_usr.border_color="#ff0000"
                    page.update()
            else:
                titt.color="#ff0025"
                titt.value="USUARIO SUSPENDIDO"
                page.update()
        else:
            titt.value="ERROR"
            page.update()
    inp_pass=ft.TextField(hint_text="Contraseña",label="Contraseña",bgcolor=f"{theme['fondo']}",password=True,icon=ft.icons.PEOPLE_ALT)
    inp_usr=ft.TextField(hint_text="Nombre de usuario",label="Nombre de usuario",bgcolor=f"{theme['fondo']}",icon=ft.icons.KEY)
    titt=ft.Text(value="INICIO DE SESION",color="WHITE",size=32,font_family="Berlin Sans FB")
    btn=ft.ElevatedButton(content=ft.Text("INICIAR SESION",color="WHITE",font_family="Berlin Sans FB"),bgcolor=f"{theme['maincolor']}",width=300,on_click=on_click_lgoin)
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
                            inp_usr
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            inp_pass
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            btn
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            ft.Text(value="¿CONTRASEÑA OLVIDADA?",color="WHITE",size=12,font_family="Berlin Sans FB")
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            ft.IconButton(icon=ft.icons.KEYBOARD_RETURN,icon_color="WHITE",icon_size=32,on_click=lambda _: page.go('/index'))
                        ],alignment=ft.MainAxisAlignment.CENTER,
                    )
                ]
                )
            )
        )
    )
    return new