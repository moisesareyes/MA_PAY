import flet as ft
def user_edit(page:ft.Page,user,theme):
    import mysql.connector
    mydb=mysql.connector.connect(host="192.168.0.100",user="root",password="",database="test")
    crs=mydb.cursor()
    sql=f"SELECT `User_name`, `Email`, `Pass`, `Tlf` FROM `usuario` WHERE `UserID`='{user}'"
    crs.execute(sql)
    inf_usr=crs.fetchone()
    def onclickcomp(e):
        def comprobacion(ref,passwd,email,telefono,titlo):
            if ref.value==passwd.value:
                sql=f"UPDATE `usuario` SET `Email`='{email.value}',`Pass`='{passwd.value}',`Tlf`='{telefono.value}' WHERE `UserID`='{user}'"
                crs.execute(sql)
                mydb.commit()
                email.disabled
                ref.disabled
                telefono.disabled
                passwd.disabled
                titlo.color="#32a852"
                titlo.value="GUARDADO"
                page.update()
                mydb.close()
            else:print("a")
        def verificacion(ref,passwd,email,telefono):
            ver=list()
            if ref.value=="":
                ref.label="LLENAR CAMPO"
                ref.border_color="#ffffff"
                ref.color="#ffffff"
                ref.bgcolor="#ff0000"
                ref.hint_text="LLENAR CAMPO"
                page.update()
                ver.append(False)
            else:ver.append(True)
            if passwd.value=="":
                passwd.label="LLENAR CAMPO"
                passwd.border_color="#ffffff"
                passwd.color="#ffffff"
                passwd.bgcolor="#ff0000"
                passwd.hint_text="LLENAR CAMPO"
                page.update()
                ver.append(False)
            else:ver.append(True)
            if email.value=="":
                email.label="LLENAR CAMPO"
                email.border_color="#ffffff"
                email.color="#ffffff"
                email.bgcolor="#ff0000"
                email.hint_text="LLENAR CAMPO"
                page.update()
                ver.append(False)
            else:ver.append(True)
            if telefono.value=="":
                telefono.label="LLENAR CAMPO"
                telefono.border_color="#ffffff"
                telefono.color="#ffffff"
                telefono.bgcolor="#ff0000"
                telefono.hint_text="LLENAR CAMPO"
                page.update()
                ver.append(False)
            else:ver.append(True)
            testC=len(passwd.value)
            if testC<8:
                passwd.label=f"MINIMO 8 CARACTERES"
                passwd.hint_text=f"MINIMO 8 CARACTERES"
                passwd.color="#ffffff"
                passwd.bgcolor="#ff0000"
                page.update()
                ver.append(False)
            else:ver.append(True)
            nums = [caracter.isdigit() for caracter in passwd.value]
            strs= [caracter.isalpha() for caracter in passwd.value]
            mayus= [caracter.isupper() for caracter in passwd.value]
            minus= [caracter.islower() for caracter in passwd.value]
            if any(nums) is False or any(strs) is False or any(mayus) is False or any(minus) is False:
                passwd.label=f"Utilice mayúsculas, minúsculas, números"
                passwd.hint_text=f"Utilice mayúsculas, minúsculas, números"
                passwd.color="#ffffff"
                passwd.bgcolor="#ff0000"
                page.update()
                ver.append(False)
            else: ver.append(True)
            return ver
        elfin=all(verificacion(inp_pass,inp_passrd,inp_email,inp_tlf))
        print(elfin)
        if elfin==True:
            comprobacion(inp_pass,inp_passrd,inp_email,inp_tlf,titulo)
    titulo=ft.Text(value=f"{inf_usr[0]}",color="WHITE",font_family="Berlin Sans FB",size=32)
    inp_email=ft.TextField(value=f"{inf_usr[1]}",hint_text="Email",label="Email",bgcolor=f"{theme['fondo']}",width=150)
    inp_tlf=ft.TextField(value=f"{inf_usr[3]}",hint_text="Telefono",label="Telefono",bgcolor=f"{theme['fondo']}",width=150,input_filter=ft.NumbersOnlyInputFilter())
    inp_pass=ft.TextField(hint_text="Contraseña",label="Contraseña",bgcolor=f"{theme['fondo']}",width=150,password=True)
    inp_passrd=ft.TextField(hint_text="Repita la contraseña",label="Repetir contraseña",bgcolor=f"{theme['fondo']}",width=150,password=True)
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    submit=ft.ElevatedButton(content=ft.Text("GUARDAR",color="WHITE",font_family="Berlin Sans FB"),bgcolor=f"{theme['maincolor']}",width=300,on_click=onclickcomp)
    new=(
        ft.Column(
            [
                ft.Row(
                    [
                        titulo,
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
                )
            ]
        )
    )
    return new