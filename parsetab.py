
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'PTCOMA TEMPORAL and asigna band bipunto bnot bor bxor cor1 cor2 decimal depuntero devfunc diferente direccion div entero iden igual mas mayor mayori menor menori mod not or par1 par2 parametro pila por puntero res shiftder shiftizq string t_abs t_array t_char t_exit t_float t_goto t_int t_print t_read t_unset t_xors         : etiquetasetiquetas : etiquetas etiquetaetiquetas : etiquetasentencias : sentencias sentenciasentencias         : sentenciaetiqueta : iden bipunto sentenciassentencia : asignacion\n                  | GOTO\n                  | UNSET\n                  | PRINT\n                  | EXIT\n                  | ASIGNACION_ARR\n                  | as_punteroASIGNACION_ARR : asignado L_ACCESOS asignado exp PTCOMAUNSET : t_unset par1 asignado par2 PTCOMAGOTO : t_goto iden bipuntoPRINT : t_print par1 exp par2 PTCOMAasignacion : asignado asigna exp PTCOMAas_puntero : asignado asigna depuntero asignado PTCOMAEXIT : t_exit PTCOMAasignado  : TEMPORAL\n                  | puntero\n                  | direccion\n                  | parametro\n                  | devfunc\n                  | pila\n                  | idenexp :  exp1 bxor exp1\n            | exp1 t_xor  exp1exp :    exp1exp1 :   exp2 bor exp2\n            | exp2 or  exp2\n            | exp2 shiftizq exp2\n            | exp2 shiftder exp2exp1 : exp2exp2 :   exp3 band exp3\n            | exp3 and  exp3exp2 : exp3exp3 :   exp4 igual exp4\n            | exp4 diferente  exp4exp3 : exp4exp4 :   exp5 mayor exp5\n            | exp5 mayori exp5\n            | exp5 menor exp5\n            | exp5 menori  exp5exp4 : exp5exp5 :   exp6 mas exp6\n            | exp6 res exp6exp5 : exp6exp6 :   exp7 por exp7\n            | exp7 div exp7\n            | exp7 mod exp7exp6 : t_abs par1 exp7 par2exp6 : exp7exp7 : res exp11\n            | not exp11\n            | bnot exp11exp11 : asignado L_ACCESOSL_ACCESOS : L_ACCESOS accesoL_ACCESOS : accesoacceso : cor1 exp8 cor2exp11 : exp8exp7 : exp11exp8 :  string\n              | iden\n              | entero\n              | decimal\n              | TEMPORAL\n              | puntero\n              | direccion\n              | parametro\n              | devfunc\n              | pilaexp8 : par1 t_int par2 exp\n            | par1 t_float par2 exp\n            | par1 t_char par2 expexp8 : t_read par1 par2'
    
