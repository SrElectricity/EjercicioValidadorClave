from validadorclave.modelo.errores import ValidadorError
from validadorclave.modelo.validador import ReglaValidacion, Validador, ReglaValidacionCalisto, ReglaValidacionGanimedes


def validar_clave(clave: str, reglas: list[ReglaValidacion]):
    for regla in reglas:
        validador: Validador = Validador(regla)
        try:
            validador.es_valida(clave)
        except ValidadorError as err:
            print(f'Error: {type(regla).__name__}: {err}')
        else:
            print(f'INFO: La clave es valida segun la regla {type(regla).__name__}')



if __name__ == '__main__':
    clave: str = input('Ingrese clave: ')
    validar_clave(clave, [ReglaValidacionGanimedes(), ReglaValidacionCalisto()])