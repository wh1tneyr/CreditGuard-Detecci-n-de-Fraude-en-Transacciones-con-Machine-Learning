# Librerias ---------------------------------------- 
import os, sys
import platform 

# Systema operativo ---------------------------------------- 

sistema_operativo = platform.system()

# Definir extension de ejecutables ---------------------------------------- 

if sistema_operativo == 'Windows':
        extension_binarios = ".exe"
else:
        extension_binarios = ""
        