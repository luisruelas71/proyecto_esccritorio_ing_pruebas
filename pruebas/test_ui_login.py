import re
import pytest
from playwright.sync_api import Page, expect

BASE_URL = "http://localhost:8080/vistas/Login/Login"

TXT_USUARIO = "input[id$='txtUser']"
TXT_PASSWORD = "input[id$='txtPass']"
BTN_INGRESAR = "input[id$='btnLogin']"
LBL_MENSAJE = "span[id$='lblError']"

@pytest.fixture(scope="function", autouse=True)
def abrir_login(page: Page):
    page.goto(BASE_URL, wait_until="domcontentloaded")

def test_login_exitoso(page: Page):
    page.fill(TXT_USUARIO, "Admin")
    page.fill(TXT_PASSWORD, "admin123")
    page.click(BTN_INGRESAR)
    expect(page).to_have_url(re.compile(r"/vistas/Modulos/Modulos"), timeout=7000)

def test_login_usuario_incorrecto(page: Page):
    page.fill(TXT_USUARIO, "Admin2")
    page.fill(TXT_PASSWORD, "admin124")
    page.click(BTN_INGRESAR)    
    expect(page.locator(LBL_MENSAJE)).to_contain_text("Usuario o contraseña incorrectos")

def test_login_password_incorrecta(page: Page):
    page.fill(TXT_USUARIO, "Admin")
    page.fill(TXT_PASSWORD, "Admin124")
    page.click(BTN_INGRESAR)    
    expect(page.locator(LBL_MENSAJE)).to_contain_text("Usuario o contraseña incorrectos")

def test_login_usuario_vacio(page: Page):
    page.fill(TXT_USUARIO, "")
    page.fill(TXT_PASSWORD, "Admin123")
    page.click(BTN_INGRESAR)    
    expect(page.locator(LBL_MENSAJE)).to_contain_text("Debe ingresar un nombre de usuario")

def test_login_password_vacia(page: Page):
    page.fill(TXT_USUARIO, "Admin")
    page.fill(TXT_PASSWORD, "")
    page.click(BTN_INGRESAR)    
    expect(page.locator(LBL_MENSAJE)).to_contain_text("Debe ingresar una contraseña")

def test_login_campos_vacios(page: Page):
    page.fill(TXT_USUARIO, "")
    page.fill(TXT_PASSWORD, "")
    page.click(BTN_INGRESAR)    
    expect(page.locator(LBL_MENSAJE)).to_contain_text("Debe ingresar un nombre de usuario")

#def test_password_incorrecto(page: Page):
#    page.fill(TXT_USUARIO, "Admin")
#    page.fill(TXT_PASSWORD, "admin1")
#    page.click(BTN_INGRESAR)
#    expect(page).to_have_url(re.compile(r"/vistas/Modulos/Modulos"), timeout=7000)



#python -m pytest pruebas/test_ui_login.py pruebas/test_ui_consulta_usuarios.py pruebas/test_ui_consulta_productos.py
#python -m pytest pruebas/test_ui_login.py -v --cov=.
#python -m pytest pruebas/test_ui_login.py -v --cov=.
#python -m pytest pruebas/test_ui_login.py -v --headed --slowmo 1000
#python -m pytest pruebas/test_ui_consulta_usuarios.py -v --headed --slowmo 1000
#python -m pytest pruebas/test_ui_consulta_usuarios.py -v --cov=. --cov-report=term --cov-report=html --html=report.html
#python -m pytest pruebas/test_ui_login.py pruebas/test_ui_consulta_usuarios.py pruebas/test_ui_consulta_productos.py -v --cov=. --cov-report=term --cov-report=html --html=report.html 