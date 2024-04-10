import flet as ft
def terms (page:ft.Page,user):
    page.scroll='always'
    if not user=="PEE-35141":
        new=ft.Container(
            content=(
                ft.Column(
                    [
                        ft.Column(
                            [
                                ft.Text("TERMINOS Y CONDICIONES",color="BLACK",size=32,font_family="Berlin Sans FB")
                            ],alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Column(
                            [
                                ft.Text("Bienvenido/a a nuestra aplicación Ma Pay. Antes de utilizar nuestros servicios, lea detenidamente estos términos y condiciones. Al utilizar nuestra aplicación, usted AUTOMATICAMENTE ACEPTA regirse por estos términos y condiciones.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("*1. Servicio Ma Pay*",color="BLACK",size=16,font_family="Berlin Sans FB")

                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("1.1. Nuestra aplicación ofrece servicios de realizar transferencias, retiros y recargas en dólares y bolívares.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("*2. Registro y Cuenta de Usuario*",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("2.1. Para utilizar nuestros servicios, los usuarios deben registrarse y crear una cuenta de usuario.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("2.2. Los usuarios son responsables de mantener la confidencialidad de su información de inicio de sesión y son responsables de todas las actividades que ocurran en su cuenta.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("*3. Transferencias y Pagos*",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("3.1. Los usuarios pueden realizar transferencias de fondos a otros usuarios de la aplicación o a cuentas bancarias externas.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("3.2. Todas las transferencias y pagos están sujetos a las tarifas y límites establecidos por nuestra aplicación, que pueden estar sujetos a cambios sin previo aviso.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("*4. Retiros*",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("4.1. Los usuarios pueden retirar fondos de su Ma Pay a cuentas bancarias externas o a través de otros métodos de pago disponibles en la aplicación.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("4.2. Los retiros están sujetos a tarifas y límites establecidos por nuestra aplicación.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("*5. Recargas*",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("5.1. Los usuarios pueden recargar fondos en su Ma Pay mediante métodos de pago aceptados por nuestra aplicación.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("5.2. Las recargas están sujetas a tarifas y límites establecidos por nuestra aplicación.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("*6. Divisas*",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("6.1. Nuestra aplicación permite realizar transacciones en dólares y bolívares.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("6.2. Los tipos de cambio aplicables a las transacciones en diferentes monedas están sujetos a fluctuaciones del mercado y pueden cambiar en cualquier momento sin previo aviso.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("*7. Seguridad*",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("7.1. Nos comprometemos a mantener la seguridad de la información del usuario y a protegerla contra el acceso no autorizado o el uso indebido.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("7.2. Los usuarios son responsables de mantener la seguridad de su cuenta y deben informar cualquier actividad sospechosa de inmediato.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("*8. Responsabilidad*",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("8.1. No nos hacemos responsables de cualquier pérdida, daño o costo incurrido como resultado del uso de nuestros servicios, excepto en la medida en que la ley lo permita.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("*9. Modificaciones*",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("9.1. Nos reservamos el derecho de modificar estos términos y condiciones en cualquier momento sin previo aviso.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("9.2. Los cambios entrarán en vigencia tan pronto como se publiquen en nuestra aplicación.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("*10. Ley Aplicable*",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("10.1. Estos términos y condiciones se rigen por las leyes del país en el que operamos nuestra aplicación.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("Al utilizar nuestra aplicación Ma Pay, usted acepta estar sujeto a estos términos y condiciones. Si no está de acuerdo con estos términos y condiciones, no utilice nuestra aplicación.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                    ]
                )
            )
        )
        return new
    else:
        new=ft.Container(
            content=(
                ft.Column(
                    [
                        ft.Column(
                            [
                                ft.Text("TERMINOS Y CONDICIONES",color="BLACK",size=32,font_family="Berlin Sans FB")
                            ],alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Column(
                            [
                                ft.Text("Bienvenido/a a nuestra aplicación Ma Pay. Antes de utilizar nuestros servicios, lea detenidamente estos términos y condiciones. Al utilizar nuestra aplicación, usted AUTOMATICAMENTE ACEPTA regirse por estos términos y condiciones.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("*1. Servicio Ma Pay*",color="BLACK",size=16,font_family="Berlin Sans FB")

                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("1.1. Nuestra aplicación ofrece servicios de realizar transferencias, retiros y recargas en dólares y bolívares.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("*2. Registro y Cuenta de Usuario*",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("2.1. Para utilizar nuestros servicios, los usuarios deben registrarse y crear una cuenta de usuario.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("2.2. Los usuarios son responsables de mantener la confidencialidad de su información de inicio de sesión y son responsables de todas las actividades que ocurran en su cuenta.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("*3. Transferencias y Pagos*",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("3.1. Los usuarios pueden realizar transferencias de fondos a otros usuarios de la aplicación o a cuentas bancarias externas.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("3.2. Todas las transferencias y pagos están sujetos a las tarifas y límites establecidos por nuestra aplicación, que pueden estar sujetos a cambios sin previo aviso.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("*4. Retiros*",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("4.1. Los usuarios pueden retirar fondos de su Ma Pay a cuentas bancarias externas o a través de otros métodos de pago disponibles en la aplicación.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("4.2. Los retiros están sujetos a tarifas y límites establecidos por nuestra aplicación.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("*5. Recargas*",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("5.1. Los usuarios pueden recargar fondos en su Ma Pay mediante métodos de pago aceptados por nuestra aplicación.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("5.2. Las recargas están sujetas a tarifas y límites establecidos por nuestra aplicación.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("*6. Divisas*",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("6.1. Nuestra aplicación permite realizar transacciones en dólares y bolívares.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("6.2. Los tipos de cambio aplicables a las transacciones en diferentes monedas están sujetos a fluctuaciones del mercado y pueden cambiar en cualquier momento sin previo aviso.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("*7. Seguridad*",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("7.1. Nos comprometemos a mantener la seguridad de la información del usuario y a protegerla contra el acceso no autorizado o el uso indebido.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("7.2. Los usuarios son responsables de mantener la seguridad de su cuenta y deben informar cualquier actividad sospechosa de inmediato.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("*8. Responsabilidad*",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("8.1. No nos hacemos responsables de cualquier pérdida, daño o costo incurrido como resultado del uso de nuestros servicios, excepto en la medida en que la ley lo permita.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("*9. Modificaciones*",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("9.1. Nos reservamos el derecho de modificar estos términos y condiciones en cualquier momento sin previo aviso.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("9.2. Los cambios entrarán en vigencia tan pronto como se publiquen en nuestra aplicación.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("*10. Ley Aplicable*",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("10.1. Estos términos y condiciones se rigen por las leyes del país en el que operamos nuestra aplicación.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Text("Al utilizar nuestra aplicación Ma Pay, usted acepta estar sujeto a estos términos y condiciones. Si no está de acuerdo con estos términos y condiciones, no utilice nuestra aplicación.",color="BLACK",size=16,font_family="Berlin Sans FB")
                            ]
                        ),
                        ft.Row(
                            [
                                ft.IconButton(icon=ft.icons.KEYBOARD_RETURN,icon_color="WHITE",icon_size=32,on_click=lambda _: page.go('/index'))
                            ],alignment=ft.MainAxisAlignment.CENTER,)
                    ]
                )
            )
        )
        return new