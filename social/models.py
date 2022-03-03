
from dataclasses import Field
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Profile(models.Model):
    #si se borra un perfil tambien se borra todo lo relacionado
    usuario = models.OneToOneField(User,on_delete=models.CASCADE)
    imagen=models.ImageField(default='perfil1.png')
    def __str__(self) :
        return f'Perfil de { self.usuario.username}'
    def following(self):
        user_ids = Relationship.objects.filter(from_user=self.usuario)\
								.values_list('to_user_id', flat=True)
        return User.objects.filter(id__in=user_ids)
    def followers(self):
        user_ids = Relationship.objects.filter(to_user=self.usuario)\
								.values_list('from_user_id', flat=True)
        return User.objects.filter(id__in=user_ids)

	


class Post(models.Model):
    usuario=models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    timestamp=models.DateTimeField(default=timezone.now)
    contenido=models.TextField()
    #define el comportamiento de cierta clases
    class Meta:
         ordering=['-timestamp']
    #permite identificar el usuario y el contendio de su post,mostrarlo en la tabla en lugar de object(1)
    def __str__(self) :
        return f'{self.usuario.username}:{self.contenido}'




class Relationship(models.Model):
	from_user = models.ForeignKey(User, related_name='relationships', on_delete=models.CASCADE)
	to_user = models.ForeignKey(User, related_name='related_to', on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.from_user} to {self.to_user}'

	class Meta:
		indexes = [
		models.Index(fields=['from_user', 'to_user',]),
		]
