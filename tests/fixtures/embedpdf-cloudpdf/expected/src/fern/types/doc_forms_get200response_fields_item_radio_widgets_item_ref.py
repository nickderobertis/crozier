

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_forms_get200response_fields_item_radio_widgets_item_ref_index_page import (
    DocFormsGet200ResponseFieldsItemRadioWidgetsItemRefIndexPage,
)
from .doc_forms_get200response_fields_item_radio_widgets_item_ref_index_revision import (
    DocFormsGet200ResponseFieldsItemRadioWidgetsItemRefIndexRevision,
)
from .doc_forms_get200response_fields_item_radio_widgets_item_ref_nm_page import (
    DocFormsGet200ResponseFieldsItemRadioWidgetsItemRefNmPage,
)
from .doc_forms_get200response_fields_item_radio_widgets_item_ref_object_number_page import (
    DocFormsGet200ResponseFieldsItemRadioWidgetsItemRefObjectNumberPage,
)


class DocFormsGet200ResponseFieldsItemRadioWidgetsItemRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocFormsGet200ResponseFieldsItemRadioWidgetsItemRefObjectNumberPage
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


class DocFormsGet200ResponseFieldsItemRadioWidgetsItemRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocFormsGet200ResponseFieldsItemRadioWidgetsItemRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocFormsGet200ResponseFieldsItemRadioWidgetsItemRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocFormsGet200ResponseFieldsItemRadioWidgetsItemRefIndexPage
    index: int
    revision: DocFormsGet200ResponseFieldsItemRadioWidgetsItemRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocFormsGet200ResponseFieldsItemRadioWidgetsItemRef = typing_extensions.Annotated[
    typing.Union[
        DocFormsGet200ResponseFieldsItemRadioWidgetsItemRef_ObjectNumber,
        DocFormsGet200ResponseFieldsItemRadioWidgetsItemRef_Nm,
        DocFormsGet200ResponseFieldsItemRadioWidgetsItemRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
