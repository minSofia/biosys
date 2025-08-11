#from pyairtable import Api
from pyairtable.orm import Model
from pyairtable.orm import fields

class Usuario (Model):
    clave = fields.TextField("clave")
    contra = fields.TextField("contra")
    nombre = fields.TextField("nombre")
    admin = fields.CheckboxField("admin")
    class Meta:
        api_key = "patsGFavIfvQKLWAi.b36b4400714bcef6def6951edbc607e5ae3356ce32a89c044d237e50b1ecda4c"
        base_id = "appEm46lOJ755qpUP"
        table_name = "usuario"

class Bioenergia (Model):
    cultivo = fields.TextField("cultivo")
    parte = fields.TextField("parte")
    cantidad = fields.FloatField("cantidad")
    area = fields.FloatField("area")
    energia = fields.FloatField("energia")
    municipio = fields.TextField("municipio")
    latitud = fields.FloatField("latitud")
    longitud = fields.FloatField("longitud")
    humedad = fields.FloatField("humedad")
    class Meta:
        api_key = "patsGFavIfvQKLWAi.b36b4400714bcef6def6951edbc607e5ae3356ce32a89c044d237e50b1ecda4c"
        base_id = "appEm46lOJ755qpUP"
        table_name = "bioenergia"

#cacao = Bioenergia(
    #cultivo = "Cacao",
    #parte = "Cáscara",
    #cantidad = 2.0,
    #area = 3.0,
    #energia = 18.0,
    #municipio = "Cunduacán",
    #latitud = 18.076169,
    #longitud = 21.021114
#)
#cacao.save()


#api = Api("patsGFavIfvQKLWAi.b36b4400714bcef6def6951edbc607e5ae3356ce32a89c044d237e50b1ecda4c")
#tabla = api.table("appEm46lOJ755qpUP","usuario")

#Altas

#yo = {'clave': 'narvaez',
    #'contra': 'narvaez',
    #'nombre': 'Sonia Narváez',
    #'admin': 1
#}
#tabla.create(yo)

#Consultas
#registros = tabla.all()
#for r in registros:
    #print(r["fields"])
