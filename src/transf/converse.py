import flet as ft
from user_controls.sql import conector
def converse (page: ft.Page,user,theme):
            mydb=conector()
            bcv=36.29
            crs=mydb.cursor()
            sql=f"SELECT * FROM `billetera` WHERE `poseedor`='{user}' AND `tipo`='USD'"
            crs.execute(sql)
            inf=crs.fetchone()
            sql=f"SELECT * FROM `billetera` WHERE `poseedor`='{user}' AND `tipo`='Bs.D'"
            crs.execute(sql)
            inf_bs=crs.fetchone()
            def on_change_converse(e):
                def op(method,new_cono,old_cono,show):
                    if method.value=="USD to Bs.D":
                        old_max=inf[3]
                        old_cono.value=f"{old_max}"
                        if new_cono.value:
                            temp=int(new_cono.value)*bcv
                            show.value=f"Cambio: {temp} Bs.D"
                        else: show.value=f"Cambio: "
                    page.update()
                    if method.value=="Bs.D to USD":
                        old_max=inf_bs[3]/bcv
                        old_cono.value=f"{old_max}"
                        if new_cono.value:
                            temp=int(new_cono.value)
                            show.value=f"Cambio: {temp} $"
                        else: show.value=f"Cambio: "
                    page.update()
                op(dd_method,monto,maxi,newcambio)
            def on_click_converse(e):
                def comp(method,monto,maxi):
                    ver=list()
                    if not method.value:
                        method.hint_text="OBLIGATORIO"
                        method.border_color="#ff0000"
                        page.update()
                        ver.append(False)
                    if not monto.value:
                        monto.hint_text="OBLIGATORIO"
                        monto.border_color="#ff0000"
                        page.update()
                        ver.append(False)
                    if monto.value:
                        if int(monto.value)>float(maxi.value) or 5>int(monto.value):
                            ver.append(False)
                        else:ver.append(True)
                    return ver
                def converse(method,cambio,maxi):
                    if method.value=="USD to Bs.D":
                        new_old=inf[3]-int(cambio.value)
                        temp=int(cambio.value)*bcv
                        new=float(inf_bs[3])+temp
                        sql=f"UPDATE `billetera` SET `cantidad`={new_old},`act`=CURRENT_TIMESTAMP WHERE `poseedor`='{user}' AND `tipo`='USD'"
                        sql2=f"UPDATE `billetera` SET `cantidad`={new},`act`=CURRENT_TIMESTAMP WHERE `poseedor`='{user}' AND `tipo`='Bs.D'"
                        crs.execute(sql)
                        crs.execute(sql2)
                        mydb.commit()
                        sql=f"SELECT * FROM `billetera` WHERE `poseedor`='{user}' AND `tipo`='USD'"
                        crs.execute(sql)
                        newinf=crs.fetchone()
                        maxi.value=newinf[3]
                        page.update()
                        new_hit=(user,user,"converse",method.value,"confirmado",temp,inf_bs[4],inf[4])
                        sql="INSERT INTO `historial`(`servidor`, `recep`, `tipo`, `moneda`, `status`, `cantidad`, `billetera1`, `billetera2`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                        crs.execute(sql,new_hit)
                        mydb.commit()
                        mydb.close()

                    if method.value=="Bs.D to USD":
                        temp=int(cambio.value)*bcv
                        new_old=float(inf_bs[3])-temp
                        new=inf[3]+int(cambio.value)
                        sql=f"UPDATE `billetera` SET `cantidad`={new},`act`=CURRENT_TIMESTAMP WHERE `poseedor`='{user}' AND `tipo`='USD'"
                        sql2=f"UPDATE `billetera` SET `cantidad`={new_old},`act`=CURRENT_TIMESTAMP WHERE `poseedor`='{user}' AND `tipo`='Bs.D'"
                        crs.execute(sql)
                        crs.execute(sql2)
                        mydb.commit()
                        sql=f"SELECT * FROM `billetera` WHERE `poseedor`='{user}' AND `tipo`='Bs.D'"
                        crs.execute(sql)
                        newinf=crs.fetchone()
                        maxi.value=newinf[3]
                        page.update()
                        new_hit=(user,user,"converse",method.value,"confirmado",temp,inf[4],inf_bs[4])
                        sql="INSERT INTO `historial`(`servidor`, `recep`, `tipo`, `moneda`, `status`, `cantidad`, `billetera1`, `billetera2`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                        crs.execute(sql,new_hit)
                        mydb.commit()
                        mydb.close()
                ver=comp(dd_method,monto,maxi)
                verificacion=all(ver)
                if verificacion==True:
                    converse(dd_method,monto,maxi)
                    monto.value=""
                    monto.disabled=True
                    dd_method.disabled=True
                    titl.value="Cambio Exitoso"
                    titl.color="#60d147"
                    page.update()
                else: pass
            dd_method = ft.Dropdown(
                on_change=on_change_converse,
                bgcolor="WHITE",
                width=300,
                options=[
                    ft.dropdown.Option("USD to Bs.D"),
                    ft.dropdown.Option("Bs.D to USD")
                ],
            )
            page.scroll='always'
            monto=ft.TextField(label="MONTO $",hint_text="MONTO$$$",input_filter=ft.NumbersOnlyInputFilter(),color="BLACK",width=300,on_change=on_change_converse)
            cambio=ft.ElevatedButton(content=ft.Text("CAMBIAR",color="WHITE",font_family="Berlin Sans FB"),bgcolor=f"{theme['maincolor']}",width=300,on_click=on_click_converse)
            maxi=ft.TextField(label="MONTO MAXIMO",hint_text="MONTO MAXIMO",bgcolor=theme['fondo'],color="BLACK",width=300,disabled=True)
            titl=ft.Text("CONVERSION",color="BLACK",size=32,font_family="Berlin Sans FB")
            newcambio=ft.Text("Cambio: ",color="BLACK",size=16,font_family="Berlin Sans FB")
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
                                    newcambio
                                ],alignment=ft.MainAxisAlignment.CENTER
                            ),
                            ft.Row(
                                [
                                    dd_method
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
                                    ft.Text("MINIMO 5 USD AL CAMBIO",color="BLACK",size=12,font_family="Berlin Sans FB")
                                ],alignment=ft.MainAxisAlignment.CENTER
                            )
                        ]
                    )
                )
            )
            if not user=="PEE-35141":return new
            else:pass