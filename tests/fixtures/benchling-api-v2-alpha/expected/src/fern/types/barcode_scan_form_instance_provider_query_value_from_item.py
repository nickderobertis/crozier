

import typing

from .form_barcode_value_reference import FormBarcodeValueReference
from .form_field_value_reference import FormFieldValueReference
from .form_raw_string_query_value_part import FormRawStringQueryValuePart

BarcodeScanFormInstanceProviderQueryValueFromItem = typing.Union[
    FormBarcodeValueReference, FormRawStringQueryValuePart, FormFieldValueReference
]