_lr_action_items = {'iden':([0,2,3,5,6,7,8,9,10,11,12,13,14,15,16,18,22,23,24,25,26,27,28,29,30,31,32,34,35,36,39,46,51,52,65,66,75,79,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,99,100,101,109,112,133,134,135,137,138,139,],[4,4,-3,-2,7,-27,7,-5,-7,-8,-9,-10,-11,-12,-13,33,-21,-22,-23,-24,-25,-26,-4,60,7,-60,68,7,60,-20,7,60,60,60,60,-59,-16,-18,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,-61,-19,60,60,60,-14,-15,-17,]),'$end':([1,2,3,5,8,9,10,11,12,13,14,15,16,28,36,75,79,112,137,138,139,],[0,-1,-3,-2,-6,-5,-7,-8,-9,-10,-11,-12,-13,-4,-20,-16,-18,-19,-14,-15,-17,]),'bipunto':([4,33,],[6,75,]),'t_goto':([6,8,9,10,11,12,13,14,15,16,28,36,75,79,112,137,138,139,],[18,18,-5,-7,-8,-9,-10,-11,-12,-13,-4,-20,-16,-18,-19,-14,-15,-17,]),'t_unset':([6,8,9,10,11,12,13,14,15,16,28,36,75,79,112,137,138,139,],[19,19,-5,-7,-8,-9,-10,-11,-12,-13,-4,-20,-16,-18,-19,-14,-15,-17,]),'t_print':([6,8,9,10,11,12,13,14,15,16,28,36,75,79,112,137,138,139,],[20,20,-5,-7,-8,-9,-10,-11,-12,-13,-4,-20,-16,-18,-19,-14,-15,-17,]),'t_exit':([6,8,9,10,11,12,13,14,15,16,28,36,75,79,112,137,138,139,],[21,21,-5,-7,-8,-9,-10,-11,-12,-13,-4,-20,-16,-18,-19,-14,-15,-17,]),'TEMPORAL':([6,7,8,9,10,11,12,13,14,15,16,22,23,24,25,26,27,28,29,30,31,32,34,35,36,39,46,51,52,65,66,75,79,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,99,100,101,109,112,133,134,135,137,138,139,],[22,-27,22,-5,-7,-8,-9,-10,-11,-12,-13,-21,-22,-23,-24,-25,-26,-4,54,22,-60,69,22,54,-20,22,54,54,54,54,-59,-16,-18,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,-61,-19,54,54,54,-14,-15,-17,]),'puntero':([6,7,8,9,10,11,12,13,14,15,16,22,23,24,25,26,27,28,29,30,31,32,34,35,36,39,46,51,52,65,66,75,79,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,99,100,101,109,112,133,134,135,137,138,139,],[23,-27,23,-5,-7,-8,-9,-10,-11,-12,-13,-21,-22,-23,-24,-25,-26,-4,55,23,-60,70,23,55,-20,23,55,55,55,55,-59,-16,-18,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,-61,-19,55,55,55,-14,-15,-17,]),'direccion':([6,7,8,9,10,11,12,13,14,15,16,22,23,24,25,26,27,28,29,30,31,32,34,35,36,39,46,51,52,65,66,75,79,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,99,100,101,109,112,133,134,135,137,138,139,],[24,-27,24,-5,-7,-8,-9,-10,-11,-12,-13,-21,-22,-23,-24,-25,-26,-4,56,24,-60,71,24,56,-20,24,56,56,56,56,-59,-16,-18,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,-61,-19,56,56,56,-14,-15,-17,]),'parametro':([6,7,8,9,10,11,12,13,14,15,16,22,23,24,25,26,27,28,29,30,31,32,34,35,36,39,46,51,52,65,66,75,79,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,99,100,101,109,112,133,134,135,137,138,139,],[25,-27,25,-5,-7,-8,-9,-10,-11,-12,-13,-21,-22,-23,-24,-25,-26,-4,57,25,-60,72,25,57,-20,25,57,57,57,57,-59,-16,-18,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,-61,-19,57,57,57,-14,-15,-17,]),'devfunc':([6,7,8,9,10,11,12,13,14,15,16,22,23,24,25,26,27,28,29,30,31,32,34,35,36,39,46,51,52,65,66,75,79,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,99,100,101,109,112,133,134,135,137,138,139,],[26,-27,26,-5,-7,-8,-9,-10,-11,-12,-13,-21,-22,-23,-24,-25,-26,-4,58,26,-60,73,26,58,-20,26,58,58,58,58,-59,-16,-18,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,-61,-19,58,58,58,-14,-15,-17,]),'pila':([6,7,8,9,10,11,12,13,14,15,16,22,23,24,25,26,27,28,29,30,31,32,34,35,36,39,46,51,52,65,66,75,79,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,99,100,101,109,112,133,134,135,137,138,139,],[27,-27,27,-5,-7,-8,-9,-10,-11,-12,-13,-21,-22,-23,-24,-25,-26,-4,59,27,-60,74,27,59,-20,27,59,59,59,59,-59,-16,-18,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,-61,-19,59,59,59,-14,-15,-17,]),'asigna':([7,17,22,23,24,25,26,27,],[-27,29,-21,-22,-23,-24,-25,-26,]),'cor1':([7,17,22,23,24,25,26,27,30,31,37,54,55,56,57,58,59,60,66,78,109,],[-27,32,-21,-22,-23,-24,-25,-26,32,-60,32,-21,-22,-23,-24,-25,-26,-27,-59,32,-61,]),'t_abs':([7,22,23,24,25,26,27,29,35,65,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,133,134,135,],[-27,-21,-22,-23,-24,-25,-26,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'res':([7,22,23,24,25,26,27,29,31,35,40,41,42,43,44,45,47,50,53,54,55,56,57,58,59,60,61,62,63,65,66,78,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,105,106,109,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,133,134,135,136,140,141,142,143,],[-27,-21,-22,-23,-24,-25,-26,46,-60,46,-30,-35,-38,-41,-46,96,-54,-63,-62,-68,-69,-70,-71,-72,-73,-65,-64,-66,-67,46,-59,-58,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,-55,46,46,46,46,-56,-57,-61,-28,-29,-31,-32,-33,-34,-36,-37,-39,-40,-42,-43,-44,-45,-47,-48,-50,-51,-52,46,46,46,-77,-53,-74,-75,-76,]),'not':([7,22,23,24,25,26,27,29,35,65,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,99,100,101,133,134,135,],[-27,-21,-22,-23,-24,-25,-26,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'bnot':([7,22,23,24,25,26,27,29,35,65,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,99,100,101,133,134,135,],[-27,-21,-22,-23,-24,-25,-26,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'string':([7,22,23,24,25,26,27,29,32,35,46,51,52,65,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,99,100,101,133,134,135,],[-27,-21,-22,-23,-24,-25,-26,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,]),'entero':([7,22,23,24,25,26,27,29,32,35,46,51,52,65,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,99,100,101,133,134,135,],[-27,-21,-22,-23,-24,-25,-26,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,]),'decimal':([7,22,23,24,25,26,27,29,32,35,46,51,52,65,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,99,100,101,133,134,135,],[-27,-21,-22,-23,-24,-25,-26,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,]),'par1':([7,19,20,22,23,24,25,26,27,29,32,35,46,48,51,52,64,65,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,99,100,101,133,134,135,],[-27,34,35,-21,-22,-23,-24,-25,-26,49,49,49,49,101,49,49,107,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'t_read':([7,22,23,24,25,26,27,29,32,35,46,51,52,65,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,99,100,101,133,134,135,],[-27,-21,-22,-23,-24,-25,-26,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,]),'par2':([7,22,23,24,25,26,27,31,40,41,42,43,44,45,47,50,53,54,55,56,57,58,59,60,61,62,63,66,76,77,78,97,102,103,104,105,106,107,109,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,136,140,141,142,143,],[-27,-21,-22,-23,-24,-25,-26,-60,-30,-35,-38,-41,-46,-49,-54,-63,-62,-68,-69,-70,-71,-72,-73,-65,-64,-66,-67,-59,110,111,-58,-55,133,134,135,-56,-57,136,-61,-28,-29,-31,-32,-33,-34,-36,-37,-39,-40,-42,-43,-44,-45,-47,-48,-50,-51,-52,140,-77,-53,-74,-75,-76,]),'PTCOMA':([7,21,22,23,24,25,26,27,31,38,40,41,42,43,44,45,47,50,53,54,55,56,57,58,59,60,61,62,63,66,78,80,97,105,106,108,109,110,111,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,136,140,141,142,143,],[-27,36,-21,-22,-23,-24,-25,-26,-60,79,-30,-35,-38,-41,-46,-49,-54,-63,-62,-68,-69,-70,-71,-72,-73,-65,-64,-66,-67,-59,-58,112,-55,-56,-57,137,-61,138,139,-28,-29,-31,-32,-33,-34,-36,-37,-39,-40,-42,-43,-44,-45,-47,-48,-50,-51,-52,-77,-53,-74,-75,-76,]),'depuntero':([29,],[39,]),'por':([31,40,41,42,43,44,45,47,50,53,54,55,56,57,58,59,60,61,62,63,66,78,97,105,106,109,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,136,140,141,142,143,],[-60,-30,-35,-38,-41,-46,-49,98,-63,-62,-68,-69,-70,-71,-72,-73,-65,-64,-66,-67,-59,-58,-55,-56,-57,-61,-28,-29,-31,-32,-33,-34,-36,-37,-39,-40,-42,-43,-44,-45,-47,-48,-50,-51,-52,-77,-53,-74,-75,-76,]),'div':([31,40,41,42,43,44,45,47,50,53,54,55,56,57,58,59,60,61,62,63,66,78,97,105,106,109,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,136,140,141,142,143,],[-60,-30,-35,-38,-41,-46,-49,99,-63,-62,-68,-69,-70,-71,-72,-73,-65,-64,-66,-67,-59,-58,-55,-56,-57,-61,-28,-29,-31,-32,-33,-34,-36,-37,-39,-40,-42,-43,-44,-45,-47,-48,-50,-51,-52,-77,-53,-74,-75,-76,]),'mod':([31,40,41,42,43,44,45,47,50,53,54,55,56,57,58,59,60,61,62,63,66,78,97,105,106,109,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,136,140,141,142,143,],[-60,-30,-35,-38,-41,-46,-49,100,-63,-62,-68,-69,-70,-71,-72,-73,-65,-64,-66,-67,-59,-58,-55,-56,-57,-61,-28,-29,-31,-32,-33,-34,-36,-37,-39,-40,-42,-43,-44,-45,-47,-48,-50,-51,-52,-77,-53,-74,-75,-76,]),'mas':([31,40,41,42,43,44,45,47,50,53,54,55,56,57,58,59,60,61,62,63,66,78,97,105,106,109,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,136,140,141,142,143,],[-60,-30,-35,-38,-41,-46,95,-54,-63,-62,-68,-69,-70,-71,-72,-73,-65,-64,-66,-67,-59,-58,-55,-56,-57,-61,-28,-29,-31,-32,-33,-34,-36,-37,-39,-40,-42,-43,-44,-45,-47,-48,-50,-51,-52,-77,-53,-74,-75,-76,]),'mayor':([31,40,41,42,43,44,45,47,50,53,54,55,56,57,58,59,60,61,62,63,66,78,97,105,106,109,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,136,140,141,142,143,],[-60,-30,-35,-38,-41,91,-49,-54,-63,-62,-68,-69,-70,-71,-72,-73,-65,-64,-66,-67,-59,-58,-55,-56,-57,-61,-28,-29,-31,-32,-33,-34,-36,-37,-39,-40,-42,-43,-44,-45,-47,-48,-50,-51,-52,-77,-53,-74,-75,-76,]),'mayori':([31,40,41,42,43,44,45,47,50,53,54,55,56,57,58,59,60,61,62,63,66,78,97,105,106,109,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,136,140,141,142,143,],[-60,-30,-35,-38,-41,92,-49,-54,-63,-62,-68,-69,-70,-71,-72,-73,-65,-64,-66,-67,-59,-58,-55,-56,-57,-61,-28,-29,-31,-32,-33,-34,-36,-37,-39,-40,-42,-43,-44,-45,-47,-48,-50,-51,-52,-77,-53,-74,-75,-76,]),'menor':([31,40,41,42,43,44,45,47,50,53,54,55,56,57,58,59,60,61,62,63,66,78,97,105,106,109,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,136,140,141,142,143,],[-60,-30,-35,-38,-41,93,-49,-54,-63,-62,-68,-69,-70,-71,-72,-73,-65,-64,-66,-67,-59,-58,-55,-56,-57,-61,-28,-29,-31,-32,-33,-34,-36,-37,-39,-40,-42,-43,-44,-45,-47,-48,-50,-51,-52,-77,-53,-74,-75,-76,]),'menori':([31,40,41,42,43,44,45,47,50,53,54,55,56,57,58,59,60,61,62,63,66,78,97,105,106,109,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,136,140,141,142,143,],[-60,-30,-35,-38,-41,94,-49,-54,-63,-62,-68,-69,-70,-71,-72,-73,-65,-64,-66,-67,-59,-58,-55,-56,-57,-61,-28,-29,-31,-32,-33,-34,-36,-37,-39,-40,-42,-43,-44,-45,-47,-48,-50,-51,-52,-77,-53,-74,-75,-76,]),'igual':([31,40,41,42,43,44,45,47,50,53,54,55,56,57,58,59,60,61,62,63,66,78,97,105,106,109,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,136,140,141,142,143,],[-60,-30,-35,-38,89,-46,-49,-54,-63,-62,-68,-69,-70,-71,-72,-73,-65,-64,-66,-67,-59,-58,-55,-56,-57,-61,-28,-29,-31,-32,-33,-34,-36,-37,-39,-40,-42,-43,-44,-45,-47,-48,-50,-51,-52,-77,-53,-74,-75,-76,]),'diferente':([31,40,41,42,43,44,45,47,50,53,54,55,56,57,58,59,60,61,62,63,66,78,97,105,106,109,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,136,140,141,142,143,],[-60,-30,-35,-38,90,-46,-49,-54,-63,-62,-68,-69,-70,-71,-72,-73,-65,-64,-66,-67,-59,-58,-55,-56,-57,-61,-28,-29,-31,-32,-33,-34,-36,-37,-39,-40,-42,-43,-44,-45,-47,-48,-50,-51,-52,-77,-53,-74,-75,-76,]),'band':([31,40,41,42,43,44,45,47,50,53,54,55,56,57,58,59,60,61,62,63,66,78,97,105,106,109,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,136,140,141,142,143,],[-60,-30,-35,87,-41,-46,-49,-54,-63,-62,-68,-69,-70,-71,-72,-73,-65,-64,-66,-67,-59,-58,-55,-56,-57,-61,-28,-29,-31,-32,-33,-34,-36,-37,-39,-40,-42,-43,-44,-45,-47,-48,-50,-51,-52,-77,-53,-74,-75,-76,]),'and':([31,40,41,42,43,44,45,47,50,53,54,55,56,57,58,59,60,61,62,63,66,78,97,105,106,109,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,136,140,141,142,143,],[-60,-30,-35,88,-41,-46,-49,-54,-63,-62,-68,-69,-70,-71,-72,-73,-65,-64,-66,-67,-59,-58,-55,-56,-57,-61,-28,-29,-31,-32,-33,-34,-36,-37,-39,-40,-42,-43,-44,-45,-47,-48,-50,-51,-52,-77,-53,-74,-75,-76,]),'bor':([31,40,41,42,43,44,45,47,50,53,54,55,56,57,58,59,60,61,62,63,66,78,97,105,106,109,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,136,140,141,142,143,],[-60,-30,83,-38,-41,-46,-49,-54,-63,-62,-68,-69,-70,-71,-72,-73,-65,-64,-66,-67,-59,-58,-55,-56,-57,-61,-28,-29,-31,-32,-33,-34,-36,-37,-39,-40,-42,-43,-44,-45,-47,-48,-50,-51,-52,-77,-53,-74,-75,-76,]),'or':([31,40,41,42,43,44,45,47,50,53,54,55,56,57,58,59,60,61,62,63,66,78,97,105,106,109,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,136,140,141,142,143,],[-60,-30,84,-38,-41,-46,-49,-54,-63,-62,-68,-69,-70,-71,-72,-73,-65,-64,-66,-67,-59,-58,-55,-56,-57,-61,-28,-29,-31,-32,-33,-34,-36,-37,-39,-40,-42,-43,-44,-45,-47,-48,-50,-51,-52,-77,-53,-74,-75,-76,]),'shiftizq':([31,40,41,42,43,44,45,47,50,53,54,55,56,57,58,59,60,61,62,63,66,78,97,105,106,109,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,136,140,141,142,143,],[-60,-30,85,-38,-41,-46,-49,-54,-63,-62,-68,-69,-70,-71,-72,-73,-65,-64,-66,-67,-59,-58,-55,-56,-57,-61,-28,-29,-31,-32,-33,-34,-36,-37,-39,-40,-42,-43,-44,-45,-47,-48,-50,-51,-52,-77,-53,-74,-75,-76,]),'shiftder':([31,40,41,42,43,44,45,47,50,53,54,55,56,57,58,59,60,61,62,63,66,78,97,105,106,109,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,136,140,141,142,143,],[-60,-30,86,-38,-41,-46,-49,-54,-63,-62,-68,-69,-70,-71,-72,-73,-65,-64,-66,-67,-59,-58,-55,-56,-57,-61,-28,-29,-31,-32,-33,-34,-36,-37,-39,-40,-42,-43,-44,-45,-47,-48,-50,-51,-52,-77,-53,-74,-75,-76,]),'bxor':([31,40,41,42,43,44,45,47,50,53,54,55,56,57,58,59,60,61,62,63,66,78,97,105,106,109,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,136,140,141,142,143,],[-60,81,-35,-38,-41,-46,-49,-54,-63,-62,-68,-69,-70,-71,-72,-73,-65,-64,-66,-67,-59,-58,-55,-56,-57,-61,-28,-29,-31,-32,-33,-34,-36,-37,-39,-40,-42,-43,-44,-45,-47,-48,-50,-51,-52,-77,-53,-74,-75,-76,]),'t_xor':([31,40,41,42,43,44,45,47,50,53,54,55,56,57,58,59,60,61,62,63,66,78,97,105,106,109,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,136,140,141,142,143,],[-60,82,-35,-38,-41,-46,-49,-54,-63,-62,-68,-69,-70,-71,-72,-73,-65,-64,-66,-67,-59,-58,-55,-56,-57,-61,-28,-29,-31,-32,-33,-34,-36,-37,-39,-40,-42,-43,-44,-45,-47,-48,-50,-51,-52,-77,-53,-74,-75,-76,]),'cor2':([31,40,41,42,43,44,45,47,50,53,54,55,56,57,58,59,60,61,62,63,66,67,68,69,70,71,72,73,74,78,97,105,106,109,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,136,140,141,142,143,],[-60,-30,-35,-38,-41,-46,-49,-54,-63,-62,-68,-69,-70,-71,-72,-73,-65,-64,-66,-67,-59,109,-65,-68,-69,-70,-71,-72,-73,-58,-55,-56,-57,-61,-28,-29,-31,-32,-33,-34,-36,-37,-39,-40,-42,-43,-44,-45,-47,-48,-50,-51,-52,-77,-53,-74,-75,-76,]),'t_int':([49,],[102,]),'t_float':([49,],[103,]),'t_char':([49,],[104,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'s':([0,],[1,]),'etiquetas':([0,],[2,]),'etiqueta':([0,2,],[3,5,]),'sentencias':([6,],[8,]),'sentencia':([6,8,],[9,28,]),'asignacion':([6,8,],[10,10,]),'GOTO':([6,8,],[11,11,]),'UNSET':([6,8,],[12,12,]),'PRINT':([6,8,],[13,13,]),'EXIT':([6,8,],[14,14,]),'ASIGNACION_ARR':([6,8,],[15,15,]),'as_puntero':([6,8,],[16,16,]),'asignado':([6,8,29,30,34,35,39,46,51,52,65,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,99,100,101,133,134,135,],[17,17,37,65,76,37,80,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'L_ACCESOS':([17,37,],[30,78,]),'acceso':([17,30,37,78,],[31,66,31,66,]),'exp':([29,35,65,133,134,135,],[38,77,108,141,142,143,]),'exp1':([29,35,65,81,82,133,134,135,],[40,40,40,113,114,40,40,40,]),'exp2':([29,35,65,81,82,83,84,85,86,133,134,135,],[41,41,41,41,41,115,116,117,118,41,41,41,]),'exp3':([29,35,65,81,82,83,84,85,86,87,88,133,134,135,],[42,42,42,42,42,42,42,42,42,119,120,42,42,42,]),'exp4':([29,35,65,81,82,83,84,85,86,87,88,89,90,133,134,135,],[43,43,43,43,43,43,43,43,43,43,43,121,122,43,43,43,]),'exp5':([29,35,65,81,82,83,84,85,86,87,88,89,90,91,92,93,94,133,134,135,],[44,44,44,44,44,44,44,44,44,44,44,44,44,123,124,125,126,44,44,44,]),'exp6':([29,35,65,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,133,134,135,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,127,128,45,45,45,]),'exp7':([29,35,65,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,99,100,101,133,134,135,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,129,130,131,132,47,47,47,]),'exp11':([29,35,46,51,52,65,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,99,100,101,133,134,135,],[50,50,97,105,106,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'exp8':([29,32,35,46,51,52,65,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,99,100,101,133,134,135,],[53,67,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> s","S'",1,None,None,None),
  ('s -> etiquetas','s',1,'p_inicio','gramatica.py',170),
  ('etiquetas -> etiquetas etiqueta','etiquetas',2,'p_etiquetas_etiquetas','gramatica.py',175),
  ('etiquetas -> etiqueta','etiquetas',1,'p_etiquetas_etiqueta','gramatica.py',180),
  ('sentencias -> sentencias sentencia','sentencias',2,'p_sentencias_sentencias','gramatica.py',185),
  ('sentencias -> sentencia','sentencias',1,'p_sentencias_sentencia','gramatica.py',192),
  ('etiqueta -> iden bipunto sentencias','etiqueta',3,'p_etiquetas','gramatica.py',197),
  ('sentencia -> asignacion','sentencia',1,'p_sentencia','gramatica.py',202),
  ('sentencia -> GOTO','sentencia',1,'p_sentencia','gramatica.py',203),
  ('sentencia -> UNSET','sentencia',1,'p_sentencia','gramatica.py',204),
  ('sentencia -> PRINT','sentencia',1,'p_sentencia','gramatica.py',205),
  ('sentencia -> EXIT','sentencia',1,'p_sentencia','gramatica.py',206),
  ('sentencia -> ASIGNACION_ARR','sentencia',1,'p_sentencia','gramatica.py',207),
  ('sentencia -> as_puntero','sentencia',1,'p_sentencia','gramatica.py',208),
  ('ASIGNACION_ARR -> asignado L_ACCESOS asignado exp PTCOMA','ASIGNACION_ARR',5,'p_asignacion_arreglo','gramatica.py',212),
  ('UNSET -> t_unset par1 asignado par2 PTCOMA','UNSET',5,'p_unset','gramatica.py',217),
  ('GOTO -> t_goto iden bipunto','GOTO',3,'p_goto','gramatica.py',222),
  ('PRINT -> t_print par1 exp par2 PTCOMA','PRINT',5,'p_print','gramatica.py',227),
  ('asignacion -> asignado asigna exp PTCOMA','asignacion',4,'p_asignacion','gramatica.py',232),
  ('as_puntero -> asignado asigna depuntero asignado PTCOMA','as_puntero',5,'p_puntero','gramatica.py',237),
  ('EXIT -> t_exit PTCOMA','EXIT',2,'p_exit','gramatica.py',241),
  ('asignado -> TEMPORAL','asignado',1,'p_aguardar','gramatica.py',245),
  ('asignado -> puntero','asignado',1,'p_aguardar','gramatica.py',246),
  ('asignado -> direccion','asignado',1,'p_aguardar','gramatica.py',247),
  ('asignado -> parametro','asignado',1,'p_aguardar','gramatica.py',248),
  ('asignado -> devfunc','asignado',1,'p_aguardar','gramatica.py',249),
  ('asignado -> pila','asignado',1,'p_aguardar','gramatica.py',250),
  ('asignado -> iden','asignado',1,'p_aguardar','gramatica.py',251),
  ('exp -> exp1 bxor exp1','exp',3,'p_exp','gramatica.py',254),
  ('exp -> exp1 t_xor exp1','exp',3,'p_exp','gramatica.py',255),
  ('exp -> exp1','exp',1,'p_exp_2','gramatica.py',260),
  ('exp1 -> exp2 bor exp2','exp1',3,'p_exp1','gramatica.py',264),
  ('exp1 -> exp2 or exp2','exp1',3,'p_exp1','gramatica.py',265),
  ('exp1 -> exp2 shiftizq exp2','exp1',3,'p_exp1','gramatica.py',266),
  ('exp1 -> exp2 shiftder exp2','exp1',3,'p_exp1','gramatica.py',267),
  ('exp1 -> exp2','exp1',1,'p_exp1_2','gramatica.py',272),
  ('exp2 -> exp3 band exp3','exp2',3,'p_exp2','gramatica.py',276),
  ('exp2 -> exp3 and exp3','exp2',3,'p_exp2','gramatica.py',277),
  ('exp2 -> exp3','exp2',1,'p_exp2_2','gramatica.py',282),
  ('exp3 -> exp4 igual exp4','exp3',3,'p_exp3','gramatica.py',286),
  ('exp3 -> exp4 diferente exp4','exp3',3,'p_exp3','gramatica.py',287),
  ('exp3 -> exp4','exp3',1,'p_exp3_2','gramatica.py',292),
  ('exp4 -> exp5 mayor exp5','exp4',3,'p_exp4','gramatica.py',296),
  ('exp4 -> exp5 mayori exp5','exp4',3,'p_exp4','gramatica.py',297),
  ('exp4 -> exp5 menor exp5','exp4',3,'p_exp4','gramatica.py',298),
  ('exp4 -> exp5 menori exp5','exp4',3,'p_exp4','gramatica.py',299),
  ('exp4 -> exp5','exp4',1,'p_exp4_2','gramatica.py',304),
  ('exp5 -> exp6 mas exp6','exp5',3,'p_exp5','gramatica.py',308),
  ('exp5 -> exp6 res exp6','exp5',3,'p_exp5','gramatica.py',309),
  ('exp5 -> exp6','exp5',1,'p_exp5_2','gramatica.py',315),
  ('exp6 -> exp7 por exp7','exp6',3,'p_exp6','gramatica.py',319),
  ('exp6 -> exp7 div exp7','exp6',3,'p_exp6','gramatica.py',320),
  ('exp6 -> exp7 mod exp7','exp6',3,'p_exp6','gramatica.py',321),
  ('exp6 -> t_abs par1 exp7 par2','exp6',4,'p_exp6_2','gramatica.py',326),
  ('exp6 -> exp7','exp6',1,'p_exp6_3','gramatica.py',333),
  ('exp7 -> res exp11','exp7',2,'p_exp7','gramatica.py',337),
  ('exp7 -> not exp11','exp7',2,'p_exp7','gramatica.py',338),
  ('exp7 -> bnot exp11','exp7',2,'p_exp7','gramatica.py',339),
  ('exp11 -> asignado L_ACCESOS','exp11',2,'p_acceso_arr','gramatica.py',344),
  ('L_ACCESOS -> L_ACCESOS acceso','L_ACCESOS',2,'p_L_ACCESOS','gramatica.py',351),
  ('L_ACCESOS -> acceso','L_ACCESOS',1,'p_L_ACCESOS_1','gramatica.py',356),
  ('acceso -> cor1 exp8 cor2','acceso',3,'p_acceso','gramatica.py',360),
  ('exp11 -> exp8','exp11',1,'p_exp11','gramatica.py',364),
  ('exp7 -> exp11','exp7',1,'p_exp7_2','gramatica.py',368),
  ('exp8 -> string','exp8',1,'p_exp8','gramatica.py',372),
  ('exp8 -> iden','exp8',1,'p_exp8','gramatica.py',373),
  ('exp8 -> entero','exp8',1,'p_exp8','gramatica.py',374),
  ('exp8 -> decimal','exp8',1,'p_exp8','gramatica.py',375),
  ('exp8 -> TEMPORAL','exp8',1,'p_exp8','gramatica.py',376),
  ('exp8 -> puntero','exp8',1,'p_exp8','gramatica.py',377),
  ('exp8 -> direccion','exp8',1,'p_exp8','gramatica.py',378),
  ('exp8 -> parametro','exp8',1,'p_exp8','gramatica.py',379),
  ('exp8 -> devfunc','exp8',1,'p_exp8','gramatica.py',380),
  ('exp8 -> pila','exp8',1,'p_exp8','gramatica.py',381),
  ('exp8 -> par1 t_int par2 exp','exp8',4,'p_casts','gramatica.py',388),
  ('exp8 -> par1 t_float par2 exp','exp8',4,'p_casts','gramatica.py',389),
  ('exp8 -> par1 t_char par2 exp','exp8',4,'p_casts','gramatica.py',390),
  ('exp8 -> t_read par1 par2','exp8',3,'p_read','gramatica.py',397),
]
