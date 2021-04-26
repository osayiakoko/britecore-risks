from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ..enums import FieldDataType
from ..models import EnumFieldValueChoice, RiskType, RiskTypeField
from ..utils import get_enum_fields_id, get_enum_field_options


class RiskTypeViewSet(GenericViewSet):
    """
    A simple ViewSet for listing or retrieving risk types.
    """

    queryset = RiskType.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        risk_type_fields = RiskTypeField.objects.filter(risk_type__in=queryset).values()
        risk_types = queryset.values()

        # create list of enum fields id and retrieve enum values from db
        enum_fields_id = get_enum_fields_id(risk_type_fields)
        if enum_fields_id:
            enum_fields_options = EnumFieldValueChoice.objects.filter(risk_enum_field__in=enum_fields_id)

        # loops through risk_types and appends designated fields to each risk_type
        # as well as checking if the fields are of type enum in other to append choice
        for risk_type in risk_types:
            fields = []
            for field in risk_type_fields:
                if field['risk_type_id'] == risk_type['id']:
                    if field['field_type'] == FieldDataType.ENUM:
                        field['choices'] = get_enum_field_options(field, enum_fields_options)
                    fields.append(field)

            risk_type['fields'] = fields
        return Response(risk_types)


    def retrieve(self, request, pk):
        obj = self.get_object()
        risk_type_fields = obj.risk_type_fields.all().values()
        risk_type = model_to_dict(obj)

        # get list of enum fields id
        enum_fields_id = get_enum_fields_id(risk_type_fields)

        # if risk_type has field(s) of type enum
        if enum_fields_id:
            enum_fields_options = EnumFieldValueChoice.objects.filter(risk_enum_field__in=enum_fields_id)

            # loops through fields and appends choices to enum fields
            for field in risk_type_fields:
                if field['field_type'] == FieldDataType.ENUM:
                    field['choices'] = get_enum_field_options(field, enum_fields_options)

        risk_type['fields'] = risk_type_fields
        return Response(risk_type)
