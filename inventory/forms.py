from django import forms

class ab_detail_form(forms.Form):
    analyte = forms.CharField(label='Your name', max_length=20)
    fluor = forms.CharField(label='Your name', max_length=20)
    manufacturer = forms.CharField(label='Your name', max_length=25)
    item_number = forms.CharField(label='Your name', max_length=25)
    manu_volume = forms.DecimalField( max_digits=7, decimal_places=2 )
    volume_per_test = forms.DecimalField( max_digits=7, decimal_places=2 )
    volume_per_vial = forms.DecimalField( max_digits=7, decimal_places=2 )
    concentration = forms.DecimalField( max_digits=7, decimal_places=2 )
    isotype = forms.CharField(label='Your name', max_length=20)
    light_chain = forms.CharField(label='Your name', max_length=20)
    clone = forms.CharField(label='Your name', max_length=20)
    control_cells = forms.CharField(label='Your name', max_length=750)
