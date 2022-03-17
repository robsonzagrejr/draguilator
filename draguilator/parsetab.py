
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN BREAK COMMA DEFINE DIVIDE ELSE EQUAL_TO FLOAT FLOAT_CONSTANT FOR GREATER_EQUAL_THAN GREATER_THAN IDENT IF INT INT_CONSTANT LBRACES LBRACKET LESS_EQUAL_THAN LESS_THAN LPAREN MINUS MODULO NEW NOT_EQUAL_TO NULL PLUS PRINT RBRACES RBRACKET READ RETURN RPAREN SEMICOLON STRING STRING_CONSTANT TIMESprogram : make_scope statement close_scope\n              | make_scope funclist close_scope\n              | make_scope empty close_scope\n    funclist : funcdef _funclist\n    _funclist : funclist\n                | empty\n    funcdef : DEFINE IDENT make_scope LPAREN paramlist RPAREN LBRACES statelist RBRACES close_scope\n    paramlist : INT IDENT _paramlist\n                | FLOAT IDENT _paramlist\n                | STRING IDENT _paramlist\n                | empty\n    _paramlist : COMMA paramlist\n                 | empty\n    statement : vardecl SEMICOLON\n                | atribstat SEMICOLON\n                | printstat SEMICOLON\n                | readstat SEMICOLON\n                | returnstat SEMICOLON\n                | ifstat\n                | forstat\n                | LBRACES statelist RBRACES \n                | check_loop_scope BREAK SEMICOLON\n                | SEMICOLON\n    vardecl : INT IDENT vardecl_line\n              | FLOAT IDENT vardecl_line\n              | STRING IDENT vardecl_line\n    vardecl_line : LBRACKET INT_CONSTANT RBRACKET vardecl_line\n                   | empty\n    atribstat : lvalue ASSIGN _atribstat\n    _atribstat : PLUS _atribstat_help\n                 | MINUS _atribstat_help\n                 | __atribstat\n                 | IDENT ___atribstat\n                 | allocexpression\n    _atribstat_help : IDENT lvalue_line term_line numexpression_line _expression\n                      | __atribstat\n    __atribstat : _node_int_constant term_line numexpression_line _expression\n                 | _node_float_constant term_line numexpression_line _expression\n                 | _node_str_constant term_line numexpression_line _expression\n                 | _node_null_constant term_line numexpression_line _expression\n                 | LPAREN numexpression RPAREN term_line numexpression_line _expression\n    ___atribstat : lvalue_line term_line numexpression_line _expression\n                  | LPAREN paramlistcall RPAREN\n    paramlistcall : IDENT _paramlistcall\n\t\t\t         | empty\n    _paramlistcall : COMMA paramlistcall\n\t\t\t          | empty\n    printstat : PRINT expression\n    readstat : READ lvalue\n    returnstat : RETURN\n    ifstat : IF make_scope LPAREN make_expression_goto RPAREN LBRACES statelist RBRACES close_scope _ifstat\n    _ifstat : make_scope ELSE statement close_scope\n              | empty\n    forstat : FOR make_loop_scope LPAREN atribstat SEMICOLON make_loop_label make_expression_goto SEMICOLON atribstat RPAREN  statement close_scope\n    statelist : statement _statelist\n    _statelist : statelist\n                 | empty\n    allocexpression : NEW _allocexpression\n    _allocexpression : INT allocexpression_line\n                       | FLOAT allocexpression_line\n                       | STRING allocexpression_line\n    allocexpression_line : LBRACKET numexpression RBRACKET _allocexpression_line\n    _allocexpression_line : allocexpression_line\n                            | empty\n    expression : numexpression _expression\n    _expression : LESS_THAN numexpression\n                  | GREATER_THAN numexpression\n                  | LESS_EQUAL_THAN numexpression\n                  | GREATER_EQUAL_THAN numexpression\n                  | EQUAL_TO numexpression\n                  | NOT_EQUAL_TO numexpression\n                  | empty\n    numexpression : term numexpression_line\n    numexpression_line : PLUS term numexpression_line\n                         | MINUS term numexpression_line\n                         | empty\n    term : unaryexpr term_line\n    term_line : TIMES unaryexpr term_line\n                | DIVIDE unaryexpr term_line\n                | MODULO unaryexpr term_line\n                | empty\n    unaryexpr : factor\n                 | PLUS factor\n                 | MINUS factor\n    factor : _node_int_constant \n             | _node_float_constant\n             | _node_str_constant\n             | _node_null_constant\n             | lvalue\n             | LPAREN numexpression RPAREN\n    _node_int_constant : INT_CONSTANT\n    _node_float_constant : FLOAT_CONSTANT\n    _node_str_constant : STRING_CONSTANT\n    _node_null_constant : NULL\n    lvalue : IDENT lvalue_line\n    lvalue_line : LBRACKET numexpression RBRACKET lvalue_line\n                  | empty\n    make_scope :make_loop_scope :make_loop_label :make_expression_goto : expressioncheck_loop_scope :close_scope :empty :'
    
