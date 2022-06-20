from django.test import TestCase
from .models import Profile,Business,NeighbourHood



# Create your tests here.
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.Prof= Profile( id = '1', user ='sareto',bio='Wealthy', profile_picture = 'example.jpg',email='sareto@gmail.com',phone_number='0712345678',neighbourhood='Kitengela' )
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Prof,Profile)) 

class NeighbourHoodTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.Juja = Location.objects.create(name="Juja")
        self.test_neighbourhood = NeighbourHood.objects.create(name='kitengela',location='Nairobi',admin='sareto',image='example.jpg',description='serene place',occupants='1')
        self.test_neighbourhood.save()


    def test_save_method(self):
        self.test_neighbourhood.save()
        test_neighbourhoods = NeighbourHood.objects.all()
        self.assertTrue(len(test_neighbourhoods) > 0)
            
    
    def test_delete_method(self):
        self.Neighbourhood.delete_neighbourhood()
        neighbourhoods = NeighbourHood.objects.all()
        self.assertTrue(len(neighbourhoods)==0)   
        
    def tearDown(self):
        NeighbourHood.objects.all().delete()
        
        

           
class BusinessTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.Busi = Location.objects.create(name="bst")

        self.test_business = Business.objects.create(name='Spashop',image='example.jpg',user='sareto',email='example@gmail.com',phone_number='0712345678',neighbourhood='kitengela')

        self.test_business.save()

    def test_save_method(self):
        self.test_business.save()
        test_business = Business.objects.all()
        self.assertTrue(len(test_business) > 0)
            
    
    def test_delete_method(self):
        self.Business.delete_business()
        business = Business.objects.all()
        self.assertTrue(len(business)==0)   
        
    def tearDown(self):
        Business.objects.all().delete()         