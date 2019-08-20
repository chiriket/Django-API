from django.db import models
from django.contrib.auth.models import User



   

class Profile(models.Model):
  
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile',blank=True, null=True)
    

    
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile

    @classmethod
    def get_profiles(cls):
        profiles = cls.objects.all()
        return profiles
    
   



