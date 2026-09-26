

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_forms_get200response_fields_item_unknown_widgets_item_ref_index_page import (
    DocFormsGet200ResponseFieldsItemUnknownWidgetsItemRefIndexPage,
)
from .doc_forms_get200response_fields_item_unknown_widgets_item_ref_index_revision import (
    DocFormsGet200ResponseFieldsItemUnknownWidgetsItemRefIndexRevision,
)
from .doc_forms_get200response_fields_item_unknown_widgets_item_ref_nm_page import (
    DocFormsGet200ResponseFieldsItemUnknownWidgetsItemRefNmPage,
)
from .doc_forms_get200response_fields_item_unknown_widgets_item_ref_object_number_page import (
    DocFormsGet200ResponseFieldsItemUnknownWidgetsItemRefObjectNumberPage,
)


class DocFormsGet200ResponseFieldsItemUnknownWidgetsItemRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocFormsGet200ResponseFieldsItemUnknownWidgetsItemRefObjectNumberPage
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


class DocFormsGet200ResponseFieldsItemUnknownWidgetsItemRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocFormsGet200ResponseFieldsItemUnknownWidgetsItemRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocFormsGet200ResponseFieldsItemUnknownWidgetsItemRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocFormsGet200ResponseFieldsItemUnknownWidgetsItemRefIndexPage
    index: int
    revision: DocFormsGet200ResponseFieldsItemUnknownWidgetsItemRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocFormsGet200ResponseFieldsItemUnknownWidgetsItemRef = typing_extensions.Annotated[
    typing.Union[
        DocFormsGet200ResponseFieldsItemUnknownWidgetsItemRef_ObjectNumber,
        DocFormsGet200ResponseFieldsItemUnknownWidgetsItemRef_Nm,
        DocFormsGet200ResponseFieldsItemUnknownWidgetsItemRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
