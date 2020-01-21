from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator
from django.core.validators import DecimalValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

# Manufacturer
def validate_integer(value):
    if not isinstance(value,int) or len(str(value)) != 5:
        raise ValidationError(_('%(value)s is not a valid number'),params={'value': value},)
def validate_phone(value):
    match_num=re.search(r'^(\d{3}-\d{4})',value)
    if not match_num:
        raise ValidationError(_('%(value)s is not a valid phone number (456-4575)'),params={'value': value},)
def validate_areacode(value):
    if not isinstance(value,int) or len(str(value)) != 3:
        raise ValidationError(_('%(value)s is not a valid number'),params={'value': value},)
def validate_account(value):
    match_num=re.search(r'^(\d{16})',value)
    if not match_num:
        raise ValidationError(_('%(value)s is not a valid number (accounts are 16 digits)'),params={'value': value},)
def integerval_validator(value):
    if not isinstance(value,int) or len(str(value)) > 8:
        raise ValidationError(_('%(value)s is not a valid number'),params={'value': value},)
def decimal_validator(value):
    match_num=re.match(r'\d+(?:[.]\d{2})?$', '40.12')
    if not match_num:
        raise ValidationError(_('%(value)s is not a valid number (2 decimal places)'),params={'value': value},)

# Create your models here.
class Manufacturer(models.Model):
    MAN_CODE     = models.AutoField(primary_key=True)
    MAN_COMPANY  = models.CharField(max_length=50)
    MAN_STREET   = models.CharField(max_length=30)
    MAN_CITY     = models.CharField(max_length=30)
    MAN_STATE    = models.CharField(max_length=30)
    MAN_ZIP      = models.IntegerField(validators=[validate_integer])
    MAN_AREACODE = models.IntegerField(validators=[validate_areacode])
    MAN_PHONE    = models.CharField(max_length=8,validators=[validate_phone])
    MAN_ACCNUM   = models.CharField(max_length=16,validators=[validate_account])

class Brand(models.Model):
    BRAND_LEVEL_CHOICES = (
        ('premium', 'premium'),
        ('mid-level', 'mid-level'),
        ('entry-level', 'entry-level'),
    )
    BRAND_ID    =  models.AutoField(primary_key=True)
    BRAND_NAME  = models.CharField(max_length=30)
    BRAND_LEVEL = models.CharField(max_length=30,choices=BRAND_LEVEL_CHOICES)
    MAN_CODE    = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

class Model(models.Model):
    MODEL_NUM     = models.AutoField(primary_key=True)
    MODEL_JETS    = models.IntegerField(validators=[integerval_validator])
    MODEL_MOTORS  = models.IntegerField(validators=[integerval_validator])
    MODEL_HP      = models.IntegerField(validators=[integerval_validator])
    MODEL_SRP     = models.DecimalField(max_digits=8, decimal_places=2, validators=[decimal_validator]) # los validators fastidian buscar forma de validar
    MODEL_HWRP    = models.DecimalField(max_digits=8, decimal_places=2, validators=[decimal_validator])
    MODEL_WEIGTH  = models.DecimalField(max_digits=8, decimal_places=2, validators=[decimal_validator])
    MODEL_WATCAP  = models.DecimalField(max_digits=8, decimal_places=2, validators=[decimal_validator])
    MODEL_SEATCAP = models.IntegerField(validators=[integerval_validator])
    BRAND_ID      = models.ForeignKey(Brand, on_delete=models.CASCADE)
