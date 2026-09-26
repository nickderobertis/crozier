

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_forms_get200response_fields_item_combobox_widgets_item_ref_index_page import (
    DocFormsGet200ResponseFieldsItemComboboxWidgetsItemRefIndexPage,
)
from .doc_forms_get200response_fields_item_combobox_widgets_item_ref_index_revision import (
    DocFormsGet200ResponseFieldsItemComboboxWidgetsItemRefIndexRevision,
)
from .doc_forms_get200response_fields_item_combobox_widgets_item_ref_nm_page import (
    DocFormsGet200ResponseFieldsItemComboboxWidgetsItemRefNmPage,
)
from .doc_forms_get200response_fields_item_combobox_widgets_item_ref_object_number_page import (
    DocFormsGet200ResponseFieldsItemComboboxWidgetsItemRefObjectNumberPage,
)


class DocFormsGet200ResponseFieldsItemComboboxWidgetsItemRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocFormsGet200ResponseFieldsItemComboboxWidgetsItemRefObjectNumberPage
    annot_object_number: typing_extensions.Annotated[
        int, FieldMetadata(alias="annotObjectNumber"), pydantic.Field(alias="annotObjectNumber")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocFormsGet200ResponseFieldsItemComboboxWidgetsItemRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocFormsGet200ResponseFieldsItemComboboxWidgetsItemRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocFormsGet200ResponseFieldsItemComboboxWidgetsItemRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocFormsGet200ResponseFieldsItemComboboxWidgetsItemRefIndexPage
    index: int
    revision: DocFormsGet200ResponseFieldsItemComboboxWidgetsItemRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocFormsGet200ResponseFieldsItemComboboxWidgetsItemRef = typing_extensions.Annotated[
    typing.Union[
        DocFormsGet200ResponseFieldsItemComboboxWidgetsItemRef_ObjectNumber,
        DocFormsGet200ResponseFieldsItemComboboxWidgetsItemRef_Nm,
        DocFormsGet200ResponseFieldsItemComboboxWidgetsItemRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
