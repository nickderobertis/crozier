

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_forms_get200response_fields_item_checkbox_widgets_item_ref_index_page import (
    DocFormsGet200ResponseFieldsItemCheckboxWidgetsItemRefIndexPage,
)
from .doc_forms_get200response_fields_item_checkbox_widgets_item_ref_index_revision import (
    DocFormsGet200ResponseFieldsItemCheckboxWidgetsItemRefIndexRevision,
)
from .doc_forms_get200response_fields_item_checkbox_widgets_item_ref_nm_page import (
    DocFormsGet200ResponseFieldsItemCheckboxWidgetsItemRefNmPage,
)
from .doc_forms_get200response_fields_item_checkbox_widgets_item_ref_object_number_page import (
    DocFormsGet200ResponseFieldsItemCheckboxWidgetsItemRefObjectNumberPage,
)


class DocFormsGet200ResponseFieldsItemCheckboxWidgetsItemRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocFormsGet200ResponseFieldsItemCheckboxWidgetsItemRefObjectNumberPage
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


class DocFormsGet200ResponseFieldsItemCheckboxWidgetsItemRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocFormsGet200ResponseFieldsItemCheckboxWidgetsItemRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocFormsGet200ResponseFieldsItemCheckboxWidgetsItemRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocFormsGet200ResponseFieldsItemCheckboxWidgetsItemRefIndexPage
    index: int
    revision: DocFormsGet200ResponseFieldsItemCheckboxWidgetsItemRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocFormsGet200ResponseFieldsItemCheckboxWidgetsItemRef = typing_extensions.Annotated[
    typing.Union[
        DocFormsGet200ResponseFieldsItemCheckboxWidgetsItemRef_ObjectNumber,
        DocFormsGet200ResponseFieldsItemCheckboxWidgetsItemRef_Nm,
        DocFormsGet200ResponseFieldsItemCheckboxWidgetsItemRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
