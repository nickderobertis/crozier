

import typing

from .barcode_form_field import BarcodeFormField
from .date_selection_form_field import DateSelectionFormField
from .entity_link_form_field import EntityLinkFormField
from .free_form_text_form_field import FreeFormTextFormField
from .string_select_form_field import StringSelectFormField

NestedFormDefinitionFieldsItem = typing.Union[
    StringSelectFormField, FreeFormTextFormField, DateSelectionFormField, EntityLinkFormField, BarcodeFormField
]
