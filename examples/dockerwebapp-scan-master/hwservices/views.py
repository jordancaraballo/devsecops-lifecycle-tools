from django.shortcuts import render, render_to_response
from django.contrib import admin
from hwservices.models import Manufacturer as manufacturer
from hwservices.models import Brand as brand
from hwservices.models import Model as model
from django.db import connection
from django.db.models import Count, Sum



# Create your views here.
def index(request):
    return render_to_response('index.html')

def tables(request):
    # Manufacturer full table
    ismanufacturer = manufacturer.objects.all()

    # Brand full table
    isbrand = brand.objects.all()

    # Model full table
    ismodel = model.objects.all()

    # Report #1 - how many accounts do we have in each state
    # SELECT MAN_STATE, COUNT(*) as Total FROM Manufacturer group by MAN_STATE
    isreport1 = manufacturer.objects.values("MAN_STATE").annotate(Count("MAN_STATE"))

    # Report #2 - manufacturers accounts per state
    # select UNIQUE MAN_COMPANY,MAN_ACCNUM from manufacturer
    isreport2 = manufacturer.objects.values("MAN_STATE","MAN_ACCNUM").order_by("MAN_STATE").distinct()

    # Report #3 - number of models per brand
    # select BRAND_NAME, COUNT(*) as Total from brand natural join model group by BRAND_NAME
    isreport3 = brand.objects.select_related('brand__model').values("BRAND_NAME").annotate(Count("BRAND_NAME"))

    # Report #4 - number of brands per company
    # select MAN_COMPANY, COUNT(*) from manufacturer natural join brand group by MAN_COMPANY
    isreport4 = manufacturer.objects.select_related('manufacturer__brand').values("MAN_COMPANY").annotate(Count("MAN_COMPANY"))

    # Report #5 - model prices per brand
    # select BRAND_NAME || ' ' || BRAND_LEVEL as Brand, MODEL_NUM, MODEL_HWRP from brand natural join model
    # order by MODEL_HWRP desc
    isreport5 = brand.objects.select_related('brand__model').values("BRAND_NAME","BRAND_LEVEL","model__MODEL_NUM","model__MODEL_HWRP").annotate(Count("model__MODEL_HWRP")).order_by("-model__MODEL_HWRP").distinct()

    # Report #6 - Money per company if models are completely selled
    # select BRAND_NAME, SUM(MODEL_HWRP) as Total from brand natural join model
    # group by BRAND_NAME
    # order by Total desc
    isreport6 = brand.objects.select_related('brand__model').values("BRAND_NAME").annotate(Sum("model__MODEL_HWRP")).order_by("-model__MODEL_HWRP__sum").distinct()

    return render(request, 'list.html', locals())
