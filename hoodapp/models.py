from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


# Create your models here.
class NeighbourHood(models.Model):
    name = models.CharField(max_length=100,blank=True) 
    image = CloudinaryField('image', default='image')
    health_email = models.EmailField(max_length=100,blank=True,null=True)
    health_center=models.CharField(max_length=100,blank=True,null=True)
    health_contact = models.IntegerField(default=0, null=True, blank=True)
    authority_email = models.EmailField(max_length=100,blank=True,null=True)
    authority_center=models.CharField(max_length=100,blank=True,null=True)
    authority_contact = models.IntegerField(default=0, null=True, blank=True)
    location = models.CharField(max_length=100,blank=True)
    admin = models.ForeignKey(User,on_delete = models.CASCADE,related_name='administration',null=True)
    description = models.TextField( max_length=550, blank=True, null=True)
    location= models.CharField(max_length=60, blank=True, null=True)
    occupants_count = models.IntegerField(default=0,null  = True ,blank = True)
    post_date = models.DateTimeField(auto_now=True)
      
    
    def __str__(self):
        return self.name 
    
    def create_neighborhood(self):
        """
        A method that creates a neighbourhood
        """
        self.save()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        """
        A method that finds a neighbourhood using its id
        """

         
        hoods=NeighbourHood.objects.filter(id=neighborhood_id) 
        return hoods
            
    # @classmethod
    # def search_by_name(cls,search_term):
    #     """
    #     A method that searches a neighborhood
    #     """          
    #     neighborhood = cls.objects.filter(name__icontains = search_term).all()
    #     return neighborhood
    
    @classmethod
    def update_neighbourhood(cls, id):
        """
        A method that updates a neighbourhood
        """
        neighbourhood = cls.objects.filter(id=id).update(id=id)
        return neighbourhood   

    def delete_neighborhood(self):
        """
        A method that deletes a neighbourhood
        """
        self.delete() 

   
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE , related_name='profile')
    bio = models.TextField(max_length=300,blank =True)
    email = models.CharField(max_length=100, blank =True,null=True)
    profile_pic=CloudinaryField('image',default='image')
    phone_no = models.IntegerField(blank=True,null=True)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.SET_NULL, null=True, related_name='neighbour', blank=True)
    post_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user  

class Business(models.Model):
    name = models.CharField(max_length=200, blank=True,null=True)
    image = CloudinaryField('image', default='image')
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)     
    email =  models.CharField(max_length=100, blank=True,null=True)
    phone_no = models.IntegerField(blank=True)
    neighbourhood = models.ForeignKey(NeighbourHood,on_delete=models.CASCADE, related_name='business',null=True)
    post_date = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, max_length=300)
   

    def __str__(self):
        return self.name      
    
    def create_business(self):
        """
        A method that creates a business
        """
        self.save()
    
            
    @classmethod
    def search_business(cls,search_term):
        """
        A method that searches a business
        """          
        businesses = cls.objects.filter(name__icontains = search_term).all()
        return businesses 
    
    @classmethod
    def find_business(cls, business_id):
        """
        A method that finds a business using its id
        """         
        business = Business.objects.filter(id=business_id)
        return business  
    
    @classmethod
    def update_business(cls, id):
        """
        A method that updates a business using its id
        """  
        business = cls.objects.filter(id=id).update(id=id)
        return business

    def delete_business(self):
        """
        A method that deletes a business
        """        
        self.delete()



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    title = models.CharField(max_length=200,blank=True)
    info =  HTMLField(blank=True,null=True)
    neighbourhood= models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, related_name='neighbourhood_post')
    post_date = models.DateField(auto_now_add=True)
    image= CloudinaryField('image' , default='image')

    def __str__(self):
        return self.title
         
    @classmethod
    def get_post(cls, id):
        """
        A method that gets a post using the given id
        """   
        post = Post.objects.filter(id=neighbourhood)
        return post     
    




