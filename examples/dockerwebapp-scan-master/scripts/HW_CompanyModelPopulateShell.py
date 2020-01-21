# Add data through manage.py shell
# Manufacturer model
# python manage.py shell
# Author: Jordan A Caraballo Vega
from hwservices.models import Manufacturer, Brand, Model
with open('../data/DataManu.sql') as f:
    lines = f.read().splitlines()

for l in lines:
    i = l.split(',')
    q = Manufacturer(MAN_CODE=i[0],MAN_COMPANY=i[1], MAN_STREET=i[2],MAN_CITY=i[3],MAN_STATE=i[4],MAN_ZIP=i[5],MAN_AREACODE=i[6],MAN_PHONE=i[7],MAN_ACCNUM=i[8])
    q.save()

# Brand model
from hwservices.models import Manufacturer, Brand, Model
with open('../data/DataBrand.sql') as f:
    lines = f.read().splitlines()
objectsList = Manufacturer.objects.all()
for l in lines:
    i = l.split(',')
    q = Brand(BRAND_ID=i[0],BRAND_NAME=i[1],BRAND_LEVEL=i[2],MAN_CODE=objectsList[int(i[3])-1])
    q.save()

# Model number
from hwservices.models import Manufacturer, Brand, Model
with open('../data/DataModel.sql') as f:
    lines = f.read().splitlines()
objectsList = Brand.objects.all()
for l in lines:
    i = l.split(',')
    q = Model(MODEL_NUM=i[0],MODEL_JETS=i[1],MODEL_MOTORS=i[2],MODEL_HP=i[3],MODEL_SRP=i[4],MODEL_HWRP=i[5],MODEL_WEIGTH=i[6],MODEL_WATCAP=i[7],MODEL_SEATCAP=i[8],BRAND_ID=objectsList[int(i[9])-1])
    q.save()
