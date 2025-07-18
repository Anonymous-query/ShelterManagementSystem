from django.db import models
from django.contrib.auth.models import User

class AnimalSpecies(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Animal Species'

class AnimalBread(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Animal Bread'

class Animals(models.Model):
    HEALTH_CHOICE = (
        ('good', 'Good'),
        ('injure', 'Injure'),
        ('bad', 'Bad')
    )

    ADOPTION_CHOICE = (
        ('pending', 'Pending' ),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    )
    species = models.ForeignKey(AnimalSpecies, on_delete=models.CASCADE)
    breed = models.ForeignKey(AnimalBread, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(default=0)
    health_status = models.CharField(max_length=10, choices=HEALTH_CHOICE, default='good')
    adoption_status = models.CharField(max_length=10, choices=ADOPTION_CHOICE, default='pending')

    create_at = models.DateTimeField(auto_now_add=True)
    modified_At = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.species.name} - {self.breed.name}'
    
    class Meta:
        verbose_name = 'Animal'


class AdoptionRequest(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending' ),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animals, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='pending')

    def __str__(self):
        return f'{self.user.username} {self.animal.species.name} - {self.status}'
    
    class Meta:
        verbose_name = 'Adoption Request'