_lr_action_items = {'LBRACES':([0,2,7,12,13,14,31,32,33,34,35,37,70,74,171,191,193,204,215,219,223,224,225,227,228,229,230,231,],[-98,14,-23,-19,-20,14,-14,-15,-16,-17,-18,14,-21,-22,191,14,204,14,-103,-104,-51,-53,14,14,-103,-103,-54,-52,]),'SEMICOLON':([0,2,6,7,8,9,10,11,12,13,14,18,24,31,32,33,34,35,37,38,42,43,45,46,47,49,50,51,52,53,56,57,58,59,60,62,63,64,65,66,70,74,75,77,79,80,81,84,85,86,87,88,89,90,93,100,101,104,105,109,110,111,117,118,119,120,121,122,123,125,126,127,128,130,134,135,136,137,138,139,140,141,142,143,144,145,147,148,150,151,152,153,157,158,159,160,161,162,164,165,166,167,168,169,170,178,179,180,181,185,186,187,188,189,191,197,198,200,201,203,204,210,211,212,213,214,215,219,223,224,225,227,228,229,230,231,],[-98,7,31,-23,32,33,34,35,-19,-20,7,-104,-50,-14,-15,-16,-17,-18,7,74,-104,-95,-97,-104,-104,-48,-104,-104,-104,-82,-85,-86,-87,-88,-89,-91,-92,-93,-94,-49,-21,-22,-24,-28,-25,-26,-29,-32,-104,-34,-104,-104,-104,-104,-65,-72,-73,-76,-77,-81,-83,-84,-104,-30,-104,-36,-31,-33,-104,-104,-104,-104,-104,-58,-66,-67,-68,-69,-70,-71,-104,-104,-104,-104,-104,-90,-101,172,-104,-96,-104,-104,-104,-104,-104,-104,-104,-59,-60,-61,-74,-75,-78,-79,-80,-27,-104,-104,-43,-37,-38,-39,-40,-104,7,-104,-42,-104,-104,216,7,-35,-41,-62,-63,-64,-103,-104,-51,-53,7,7,-103,-103,-54,-52,]),'INT':([0,2,7,12,13,14,31,32,33,34,35,37,70,74,92,149,191,204,206,215,219,223,224,225,227,228,229,230,231,],[-98,17,-23,-19,-20,17,-14,-15,-16,-17,-18,17,-21,-22,131,174,17,17,174,-103,-104,-51,-53,17,17,-103,-103,-54,-52,]),'FLOAT':([0,2,7,12,13,14,31,32,33,34,35,37,70,74,92,149,191,204,206,215,219,223,224,225,227,228,229,230,231,],[-98,19,-23,-19,-20,19,-14,-15,-16,-17,-18,19,-21,-22,132,175,19,19,175,-103,-104,-51,-53,19,19,-103,-103,-54,-52,]),'STRING':([0,2,7,12,13,14,31,32,33,34,35,37,70,74,92,149,191,204,206,215,219,223,224,225,227,228,229,230,231,],[-98,20,-23,-19,-20,20,-14,-15,-16,-17,-18,20,-21,-22,133,176,20,20,176,-103,-104,-51,-53,20,20,-103,-103,-54,-52,]),'PRINT':([0,2,7,12,13,14,31,32,33,34,35,37,70,74,191,204,215,219,223,224,225,227,228,229,230,231,],[-98,22,-23,-19,-20,22,-14,-15,-16,-17,-18,22,-21,-22,22,22,-103,-104,-51,-53,22,22,-103,-103,-54,-52,]),'READ':([0,2,7,12,13,14,31,32,33,34,35,37,70,74,191,204,215,219,223,224,225,227,228,229,230,231,],[-98,23,-23,-19,-20,23,-14,-15,-16,-17,-18,23,-21,-22,23,23,-103,-104,-51,-53,23,23,-103,-103,-54,-52,]),'RETURN':([0,2,7,12,13,14,31,32,33,34,35,37,70,74,191,204,215,219,223,224,225,227,228,229,230,231,],[-98,24,-23,-19,-20,24,-14,-15,-16,-17,-18,24,-21,-22,24,24,-103,-104,-51,-53,24,24,-103,-103,-54,-52,]),'IF':([0,2,7,12,13,14,31,32,33,34,35,37,70,74,191,204,215,219,223,224,225,227,228,229,230,231,],[-98,25,-23,-19,-20,25,-14,-15,-16,-17,-18,25,-21,-22,25,25,-103,-104,-51,-53,25,25,-103,-103,-54,-52,]),'FOR':([0,2,7,12,13,14,31,32,33,34,35,37,70,74,191,204,215,219,223,224,225,227,228,229,230,231,],[-98,26,-23,-19,-20,26,-14,-15,-16,-17,-18,26,-21,-22,26,26,-103,-104,-51,-53,26,26,-103,-103,-54,-52,]),'DEFINE':([0,2,16,221,226,],[-98,27,27,-103,-7,]),'IDENT':([0,2,7,12,13,14,17,19,20,22,23,27,31,32,33,34,35,37,44,48,54,55,61,70,74,82,83,91,94,95,96,97,98,99,102,103,106,107,108,113,114,124,163,172,174,175,176,183,191,192,204,215,216,219,223,224,225,227,228,229,230,231,],[-98,18,-23,-19,-20,18,42,46,47,18,18,69,-14,-15,-16,-17,-18,18,18,85,18,18,18,-21,-22,119,119,18,18,18,18,18,18,18,18,18,18,18,18,18,18,155,18,-100,194,195,196,155,18,18,18,-103,18,-104,-51,-53,18,18,-103,-103,-54,-52,]),'BREAK':([0,2,7,12,13,14,15,31,32,33,34,35,37,70,74,191,204,215,219,223,224,225,227,228,229,230,231,],[-98,-102,-23,-19,-20,-102,38,-14,-15,-16,-17,-18,-102,-21,-22,-102,-102,-103,-104,-51,-53,-102,-102,-103,-103,-54,-52,]),'$end':([0,1,2,3,4,5,7,12,13,16,28,29,30,31,32,33,34,35,39,40,41,70,74,215,219,221,223,224,226,228,229,230,231,],[-98,0,-104,-103,-103,-103,-23,-19,-20,-104,-1,-2,-3,-14,-15,-16,-17,-18,-4,-5,-6,-21,-22,-103,-104,-103,-51,-53,-7,-103,-103,-54,-52,]),'RBRACES':([7,12,13,31,32,33,34,35,36,37,70,71,72,73,74,202,215,217,219,223,224,228,229,230,231,],[-23,-19,-20,-14,-15,-16,-17,-18,70,-104,-21,-55,-56,-57,-22,215,-103,221,-104,-51,-53,-103,-103,-54,-52,]),'LBRACKET':([18,42,46,47,85,117,119,131,132,133,150,201,],[44,76,76,76,44,44,44,163,163,163,76,163,]),'ASSIGN':([18,21,43,45,117,151,],[-104,48,-95,-97,-104,-96,]),'TIMES':([18,43,45,52,53,56,57,58,59,60,62,63,64,65,85,87,88,89,90,110,111,117,119,123,142,143,144,145,151,152,161,],[-104,-95,-97,106,-82,-85,-86,-87,-88,-89,-91,-92,-93,-94,-104,106,106,106,106,-83,-84,-104,-104,106,106,106,106,-90,-96,106,106,]),'DIVIDE':([18,43,45,52,53,56,57,58,59,60,62,63,64,65,85,87,88,89,90,110,111,117,119,123,142,143,144,145,151,152,161,],[-104,-95,-97,107,-82,-85,-86,-87,-88,-89,-91,-92,-93,-94,-104,107,107,107,107,-83,-84,-104,-104,107,107,107,107,-90,-96,107,107,]),'MODULO':([18,43,45,52,53,56,57,58,59,60,62,63,64,65,85,87,88,89,90,110,111,117,119,123,142,143,144,145,151,152,161,],[-104,-95,-97,108,-82,-85,-86,-87,-88,-89,-91,-92,-93,-94,-104,108,108,108,108,-83,-84,-104,-104,108,108,108,108,-90,-96,108,108,]),'PLUS':([18,22,43,44,45,48,51,52,53,56,57,58,59,60,61,62,63,64,65,85,87,88,89,90,91,94,95,96,97,98,99,102,103,105,106,107,108,109,110,111,113,117,119,123,125,126,127,128,140,141,142,143,144,145,151,152,153,161,163,168,169,170,172,179,189,192,],[-104,54,-95,54,-97,82,102,-104,-82,-85,-86,-87,-88,-89,54,-91,-92,-93,-94,-104,-104,-104,-104,-104,54,54,54,54,54,54,54,54,54,-77,54,54,54,-81,-83,-84,54,-104,-104,-104,102,102,102,102,102,102,-104,-104,-104,-90,-96,-104,102,-104,54,-78,-79,-80,-100,102,102,54,]),'MINUS':([18,22,43,44,45,48,51,52,53,56,57,58,59,60,61,62,63,64,65,85,87,88,89,90,91,94,95,96,97,98,99,102,103,105,106,107,108,109,110,111,113,117,119,123,125,126,127,128,140,141,142,143,144,145,151,152,153,161,163,168,169,170,172,179,189,192,],[-104,55,-95,55,-97,83,103,-104,-82,-85,-86,-87,-88,-89,55,-91,-92,-93,-94,-104,-104,-104,-104,-104,55,55,55,55,55,55,55,55,55,-77,55,55,55,-81,-83,-84,55,-104,-104,-104,103,103,103,103,103,103,-104,-104,-104,-90,-96,-104,103,-104,55,-78,-79,-80,-100,103,103,55,]),'LESS_THAN':([18,43,45,50,51,52,53,56,57,58,59,60,62,63,64,65,85,87,88,89,90,101,104,105,109,110,111,117,119,123,125,126,127,128,140,141,142,143,144,145,151,152,153,157,158,159,160,161,166,167,168,169,170,179,180,189,197,200,],[-104,-95,-97,94,-104,-104,-82,-85,-86,-87,-88,-89,-91,-92,-93,-94,-104,-104,-104,-104,-104,-73,-76,-77,-81,-83,-84,-104,-104,-104,-104,-104,-104,-104,-104,-104,-104,-104,-104,-90,-96,-104,-104,94,94,94,94,-104,-74,-75,-78,-79,-80,-104,94,-104,94,94,]),'GREATER_THAN':([18,43,45,50,51,52,53,56,57,58,59,60,62,63,64,65,85,87,88,89,90,101,104,105,109,110,111,117,119,123,125,126,127,128,140,141,142,143,144,145,151,152,153,157,158,159,160,161,166,167,168,169,170,179,180,189,197,200,],[-104,-95,-97,95,-104,-104,-82,-85,-86,-87,-88,-89,-91,-92,-93,-94,-104,-104,-104,-104,-104,-73,-76,-77,-81,-83,-84,-104,-104,-104,-104,-104,-104,-104,-104,-104,-104,-104,-104,-90,-96,-104,-104,95,95,95,95,-104,-74,-75,-78,-79,-80,-104,95,-104,95,95,]),'LESS_EQUAL_THAN':([18,43,45,50,51,52,53,56,57,58,59,60,62,63,64,65,85,87,88,89,90,101,104,105,109,110,111,117,119,123,125,126,127,128,140,141,142,143,144,145,151,152,153,157,158,159,160,161,166,167,168,169,170,179,180,189,197,200,],[-104,-95,-97,96,-104,-104,-82,-85,-86,-87,-88,-89,-91,-92,-93,-94,-104,-104,-104,-104,-104,-73,-76,-77,-81,-83,-84,-104,-104,-104,-104,-104,-104,-104,-104,-104,-104,-104,-104,-90,-96,-104,-104,96,96,96,96,-104,-74,-75,-78,-79,-80,-104,96,-104,96,96,]),'GREATER_EQUAL_THAN':([18,43,45,50,51,52,53,56,57,58,59,60,62,63,64,65,85,87,88,89,90,101,104,105,109,110,111,117,119,123,125,126,127,128,140,141,142,143,144,145,151,152,153,157,158,159,160,161,166,167,168,169,170,179,180,189,197,200,],[-104,-95,-97,97,-104,-104,-82,-85,-86,-87,-88,-89,-91,-92,-93,-94,-104,-104,-104,-104,-104,-73,-76,-77,-81,-83,-84,-104,-104,-104,-104,-104,-104,-104,-104,-104,-104,-104,-104,-90,-96,-104,-104,97,97,97,97,-104,-74,-75,-78,-79,-80,-104,97,-104,97,97,]),'EQUAL_TO':([18,43,45,50,51,52,53,56,57,58,59,60,62,63,64,65,85,87,88,89,90,101,104,105,109,110,111,117,119,123,125,126,127,128,140,141,142,143,144,145,151,152,153,157,158,159,160,161,166,167,168,169,170,179,180,189,197,200,],[-104,-95,-97,98,-104,-104,-82,-85,-86,-87,-88,-89,-91,-92,-93,-94,-104,-104,-104,-104,-104,-73,-76,-77,-81,-83,-84,-104,-104,-104,-104,-104,-104,-104,-104,-104,-104,-104,-104,-90,-96,-104,-104,98,98,98,98,-104,-74,-75,-78,-79,-80,-104,98,-104,98,98,]),'NOT_EQUAL_TO':([18,43,45,50,51,52,53,56,57,58,59,60,62,63,64,65,85,87,88,89,90,101,104,105,109,110,111,117,119,123,125,126,127,128,140,141,142,143,144,145,151,152,153,157,158,159,160,161,166,167,168,169,170,179,180,189,197,200,],[-104,-95,-97,99,-104,-104,-82,-85,-86,-87,-88,-89,-91,-92,-93,-94,-104,-104,-104,-104,-104,-73,-76,-77,-81,-83,-84,-104,-104,-104,-104,-104,-104,-104,-104,-104,-104,-104,-104,-90,-96,-104,-104,99,99,99,99,-104,-74,-75,-78,-79,-80,-104,99,-104,99,99,]),'RBRACKET':([18,43,45,51,52,53,56,57,58,59,60,62,63,64,65,78,101,104,105,109,110,111,116,117,140,141,142,143,144,145,151,166,167,168,169,170,190,],[-104,-95,-97,-104,-104,-82,-85,-86,-87,-88,-89,-91,-92,-93,-94,117,-73,-76,-77,-81,-83,-84,150,-104,-104,-104,-104,-104,-104,-90,-96,-74,-75,-78,-79,-80,201,]),'RPAREN':([18,43,45,50,51,52,53,56,57,58,59,60,62,63,64,65,81,84,85,86,87,88,89,90,93,100,101,104,105,109,110,111,112,117,118,119,120,121,122,123,124,125,126,127,128,129,130,134,135,136,137,138,139,140,141,142,143,144,145,146,147,149,151,152,153,154,155,156,157,158,159,160,161,162,164,165,166,167,168,169,170,173,177,179,180,181,182,183,184,185,186,187,188,189,194,195,196,197,198,199,200,201,205,206,207,208,209,210,211,212,213,214,218,220,],[-104,-95,-97,-104,-104,-104,-82,-85,-86,-87,-88,-89,-91,-92,-93,-94,-29,-32,-104,-34,-104,-104,-104,-104,-65,-72,-73,-76,-77,-81,-83,-84,145,-104,-30,-104,-36,-31,-33,-104,-104,-104,-104,-104,-104,161,-58,-66,-67,-68,-69,-70,-71,-104,-104,-104,-104,-104,-90,171,-101,-104,-96,-104,-104,181,-104,-45,-104,-104,-104,-104,-104,-59,-60,-61,-74,-75,-78,-79,-80,193,-11,-104,-104,-43,-44,-104,-47,-37,-38,-39,-40,-104,-104,-104,-104,-104,-42,-46,-104,-104,-8,-104,-13,-9,-10,-35,-41,-62,-63,-64,-12,225,]),'LPAREN':([22,25,26,44,48,54,55,61,67,68,69,82,83,85,91,94,95,96,97,98,99,102,103,106,107,108,113,115,163,172,192,],[61,-98,-99,61,91,61,61,61,113,114,-98,91,91,124,61,61,61,61,61,61,61,61,61,61,61,61,61,149,61,-100,61,]),'INT_CONSTANT':([22,44,48,54,55,61,76,82,83,91,94,95,96,97,98,99,102,103,106,107,108,113,163,172,192,],[62,62,62,62,62,62,116,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,-100,62,]),'FLOAT_CONSTANT':([22,44,48,54,55,61,82,83,91,94,95,96,97,98,99,102,103,106,107,108,113,163,172,192,],[63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,-100,63,]),'STRING_CONSTANT':([22,44,48,54,55,61,82,83,91,94,95,96,97,98,99,102,103,106,107,108,113,163,172,192,],[64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,-100,64,]),'NULL':([22,44,48,54,55,61,82,83,91,94,95,96,97,98,99,102,103,106,107,108,113,163,172,192,],[65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,-100,65,]),'NEW':([48,],[92,]),'COMMA':([155,194,195,196,],[183,206,206,206,]),'ELSE':([215,219,222,],[-103,-98,227,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'make_scope':([0,25,69,219,],[2,67,115,222,]),'statement':([2,14,37,191,204,225,227,],[3,37,37,37,37,228,229,]),'funclist':([2,16,],[4,40,]),'empty':([2,16,18,37,42,46,47,50,51,52,85,87,88,89,90,117,119,123,124,125,126,127,128,140,141,142,143,144,149,150,152,153,155,157,158,159,160,161,179,180,183,189,194,195,196,197,200,201,206,219,],[5,41,45,73,77,77,77,100,104,109,45,109,109,109,109,45,45,109,156,104,104,104,104,104,104,109,109,109,177,77,109,104,184,100,100,100,100,109,104,100,156,104,207,207,207,100,100,214,177,224,]),'vardecl':([2,14,37,191,204,225,227,],[6,6,6,6,6,6,6,]),'atribstat':([2,14,37,114,191,204,216,225,227,],[8,8,8,148,8,8,220,8,8,]),'printstat':([2,14,37,191,204,225,227,],[9,9,9,9,9,9,9,]),'readstat':([2,14,37,191,204,225,227,],[10,10,10,10,10,10,10,]),'returnstat':([2,14,37,191,204,225,227,],[11,11,11,11,11,11,11,]),'ifstat':([2,14,37,191,204,225,227,],[12,12,12,12,12,12,12,]),'forstat':([2,14,37,191,204,225,227,],[13,13,13,13,13,13,13,]),'check_loop_scope':([2,14,37,191,204,225,227,],[15,15,15,15,15,15,15,]),'funcdef':([2,16,],[16,16,]),'lvalue':([2,14,22,23,37,44,54,55,61,91,94,95,96,97,98,99,102,103,106,107,108,113,114,163,191,192,204,216,225,227,],[21,21,60,66,21,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,21,60,21,60,21,21,21,21,]),'close_scope':([3,4,5,215,221,228,229,],[28,29,30,219,226,230,231,]),'statelist':([14,37,191,204,],[36,72,202,217,]),'_funclist':([16,],[39,]),'lvalue_line':([18,85,117,119,],[43,123,151,152,]),'expression':([22,113,192,],[49,147,147,]),'numexpression':([22,44,61,91,94,95,96,97,98,99,113,163,192,],[50,78,112,129,134,135,136,137,138,139,50,190,50,]),'term':([22,44,61,91,94,95,96,97,98,99,102,103,113,163,192,],[51,51,51,51,51,51,51,51,51,51,140,141,51,51,51,]),'unaryexpr':([22,44,61,91,94,95,96,97,98,99,102,103,106,107,108,113,163,192,],[52,52,52,52,52,52,52,52,52,52,52,52,142,143,144,52,52,52,]),'factor':([22,44,54,55,61,91,94,95,96,97,98,99,102,103,106,107,108,113,163,192,],[53,53,110,111,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'_node_int_constant':([22,44,48,54,55,61,82,83,91,94,95,96,97,98,99,102,103,106,107,108,113,163,192,],[56,56,87,56,56,56,87,87,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,]),'_node_float_constant':([22,44,48,54,55,61,82,83,91,94,95,96,97,98,99,102,103,106,107,108,113,163,192,],[57,57,88,57,57,57,88,88,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,]),'_node_str_constant':([22,44,48,54,55,61,82,83,91,94,95,96,97,98,99,102,103,106,107,108,113,163,192,],[58,58,89,58,58,58,89,89,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,]),'_node_null_constant':([22,44,48,54,55,61,82,83,91,94,95,96,97,98,99,102,103,106,107,108,113,163,192,],[59,59,90,59,59,59,90,90,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,]),'make_loop_scope':([26,],[68,]),'_statelist':([37,],[71,]),'vardecl_line':([42,46,47,150,],[75,79,80,178,]),'_atribstat':([48,],[81,]),'__atribstat':([48,82,83,],[84,120,120,]),'allocexpression':([48,],[86,]),'_expression':([50,157,158,159,160,180,197,200,],[93,185,186,187,188,198,210,211,]),'numexpression_line':([51,125,126,127,128,140,141,153,179,189,],[101,157,158,159,160,166,167,180,197,200,]),'term_line':([52,87,88,89,90,123,142,143,144,152,161,],[105,125,126,127,128,153,168,169,170,179,189,]),'_atribstat_help':([82,83,],[118,121,]),'___atribstat':([85,],[122,]),'_allocexpression':([92,],[130,]),'make_expression_goto':([113,192,],[146,203,]),'paramlistcall':([124,183,],[154,199,]),'allocexpression_line':([131,132,133,201,],[162,164,165,213,]),'paramlist':([149,206,],[173,218,]),'_paramlistcall':([155,],[182,]),'make_loop_label':([172,],[192,]),'_paramlist':([194,195,196,],[205,208,209,]),'_allocexpression_line':([201,],[212,]),'_ifstat':([219,],[223,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> make_scope statement close_scope','program',3,'p_program','draguimantic.py',31),
  ('program -> make_scope funclist close_scope','program',3,'p_program','draguimantic.py',32),
  ('program -> make_scope empty close_scope','program',3,'p_program','draguimantic.py',33),
  ('funclist -> funcdef _funclist','funclist',2,'p_funclist','draguimantic.py',39),
  ('_funclist -> funclist','_funclist',1,'p__funclist','draguimantic.py',45),
  ('_funclist -> empty','_funclist',1,'p__funclist','draguimantic.py',46),
  ('funcdef -> DEFINE IDENT make_scope LPAREN paramlist RPAREN LBRACES statelist RBRACES close_scope','funcdef',10,'p_funcdef','draguimantic.py',52),
  ('paramlist -> INT IDENT _paramlist','paramlist',3,'p_paramlist','draguimantic.py',61),
  ('paramlist -> FLOAT IDENT _paramlist','paramlist',3,'p_paramlist','draguimantic.py',62),
  ('paramlist -> STRING IDENT _paramlist','paramlist',3,'p_paramlist','draguimantic.py',63),
  ('paramlist -> empty','paramlist',1,'p_paramlist','draguimantic.py',64),
  ('_paramlist -> COMMA paramlist','_paramlist',2,'p__paramlist','draguimantic.py',73),
  ('_paramlist -> empty','_paramlist',1,'p__paramlist','draguimantic.py',74),
  ('statement -> vardecl SEMICOLON','statement',2,'p_statement','draguimantic.py',80),
  ('statement -> atribstat SEMICOLON','statement',2,'p_statement','draguimantic.py',81),
  ('statement -> printstat SEMICOLON','statement',2,'p_statement','draguimantic.py',82),
  ('statement -> readstat SEMICOLON','statement',2,'p_statement','draguimantic.py',83),
  ('statement -> returnstat SEMICOLON','statement',2,'p_statement','draguimantic.py',84),
  ('statement -> ifstat','statement',1,'p_statement','draguimantic.py',85),
  ('statement -> forstat','statement',1,'p_statement','draguimantic.py',86),
  ('statement -> LBRACES statelist RBRACES','statement',3,'p_statement','draguimantic.py',87),
  ('statement -> check_loop_scope BREAK SEMICOLON','statement',3,'p_statement','draguimantic.py',88),
  ('statement -> SEMICOLON','statement',1,'p_statement','draguimantic.py',89),
  ('vardecl -> INT IDENT vardecl_line','vardecl',3,'p_vardecl','draguimantic.py',95),
  ('vardecl -> FLOAT IDENT vardecl_line','vardecl',3,'p_vardecl','draguimantic.py',96),
  ('vardecl -> STRING IDENT vardecl_line','vardecl',3,'p_vardecl','draguimantic.py',97),
  ('vardecl_line -> LBRACKET INT_CONSTANT RBRACKET vardecl_line','vardecl_line',4,'p_vardecl_line','draguimantic.py',105),
  ('vardecl_line -> empty','vardecl_line',1,'p_vardecl_line','draguimantic.py',106),
  ('atribstat -> lvalue ASSIGN _atribstat','atribstat',3,'p_atribstat','draguimantic.py',111),
  ('_atribstat -> PLUS _atribstat_help','_atribstat',2,'p__atribstat','draguimantic.py',120),
  ('_atribstat -> MINUS _atribstat_help','_atribstat',2,'p__atribstat','draguimantic.py',121),
  ('_atribstat -> __atribstat','_atribstat',1,'p__atribstat','draguimantic.py',122),
  ('_atribstat -> IDENT ___atribstat','_atribstat',2,'p__atribstat','draguimantic.py',123),
  ('_atribstat -> allocexpression','_atribstat',1,'p__atribstat','draguimantic.py',124),
  ('_atribstat_help -> IDENT lvalue_line term_line numexpression_line _expression','_atribstat_help',5,'p__atribstat_help','draguimantic.py',170),
  ('_atribstat_help -> __atribstat','_atribstat_help',1,'p__atribstat_help','draguimantic.py',171),
  ('__atribstat -> _node_int_constant term_line numexpression_line _expression','__atribstat',4,'p___atribstat','draguimantic.py',198),
  ('__atribstat -> _node_float_constant term_line numexpression_line _expression','__atribstat',4,'p___atribstat','draguimantic.py',199),
  ('__atribstat -> _node_str_constant term_line numexpression_line _expression','__atribstat',4,'p___atribstat','draguimantic.py',200),
  ('__atribstat -> _node_null_constant term_line numexpression_line _expression','__atribstat',4,'p___atribstat','draguimantic.py',201),
  ('__atribstat -> LPAREN numexpression RPAREN term_line numexpression_line _expression','__atribstat',6,'p___atribstat','draguimantic.py',202),
  ('___atribstat -> lvalue_line term_line numexpression_line _expression','___atribstat',4,'p____atribstat','draguimantic.py',229),
  ('___atribstat -> LPAREN paramlistcall RPAREN','___atribstat',3,'p____atribstat','draguimantic.py',230),
  ('paramlistcall -> IDENT _paramlistcall','paramlistcall',2,'p_paramlistcall','draguimantic.py',262),
  ('paramlistcall -> empty','paramlistcall',1,'p_paramlistcall','draguimantic.py',263),
  ('_paramlistcall -> COMMA paramlistcall','_paramlistcall',2,'p__paramlistcall','draguimantic.py',273),
  ('_paramlistcall -> empty','_paramlistcall',1,'p__paramlistcall','draguimantic.py',274),
  ('printstat -> PRINT expression','printstat',2,'p_printstat','draguimantic.py',280),
  ('readstat -> READ lvalue','readstat',2,'p_readstat','draguimantic.py',287),
  ('returnstat -> RETURN','returnstat',1,'p_returnstat','draguimantic.py',294),
  ('ifstat -> IF make_scope LPAREN make_expression_goto RPAREN LBRACES statelist RBRACES close_scope _ifstat','ifstat',10,'p_ifstat','draguimantic.py',301),
  ('_ifstat -> make_scope ELSE statement close_scope','_ifstat',4,'p__ifstat','draguimantic.py',307),
  ('_ifstat -> empty','_ifstat',1,'p__ifstat','draguimantic.py',308),
  ('forstat -> FOR make_loop_scope LPAREN atribstat SEMICOLON make_loop_label make_expression_goto SEMICOLON atribstat RPAREN statement close_scope','forstat',12,'p_forstat','draguimantic.py',314),
  ('statelist -> statement _statelist','statelist',2,'p_statelist','draguimantic.py',320),
  ('_statelist -> statelist','_statelist',1,'p__statelist','draguimantic.py',326),
  ('_statelist -> empty','_statelist',1,'p__statelist','draguimantic.py',327),
  ('allocexpression -> NEW _allocexpression','allocexpression',2,'p_allocexpression','draguimantic.py',333),
  ('_allocexpression -> INT allocexpression_line','_allocexpression',2,'p__allocexpression','draguimantic.py',340),
  ('_allocexpression -> FLOAT allocexpression_line','_allocexpression',2,'p__allocexpression','draguimantic.py',341),
  ('_allocexpression -> STRING allocexpression_line','_allocexpression',2,'p__allocexpression','draguimantic.py',342),
  ('allocexpression_line -> LBRACKET numexpression RBRACKET _allocexpression_line','allocexpression_line',4,'p_allocexpression_line','draguimantic.py',349),
  ('_allocexpression_line -> allocexpression_line','_allocexpression_line',1,'p__allocexpression_line','draguimantic.py',360),
  ('_allocexpression_line -> empty','_allocexpression_line',1,'p__allocexpression_line','draguimantic.py',361),
  ('expression -> numexpression _expression','expression',2,'p_expression','draguimantic.py',369),
  ('_expression -> LESS_THAN numexpression','_expression',2,'p__expression','draguimantic.py',377),
  ('_expression -> GREATER_THAN numexpression','_expression',2,'p__expression','draguimantic.py',378),
  ('_expression -> LESS_EQUAL_THAN numexpression','_expression',2,'p__expression','draguimantic.py',379),
  ('_expression -> GREATER_EQUAL_THAN numexpression','_expression',2,'p__expression','draguimantic.py',380),
  ('_expression -> EQUAL_TO numexpression','_expression',2,'p__expression','draguimantic.py',381),
  ('_expression -> NOT_EQUAL_TO numexpression','_expression',2,'p__expression','draguimantic.py',382),
  ('_expression -> empty','_expression',1,'p__expression','draguimantic.py',383),
  ('numexpression -> term numexpression_line','numexpression',2,'p_numexpression','draguimantic.py',395),
  ('numexpression_line -> PLUS term numexpression_line','numexpression_line',3,'p_numexpression_line','draguimantic.py',408),
  ('numexpression_line -> MINUS term numexpression_line','numexpression_line',3,'p_numexpression_line','draguimantic.py',409),
  ('numexpression_line -> empty','numexpression_line',1,'p_numexpression_line','draguimantic.py',410),
  ('term -> unaryexpr term_line','term',2,'p_term','draguimantic.py',425),
  ('term_line -> TIMES unaryexpr term_line','term_line',3,'p_term_line','draguimantic.py',439),
  ('term_line -> DIVIDE unaryexpr term_line','term_line',3,'p_term_line','draguimantic.py',440),
  ('term_line -> MODULO unaryexpr term_line','term_line',3,'p_term_line','draguimantic.py',441),
  ('term_line -> empty','term_line',1,'p_term_line','draguimantic.py',442),
  ('unaryexpr -> factor','unaryexpr',1,'p_unaryexpr','draguimantic.py',457),
  ('unaryexpr -> PLUS factor','unaryexpr',2,'p_unaryexpr','draguimantic.py',458),
  ('unaryexpr -> MINUS factor','unaryexpr',2,'p_unaryexpr','draguimantic.py',459),
  ('factor -> _node_int_constant','factor',1,'p_factor','draguimantic.py',476),
  ('factor -> _node_float_constant','factor',1,'p_factor','draguimantic.py',477),
  ('factor -> _node_str_constant','factor',1,'p_factor','draguimantic.py',478),
  ('factor -> _node_null_constant','factor',1,'p_factor','draguimantic.py',479),
  ('factor -> lvalue','factor',1,'p_factor','draguimantic.py',480),
  ('factor -> LPAREN numexpression RPAREN','factor',3,'p_factor','draguimantic.py',481),
  ('_node_int_constant -> INT_CONSTANT','_node_int_constant',1,'p__node_int_constant','draguimantic.py',495),
  ('_node_float_constant -> FLOAT_CONSTANT','_node_float_constant',1,'p__node_float_constant','draguimantic.py',502),
  ('_node_str_constant -> STRING_CONSTANT','_node_str_constant',1,'p__node_str_constant','draguimantic.py',509),
  ('_node_null_constant -> NULL','_node_null_constant',1,'p_node_null_constant','draguimantic.py',516),
  ('lvalue -> IDENT lvalue_line','lvalue',2,'p_lvalue','draguimantic.py',523),
  ('lvalue_line -> LBRACKET numexpression RBRACKET lvalue_line','lvalue_line',4,'p_lvalue_line','draguimantic.py',541),
  ('lvalue_line -> empty','lvalue_line',1,'p_lvalue_line','draguimantic.py',542),
  ('make_scope -> <empty>','make_scope',0,'p_make_scope','draguimantic.py',557),
  ('make_loop_scope -> <empty>','make_loop_scope',0,'p_make_loop_scope','draguimantic.py',564),
  ('make_loop_label -> <empty>','make_loop_label',0,'p_make_loop_label','draguimantic.py',571),
  ('make_expression_goto -> expression','make_expression_goto',1,'p_make_expression_goto','draguimantic.py',576),
  ('check_loop_scope -> <empty>','check_loop_scope',0,'p_check_loop_scope','draguimantic.py',581),
  ('close_scope -> <empty>','close_scope',0,'p_close_scope','draguimantic.py',588),
  ('empty -> <empty>','empty',0,'p_empty','draguimantic.py',595),
]
