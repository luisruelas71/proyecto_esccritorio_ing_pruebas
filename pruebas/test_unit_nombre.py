import pytest

def validar_nombre_producto(nombre):
    """Lógica para validar el nombre del producto."""
    
    if nombre is None or str(nombre).strip() == "":
        return "El campo nombre no puede estar vacío"
    if isinstance(nombre, (int, float)):
        return "El nombre no puede ser un valor numérico"
    
    nombre_str = str(nombre)
    if len(nombre_str) > 50:
        return "El nombre no debe superar los 50 caracteres"
    
    caracteres_invalidos = set('!"#$%&/()=')
    if any(char in caracteres_invalidos for char in nombre_str):
        return "El nombre contiene caracteres especiales no válidos"
    return True


def test_nombre_exitoso():
    assert validar_nombre_producto("Serrucho") is True

def test_nombre_vacio():
    assert validar_nombre_producto(None) == "El campo nombre no puede estar vacío"
    assert validar_nombre_producto("   ") == "El campo nombre no puede estar vacío"

def test_nombre_numerico():
    assert validar_nombre_producto(-1) == "El nombre no puede ser un valor numérico"
    assert validar_nombre_producto(100) == "El nombre no puede ser un valor numérico"

def test_nombre_caracteres_especiales():
    assert validar_nombre_producto('!"#$%&/()=') == "El nombre contiene caracteres especiales no válidos"

def test_nombre_longitud_excedida():
    largo = "DesarmadorDesarmadorDesarmadorDesarmadorDesarmadorDesarmadorDesarmador"
    assert validar_nombre_producto(largo) == "El nombre no debe superar los 50 caracteres"