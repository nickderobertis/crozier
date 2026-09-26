

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_forms_get200response_fields_item_pushbutton_widgets_item_ref_index_page import (
    DocFormsGet200ResponseFieldsItemPushbuttonWidgetsItemRefIndexPage,
)
from .doc_forms_get200response_fields_item_pushbutton_widgets_item_ref_index_revision import (
    DocFormsGet200ResponseFieldsItemPushbuttonWidgetsItemRefIndexRevision,
)
from .doc_forms_get200response_fields_item_pushbutton_widgets_item_ref_nm_page import (
    DocFormsGet200ResponseFieldsItemPushbuttonWidgetsItemRefNmPage,
)
from .doc_forms_get200response_fields_item_pushbutton_widgets_item_ref_object_number_page import (
    DocFormsGet200ResponseFieldsItemPushbuttonWidgetsItemRefObjectNumberPage,
)


class DocFormsGet200ResponseFieldsItemPushbuttonWidgetsItemRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocFormsGet200ResponseFieldsItemPushbuttonWidgetsItemRefObjectNumberPage
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


class DocFormsGet200ResponseFieldsItemPushbuttonWidgetsItemRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocFormsGet200ResponseFieldsItemPushbuttonWidgetsItemRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocFormsGet200ResponseFieldsItemPushbuttonWidgetsItemRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocFormsGet200ResponseFieldsItemPushbuttonWidgetsItemRefIndexPage
    index: int
    revision: DocFormsGet200ResponseFieldsItemPushbuttonWidgetsItemRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocFormsGet200ResponseFieldsItemPushbuttonWidgetsItemRef = typing_extensions.Annotated[
    typing.Union[
        DocFormsGet200ResponseFieldsItemPushbuttonWidgetsItemRef_ObjectNumber,
        DocFormsGet200ResponseFieldsItemPushbuttonWidgetsItemRef_Nm,
        DocFormsGet200ResponseFieldsItemPushbuttonWidgetsItemRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
