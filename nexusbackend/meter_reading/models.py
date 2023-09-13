from django.db import models
# Create your models here.
class MeterReading(models.Model):
    current_reading = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(null=True) 
    # meter = models.ForeignKey('Meter', on_delete=models.CASCADE) this has a relationship with the meter model

    def __str__(self):
     return f"Meter Reading - Date: {self.date}, Current Reading: {self.current_reading}"


#class Meter(models.Model):
   # meter_number = models.IntegerField(unique=True)

   # def __str__(self):
      #  return f"Meter {self.meter_number}"