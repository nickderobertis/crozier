

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_forms_get200response_fields_item_listbox_widgets_item_ref_index_page import (
    DocFormsGet200ResponseFieldsItemListboxWidgetsItemRefIndexPage,
)
from .doc_forms_get200response_fields_item_listbox_widgets_item_ref_index_revision import (
    DocFormsGet200ResponseFieldsItemListboxWidgetsItemRefIndexRevision,
)
from .doc_forms_get200response_fields_item_listbox_widgets_item_ref_nm_page import (
    DocFormsGet200ResponseFieldsItemListboxWidgetsItemRefNmPage,
)
from .doc_forms_get200response_fields_item_listbox_widgets_item_ref_object_number_page import (
    DocFormsGet200ResponseFieldsItemListboxWidgetsItemRefObjectNumberPage,
)


class DocFormsGet200ResponseFieldsItemListboxWidgetsItemRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocFormsGet200ResponseFieldsItemListboxWidgetsItemRefObjectNumberPage
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


class DocFormsGet200ResponseFieldsItemListboxWidgetsItemRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocFormsGet200ResponseFieldsItemListboxWidgetsItemRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocFormsGet200ResponseFieldsItemListboxWidgetsItemRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocFormsGet200ResponseFieldsItemListboxWidgetsItemRefIndexPage
    index: int
    revision: DocFormsGet200ResponseFieldsItemListboxWidgetsItemRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocFormsGet200ResponseFieldsItemListboxWidgetsItemRef = typing_extensions.Annotated[
    typing.Union[
        DocFormsGet200ResponseFieldsItemListboxWidgetsItemRef_ObjectNumber,
        DocFormsGet200ResponseFieldsItemListboxWidgetsItemRef_Nm,
        DocFormsGet200ResponseFieldsItemListboxWidgetsItemRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
