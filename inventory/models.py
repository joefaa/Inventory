from django.db import models

class reagent( models.Model ):
    reagent_name = models.CharField( max_length=50 )
    def __str__(self):
        return(self.reagent_name)

class antibody_reagent(models.Model):
    reagent = models.OneToOneField( reagent, on_delete=models.CASCADE, primary_key=True )
    analyte = models.CharField( max_length=20 )
    fluor = models.CharField( max_length=20 )
    manufacturer = models.CharField( max_length=25 )
    item_number = models.CharField( max_length=25 )
    manu_volume = models.IntegerField( default=0 )
    volume_per_test = models.IntegerField( default=0 )
    volume_per_vial = models.IntegerField( default=0 )
    tests_per_vial = models.IntegerField( default=0 )
    concentration = models.IntegerField( default=0 )
    isotype = models.CharField( max_length=20 )
    light_chain = models.CharField( max_length=20 )
    clone = models.CharField( max_length=20 )
    control_cells = models.CharField( max_length=750 )
    def __str__(self):
        return(self.reagent.reagent_name)

# class reagent_inventory(models.Model):
#     reagent = models.ForeignKey( 'reagent', on_delete=models.CASCADE )
#     recieve_date = models.DateTimeField( 'Recieve date' )
#     lot_number = models.CharField( max_length=50 )
#     expiration_date = models.DateTimeField( 'Expiration date' )
#     in_use = models.DateTimeField( 'In use date' )
#     def __str__(self):
#         return("Lot: {} Rcv: {}".format(self.lot_number, self.recieve_date))
# class cocktail(models.Model):
#     name = models.CharField( max_length=20 )
#     r1 = models.ForeignKey( antibody_reagent, on_delete=models.CASCADE )
#     r2 = models.ForeignKey( antibody_reagent, on_delete=models.CASCADE )
#     r3 = models.ForeignKey( antibody_reagent, on_delete=models.CASCADE )
#     r4 = models.ForeignKey( antibody_reagent, on_delete=models.CASCADE )
#     r5 = models.ForeignKey( antibody_reagent, on_delete=models.CASCADE )
#     r6 = models.ForeignKey( antibody_reagent, on_delete=models.CASCADE )
#     r7 = models.ForeignKey( antibody_reagent, on_delete=models.CASCADE )
#     r8 = models.ForeignKey( antibody_reagent, on_delete=models.CASCADE )
#
# class cocktail_inventory(models.Model):
#     preparation_date = models.DateTimeField( 'Preparation date' )
#     lot_number = models.CharField( max_length=50 )
#     expiration_date = models.DateTimeField( 'Expiration date' )
#     in_use = models.DateTimeField( 'In use date' )
