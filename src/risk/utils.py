from typing import Dict, List

from risk.models import EnumFieldValueChoice

from .enums import FieldDataType


def get_enum_fields_id(fields: List[Dict]) -> List[int]:
    ids = [
        field['id'] for field in fields 
            if field['field_type'] == FieldDataType.ENUM
    ]
    return ids


def get_enum_field_options(field:Dict, fields_options: List[EnumFieldValueChoice]) -> List[str]:
    options = [
        opt.value for opt in fields_options 
            if opt.risk_enum_field_id == field['id']
    ]
    return options
