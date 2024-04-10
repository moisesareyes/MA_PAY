import flet as ft
from user_controls.sql import conector
def retirousd (page: ft.Page,user,theme):
        mydb=conector()
        crs=mydb.cursor()
        sql=f"SELECT * FROM `billetera` WHERE `poseedor`='{user}' AND `tipo`='USD'"
        crs.execute(sql)
        inf_bs=crs.fetchone()
        def on_change_b(e):
            def compr(banco,tlf):
                if not banco.value:
                    tlf.disabled=True
                    page.update()
                else:
                    tlf.disabled=False
                    if banco.value=="Zinli":
                        tlf.input_filter=ft.InputFilter(allow=True, regex_string="[0-9]", replacement_string="")
                        tlf.value=""
                    elif banco.value=="Paypal":tlf.input_filter=ft.InputFilter(allow=False, regex_string="['ñ']" , replacement_string="")
                    page.update()
            compr(dd_type,tlf)
        def on_click_b(e):
            def retirobd(usuario,banco,cantidad,tlf):
                grd=(usuario,banco.value,cantidad.value,tlf.value,'pendiente')
                sql="INSERT INTO `retiros`( `usuario`, `banco`, `cantidad`, `tlf`, `status`) VALUES (%s,%s,%s,%s,%s)"
                crs.execute(sql,grd)
                mydb.commit()
                new_hit=(usuario,banco.value,'Retiro','USD','Pendiente',cantidad.value)
                sql="INSERT INTO `historial`(`servidor`, `recep`, `tipo`, `moneda`, `status`, `cantidad`) VALUES (%s,%s,%s,%s,%s,%s)"
                crs.execute(sql,new_hit)
                mydb.commit()
                page.update()
                mydb.close()
            def comp(banco,cantidad,tlf,maximo):
                ver=list()
                if not banco.value:
                    banco.hint_text="OBLIGATORIO"
                    banco.border_color="#ff0000"
                    page.update()
                    ver.append(False)
                else: ver.append(True)
                if not cantidad.value:
                    cantidad.hint_text="OBLIGATORIO"
                    cantidad.border_color="#ff0000"
                    page.update()
                    ver.append(False)
                else: 
                    ver.append(True)
                    if float(cantidad.value)>float(maximo.value):
                        cantidad.hint_text="OBLIGATORIO"
                        cantidad.border_color="#ff0000"
                        page.update()
                        ver.append(False)
                    else: ver.append(True)
                if not tlf.value:
                    cantidad.hint_text="OBLIGATORIO"
                    cantidad.border_color="#ff0000"
                    page.update()
                    ver.append(False)
                else: ver.append(True)
                verificacion=all(ver)
                return verificacion
            myveri=comp(dd_type,cant,tlf,maxi)
            if myveri==True:
                retirobd(user,dd_type,cant,tlf)
                tit.value="RETIRO REGISTRADO"
                tit.color="#60d147"
                page.update()
            else:print("Error")
        page.scroll='always'
        rec=ft.ElevatedButton(content=ft.Text("REGISTRAR",color="WHITE",font_family="Berlin Sans FB"),bgcolor=f"{theme['maincolor']}",width=300,on_click=on_click_b)
        cant=ft.TextField(label="Cantidad",hint_text="Cantidad",input_filter=ft.NumbersOnlyInputFilter(),color="BLACK",width=300)
        tlf=ft.TextField(label="Contacto",hint_text="Contacto",input_filter=ft.NumbersOnlyInputFilter(),color="BLACK",width=300,disabled=True)
        maxi=ft.TextField(value=f"{inf_bs[3]}",label="MONTO MAXIMO",hint_text="MONTO MAXIMO",bgcolor=theme['fondo'],color="BLACK",width=300,disabled=True)
        tit=ft.Text("DATOS DE RETIRO",color="BLACK",font_family="Berlin Sans FB",size=32)
        dd_type = ft.Dropdown(
            on_change=on_change_b,
            label="Preferencia",
            bgcolor="#c4394d",
            width=300,
            options=[
                ft.dropdown.Option("Zinli"),
                ft.dropdown.Option("Paypal")
            ],
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
                                maxi
                            ],alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                            [
                                rec
                            ],alignment=ft.MainAxisAlignment.CENTER
                        )
                    ]
                )
            )
        )
        if not user=="PEE-35141":return new
        else:pass