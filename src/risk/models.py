from django.db import models
from .enums import FieldDataType


class RiskType(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name


class RiskTypeField(models.Model):
    risk_type = models.ForeignKey(RiskType, on_delete=models.CASCADE, related_name="risk_type_fields")
    field_name = models.CharField(max_length=150)
    field_type = models.CharField(max_length=50, choices=FieldDataType.choices)

    class Meta:
        unique_together = (('risk_type', 'field_name', 'field_type'))
        ordering = ('pk', )

    def __str__(self) -> str:
        return f'{self.risk_type} -> {self.field_name}({self.field_type})'


# abstract model for field values model
class FieldValueModel(models.Model):
    risk_type = models.ForeignKey(RiskType, on_delete=models.CASCADE, related_name="%(class)ss", null=True)
    risk_type_field = models.ForeignKey(RiskTypeField, on_delete=models.CASCADE, related_name='%(class)ss')
    value = None

    def __str__(self) -> str:
        return f'{self.value}'

    class Meta:
        abstract = True


# stores value for risks type with text field
class TextFieldValue(FieldValueModel):
    value = models.TextField()


# stores value for risks type with number field
class NumberFieldValue(FieldValueModel):
    value = models.IntegerField()


# stores value for risks type with date field
class DateFieldValue(FieldValueModel):
    value = models.DateField()


# provides users with possible value for EnumFieldValue
class EnumFieldValueChoice(models.Model):
    risk_enum_field = models.ForeignKey(RiskTypeField, on_delete=models.CASCADE)
    value = models.CharField(max_length=150)

    def __str__(self) -> str:
        return f'{self.risk_enum_field}: {self.value}'


# stores value for risks type with enum field
class EnumFieldValue(FieldValueModel):
    value = models.CharField(max_length=150)

    class Meta:
        unique_together = (('risk_type_field', 'value'),)
