from automata.pda.npda import NPDA

# Definimos el autómata de pila
"""'q0': {
            'a': {
                '$': {('q0', ('1', '$'))},
                '1': {('q0', ('1', '1'))},
            },
            'b': {'1': {('q1', '')}}
        },
        'q1': {
            'b': {'1': {('q1', '')}},
            '': {'$': {('q2', '$')}}
        }
        'q0': {
            '0': {
                'Z': {('q0', ('0', 'Z'))},
                '0': {('q0', ('0', '0'))},
            },
            '1': {'0': {('q1', '')}}
        },
        'q1': {
            '': {'0': {('q2', '')}}
        },
        'q2': {
            '1': {'0': {('q1', '')}},
            '': {'Z': {('q3', 'Z')}}
        }"""
characters = {chr(i) for i in range(ord('a'), ord('z')+1)} | {chr(i) for i in range(ord('A'), ord('Z')+1)}
digits = {str(i) for i in range(10)}
symbols = {'|', '!', '"', '#', '&', '/', '(', ')', '=', "'", '*', '{', '}', '[', ']', ',', ';', '.', '-', '_', '^'}
input_alphabet=(characters | digits | symbols)

transitions = {
    'q0': {



        letter: {
            '$': {('q2', letter+'$')}
        } for letter in characters,


    }
}


dpda = NPDA(
    states={'q0', 'q1', 'q2'},
    stack_symbols={'$', '1'},
    transitions={





    },

    initial_state='q0',
    input_symbols = input_alphabet,
    initial_stack_symbol='$',
    final_states={'q2'}
)

# Verificamos si una cadena es aceptada por el autómata
prueba = "''"+'""'
print(prueba)
print(dpda.accepts_input(prueba))
