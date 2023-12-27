from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.gis.db import models as md
# Create your models here.

class VillageMappingFile(models.Model):
    """
    Model where the village mapping file information is stored after importing from the admin
    """
    state_name = models.CharField(max_length=255, null=True, blank=True)
    ac_no = models.IntegerField(verbose_name=("AC No"),null=False,blank=False,default=99999)
    object_id  = models.IntegerField(verbose_name=("Object Id"),null=True,blank=True)
    name = models.CharField(verbose_name=("Name"),null=True,blank=True,max_length=255)
    locality = models.CharField(verbose_name=("Locality"),null=True,blank=True,max_length=3000)
    booth = models.CharField(verbose_name=("Booth"),null=True,blank=True,max_length=255)
    probable_nearby_vil_voter = models.CharField(verbose_name=("Probable Nearby Village"),max_length=2000,null=True,blank=True)
    mandal = models.CharField(verbose_name=("Mandal"),max_length=255,null=True,blank=True)
    
    class Meta:
        ordering = ['state_name','ac_no']
        
    

class VillageBoundaryModel(md.Model):
    state_name = md.CharField(max_length=255, blank=True)
    ac_no = md.IntegerField(verbose_name=('AC No'),null=True,blank=True)
    object_id  = md.BigIntegerField(verbose_name=("Object Id"),null=False,blank=False,primary_key=True)
    v_id = md.PositiveBigIntegerField(verbose_name=("ID"),null=True,blank=True)
    name = md.CharField(verbose_name=("Name"),null=True,blank=True,max_length=255)
    district = md.CharField(verbose_name=("District"),null=True,blank=True,max_length=255)
    subdistric = md.CharField(verbose_name=("Sub District"),null=True,blank=True,max_length=255)
    censusname = md.CharField(verbose_name=("Census Name"),null=True,blank=True,max_length=255)
    lgd_villag = md.CharField(verbose_name=("Lgd Village"),null=True,blank=True,max_length=255)
    level_2011 = md.CharField(verbose_name=("Level 2011"),null=True,blank=True,max_length=255)
    tru_2011 = md.CharField(verbose_name=("Tru 2011"),null=True,blank=True,max_length=255)
    geometry = md.MultiPolygonField()
    
    def __str__(self):
        return self.state_name + str(self.ac_no)
    
    class Meta:
        ordering = ['state_name','ac_no']




