

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_forms_get200response_fields_item_signature_widgets_item_ref_index_page import (
    DocFormsGet200ResponseFieldsItemSignatureWidgetsItemRefIndexPage,
)
from .doc_forms_get200response_fields_item_signature_widgets_item_ref_index_revision import (
    DocFormsGet200ResponseFieldsItemSignatureWidgetsItemRefIndexRevision,
)
from .doc_forms_get200response_fields_item_signature_widgets_item_ref_nm_page import (
    DocFormsGet200ResponseFieldsItemSignatureWidgetsItemRefNmPage,
)
from .doc_forms_get200response_fields_item_signature_widgets_item_ref_object_number_page import (
    DocFormsGet200ResponseFieldsItemSignatureWidgetsItemRefObjectNumberPage,
)


class DocFormsGet200ResponseFieldsItemSignatureWidgetsItemRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocFormsGet200ResponseFieldsItemSignatureWidgetsItemRefObjectNumberPage
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


class DocFormsGet200ResponseFieldsItemSignatureWidgetsItemRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocFormsGet200ResponseFieldsItemSignatureWidgetsItemRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocFormsGet200ResponseFieldsItemSignatureWidgetsItemRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocFormsGet200ResponseFieldsItemSignatureWidgetsItemRefIndexPage
    index: int
    revision: DocFormsGet200ResponseFieldsItemSignatureWidgetsItemRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocFormsGet200ResponseFieldsItemSignatureWidgetsItemRef = typing_extensions.Annotated[
    typing.Union[
        DocFormsGet200ResponseFieldsItemSignatureWidgetsItemRef_ObjectNumber,
        DocFormsGet200ResponseFieldsItemSignatureWidgetsItemRef_Nm,
        DocFormsGet200ResponseFieldsItemSignatureWidgetsItemRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
