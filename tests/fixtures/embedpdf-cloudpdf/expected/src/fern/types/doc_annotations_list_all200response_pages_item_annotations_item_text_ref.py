

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_text_ref_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextRefIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_text_ref_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextRefIndexRevision,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_text_ref_nm_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextRefNmPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_text_ref_object_number_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextRefObjectNumberPage,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextRefObjectNumberPage
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


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextRefIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextRef = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextRef_ObjectNumber,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextRef_Nm,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
