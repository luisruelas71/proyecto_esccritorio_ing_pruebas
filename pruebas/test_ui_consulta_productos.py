import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://localhost:44373/vistas/Productos/Productos"

TXT_CLAVE_PRODUCTO = "input[id$='txtClave']"
BTN_BUSCAR_PRODUCTO = "input[id$='btnConsulta']"
TBL_RESULTADO_PRODUCTOS = "table[id$='gvProductos']"
LBL_MENSAJE_PRODUCTO = "span[id$='lblFallo']"

@pytest.fixture(scope="function", autouse=True)
def abrir_consulta_productos(page: Page):
    page.goto(BASE_URL)

def test_consulta_producto_exitosa(page: Page):
    page.fill(TXT_CLAVE_PRODUCTO, "1")
    page.click(BTN_BUSCAR_PRODUCTO)
    expect(page.locator(TBL_RESULTADO_PRODUCTOS)).to_be_visible()

def test_consulta_producto_inexistente(page: Page):
    page.fill(TXT_CLAVE_PRODUCTO, "9999")
    page.click(BTN_BUSCAR_PRODUCTO)
    expect(page.locator(LBL_MENSAJE_PRODUCTO)).to_contain_text("No se encuentra el producto registrado")

def test_consulta_producto_clave_negativa(page: Page):
    page.fill(TXT_CLAVE_PRODUCTO, "-4")
    page.click(BTN_BUSCAR_PRODUCTO)
    expect(page.locator(LBL_MENSAJE_PRODUCTO)).to_contain_text("No se encuentra el producto registrado")

def test_consulta_producto_clave_decimal(page: Page):
    page.fill(TXT_CLAVE_PRODUCTO, "1.5")
    page.click(BTN_BUSCAR_PRODUCTO)
    expect(page.locator(LBL_MENSAJE_PRODUCTO)).to_contain_text("La cadena de entrada no tiene el formato correcto.")