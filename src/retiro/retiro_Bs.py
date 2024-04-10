import flet as ft
from user_controls.sql import conector
def retiro_bs (page: ft.Page,user,theme):
        mydb=conector()
        crs=mydb.cursor()
        sql=f"SELECT * FROM `billetera` WHERE `poseedor`='{user}' AND `tipo`='Bs.D'"
        crs.execute(sql)
        inf_bs=crs.fetchone()
        def on_change_b(e):
            def compr(banco,tlf):
                if not banco.value:
                    tlf.disabled=True
                    page.update()
                else:
                    tlf.disabled=False
                    page.update()
            compr(dd_banco,tlf)
        def on_click_b(e):
            def retirobd(usuario,banco,doc,cantidad,tlf):
                grd=(usuario,banco.value,doc.value,cantidad.value,tlf.value,'pendiente')
                sql="INSERT INTO `retiros`( `usuario`, `banco`, `documento`, `cantidad`, `tlf`, `status`) VALUES (%s,%s,%s,%s,%s,%s)"
                crs.execute(sql,grd)
                mydb.commit()
                new_hit=(usuario,banco.value,'Retiro','Bs.D','Pendiente',cantidad.value)
                sql="INSERT INTO `historial`(`servidor`, `recep`, `tipo`, `moneda`, `status`, `cantidad`) VALUES (%s,%s,%s,%s,%s,%s)"
                crs.execute(sql,new_hit)
                mydb.commit()
                page.update()
                mydb.close
            def comp(banco,doc,cantidad,tlf,maximo):
                ver=list()
                if not banco.value:
                    banco.hint_text="OBLIGATORIO"
                    banco.border_color="#ff0000"
                    page.update()
                    ver.append(False)
                else: ver.append(True)
                if not doc.value:
                    doc.hint_text="OBLIGATORIO"
                    doc.border_color="#ff0000"
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
            myveri=comp(dd_banco,doc,cant,tlf,maxi)
            if myveri==True:
                retirobd(user,dd_banco,doc,cant,tlf)
                tit.value="RETIRO REGISTRADO"
                tit.color="#60d147"
                page.update()
            else:print("Error")
        page.scroll='always'
        rec=ft.ElevatedButton(content=ft.Text("REGISTRAR",color="WHITE",font_family="Berlin Sans FB"),bgcolor=f"{theme['maincolor']}",width=300,on_click=on_click_b)
        doc=ft.TextField(label="Cedula",hint_text="Cedula",input_filter=ft.NumbersOnlyInputFilter(),color="BLACK",width=300)
        cant=ft.TextField(label="Cantidad",hint_text="Cantidad",input_filter=ft.NumbersOnlyInputFilter(),color="BLACK",width=300)
        tlf=ft.TextField(label="Telefono",hint_text="Telefono",input_filter=ft.NumbersOnlyInputFilter(),color="BLACK",width=300,disabled=True)
        maxi=ft.TextField(value=f"{inf_bs[3]}",label="MONTO MAXIMO",hint_text="MONTO MAXIMO",bgcolor=theme['fondo'],color="BLACK",width=300,disabled=True)
        tit=ft.Text("DATOS DE RETIRO",color="BLACK",font_family="Berlin Sans FB",size=32)
        dd_banco = ft.Dropdown(
            on_change=on_change_b,
            label="BANCO",
            bgcolor="#c4394d",
            width=300,
            options=[
                
                ft.dropdown.Option("0102 Banco de Venezuela, S.A.C.A."),
                ft.dropdown.Option("0104 Venezolano de Crédito"),
                ft.dropdown.Option("0105 Mercantil"),
                ft.dropdown.Option("0108 Provincial"),
                ft.dropdown.Option("0114 Bancaribe"),
                ft.dropdown.Option("0115 Exterior"),
                ft.dropdown.Option("0116 Occidental de Descuento"),
                ft.dropdown.Option("0128 Banco Caroní"),
                ft.dropdown.Option("0134 Banesco"),
                ft.dropdown.Option("0138 Banco Plaza"),
                ft.dropdown.Option("0151 BFC Banco Fondo Común"),
                ft.dropdown.Option("0156 100% Banco"),
                ft.dropdown.Option("0157 Del Sur."),
                ft.dropdown.Option("0166 Banco Agrícola de Venezuela "),
                ft.dropdown.Option("0168 Bancrecer"),
                ft.dropdown.Option("0169 Mi Banco"),
                ft.dropdown.Option("0171 Banco Activo"),
                ft.dropdown.Option("0172 Bancamiga"),
                ft.dropdown.Option("0174 Banplus"),
                ft.dropdown.Option("0175 Bicentenario del Pueblo"),
                ft.dropdown.Option("0177 Banfanb"),
                ft.dropdown.Option("0191 BNC Nacional de Crédito")
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
                                dd_banco
                            ],alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                            [
                                doc
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
                        ),
                        ft.Row(
                            [
                                ft.Text("REQUIERE PAGO MOVIL",color="BLACK",font_family="Berlin Sans FB",size=16)
                            ],alignment=ft.MainAxisAlignment.CENTER
                        )
                    ]
                )
            )
        )
        if not user=="PEE-35141":return new
        else:pass