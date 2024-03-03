from automata.pda.dpda import DPDA

# Definimos el autómata de pila
"""'q0': {
            '0': {'Z': ('q0', ('0', 'Z'))},
            '0': {'0': ('q0', ('0', '0'))},
            '1': {'0': ('q1', '')},
        },
        'q1': {
            '': {'0': ('q2', '')},
        },
        'q2': {
            '1': {'0': ('q1', '')},
            '': {'Z': ('q3', 'Z')}
        }"""
dpda = DPDA(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols={'a', 'b'},
    stack_symbols={'$', '1'},
    transitions={
        'q0': {
            'a': {'$': ('q1', ('1', '$'))},
        },
        'q1': {

            'a': {'1': ('q1', ('1', '1'))},
            'b': {'1': ('q2', '')}
        },
        'q2': {
            'b': {'1': ('q2', '')},
            '': {'$': ('q3', '$')}
        }

    },
    initial_state='q0',
    initial_stack_symbol='$',
    final_states={'q3'}
)

# Verificamos si una cadena es aceptada por el autómata
prueba = 'aabb'
print(prueba)
print(dpda.accepts_input(prueba))
