import flet as ft
from user_controls.sql import conector
def transf (page: ft.Page,user,theme):
            mydb=conector()
            crs=mydb.cursor()
            sql=f"SELECT * FROM `billetera` WHERE `poseedor`='{user}' AND `tipo`='USD'"
            crs.execute(sql)
            inf=crs.fetchone()
            sql=f"SELECT * FROM `billetera` WHERE `poseedor`='{user}' AND `tipo`='Bs.D'"
            crs.execute(sql)
            inf_bs=crs.fetchone()
            def on_change_tranf(e):
                def comp(pref,type,contacto,monto,maxi):
                    if pref.value=="USUARIO":
                        contacto.input_filter=ft.InputFilter(allow=False, regex_string="[ ]" , replacement_string="")
                        contacto.disabled=False
                        page.update()
                    if pref.value=="TELEFONO":
                        contacto.value=""
                        contacto.input_filter=ft.InputFilter(allow=True, regex_string="[0-9]", replacement_string="")
                        contacto.disabled=False
                        page.update()
                    if pref.value=="CORREO":
                        contacto.input_filter=ft.InputFilter(allow=False, regex_string="[ ]" , replacement_string="")
                        contacto.disabled=False
                        page.update()
                    if not pref.value:
                        contacto.disabled=True
                        page.update()
                    if type.value=="Bs.D":
                        maxi.value=inf_bs[3]
                        monto.disabled=False
                        page.update()
                    if type.value=="USD":
                        maxi.value=inf[3]
                        monto.disabled=False
                        page.update()
                comp(dd_pref,dd_type,contacto,monto,maxi)
            def on_click_tranf(e):
                def comp(pref,type,contacto,monto,maxi,error,titl):
                    ver=list()
                    if not pref.value:
                        pref.hint_text="OBLIGATORIO"
                        pref.border_color="#ff0000"
                        page.update()
                        ver.append(False)
                    else:ver.append(True)
                    if not type.value:
                        type.hint_text="OBLIGATORIO"
                        type.border_color="#ff0000"
                        page.update()
                        ver.append(False)
                    else:ver.append(True)
                    if not contacto.value:
                        contacto.hint_text="OBLIGATORIO"
                        contacto.border_color="#ff0000"
                        page.update()
                        ver.append(False)
                    else:ver.append(True)
                    if not monto.value:
                        monto.hint_text="OBLIGATORIO"
                        monto.border_color="#ff0000"
                        page.update()
                        ver.append(False)
                    else:ver.append(True)
                    verificacion=all(ver)
                    if verificacion==True:
                        sql=f"SELECT `UserID` FROM `usuario` WHERE `User_name`='{contacto.value}' OR `Email`='{contacto.value}' OR `Tlf`='{contacto.value}'"
                        crs.execute(sql)
                        id=crs.fetchone()
                        if not id:
                            contacto.label=f"{pref.value} NO EXISTE"
                            contacto.hint_text=f"{pref.value} NO EXISTE"
                            contacto.border_color="#ff0000"
                            page.update()
                        elif id:
                            if int(monto.value)>int(maxi.value):
                                error.color="#ff0000"
                                page.update()
                            elif 5>int(monto.value):
                                error.color="#ff0000"
                                page.update()
                            else:
                                sql=f"SELECT * FROM `billetera` WHERE `poseedor`='{id[0]}' AND `tipo`='{type.value}'"
                                crs.execute(sql)
                                inf_rcp=crs.fetchone()
                                sql=f"SELECT * FROM `billetera` WHERE `poseedor`='{user}' AND `tipo`='{type.value}'"
                                crs.execute(sql)
                                inf_usr=crs.fetchone()
                                new_to_rcp=inf_rcp[3]+int(monto.value)
                                new_to_usr=inf_usr[3]-int(monto.value)
                                sql=f"UPDATE `billetera` SET `cantidad`={new_to_rcp},`act`=CURRENT_TIMESTAMP WHERE `billeteraID`='{inf_rcp[4]}' "
                                sql2=f"UPDATE `billetera` SET `cantidad`={new_to_usr},`act`=CURRENT_TIMESTAMP WHERE `billeteraID`='{inf_usr[4]}' "
                                crs.execute(sql)
                                crs.execute(sql2)
                                monto.disabled=True
                                contacto.disabled=True
                                type.disabled=True
                                pref.disabled=True
                                titl.value="TRANSACCION COMPLETA"
                                titl.color="#60d147"
                                page.update()
                                mydb.commit()
                                new_hit=(user,id[0],"transferencia",type.value,"confirmado",monto.value,inf_rcp[4],inf_usr[4])
                                sql="INSERT INTO `historial`(`servidor`, `recep`, `tipo`, `moneda`, `status`, `cantidad`, `billetera1`, `billetera2`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                                crs.execute(sql,new_hit)
                                mydb.commit()
                                mydb.close()
                    else: print("ERROR")
                comp(dd_pref,dd_type,contacto,monto,maxi,error,titl)
            dd_pref = ft.Dropdown(
                on_change=on_change_tranf,
                label="PREFERENCIA DE USUARIO",
                bgcolor="WHITE",
                width=300,
                options=[
                    ft.dropdown.Option("USUARIO"),
                    ft.dropdown.Option("TELEFONO"),
                    ft.dropdown.Option("CORREO")
                ],
            )
            dd_type = ft.Dropdown(
                on_change=on_change_tranf,
                label="TIPO DE CAMBIO",
                bgcolor="WHITE",
                width=300,
                options=[
                    ft.dropdown.Option("USD"),
                    ft.dropdown.Option("Bs.D"),
                ],
            )
            page.scroll='always'
            contacto=ft.TextField(label="CONTACTO",hint_text="CONTACTO",bgcolor=f"{theme['fondo']}",width=300,disabled=True)
            monto=ft.TextField(label="MONTO",hint_text="MONTO",input_filter=ft.NumbersOnlyInputFilter(),color="BLACK",width=300,disabled=True)
            cambio=ft.ElevatedButton(content=ft.Text("ACEPTAR",color="WHITE",font_family="Berlin Sans FB"),bgcolor=f"{theme['maincolor']}",width=300,on_click=on_click_tranf)
            maxi=ft.TextField(label="MONTO MAXIMO",hint_text="MONTO MAXIMO",bgcolor=f"{theme['fondo']}",width=300,disabled=True)
            error=ft.Text("MINIMO 5 USD AL CAMBIO",color="BLACK",size=12,font_family="Berlin Sans FB")
            titl=ft.Text("TRANSFERENCIA",color="BLACK",size=32,font_family="Berlin Sans FB")
            new=ft.Container(
                content=(
                    ft.Column(
                        [
                            ft.Row(
                                [
                                    titl
                                ],alignment=ft.MainAxisAlignment.CENTER
                            ),
                            ft.Row(
                                [
                                    dd_pref
                                ],alignment=ft.MainAxisAlignment.CENTER
                            ),
                            ft.Row(
                                [
                                    dd_type
                                ],alignment=ft.MainAxisAlignment.CENTER
                            ),
                            ft.Row(
                                [
                                    contacto
                                ],alignment=ft.MainAxisAlignment.CENTER
                            ),
                            ft.Row(
                                [
                                    monto
                                ],alignment=ft.MainAxisAlignment.CENTER
                            ),
                            ft.Row(
                                [
                                    maxi
                                ],alignment=ft.MainAxisAlignment.CENTER
                            ),
                            ft.Row(
                                [
                                    cambio
                                ],alignment=ft.MainAxisAlignment.CENTER
                            ),
                            ft.Row(
                                [
                                    error
                                ],alignment=ft.MainAxisAlignment.CENTER
                            )
                        ]
                    )
                )
            )
            if not user=="PEE-35141":return new
            else:pass