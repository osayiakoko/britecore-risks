from django.contrib import admin
from risk.models import (
    RiskType,
    RiskTypeField,
    TextFieldValue,
    NumberFieldValue,
    DateFieldValue,
    EnumFieldValue,
    EnumFieldValueChoice
)

# Register your models here.
admin.site.register(RiskType)
admin.site.register(RiskTypeField)
admin.site.register(TextFieldValue)
admin.site.register(NumberFieldValue)
admin.site.register(DateFieldValue)
admin.site.register(EnumFieldValue)
admin.site.register(EnumFieldValueChoice)
