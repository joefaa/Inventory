from django.contrib import admin

from .models import reagent, antibody_reagent


admin.site.register(reagent)
admin.site.register(antibody_reagent)
