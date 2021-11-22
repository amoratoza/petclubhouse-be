from rest_framework import serializers
from petapp.models.pet import Pet

class PetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pet
		fields = ['name','breed','age']

def to_representation(self, obj):
        pet = Pet.objects.get(id=obj.id)
        user = User.objects.get(id=pet.user_id)
        return{
        		'id':pet.id,
        		'name':pet.name,
        		'breed':pet.breed,
        		'age':pet.breed,
        		'user':{
        				'id':user.id,
        				'name':user.name
        		}
        }
