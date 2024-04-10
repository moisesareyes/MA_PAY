import flet as ft
from src.index import index
from src.transf_main import transf_main
from src.main_retiro import main_ret
from src.config import config
from src.transf.converse import converse
from src.transf.recargas import recg
from src.transf.trasnf import transf
from src.retiro.retiro_Bs import retiro_bs
from src.history import history
from main_index import indexforusr
from reg import reg_user
from inicio import loginp
from src.fixes.auxiliar import aux
from src.retiro.retirousd import retirousd
from src.config01.themes import newthemes
from src.config01.terminos import terms
from src.config01.useredit import user_edit
import json
import time

class router:
    def __init__(self,page,ft,theme) :
        global nopage
        nopage=page
        global notheme
        notheme=theme
        with open ('usr.json','r') as file:
            inf=file.read()
        infj=json.loads(inf)
        user=infj['user']
        self.page=page
        self.ft=ft
        self.routes={
            '/':index(page,user,notheme),
            '/a':aux(nopage,user,notheme),
            '/transf':transf_main(page,user,notheme),
            '/retiro':main_ret(page,user,notheme),
            '/transf/converse':converse(page,user,notheme),
            '/transf/recarga':recg(page,user,notheme),
            '/transf/transferencia':transf(page,user,notheme),
            '/retiro/bsd':retiro_bs(page,user,notheme),
            '/retiro/usd':retirousd(page,user,notheme),
            '/config':config(page,user,notheme),
            '/config/terminos':terms(nopage,user),
            '/config/theme':newthemes(nopage),
            '/config/user':user_edit(nopage,user,notheme),
            '/history':history(page,user,notheme),
            '/index':indexforusr(page,notheme),
            '/index/reg':reg_user(page,notheme),
            '/index/login':loginp(page,notheme)}
        self.body=ft.Container(content=self.routes['/'])
    def route_change(self,route):
            with open ('usr.json','r') as file:
                inf=file.read()
            infj=json.loads(inf)
            user=infj['user']
            self.body.clean()
            self.body.content=self.routes[route.route]
            self.body.update()
            self.routes={
                '/a':aux(nopage,user,notheme),
                '/':index(nopage,user,notheme),
                '/transf':transf_main(nopage,user,notheme),
                '/retiro':main_ret(nopage,user,notheme),
                '/transf/converse':converse(nopage,user,notheme),
                '/transf/recarga':recg(nopage,user,notheme),
                '/transf/transferencia':transf(nopage,user,notheme),
                '/retiro/usd':retirousd(nopage,user,notheme),
                '/retiro/bsd':retiro_bs(nopage,user,notheme),
                '/config':config(nopage,user,notheme),
                '/config/theme':newthemes(nopage),
                '/config/terminos':terms(nopage,user),
                '/config/user':user_edit(nopage,user,notheme),
                '/history':history(nopage,user,notheme),
                '/index':indexforusr(nopage,notheme),
                '/index/reg':reg_user(nopage,notheme),
                '/index/login':loginp(nopage,notheme)}