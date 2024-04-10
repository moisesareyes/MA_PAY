import flet as ft
from user_controls.themes import *
import json
from inicio import redirr
from user_controls.sql import conector
def reg_user(page: ft.Page,theme):
    mydb=conector()
    ft.border_radius.all(0)
    def on_click_reg(e):
        def comp(para,metro):
            cursor1=mydb.cursor()
            sql=f"SELECT `{para}` FROM `usuario` WHERE `{para}`='{metro.value}'"
            cursor1.execute(sql)
            myresult = cursor1.fetchone()
            if myresult:
                metro.label="EN USO"
                metro.hint_text="LLENAR CAMPO"
                metro.border_color="#ffffff"
                metro.color="#ffffff"
                metro.bgcolor="#ff0000"
                page.update()
                return False
            else:
                return True
        def contado(contar,long):
            testC=len(long.value)
            if testC<contar:
                long.label=f"MINIMO {contar} CARACTERES"
                long.hint_text=f"MINIMO {contar} CARACTERES"
                long.color="#ffffff"
                long.bgcolor="#ff0000"
                page.update()
                return False
            else: return True
        def char(ctr):
            nums = [caracter.isdigit() for caracter in ctr.value]
            strs= [caracter.isalpha() for caracter in ctr.value]
            mayus= [caracter.isupper() for caracter in ctr.value]
            minus= [caracter.islower() for caracter in ctr.value]
            if any(nums) is False or any(strs) is False or any(mayus) is False or any(minus) is False:
                ctr.label=f"Utilice mayúsculas, minúsculas, números"
                ctr.hint_text=f"Utilice mayúsculas, minúsculas, números"
                ctr.color="#ffffff"
                ctr.bgcolor="#ff0000"
                page.update()
                return False
            else: return True
        def repeat(eat,rep):
            if rep.value==eat.value:
                return True
            else:
                rep.label="LAS CONTRASEÑAS DEBEN SER IGUALES"
                rep.hint_text="LLENAR CAMPO"
                rep.border_color="#ffffff"
                rep.color="#ffffff"
                rep.bgcolor="#ff0000"
                page.update()
                return False
        def verificacion(inpusr,inpnom,inpll,inpmail,inptlf,inpass,inpassword,titulo):
            if inpusr.value=="":
                inpusr.label="LLENAR CAMPO"
                inpusr.border_color="#ffffff"
                inpusr.color="#ffffff"
                inpusr.bgcolor="#ff0000"
                inpusr.hint_text="LLENAR CAMPO"
                page.update()
            elif inpnom.value=="":
                inpnom.label="LLENAR CAMPO"
                inpnom.border_color="#ffffff"
                inpnom.color="#ffffff"
                inpnom.bgcolor="#ff0000"
                inpnom.hint_text="LLENAR CAMPO"
                page.update()
            elif inpll.value=="":
                inpll.label="LLENAR CAMPO"
                inpll.border_color="#ffffff"
                inpll.color="#ffffff"
                inpll.bgcolor="#ff0000"
                inpll.hint_text="LLENAR CAMPO"
                page.update()
            elif inpmail.value=="":
                inpmail.label="LLENAR CAMPO"
                inpmail.hint_text="LLENAR CAMPO"
                inpmail.border_color="#ffffff"
                inpmail.color="#ffffff"
                inpmail.bgcolor="#ff0000"
                page.update()
            elif inptlf.value=="":
                inptlf.label="LLENAR CAMPO"
                inptlf.hint_text="LLENAR CAMPO"
                inptlf.border_color="#ffffff"
                inptlf.color="#ffffff"
                inptlf.bgcolor="#ff0000"
                page.update()
            elif inpass.value=="":
                inpass.label="LLENAR CAMPO"
                inpass.hint_text="LLENAR CAMPO"
                inpass.border_color="#ffffff"
                inpass.color="#ffffff"
                inpass.bgcolor="#ff0000"
                page.update()
            elif inpassword.value=="":
                inpassword.label="LLENAR CAMPO"
                inpassword.hint_text="LLENAR CAMPO"
                inpassword.border_color="#ffffff"
                inpassword.color="#ffffff"
                inpassword.bgcolor="#ff0000"
                page.update()
            else: 
                ver1=comp("User_name",inpusr)
                ver2=comp("Email",inpmail)
                ver3=comp("Tlf",inptlf)
                ver4=contado(5,inpusr)
                ver5=contado(8,inptlf)
                ver6=contado(8,inp_pass)
                ver7=char(inpass)
                ver8=repeat(inpass,inpassword)
                verifi=(ver1,ver2,ver3,ver4,ver5,ver6,ver7,ver8)
                ver=all(verifi)
                print(f"Toal:{ver} des{verifi}")
                if ver==True:
                    inpname=inp_usr.value[0]+inp_usr.value[2]+inp_usr.value[4]+"-"+inp_tlf.value[2]+inp_tlf.value[3]+inp_tlf.value[-3]+inp_tlf.value[-2]+inp_tlf.value[-1]
                    inps=(inpname,inp_nombre.value,inp_apellido.value,inp_usr.value,inp_email.value,inp_pass.value,inp_tlf.value)
                    sql="INSERT INTO `usuario`(`UserID`,`Nombre`, `Apellido`, `User_name`, `Email`, `Pass`, `Tlf`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                    crs=mydb.cursor()
                    crs.execute(sql,inps)
                    mydb.commit()
                    newB=f"{inpname}-BSD"
                    sql="INSERT INTO `billetera`(`poseedor`, `tipo`, `cantidad`, `billeteraID`) VALUES (%s,%s,%s,%s)"
                    entrada=(inpname,'Bs.D',0,newB)
                    crs.execute(sql,entrada)
                    mydb.commit()
                    newD=f"{inpname}-USD"
                    sql="INSERT INTO `billetera`(`poseedor`, `tipo`, `cantidad`, `billeteraID`) VALUES (%s,%s,%s,%s)"
                    entrada=(inpname,'USD',0,newD)
                    crs.execute(sql,entrada)
                    mydb.commit()
                    mydb.close()
                    titulo.value="REGISTRO COMPLETO"
                    inpusr.disabled=True
                    inpusr.value=""
                    inpmail.disabled=True
                    inpmail.value=""
                    inptlf.disabled=True
                    inptlf.value=""
                    with open ('usr.json','r') as file:
                        inf=file.read()
                    infj=json.loads(inf)
                    theme=infj['theme']
                    futurejson={'user':f'{inpname}','theme':f'{theme}'}
                    with open ('usr.json','w') as file:
                        json.dump(futurejson,file)
                    page.go('/')
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
                    print("Error")
                    titulo.text="ERRRORR"
        verificacion(inp_usr,inp_nombre,inp_apellido,inp_email,inp_tlf,inp_pass,inp_passrd,titulo)
    titulo=ft.Text(value="REGISTRO DE USUARIO",color="WHITE",font_family="Berlin Sans FB",size=32)
    inp_usr = ft.TextField(hint_text="Usuario",label="Usuario",bgcolor=f"{theme['fondo']}",width=300,input_filter=ft.InputFilter(allow=False, regex_string="[ ]" , replacement_string=""))
    inp_nombre=ft.TextField(hint_text="Nombre",label="Nombre",bgcolor=f"{theme['fondo']}",width=150)
    inp_apellido=ft.TextField(hint_text="Apellido",label="Apellido",bgcolor=f"{theme['fondo']}",width=150)
    inp_email=ft.TextField(hint_text="Email",label="Email",bgcolor=f"{theme['fondo']}",width=150)
    inp_tlf=ft.TextField(hint_text="Telefono",label="Telefono",bgcolor=f"{theme['fondo']}",width=150,input_filter=ft.NumbersOnlyInputFilter())
    inp_pass=ft.TextField(hint_text="Contraseña",label="Contraseña",bgcolor=f"{theme['fondo']}",width=150,password=True)
    inp_passrd=ft.TextField(hint_text="Repita la contraseña",label="Repetir contraseña",bgcolor=f"{theme['fondo']}",width=150,password=True)
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    submit=ft.ElevatedButton(content=ft.Text("REGISTRAR",color="WHITE",font_family="Berlin Sans FB"),bgcolor=f"{theme['maincolor']}",width=300,on_click=on_click_reg)
    new=(
        ft.Column(
            [
                ft.Row([ft.Image(height=100,src=f"/images/banner.png",fit=ft.ImageFit.CONTAIN)],alignment=ft.MainAxisAlignment.CENTER),
                ft.Row(
                    [
                        titulo,
                    ],alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        inp_usr,
                    ],alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        inp_nombre,
                        inp_apellido
                    ],alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        inp_email,
                        inp_tlf
                    ],alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        inp_pass, 
                        inp_passrd
                    ],alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        submit
                    ],alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        ft.IconButton(icon=ft.icons.KEYBOARD_RETURN,icon_color="WHITE",icon_size=32,on_click=lambda _: page.go('/index'))
                    ],alignment=ft.MainAxisAlignment.CENTER,
                )
            ]
        )
    )
    return new
