import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'NUMBER',
    'ALPHABET',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'FLOOR_DIVIDE',
    'MODULUS',
    'POWER',
    'LPAREN',
    'RPAREN',
    'LCURLY',
    'RCURLY',
    'LSQUARE',
    'RSQUARE',
    'COMMA',
    'COLON',
    'WHILE',
    'FOR',
    'FUNCTION',
    'RETURN',
    'IN',
    'ASSIGN',
    'EQUALS',
    'NOTEQUAL',
    'LESS',
    'LESSEQUAL',
    'GREATER',
    'GREATEREQUAL',
    'IF',
    'ELSE',
    'PRINT',
    'STRING_LITERAL',
)

def t_ALPHABET(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ALPHABET')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING_LITERAL(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t

reserved = {
    'while': 'WHILE',
    'for': 'FOR',
    'do_while': 'DO_WHILE',
    'def': 'FUNCTION',
    'return': 'RETURN',
    'in': 'IN',
    'True': 'NUMBER',
    'False': 'NUMBER',
    'None': 'NUMBER',
    'list': 'ALPHABET',
    'tuple': 'ALPHABET',
    'dict': 'ALPHABET',
    'if': 'IF',
    'else': 'ELSE',
    'print': 'PRINT',
}

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_FLOOR_DIVIDE = r'//'
t_MODULUS = r'%'
t_POWER = r'\*\*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_LSQUARE = r'\['
t_RSQUARE = r'\]'
t_COMMA = r','
t_COLON = r':'
t_ASSIGN = r'='
t_EQUALS = r'=='
t_NOTEQUAL = r'!='
t_LESS = r'<'
t_LESSEQUAL = r'<='
t_GREATER = r'>'
t_GREATEREQUAL = r'>='

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'FLOOR_DIVIDE', 'MODULUS'),
    ('right', 'POWER')
)

def t_error(t):
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def p_error(p):
    print("syntax error")

def p_statement(p):
    '''
    statement : assignment
              | while_loop
              | for_loop
              | function_declaration
              | list_declaration
              | if_statement
              | print_statement
    '''
    print("Parsed successfully!")

def p_expression(p):
    '''
    expression : NUMBER
               | ALPHABET
               | expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | expression FLOOR_DIVIDE expression
               | expression MODULUS expression
               | LPAREN expression RPAREN
               | expression EQUALS expression
               | expression NOTEQUAL expression
               | expression LESS expression
               | expression LESSEQUAL expression
               | expression GREATER expression
               | expression GREATEREQUAL expression
               | expression POWER expression %prec POWER
    '''

def p_assignment(p):
    '''
    assignment : ALPHABET ASSIGN expression
    '''

def p_while_loop(p):
    '''
    while_loop : WHILE expression COLON statement
    '''

def p_for_loop(p):
    '''
    for_loop : FOR ALPHABET IN expression COLON statement 
             | FOR ALPHABET IN expression COLON
    '''

def p_function_declaration(p):
    '''
    function_declaration : FUNCTION ALPHABET LPAREN ALPHABET COMMA ALPHABET RPAREN COLON statement
                         | FUNCTION ALPHABET LPAREN ALPHABET COMMA ALPHABET RPAREN COLON statement RETURN expression
                         | FUNCTION ALPHABET LPAREN assignment COMMA assignment RPAREN COLON statement RETURN expression 
    '''

def p_list_declaration(p):
    '''
    list_declaration : ALPHABET ASSIGN LSQUARE list_items RSQUARE
                     | ALPHABET ASSIGN LCURLY dict_items RCURLY
                     | ALPHABET ASSIGN LPAREN tuple_items RPAREN
    '''

def p_list_items(p):
    '''
    list_items : expression
               | list_items COMMA expression
    '''

def p_dict_items(p):
    '''
    dict_items : key_value
               | dict_items COMMA key_value
    '''

def p_key_value(p):
    '''
    key_value : expression COLON expression 
    '''

def p_tuple_items(p):
    '''
    tuple_items : expression COMMA expression 
                | tuple_items COMMA expression
    '''

def p_if_statement(p):
    '''
    if_statement : IF expression COLON statement
                 | IF expression COLON statement else_statement
    '''

def p_else_statement(p):
    '''
    else_statement : ELSE COLON statement
    '''

def p_print_statement(p):
    '''
    print_statement : PRINT LPAREN STRING_LITERAL RPAREN
    '''

lexer = lex.lex()
parser = yacc.yacc()

while True:
    try:
        s = input("Enter your Python-like code (or 'exit' to quit): \n")
        if s.lower() == 'exit':
            break
        result = parser.parse(s)
    except Exception as e:
        print(f"Parsing Error: {e}")
