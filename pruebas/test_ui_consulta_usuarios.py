import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://localhost:44373/vistas/Usuario/Usuario"

TXT_ID_USUARIO = "input[id$='txtId']"
BTN_BUSCAR_USUARIO = "input[id$='btnConsulta']"
TBL_RESULTADO_USUARIOS = "table[id$='gvUsuarios']"
LBL_MENSAJE_USUARIO = "span[id$='lblFallo']"

@pytest.fixture(scope="function", autouse=True)
def abrir_consulta_usuarios(page: Page):
    page.goto(BASE_URL)

def test_consulta_usuario_exitoso(page: Page):
    page.fill(TXT_ID_USUARIO, "1")
    page.click(BTN_BUSCAR_USUARIO)
    expect(page.locator(TBL_RESULTADO_USUARIOS)).to_be_visible()

#def test_consulta_usuario_inexistente(page: Page):
#    page.fill(TXT_ID_USUARIO, "9999")
#    page.click(BTN_BUSCAR_USUARIO)
#    expect(page.locator(LBL_MENSAJE_USUARIO)).to_contain_text("No se ha encontrado el ID")

#def test_consulta_usuario_id_negativo(page: Page):
#    page.fill(TXT_ID_USUARIO, "-4")
#    page.click(BTN_BUSCAR_USUARIO)
#    expect(page.locator(LBL_MENSAJE_USUARIO)).to_contain_text("No se ha encontrado el ID")

#def test_consulta_usuario_id_decimal(page: Page):
#    page.fill(TXT_ID_USUARIO, "1.5")
#    page.click(BTN_BUSCAR_USUARIO)
#    expect(page.locator(LBL_MENSAJE_USUARIO)).to_contain_text("La cadena de entrada no tiene el formato correcto.")