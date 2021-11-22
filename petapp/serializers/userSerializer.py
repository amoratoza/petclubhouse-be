from rest_framework import serializers
from petapp.models.user import User
from petapp.models.pet import Pet
from petapp.serializers.petSerializer import PetSerializer
#import logging

# Get an instance of a logger
#logger = logging.getLogger(__name__)

class UserSerializer(serializers.ModelSerializer):
    pet = PetSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'email', 'phone','pet']
            
    def create(self, validated_data):
        #logger.error("loging")
        petData = validated_data.pop('pet')
        userInstance = User.objects.create(**validated_data)
        Pet.objects.create(user=userInstance, **petData)
        return userInstance
        
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        pet = Pet.objects.get(user=obj.id)
        return {
            'id': user.id,
            'username': user.username,
            'name': user.name,
            'email': user.email,
            'phone': user.phone,
            'pet': {
                'id': pet.id,
                'name': pet.name,
                'breed': pet.breed,
                'age': age
            }
        }   
