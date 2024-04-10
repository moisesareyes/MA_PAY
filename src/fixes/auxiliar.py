import flet as ft
from user_controls.sql import conector
def aux (page:ft.Page,user,theme):
        mydb=conector()
        crs=mydb.cursor()
        sql=f"SELECT `ID`, `UserID`, `Nombre`, `Apellido`, `User_name`, `Email`, `Pass`, `Tlf`, `Reg` FROM `usuario` WHERE `UserID`='{user}'"
        crs.execute(sql)
        inf_usr=crs.fetchone()
        sql=f"SELECT `id`, `poseedor`, `tipo`, `cantidad`, `billeteraID`, `act` FROM `billetera` WHERE`poseedor`='{user}'"
        crs=mydb.cursor()
        crs.execute(sql)
        inf_bill=crs.fetchall()
        route=page.route
        carrousel = ft.Row(expand=1, wrap=False, scroll="always",alignment=ft.MainAxisAlignment.CENTER)
        page.scroll='always'
        for bill in inf_bill:
            print(bill[3])
            carrousel.controls.append(
                ft.Container(
                    border_radius=ft.border_radius.all(10),
                    border=ft.border.all(3,"BLACK"),
                    bgcolor=f"{theme['maincolor']}",
                    height=140,
                    width=325,
                    content=(
                        ft.Column(
                            [
                                ft.Row(
                                    [
                                        ft.Row(
                                            [
                                                ft.Text(value=f"{inf_usr[4]}",color="WHITE",size=20,font_family="Berlin Sans FB"),
                                            ],alignment=ft.MainAxisAlignment.START
                                        ),
                                    ]
                                ),
                                ft.Row(
                                    [
                                        ft.Text(value=f"{bill[3]} {bill[2]}",color="WHITE",size=24,font_family="Berlin Sans FB"),
                                    ],alignment=ft.MainAxisAlignment.CENTER
                                ),
                                ft.Row(
                                    [
                                        ft.Text(value=f"Ultima Actualización: {bill[5]}",color="WHITE",size=12,font_family="Berlin Sans FB")
                                    ],alignment=ft.MainAxisAlignment.CENTER
                                )
                            ]
                        )
                    )
                )
            )
        new=ft.Container(
            content=(
                ft.Column(
                    [
                        ft.Row(
                            [
                                carrousel
                            ],alignment=ft.MainAxisAlignment.CENTER
                        )
                    ]
                )
            )
        )
        if not user=="PEE-35141":
            mydb.close()
            return new
        else:mydb.close