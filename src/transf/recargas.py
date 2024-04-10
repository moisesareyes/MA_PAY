import flet as ft
from user_controls.sql import conector
import datetime
def recg (page: ft.Page,user,theme):
            mydb=conector()
            crs=mydb.cursor()
            def on_click_reg(e):
                def comp(fecha,type,datebtn,method,doc,ref,usuario,tlf,cant,tit):
                    ver=list()
                    if not fecha.value:
                        datebtn.bgcolor="#ff0000"
                        page.update()
                        ver.append(False)
                    else:ver.append(True)
                    if not type.value:
                        type.hint_text="OBLIGATORIO"
                        type.border_color="#ff0000"
                        page.update()
                        ver.append(False)
                    else:ver.append(True)
                    if not method.value:
                        method.hint_text="OBLIGATORIO"
                        method.border_color="#ff0000"
                        page.update()
                        ver.append(False)
                    else:ver.append(True)
                    if not doc.value:
                        doc.hint_text="OBLIGATORIO"
                        doc.border_color="#ff0000"
                        page.update()
                        ver.append(False)
                    else:ver.append(True)
                    if not ref.value:
                        ref.hint_text="OBLIGATORIO"
                        ref.border_color="#ff0000"
                        page.update()
                        ver.append(False)
                    else:ver.append(True)
                    if not cant.value:
                        cant.hint_text="OBLIGATORIO"
                        cant.border_color="#ff0000"
                        page.update()
                        ver.append(False)
                    else:ver.append(True)
                    if tlf.disabled==False:
                        if not tlf.value:
                            tlf.hint_text="OBLIGATORIO"
                            tlf.border_color="#ff0000"
                            page.update()
                            ver.append(False)
                        else:
                            ver.append(True)
                    else:ver.append(True)
                    verificacion=all(ver)
                    if verificacion==True:
                        if type.value=="USD":
                            new_var=(usuario,type.value,doc.value,method.value,cant.value,ref.value,"Pendiente",fecha.value)
                            sql="INSERT INTO `recarga`(`usuario`, `tipo`, `doc`, `formato`, `cantidad`,`operacion`, `status`, `fecha_tra`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                            crs.execute(sql,new_var)
                            mydb.commit()
                            tit.value="RECARGA REGISTRADA"
                            tit.color="#60d147"
                            new_hit=(usuario,'Servidor','Recarga',type.value,'Pendiente',cant.value)
                            sql="INSERT INTO `historial`(`servidor`, `recep`, `tipo`, `moneda`, `status`, `cantidad`) VALUES (%s,%s,%s,%s,%s,%s)"
                            crs.execute(sql,new_hit)
                            mydb.commit()
                            page.update()
                            mydb.close()
                        else:
                            new_var=(usuario,type.value,doc.value,method.value,cant.value,ref.value,"Pendiente",fecha.value)
                            sql="INSERT INTO `recarga`(`usuario`, `tipo`, `doc`, `formato`, `cantidad`,`operacion`, `status`, `fecha_tra`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                            crs.execute(sql,new_var)
                            mydb.commit()
                            tit.value="RECARGA REGISTRADA"
                            tit.color="#60d147"
                            new_hit=(usuario,'Servidor','Recarga',type.value,'Pendiente',cant.value)
                            sql="INSERT INTO `historial`(`servidor`, `recep`, `tipo`, `moneda`, `status`, `cantidad`) VALUES (%s,%s,%s,%s,%s,%s)"
                            crs.execute(sql,new_hit)
                            mydb.commit()
                            page.update()
                            mydb.close()
                    type.value=""
                    doc.value=""
                    method.value=""
                    cant.value=""
                    ref.value=""
                    fecha.value=""
                    page.update()
                comp(date_picker,dd_type,date_button,dd_method,doc,ref,user,tlf,cant,tit)
            def date_picker_dismissed(e):
                print(f"Date picker dismissed, value is {date_picker.value}")
            def change_date(e):
                print(f"Date picker changed, value is {date_picker.value}")
            def on_change_dis(e):
                def dis(type,method,tlf):
                    if type.value=="USD":
                        method.disabled=False
                        method.options=[
                            ft.dropdown.Option("PAYPAL")
                        ]
                        page.update()
                    if type.value=="Bs.D":
                        method.disabled=False
                        method.options=[
                            ft.dropdown.Option("TRANSFERENCIA"),
                            ft.dropdown.Option("PAGO MOVIL")
                        ]
                        page.update()
                    if not type.value:
                        method.disabled=True
                    if method.value=='PAGO MOVIL':
                        tlf.disabled=False
                        page.update()
                    if not method.value=='PAGO MOVIL':
                        tlf.disabled=True
                        page.update()
                dis(dd_type,dd_method,tlf)
            date_picker = ft.DatePicker(
                on_change=change_date,
                on_dismiss=date_picker_dismissed,
                first_date=datetime.datetime(2024, 1, 1),
                last_date=datetime.datetime.today()
            )
            page.overlay.append(date_picker)
            date_button = ft.IconButton(
                bgcolor=f"{theme['maincolor']}",
                icon_color="WHITE",
                icon_size=32,
                icon=ft.icons.CALENDAR_MONTH,
                on_click=lambda _: date_picker.pick_date(),
            )
            page.scroll='always'
            rec=ft.ElevatedButton(content=ft.Text("REGISTRAR",color="WHITE",font_family="Berlin Sans FB"),bgcolor=f"{theme['maincolor']}",width=300,on_click=on_click_reg)
            doc=ft.TextField(label="Cedula",hint_text="Cedula",input_filter=ft.NumbersOnlyInputFilter(),color="BLACK",width=300,border_color="BLACK")
            ref=ft.TextField(label="Referencia",hint_text="Referencia",input_filter=ft.NumbersOnlyInputFilter(),color="BLACK",width=300)
            cant=ft.TextField(label="Cantidad",hint_text="Cantidad",input_filter=ft.NumbersOnlyInputFilter(),color="BLACK",width=300)
            tlf=ft.TextField(label="Telefono",hint_text="Telefono",input_filter=ft.NumbersOnlyInputFilter(),color="BLACK",width=300,disabled=True)
            tit=ft.Text("REGISTRO DE RECARGA",color="BLACK",font_family="Berlin Sans FB",size=32)
            dd_type = ft.Dropdown(
                on_change=on_change_dis,
                label="TIPO DE RECARGA",
                bgcolor=f"{theme['maincolor']}",
                width=300,
                options=[
                    ft.dropdown.Option("USD"),
                    ft.dropdown.Option("Bs.D")
                ],
            )
            dd_method = ft.Dropdown(
                on_change=on_change_dis,
                disabled=True,
                label="METODO DE RECARGA",
                bgcolor="WHITE",
                width=300,
            )
            new=ft.Container(
                content=(
                    ft.Column(
                        [
                            ft.Row(
                                [
                                    tit
                                ],alignment=ft.MainAxisAlignment.CENTER
                            ),
                            ft.Row(
                                [
                                    dd_type
                                ],alignment=ft.MainAxisAlignment.CENTER
                            ),
                            ft.Row(
                                [
                                    dd_method
                                ],alignment=ft.MainAxisAlignment.CENTER
                            ),
                            ft.Row(
                                [
                                    doc
                                ],alignment=ft.MainAxisAlignment.CENTER
                            ),
                            ft.Row(
                                [
                                    ref
                                ],alignment=ft.MainAxisAlignment.CENTER
                            ),
                            ft.Row(
                                [
                                    tlf
                                ],alignment=ft.MainAxisAlignment.CENTER
                            ),
                            ft.Row(
                                [
                                    cant
                                ],alignment=ft.MainAxisAlignment.CENTER
                            ),
                            ft.Row(
                                [
                                    date_button
                                ],alignment=ft.MainAxisAlignment.CENTER
                            ),
                            ft.Row(
                                [
                                    rec
                                ],alignment=ft.MainAxisAlignment.CENTER
                            ),
                        ]
                    )
                )
            )
            if not user=="PEE-35141":return new
            else:pass