def validarCEDULA(cedula):
   cantidad=0
   while cedula!=0:
       cantidad+=1
       cedula//=10
   return cantidad==7 or cantidad==8

