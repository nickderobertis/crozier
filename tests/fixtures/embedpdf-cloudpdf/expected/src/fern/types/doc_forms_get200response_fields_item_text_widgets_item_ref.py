

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_forms_get200response_fields_item_text_widgets_item_ref_index_page import (
    DocFormsGet200ResponseFieldsItemTextWidgetsItemRefIndexPage,
)
from .doc_forms_get200response_fields_item_text_widgets_item_ref_index_revision import (
    DocFormsGet200ResponseFieldsItemTextWidgetsItemRefIndexRevision,
)
from .doc_forms_get200response_fields_item_text_widgets_item_ref_nm_page import (
    DocFormsGet200ResponseFieldsItemTextWidgetsItemRefNmPage,
)
from .doc_forms_get200response_fields_item_text_widgets_item_ref_object_number_page import (
    DocFormsGet200ResponseFieldsItemTextWidgetsItemRefObjectNumberPage,
)


class DocFormsGet200ResponseFieldsItemTextWidgetsItemRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocFormsGet200ResponseFieldsItemTextWidgetsItemRefObjectNumberPage
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


class DocFormsGet200ResponseFieldsItemTextWidgetsItemRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocFormsGet200ResponseFieldsItemTextWidgetsItemRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocFormsGet200ResponseFieldsItemTextWidgetsItemRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocFormsGet200ResponseFieldsItemTextWidgetsItemRefIndexPage
    index: int
    revision: DocFormsGet200ResponseFieldsItemTextWidgetsItemRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocFormsGet200ResponseFieldsItemTextWidgetsItemRef = typing_extensions.Annotated[
    typing.Union[
        DocFormsGet200ResponseFieldsItemTextWidgetsItemRef_ObjectNumber,
        DocFormsGet200ResponseFieldsItemTextWidgetsItemRef_Nm,
        DocFormsGet200ResponseFieldsItemTextWidgetsItemRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
