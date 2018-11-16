
from rest_framework import serializers
from principal.models import Propuesta
from wang.src.wang1 import *
class PropuestaSerializer(serializers.ModelSerializer):
	class Meta:
		model=Propuesta
		fields=('id','propuesta','respuesta')
		
	def create(self,data):
		print(f">>>Create {data}")
		prop= data['propuesta']
		print(f">>>propuesta {prop}")
		result=evaluacion(prop)
		data['respuesta']=result
		return super().create(data)