import pytest

def validar_cantidad_producto(cantidad):
    if cantidad is None or str(cantidad).strip() == "":
        return "El campo cantidad no puede estar vacío"
    
    try:
        val_float = float(cantidad)
        if not val_float.is_integer():
            return "La cantidad debe ser un número entero"
        
        val_int = int(val_float)
        if val_int <= 0:
            return "La cantidad debe ser mayor a 0"
            
        return True
    except (ValueError, TypeError):
        return "La cantidad debe ser un número válido"


def test_cantidad_exitosa():
    assert validar_cantidad_producto(1) is True
    assert validar_cantidad_producto("5") is True

def test_cantidad_campo_vacio():
    assert validar_cantidad_producto(None) == "El campo cantidad no puede estar vacío"
    assert validar_cantidad_producto("") == "El campo cantidad no puede estar vacío"

def test_cantidad_negativa():
    assert validar_cantidad_producto(-1) == "La cantidad debe ser mayor a 0"
    assert validar_cantidad_producto("-10") == "La cantidad debe ser mayor a 0"

def test_cantidad_decimal():
    assert validar_cantidad_producto(1.5) == "La cantidad debe ser un número entero"
    assert validar_cantidad_producto("2.75") == "La cantidad debe ser un número entero"

def test_cantidad_caracteres_especiales():
    assert validar_cantidad_producto('!"#$%&/()=') == "La cantidad debe ser un número válido"

def test_cantidad_con_letras():
    assert validar_cantidad_producto("uno") == "La cantidad debe ser un número válido"

    #c