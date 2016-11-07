from django.shortcuts import get_object_or_404, render
from .models import reagent, antibody_reagent
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

def index(request):
    rgt_count = reagent.objects.count()
    ab_count = antibody_reagent.objects.count()
    reagent_list = reagent.objects.order_by('id')
    context = {
        'reagent_list':reagent_list,
        'ab_count':ab_count,
        'rgt_count':rgt_count,
    }
    return render(request, 'inventory/index.html', context)

def detail(request, reagent_id):
    rg = get_object_or_404(reagent, id=reagent_id)
    context = {'rg':rg,}
    return render(request, 'inventory/detail.html', context)

def change(request, reagent_id):
    rg = get_object_or_404(antibody_reagent, reagent_id=reagent_id)
    context = {'rg':rg,}
    try:
        analyte = request.POST['analyte']
        fluor = request.POST['fluor']
        manufacturer = request.POST['manufacturer']
        item_number = request.POST['item_number']
        manu_volume = request.POST['manu_volume']
        volume_per_test = request.POST['volume_per_test']
        volume_per_vial = request.POST['volume_per_vial']
        tests_per_vial = request.POST['tests_per_vial']
        concentration = request.POST['concentration']
        isotype = request.POST['isotype']
        light_chain = request.POST['light_chain']
        clone = request.POST['clone']
        control_cells = request.POST['control_cells']
        rg.analyte = analyte
        rg.fluor = fluor
        rg.manufacturer = manufacturer
        rg.item_number = item_number
        rg.manu_volume = manu_volume
        rg.volume_per_test = volume_per_test
        rg.volume_per_vial = volume_per_vial
        rg.concentration = concentration
        rg.isotype = isotype
        rg.light_chain = light_chain
        rg.clone = clone
        rg.control_cells = control_cells
    except (KeyError):
        return render(request, 'inventory/change.html', context)
    else:
        rg.save()
        return HttpResponseRedirect(reverse('inventory:detail', args=(rg.reagent_id,)))
